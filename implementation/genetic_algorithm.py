from cut import *
from solution import *
from operations.selection import * 
from operations.fitness_functions import *
from operations.population_control import *
from operations.crossover import *
from operations.mutation import *
from operations.fuzzy_system import *
import utilities as util
import sys
import statistics as stats
sys.dont_write_bytecode = True
from enum import Enum

# Enum class to store the configurations
class configurations(Enum):
    population_size = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "population_size")
    max_number_functions = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "max_number_functions")
    max_number_test_cases = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "max_number_test_cases")
    tournament_size = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "tournament_size")
    max_number_generations = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "max_number_generations")
    fitness_max_stagnation_period = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "fitness_max_stagnation_period")
    max_number_fitness_evaluations = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "max_number_fitness_evaluations")
    fitness_function_type = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "fitness_function_type")

    selection_type = util.obtain_configuration("config.ini", "genetic_operators_configurations", "selection_type")

    crossover_type = util.obtain_configuration("config.ini", "genetic_operators_configurations", "crossover_type")
    crossover_rate = util.obtain_configuration("config.ini", "genetic_operators_configurations", "crossover_rate")
    crossover_rate_adjustment_type = util.obtain_configuration("config.ini", "genetic_operators_configurations", "crossover_rate_adjustment_type")

    mutation_type = util.obtain_configuration("config.ini", "genetic_operators_configurations", "mutation_type")
    mutation_rate = util.obtain_configuration("config.ini", "genetic_operators_configurations", "mutation_rate")
    mutation_rate_adjustment_type = util.obtain_configuration("config.ini", "genetic_operators_configurations", "mutation_rate_adjustment_type")
    
    fitness_iteration_limit = util.obtain_configuration("config.ini", "genetic_operators_configurations", "fitness_iteration_limit")
    lt_max = util.obtain_configuration("config.ini", "genetic_operators_configurations", "lt_max")
    lt_min = util.obtain_configuration("config.ini", "genetic_operators_configurations", "lt_min")
    uniform_number = util.obtain_configuration("config.ini", "genetic_operators_configurations", "uniform_number")

    fuzzy_membership_path = util.obtain_configuration("config.ini", "file_paths", "fuzzy_membership_functions")


metadata = util.read_metadata(util.obtain_configuration("config.ini", "metadata", "metadata_location"))
population = create_population(metadata, int(configurations.population_size.value), configurations)
population_fitness = obtain_fitness_values(population)

print("Fitness Population")
print(population_fitness)
print("-----------------------------------")

print("Variance of fitness population : " + str(stats.variance(population_fitness)))

#for i in range(5):
#    inputs = [random.uniform(0.0, 1.0), random.randint(0, 20), random.uniform(0.0, 0.2)]
#    print("Mutation operation")
#    print("-----------------------------------")
#    print("Before mutation : " + str(population[0].test_suite))
#    population[0].test_suite = mutation(population[0].test_suite, metadata, inputs, configurations, configurations.mutation_type.value)
#    print("After mutation : " + str(population[0].test_suite))
#    print("|--------------------------------------------|")

for i in range(2):
    print("Fuzzy System Calculation")
    print("--------------------------------")
    
    inputs = [random.uniform(0.0, 1.0), random.randint(0, 20), random.uniform(0.0, 0.2)]

    print("Inputs")
    print(inputs)

    genetic_operator_rate = crossover(population, 0, inputs, configurations, configurations.crossover_type.value)
    print("The genetic operator is crossover with the adjusted rate of " + str(genetic_operator_rate))
    genetic_operator_rate = mutation(population, 0, inputs, configurations, configurations.mutation_type.value)
    print("The genetic operator is mutation with the adjusted rate of " + str(genetic_operator_rate))
    print("|-------------------------|")

print("Test Suites Population")
for i in range(len(population)):
    print("-------------------------------------")
    print("Test Suite - " + str(population[i].test_suite))
    print("Fitness - " + str(population[i].fitness))
    print("Crossover Rate - " + str(population[i].adaptive_crossover_rate))
    print("Mutation Rate - " + str(population[i].adaptive_mutation_rate))
print("-----------------------------------")