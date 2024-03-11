from cut import *
from operations.fitness_functions import *
from solution import *
import utilities as util

'''
Function to create the initial population of random generated test suites with settings from the configuration file

Parameters:
----------
metadata : dict
    The metadata of the class context

population_size : int
    The size of the population

configurations : dict
    The configurations of the algorithm

Returns:
    population: list of test suites
'''
def create_population(metadata, population_size, configurations):
    population = []
    for individual in range(population_size):
        solution = Solution()
        solution.generate_test_suite(metadata, int(configurations.max_number_functions.value), int(configurations.max_number_test_cases.value))
        solution.adaptive_crossover_rate = random.uniform(0, 1.0)
        solution.adaptive_mutation_rate = random.uniform(0, 1.0)
        util.write_metadata(configurations.intermediate_test_suite_path.value, solution.test_suite, metadata)
        calculate_coverage_fitness(solution, configurations.fitness_function_type.value)
        population.append(solution)

    return population

'''
Function to create a offspring from the crossover or mutation genetic operators

Parameters:
----------
test_suite : list
    The test suite to create the offspring from

configurations : dict
    The configurations of the algorithm

Returns:
-------
individual : Solution
    The offspring created with specific test suite
'''
def create_offspring(test_suite, configurations, metadata):
    individual = Solution()
    individual.test_suite = test_suite
    print("Individual test suite: " + str(individual.test_suite))
    print("Previous fitness: " + str(individual.fitness))
    individual.adaptive_crossover_rate = random.uniform(0, 1.0)
    individual.adaptive_mutation_rate = random.uniform(0, 1.0)
    util.write_metadata(configurations.intermediate_test_suite_path.value, individual.test_suite, metadata)
    calculate_coverage_fitness(individual, configurations.fitness_function_type.value)
    print("New fitness: " + str(individual.fitness))
    return individual

'''
Function to calculate the remaining lifetime of each individual in the population

Parameters:
----------
population : list
    The population to calculate the remaining lifetime of

population_fitness : list
    The fitness of each individual in the population

lt_max : int
    The maximum lifetime value

lt_min : int
    The minimum lifetime value

Returns:
-------
population : list
    The population with the remaining lifetime of each individual calculated
'''
def rlt_setting(population, population_fitness, lt_max, lt_min, offpsring):
    f_average = calculate_average_fitness(population)
    f_best = max(population_fitness)
    f_worst = min(population_fitness)
    n = (lt_max - lt_min) / 2 

    if offpsring == None:
        for individual in population:
            if f_average >= individual.fitness:
                individual.remaining_lifetime = int(lt_min + n * ((individual.fitness - f_worst) / ((f_average - f_worst) if f_average != f_worst else 1)))
            else:
                individual.remaining_lifetime = int(1/2 * (lt_min + lt_max) + n * ((individual.fitness - f_average) / ((f_best - f_average) if f_best != f_average else 1)))
    else:
        if f_average >= offpsring.fitness:
            offpsring.remaining_lifetime = int(lt_min + n * ((offpsring.fitness - f_worst) / ((f_average - f_worst) if f_average != f_worst else 1)))
        else:
            offpsring.remaining_lifetime = int(1/2 * (lt_min + lt_max) + n * ((offpsring.fitness - f_average) / ((f_best - f_average) if f_best != f_average else 1)))

        return offpsring
        
    return population

''' 
Function to adjust the remaining lifetime of each individual in the population 
If the remaining lifetime of an individual is 0, the individual is removed from the population to control population size

Parameters:
----------
population : list
    The population to adjust the remaining lifetime of individuals

best_individual_fitness : int
    The best fitness value of the population

Returns:
-------
population : list
    The population with the individuals with remaining lifetime adjusted and the individuals with remaining lifetime equal to 0 removed

'''
def rlt_adjustment(population, best_individual_fitness):
    print("Best individual fitness: " + str(best_individual_fitness))
    print("Population before adjustment: ")
    for individual in population:
        print("Individual: " + str(individual.test_suite) + " - Fitness: " + str(individual.fitness) + " - Remaining lifetime: " + str(individual.remaining_lifetime))

    print("------------------------------------")
    for individual in population:
        if individual.fitness < best_individual_fitness:
            individual.remaining_lifetime = individual.remaining_lifetime - 1
    
    population = [individual for individual in population if individual.remaining_lifetime > 0]

    print("Population after adjustment: ")
    for individual in population:
        print("Individual: " + str(individual.test_suite) + " - Fitness: " + str(individual.fitness) + " - Remaining lifetime: " + str(individual.remaining_lifetime))

    return population

'''
Function that calculates the number of new chromossomes to be added to the population

Parameters:
----------
current_best_fitness : int
    The best fitness value of current iteration

old_best_fitness : int
    The best fitness value of previous iteration

initial_best_fitness : int
    The best fitness value of initial iteration

current_number_generation : int
    The current number of generation of the algorithm

max_generations : int
    The maximum number of generations of the algorithm

Returns:
-------
growth_size : int
    The number of new chromossomes to be added to the population
'''
def calculate_growth_size(current_best_fitness, old_best_fitness, initial_best_fitness, current_number_generation, max_generations, alpha):
    return int(alpha * (max_generations - current_number_generation) * ((current_best_fitness - old_best_fitness) / initial_best_fitness))

