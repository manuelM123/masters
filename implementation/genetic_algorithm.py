from cut import *
from solution import *
from operations.selection import * 
from operations.fitness_functions import *
import utilities as util
import sys
sys.dont_write_bytecode = True

from enum import Enum

# Enum class to store the configurations
class configurations(Enum):
    population_size = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "population_size")
    tournament_size = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "tournament_size")
    max_number_generations = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "max_number_generations")
    fitness_max_stagnation_period = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "fitness_max_stagnation_period")
    max_number_fitness_evaluations = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "max_number_fitness_evaluations")
    fitness_function_type = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "fitness_function_type")

    selection_type = util.obtain_configuration("config.ini", "genetic_operators_configurations", "selection_type")
    crossover_type = util.obtain_configuration("config.ini", "genetic_operators_configurations", "crossover_type")
    crossover_rate = util.obtain_configuration("config.ini", "genetic_operators_configurations", "crossover_rate")
    mutation_type = util.obtain_configuration("config.ini", "genetic_operators_configurations", "mutation_type")
    mutation_rate = util.obtain_configuration("config.ini", "genetic_operators_configurations", "mutation_rate")

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
def create_population(metadata, max_number_functions, max_number_test_cases, population_size):
    population = []
    for individual in range(population_size):
        solution = Solution()
        solution.generate_test_suite(metadata, max_number_functions, max_number_test_cases)
        util.write_metadata("results/intermediate_test_suite", solution.test_suite, metadata)
        calculate_coverage_fitness(solution, str(configurations.fitness_function_type.value))

        population.append(solution)

    return population

metadata = util.read_metadata(util.obtain_configuration("config.ini", "metadata", "metadata_location"))
population = create_population(metadata, 5, 10, 10)
population_fitness = obtain_fitness_values(population)

print("Fitness Population")
print(population_fitness)
print("-----------------------------------")

tournament_selection = Selection(str(configurations.selection_type.value)).select(population, population_fitness, int(configurations.tournament_size.value))

print("Tournament selection")
for i in range(len(tournament_selection)):
    print("-------------------------------------")
    print("Test Suite - " + str(tournament_selection[i].test_suite))
    print("Fitness - " + str(tournament_selection[i].fitness))
print("-----------------------------------")

#print("Test Suites Population")
#for i in range(len(population)):
#    print("-------------------------------------")
#    print("Test Suite - " + str(population[i].test_suite))
#    print("Fitness - " + str(population[i].fitness))
#print("-----------------------------------")