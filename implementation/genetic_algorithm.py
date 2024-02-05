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

'''
Class that contains the configurations of the genetic algorithm

It is used to store the configurations of the genetic algorithm, genetic operators, genetic algorithm optimizations and file paths
'''
class configurations(Enum):
    # Genetic algorithm configurations
    max_number_functions = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "max_number_functions")
    max_number_test_cases = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "max_number_test_cases")
    tournament_size = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "tournament_size")
    max_number_generations = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "max_number_generations")
    fitness_max_stagnation_period = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "fitness_max_stagnation_period")
    max_number_fitness_evaluations = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "max_number_fitness_evaluations")
    fitness_function_type = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "fitness_function_type")
    fitness_iteration_limit = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "fitness_iteration_limit")

    # Genetic operators configurations
    population_size = util.obtain_configuration("config.ini", "genetic_operators_configurations", "population_size")
    population_control = util.obtain_configuration("config.ini", "genetic_operators_configurations", "population_control")
    selection_type = util.obtain_configuration("config.ini", "genetic_operators_configurations", "selection_type")
    crossover_type = util.obtain_configuration("config.ini", "genetic_operators_configurations", "crossover_type")
    crossover_rate = util.obtain_configuration("config.ini", "genetic_operators_configurations", "crossover_rate")
    crossover_rate_adjustment_type = util.obtain_configuration("config.ini", "genetic_operators_configurations", "crossover_rate_adjustment_type")
    mutation_type = util.obtain_configuration("config.ini", "genetic_operators_configurations", "mutation_type")
    mutation_rate = util.obtain_configuration("config.ini", "genetic_operators_configurations", "mutation_rate")
    mutation_rate_adjustment_type = util.obtain_configuration("config.ini", "genetic_operators_configurations", "mutation_rate_adjustment_type")
    
    # Genetic algorithm optimizations configurations
    population_decrease_rate = util.obtain_configuration("config.ini", "genetic_algorithm_optimizations_configurations", "population_decrease_rate")
    uniform_number_crossover = util.obtain_configuration("config.ini", "genetic_algorithm_optimizations_configurations", "uniform_number_crossover")
    lt_max = util.obtain_configuration("config.ini", "genetic_algorithm_optimizations_configurations", "lt_max")
    lt_min = util.obtain_configuration("config.ini", "genetic_algorithm_optimizations_configurations", "lt_min")

    # File paths
    fuzzy_membership_path = util.obtain_configuration("config.ini", "file_paths", "fuzzy_membership_functions")

# Initializing parameters and variables for the genetic algorithm
metadata = util.read_metadata(util.obtain_configuration("config.ini", "metadata", "metadata_location"))
population = create_population(metadata, int(configurations.population_size.value), configurations)
population_fitness = obtain_fitness_values(population)
current_number_generation = 0
generations_without_fitness_improvement = 0

# Genetic algorithm population remaining life time (RLT) calculation for individuals
population = rlt_setting(population, population_fitness, int(configurations.lt_max.value), int(configurations.lt_min.value), None)

while current_number_generation <= int(configurations.max_number_generations.value) and generations_without_fitness_improvement <= int(configurations.fitness_max_stagnation_period.value):
    new_population = []
    first_parents_list = []
    second_parents_list = []

    while len(new_population) < len(population):
        # --- Selection operations ---

        if configurations.selection_type.value == "adaptive":
            first_parents_list, second_parents_list = select(population, population_fitness, int(configurations.tournament_size.value), configurations.selection_type.value)
            # Adaptive selection method was applied (mention that this adaptive selection method was made for even number of population size)
            # the authors do not mention which type of crossover to use, so we will use the uniform crossover and specified that each
            # individual will reproduce with the other individual in the list so there is not crossover rate to apply
            if len(first_parents_list) > 0 and len(second_parents_list) > 0: 
                for individual in range(len(first_parents_list)):
                    offsprings = uniform_crossover([first_parents_list[individual], second_parents_list[len(first_parents_list) - (individual + 1)]], configurations)
                    for offspring in offsprings:
                        offspring = rlt_setting(population, population_fitness, int(configurations.lt_max.value), int(configurations.lt_min.value), offspring)
                        print("Offspring: " + str(offspring.test_suite) + " - " + str(offspring.fitness) + " - " + str(offspring.remaining_lifetime))
                        new_population.append(offspring)
            break

        else:
            parents_selected = select(population, population_fitness, int(configurations.tournament_size.value), configurations.selection_type.value)

        # ----------------------------
            
        # --- Crossover operations ---

        pass

        # ----------------------------

        # Mutation operations
        pass

        # ----------------------------

    # Population control operations
        if bool(configurations.population_control.value):
            pass

    pass

print("Test Suites Population")
for i in range(len(population)):
    print("-------------------------------------")
    print("Test Suite - " + str(population[i].test_suite))
    print("Fitness - " + str(population[i].fitness))
    print("Crossover Rate - " + str(population[i].adaptive_crossover_rate))
    print("Mutation Rate - " + str(population[i].adaptive_mutation_rate))
    print("Adaptive Max Selections - " + str(population[i].adaptive_max_selections))
    print("Remaining Life Time - " + str(population[i].remaining_lifetime))
print("-----------------------------------")