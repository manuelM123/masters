import random
import utilities as util
from operations.fitness_functions import *
from operations.crossover import *

# Population contain test suites which are lists of test cases where each individual within the test suite is a test case
# structure of test suite: [ [test_case_1], [test_case_2], ... ]
# structure of test_case_i: [ [identifier, [parameters], [genetic operators]] ]

'''
Selection function to select the crossover type to apply to the population

Parameters:
----------
population : list
    The population to select the crossover type from

population_fitness : list
    The fitness of each individual in the population

tournament_size : int
    The size of the tournament

type : str
    The type of selection to apply to the population

Returns:
-------
parents_selection : list
    A list containing the parents selected from the population
'''
def select(population, population_fitness, tournament_size, type):
    if type == 'random':
        return random_selection(population)
    if type == 'roulette_wheel':
        return roulette_wheel_selection(population, population_fitness)
    elif type == 'tournament':
        return tournament_selection(population, tournament_size)
    elif type == 'rank':
        return rank_selection(population)
    elif type == 'adaptive':
        return adaptive_selection(population, population_fitness)
    else:
        raise ValueError('Selection type is not specified correctly')

'''
Random selection to select two parents from the population 

Parameters:
----------
population : list
    The population to select the parents from

Returns:
-------
parents_selection : list
    A list containing the two parents selected from the population
'''
def random_selection(population):
    parents_selection = [population[random.randint(0, len(population) - 1)], population[random.randint(0, len(population) - 1)]]
    while parents_selection[0] == parents_selection[1]:
        parents_selection[1] = population[random.randint(0, len(population) - 1)]
    
    return parents_selection
'''
Roulette wheel selection to select two parents from the population 
Selection probability of an individual is calculated by dividing the individual's fitness by the sum of the fitness of the population
A sum of each selection probability is calculated and a random number is generated in the interval [0, sum(population_fitness)]
The individual whose selection probability sum is greater than the random number is selected as a parent
The process is repeated until two parents are selected

Parameters:
----------
population : list
    The population to select the parents from
population_fitness : list
    The fitness of each individual in the population

Returns:
-------
parents_selection : list
    A list containing the two parents selected from the population
'''
def roulette_wheel_selection(population, population_fitness):
    # Calculate the selection probabilities for each individual
    # population_fitness is a list that holds every individual's fitness of the population 
    # When selecting a first individual, do the loop again with another random number to ensure
    # that the individual is not chosen in bias according the order of the sum of the selection probabilities 
    # Verify if the individuals selected are the same

    selection_probabilities = []
    for individual_fitness in population_fitness:
        selection_probabilities.append(round(individual_fitness / sum(population_fitness),2))
    parents_selection = []
    selection_probabilities_sum = 0
    random_number = random.uniform(0, sum(selection_probabilities))
    print("Random number: " + str(random_number))
    print(selection_probabilities)
    while len(parents_selection) < 2:
        for i in range(len(population)):
            selection_probabilities_sum += selection_probabilities[i]
            if selection_probabilities_sum >= random_number:
                parents_selection.append(population[i])
                random_number = random.uniform(0, sum(selection_probabilities))
                print("Random number: " + str(random_number))
                selection_probabilities_sum = 0
                break 
        
        if len(parents_selection) > 1 and parents_selection[0] == parents_selection[1]:
            print("Parents are the same")
            print(str(parents_selection[0].test_suite) + " " + str(parents_selection[1].test_suite))
            parents_selection.pop(1)
    return parents_selection

'''
Rank selection to select two parents from the population
The individuals are sorted in ascending order according to their fitness
The individuals are assigned a rank according to their position in the sorted list
The parents are selected by choosing two individuals at random and comparing their ranks 
The individual with the higher rank is selected as a parent and the process is repeated until two parents are selected

Parameters:
----------
population : list
    The population to select the parents from
Returns:
-------
parents_selection : list
    A list containing the two parents selected from the population
'''
def rank_selection(population):
    parents_selected = []
    sorted_population_fitness = sorted(population, key=lambda x:x.fitness)
    print("Sorted Fitness")
    for i in range(len(sorted_population_fitness)):
        sorted_population_fitness[i].rank = i + 1
        print(sorted_population_fitness[i].fitness, end="|")
    while len(parents_selected) < 2 :
        individuals_selection = random.choices(sorted_population_fitness, k=2)
        print("Individuals selection: " +  str(individuals_selection[0].rank) + "|" + str(individuals_selection[1].rank))
        if individuals_selection[0] != individuals_selection[1]:
            if individuals_selection[0].rank > individuals_selection[1].rank:
                parents_selected.append(individuals_selection[0])
            else:
                parents_selected.append(individuals_selection[1])
        if len(parents_selected) > 1 and parents_selected[0] == parents_selected[1]:
            parents_selected.pop(1)
        
    return parents_selected
