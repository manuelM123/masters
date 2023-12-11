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
        solution.adaptive_mutation_rate = random.uniform(0, 0.25)
        util.write_metadata("results/intermediate_test_suite", solution.test_suite, metadata)
        calculate_coverage_fitness(solution, str(configurations.fitness_function_type.value))
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
def create_offspring(test_suite, configurations):
    individual = Solution()
    individual.test_suite = test_suite
    calculate_coverage_fitness(individual, str(configurations.fitness_function_type.value))
    
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
def rlt_setting(population, population_fitness, lt_max, lt_min):
    f_average = calculate_average_fitness(population)
    f_best = max(population_fitness)
    f_worst = min(population_fitness)
    n = 1/2 * (lt_max - lt_min) 

    for individual in population:
        if f_average >= individual.fitness:
            individual.remaining_lifetime = lt_min + n * ((individual.fitness - f_worst) / (f_average - f_worst))
        else:
            individual.remaining_lifetime = 1/2 * (lt_min + lt_max) + n * ((individual.fitness - f_average) / (f_best - f_average))

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
    for individual in population:
        if individual.fitness != best_individual_fitness:
            individual.remaining_lifetime = individual.remaining_lifetime - 1

        if individual.remaining_lifetime <= 0:
            population.pop(population.index(individual))

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

current_iteration_number : int
    The current number of generation of the algorithm

max_generations : int
    The maximum number of generations of the algorithm

Returns:
-------
growth_size : int
    The number of new chromossomes to be added to the population
'''
def calculate_growth_size(current_best_fitness, old_best_fitness, initial_best_fitness, current_iteration_number, max_generations):
    value = random.uniform(0,1)
    return value * (max_generations - current_iteration_number) * ((current_best_fitness - old_best_fitness) / initial_best_fitness)

''' 
Function that implements the population resizing process adapted by Rajakumar and George from "APOGA: An Adaptive Population Pool Size Based Genetic Algorithm"

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
def population_resizing(population, current_best_fitness, old_best_fitness, initial_best_fitness, current_iteration_number, number_iterations, metadata, configurations):
    if current_best_fitness > old_best_fitness:
        best_individual_fitness = current_best_fitness
        population = grow_population(population, current_best_fitness, old_best_fitness, initial_best_fitness, current_iteration_number, best_individual_fitness, configurations, metadata)
        number_iterations = 0
    elif number_iterations >= int(configurations.fitness_iteration_limit.value):
        best_individual_fitness = old_best_fitness
        population = grow_population(population, current_best_fitness, old_best_fitness, initial_best_fitness, current_iteration_number, best_individual_fitness, configurations, metadata)
        number_iterations = 0
    else:
        population = shrink_population(population, configurations)
        number_iterations += 1
    
    return population, number_iterations

'''
Function that implements the population growth process adapted by Rajakumar and George from "APOGA: An Adaptive Population Pool Size Based Genetic Algorithm"

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
def grow_population(population, current_best_fitness, old_best_fitness, initial_best_fitness, current_iteration_number, best_individual_fitness, configurations, metadata):
    growth_size = calculate_growth_size(current_best_fitness, old_best_fitness, initial_best_fitness, current_iteration_number, int(configurations.max_number_generations.value))
    new_individuals = create_population(metadata, growth_size, configurations)
    new_individuals_fitness = obtain_fitness_values(new_individuals)
    new_individuals = rlt_setting(new_individuals, new_individuals_fitness, int(configurations.lt_max.value), int(configurations.lt_min.value))
    population.extend(new_individuals)
    population = rlt_adjustment(population, best_individual_fitness)

    return population
    
'''
Function that implements the population shrink process adapted by Rajakumar and George from "APOGA: An Adaptive Population Pool Size Based Genetic Algorithm"

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
def shrink_population(population, configurations):
    individuals_least_rlt = sorted(population, key=lambda x:x.remaining_lifetime)
    for individual in range(individuals_least_rlt * int(configurations.population_decrease_rate.value)):
        population.pop(population.index(individual))

    return population