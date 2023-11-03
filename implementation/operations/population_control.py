from cut import *
from operations.fitness_functions import *
from solution import *
import utilities as util

'''
Function to create the initial population of random generated test suites with settings from the configuration file

Parameters:
    metadata: metadata of the class under test
    max_number_functions: maximum number of functions to be used in the test suite
    max_number_test_cases: maximum number of test cases to be used in the test suite
    population_size: size of the population to be generated

Returns:
    population: list of test suites
'''
def create_population(metadata, population_size, configurations):
    population = []
    for individual in range(population_size):
        solution = Solution()
        solution.generate_test_suite(metadata, int(configurations.max_number_functions.value), int(configurations.max_number_test_cases.value))
        util.write_metadata("results/intermediate_test_suite", solution.test_suite, metadata)
        calculate_coverage_fitness(solution, str(configurations.fitness_function_type.value))
        population.append(solution)

    return population

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
'''
def rlt_setting(population, population_fitness, lt_max, lt_min):
    f_average = calculate_average_fitness(population)
    f_best = max(population_fitness)
    f_worst = min(population_fitness)
    n = 1/2 * (lt_max - lt_min) 

    for individual in population:
        if f_average >= individual.fitness:
            individual.remaining_lifetime = lt_min + n * (individual.fitness - f_worst) / f_average - f_worst
        else:
            individual.remaining_lifetime = 1/2 * (lt_min + lt_max) + n * (individual.fitness - f_average) / f_best - f_average

''' 
Function to adjust the remaining lifetime of each individual in the population 
If the remaining lifetime of an individual is 0, the individual is removed from the population to control population size

Parameters:
----------
population : list
    The population to adjust the remaining lifetime of

'''
def rlt_adjustment(population):
    for individual in population:
        individual.remaining_lifetime = individual.remaining_lifetime - 1

        if individual.remaining_lifetime == 0:
            population.pop(population.index(individual))

    return population

'''
Function that calculates the number of new chromossomes to be added to the population

Parameters:
----------
current_best_fitness : int
    The best fitness value of current generation

old_best_fitness : int
    The best fitness value of previous generation

initial_best_fitness : int
    The best fitness value of initial generation

max_generations : int
    The maximum number of generations of the algorithm

current_number_iteration : int
    The current number of generation of the algorithm

value : int
    A random value between [0,1] to be used in the calculation of the growth size of chromossomes

Returns:
-------
growth_size : int
    The number of new chromossomes to be added to the population
'''
def calculate_growth_size(current_best_fitness, old_best_fitness_iteration, initial_best_fitness, current_number_iteration, configurations):
    value = random.uniform(0,1)
    return value * (int(configurations.max_number_generations) - current_number_iteration) * (current_best_fitness - old_best_fitness_iteration) / initial_best_fitness

''' 
Function that implements the population resizing process adapted by Rajakumar and George from "APOGA: An Adaptive Population Pool Size Based Genetic Algorithm"

Parameters:
----------
population : list
    The population to adjust the remaining lifetime of individuals

current_best_fitness : int
    The best fitness value of current generation

old_best_fitness_iteration : int
    The best fitness value of previous generation    

old_best_fitness : int
    The old best fitness value of the population

initial_best_fitness : int
    The best fitness value of initial generation

current_number_iteration : int
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
'''
def population_resizing(population, current_best_fitness, old_best_fitness_iteration, old_best_fitness, initial_best_fitness, current_number_iteration, number_iterations, metadata, configurations):
    if current_best_fitness > old_best_fitness or number_iterations == int(configurations.fitness_iteration_limit.value):
        growth_size = calculate_growth_size(current_best_fitness, old_best_fitness_iteration, initial_best_fitness, current_number_iteration)
        population = rlt_adjustment(population)
        number_iterations = 0

        new_individuals = create_population(metadata, growth_size, configurations)
        population.extend(new_individuals)
    else:
        individuals_least_rlt = sorted(population, key=lambda x:x.remaining_lifetime)
        for individual in range(individuals_least_rlt * int(configurations.population_decrease_rate.value)):
            population.pop(population.index(individual))

    return population, number_iterations