'''
Tournament selection to select two parents from the population 
A random number of individuals are selected from the population
The individuals are compared according to their fitness

Parameters:
----------
population : list
    The population to select the parents from

tournament_size : int
    The size of the tournament

Returns:
-------
parents_selected : list
    A list containing the two parents selected from the population
'''
def tournament_selection(population, tournament_size):
    parents_selected = []
    while len(parents_selected) != 2:
        selected_individuals = random.choices(population, k=tournament_size)
        for individuals in selected_individuals:
            print("Individuals: " + str(individuals.test_suite) + "| Fitness: " + str(individuals.fitness), end="\n")
        individuals_set = set(selected_individuals)
        print("--------------------------------------------------")
        if len(selected_individuals) == len(individuals_set):
            parents_selected.append(max(selected_individuals, key=lambda x:x.fitness))
            for individual in parents_selected:
                print("Parents: " + str(individual.test_suite), end="\n")
        
        if len(parents_selected) == 2 and len(parents_selected) != len(set(parents_selected)):
            parents_selected.pop(1)
    return parents_selected
        
'''
Function that implements the selection process for a adaptive selection scheme proposed by Pham and Castellani from "Adaptive Selection Routine for Evolutionary Algorithms", DOI: https://doi.org/10.1243/09596518JSCE942

Parameters:
----------
population : list
    The population to select the parents from
population_fitness : list
    The fitness of each individual in the population
    
Returns:
-------
first_list : list
    A list containing the first half of the selected individuals
second_list : list
    A list containing the second half of the selected individuals
'''
def adaptive_selection(population, population_fitness):
    first_list = []
    second_list = []
    u_f = calculate_average_fitness(population)
    f_max = max(population_fitness)
    
    while len(first_list) == 0 or len(second_list) == 0:
        rand = random.uniform(0, 1)
        valid_individuals = []
        for individual in population:
            individual.mating_chance = individual.fitness + (f_max - u_f) * rand
            if individual.adaptive_max_selections < 2:
                valid_individuals.append(individual)

        if len(valid_individuals) >= 0 and len(valid_individuals) < 2:
            print("No valid individuals")
            break

        else:
            sorted_population_mating_chance = sorted(valid_individuals, key=lambda x:x.mating_chance, reverse=True)
            for i in range(int(len(sorted_population_mating_chance) / 2)):
                if len(first_list) != int(len(sorted_population_mating_chance) / 2):
                    first_list.append(sorted_population_mating_chance[i])
                else:
                    second_list.append(sorted_population_mating_chance[i])
                sorted_population_mating_chance[i].adaptive_max_selections += 1

    return first_list, second_list

'''
Function that implements the selection process for a adaptive selection scheme proposed by Pham and Castellani from "Adaptive Selection Routine for Evolutionary Algorithms", DOI: https://doi.org/10.1243/09596518JSCE942

It uses the two structures of selected individuals to apply the adaptive selection method by mutating individuals from the first list with individuals from the second list in the following way:
    - The first individual from the first list is mated with the last individual from the second list
    - The second individual from the first list is mated with the second last individual from the second list 
    - This goes on until the last individual from the first list is mated with the first individual from the second list

Parameters:
----------
first_parents_list : list
    The first half of the selected individuals

second_parents_list : list
    The second half of the selected individuals

population : list
    The population to update the individuals RLT values

population_fitness : list
    The fitness of each individual in the population

configurations : dict
    The configurations of the algorithm

new_population : list
    The new population to insert the offsprings

Returns:
-------
new_population : list
    A list containing the offsprings generated from the adaptive selection method
'''
def adaptive_selection_method_lists(first_parents_list, second_parents_list, population, population_fitness, configurations, new_population, metadata):
    for individual in range(len(first_parents_list)):
        offsprings = uniform_crossover([first_parents_list[individual], second_parents_list[len(first_parents_list) - (individual + 1)]], configurations, metadata)
        for offspring in offsprings:
            offspring = rlt_setting(population, population_fitness, int(configurations.lt_max.value), int(configurations.lt_min.value), offspring)
            #print("Offspring: " + str(offspring.test_suite) + " - " + str(offspring.fitness) + " - " + str(offspring.remaining_lifetime))
            new_population.append(offspring)

    return new_population