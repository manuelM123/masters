from cut import *
from solution import *
from operations.selection import * 
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


class_test = calorie_intake_calc(83.9,189,22,'M',None,'S')
metadata = util.read_metadata(util.obtain_configuration("config.ini", "metadata", "metadata_location"))
solution = Solution()
test_suite = solution.generate_test_suite(metadata, 5, 10)
util.write_metadata("results/intermediate_test_suite", test_suite, metadata)

# population_fitness = [10,20,40,30,25]
# parents_selection = Selection("roulette_wheel").select(test_suite, population_fitness)