''' 
Function that implements the population resizing process adapted by Rajakumar and George from "APOGA: An Adaptive Population Pool Size Based Genetic Algorithm", DOI: https://doi.org/10.1016/j.aasri.2013.10.043

Parameters:
----------
population : list
    The population to adjust the remaining lifetime of individuals

current_best_fitness : int
    The best fitness value of current iteration

old_best_fitness : int
    The best fitness value of previous iteration

initial_best_fitness : int
    The best fitness value of initial population

current_iteration_number : int
    The current number of generation of the algorithm

number_iterations : int
    The number of iterations of the algorithm

metadata : dict
    The metadata of the class context

configurations : dict
    The configurations of the algorithm

Returns:
-------
population : list
    The population with the new chromossomes added and the individuals with remaining lifetime equal to 0 removed

number_iterations : int
    The number of iterations of the algorithm updated for the next generation to apply the verification of iteration limit

Notes: old_best_fitness must be replaced by the current_best_fitness if the current population fitness is better than the previous population fitness
       current_best_fitness is a parameter so in the main loop of the algorithm a simple verification if the number_iterations is reseted to 0 is needed to update the old_best_fitness
'''
def population_resizing(population, current_best_fitness, old_best_fitness, initial_best_fitness, current_number_generation, number_iterations, metadata, configurations):
    if current_best_fitness > old_best_fitness:
        print("Best fitness improved")
        best_individual_fitness = current_best_fitness
        population = grow_population(population, current_best_fitness, old_best_fitness, initial_best_fitness, current_number_generation, best_individual_fitness, configurations, metadata)
        number_iterations = 0
    elif number_iterations >= int(configurations.fitness_iteration_limit.value):
        print("Fitness iteration limit reached")
        best_individual_fitness = old_best_fitness
        population = grow_population(population, current_best_fitness, old_best_fitness, initial_best_fitness, current_number_generation, best_individual_fitness, configurations, metadata)
        number_iterations = 0
    else:
        best_individual_fitness = old_best_fitness
        population = shrink_population(population, best_individual_fitness, configurations)
        number_iterations += 1
    
    return population, number_iterations

'''
Function that implements the population growth process adapted by Rajakumar and George from "APOGA: An Adaptive Population Pool Size Based Genetic Algorithm", DOI: https://doi.org/10.1016/j.aasri.2013.10.043

Parameters:
----------
population : list
    The population to adjust the remaining lifetime of individuals

current_best_fitness : int
    The best fitness value of current iteration

old_best_fitness : int
    The best fitness value of previous iteration

initial_best_fitness : int
    The best fitness value of initial population

current_number_generation : int  
    The current number of generation of the algorithm

best_individual_fitness : int
    The best fitness value of the population

configurations : dict
    The configurations of the algorithm

metadata : dict
    The metadata of the class context

Returns:
-------
population : list
    The population with the new chromossomes added and the individuals with remaining lifetime adjusted and the individuals with remaining lifetime equal to 0 removed
'''
def grow_population(population, current_best_fitness, old_best_fitness, initial_best_fitness, current_number_generation, best_individual_fitness, configurations, metadata):
    print("Growth population")
    alpha = float(configurations.alpha.value)
    print("Alpha: " + str(alpha))
    growth_size = calculate_growth_size(current_best_fitness, old_best_fitness, initial_best_fitness, current_number_generation, int(configurations.max_number_generations.value), alpha)
    if growth_size > 0:
        new_individuals = create_population(metadata, growth_size, configurations)
        new_individuals_fitness = obtain_fitness_values(new_individuals)
        print("Growth size:" + str(growth_size) + "New individuals size: " + str(len(new_individuals)))
        new_individuals = rlt_setting(new_individuals, new_individuals_fitness, int(configurations.lt_max.value), int(configurations.lt_min.value), None)

        print("Old population size grow: " + str(len(population)))
        for i in population:
            print("Individual: " + str(i.test_suite) + " - Fitness: " + str(i.fitness) + " - Remaining lifetime: " + str(i.remaining_lifetime))

        population.extend(new_individuals)

        print("-----------------------------")

        print("New population size grow: " + str(len(population)))
        for i in population:
            print("Individual: " + str(i.test_suite) + " - Fitness: " + str(i.fitness) + " - Remaining lifetime: " + str(i.remaining_lifetime))
        print("-----------------------------")

    population = rlt_adjustment(population, best_individual_fitness)

    return population
    
'''
Function that implements the population shrink process adapted by Rajakumar and George from "APOGA: An Adaptive Population Pool Size Based Genetic Algorithm", DOI: https://doi.org/10.1016/j.aasri.2013.10.043

Parameters:
----------
population : list
    The population to adjust the remaining lifetime of individuals

configurations : dict
    The configurations of the algorithm

Returns:
-------
population : list
    The population with the individuals with remaining lifetime adjusted and the individuals with remaining lifetime equal to 0 removed
'''
def shrink_population(population, best_individual_fitness, configurations):
    print("Shrink population")
    individuals_least_rlt = sorted(population, key=lambda x:x.remaining_lifetime)

    print("Old population size shrink: " + str(len(population)))

    for individual in range(int(len(individuals_least_rlt) * float(configurations.population_decrease_rate.value))):
        print("Selected individual to remove: " + str(individual))
        population.remove(individuals_least_rlt[individual])
    print("-----------------------------")

    population = rlt_adjustment(population, best_individual_fitness)

    print("New population size shrink: " + str(len(population)))

    return population


'''
Function to obtain the best individual of a population

Parameters:
----------
population : list
    The population to obtain the best individual from

Returns:
-------
best_individuals_sorted[0] : Solution
    The best individual of the population
'''
def obtain_best_individual(population):
    best_individuals_sorted = sorted(population, key=lambda x:x.fitness, reverse=True)
    return best_individuals_sorted[0]
