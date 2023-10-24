from cut import *
from solution import *
from operations.selection import * 
from operations.fitness_functions import *
import utilities as util

from enum import Enum

# Enum class to store the configurations
class configurations(Enum):
    population_size = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "population_size")
    max_number_generations = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "max_number_generations")
    fitness_max_stagnation_period = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "fitness_max_stagnation_period")
    max_number_fitness_evaluations = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "max_number_fitness_evaluations")
    fitness_function_type = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "fitness_function_type")

    selection_type = util.obtain_configuration("config.ini", "genetic_operators_configurations", "selection_type")
    crossover_type = util.obtain_configuration("config.ini", "genetic_operators_configurations", "crossover_type")
    crossover_rate = util.obtain_configuration("config.ini", "genetic_operators_configurations", "crossover_rate")
    mutation_type = util.obtain_configuration("config.ini", "genetic_operators_configurations", "mutation_type")
    mutation_rate = util.obtain_configuration("config.ini", "genetic_operators_configurations", "mutation_rate")

# A population is a set of test suites where each of them is a list of test cases
def create_population(metadata, max_number_functions, max_number_test_cases, population_size):
    population = []
    for individual in range(population_size):
        solution = Solution()
        # calculate fitness method using coverage module
        # a specification of each type of coverage is needed 

        solution.generate_test_suite(metadata, max_number_functions, max_number_test_cases)
        util.write_metadata("results/intermediate_test_suite", solution.test_suite, metadata)
        calculate_coverage_fitness(solution, str(configurations.fitness_function_type.value))

        population.append(solution)

    return population

class_test = calorie_intake_calc(83.9,189,22,'M',None,'S')
metadata = util.read_metadata(util.obtain_configuration("config.ini", "metadata", "metadata_location"))

population = create_population(metadata, 5, 10, 10)
population_fitness = obtain_fitness_values(population)

sorted_fitness = Selection(str(configurations.selection_type.value)).select(population, population_fitness)
for i in range(len(sorted_fitness)):
    print(sorted_fitness[i])

print("Test Suites Population")
for i in range(len(population)):
    print("-------------------------------------")
    print("Test Suite - " + str(population[i].test_suite))
    print("Fitness - " + str(population[i].fitness))
print("-----------------------------------")

print("Fitness Population")
print(population_fitness)
print("-----------------------------------")


parents_selection = Selection(str(configurations.selection_type.value)).select(population, population_fitness)

for individual in parents_selection:
    print("Parent - " + str(individual.test_suite))
    print("Fitness - " + str(individual.fitness))