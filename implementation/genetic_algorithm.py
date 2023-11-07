from cut import *
from solution import *
from operations.selection import * 
from operations.fitness_functions import *
from operations.population_control import *
from operations.crossover import *
import utilities as util
import sys
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
    mutation_type = util.obtain_configuration("config.ini", "genetic_operators_configurations", "mutation_type")
    mutation_rate = util.obtain_configuration("config.ini", "genetic_operators_configurations", "mutation_rate")
    fitness_iteration_limit = util.obtain_configuration("config.ini", "genetic_operators_configurations", "fitness_iteration_limit")
    lt_max = util.obtain_configuration("config.ini", "genetic_operators_configurations", "lt_max")
    lt_min = util.obtain_configuration("config.ini", "genetic_operators_configurations", "lt_min")
    uniform_number = util.obtain_configuration("config.ini", "genetic_operators_configurations", "uniform_number")


metadata = util.read_metadata(util.obtain_configuration("config.ini", "metadata", "metadata_location"))
population = create_population(metadata, int(configurations.population_size.value), configurations)
population_fitness = obtain_fitness_values(population)

print("Fitness Population")
print(population_fitness)
print("-----------------------------------")

parent1 = random.randint(0, len(population) - 1)
parent2 = random.randint(0, len(population) - 1)

parents = [parent1, parent2]
parents_set = set([parent1, parent2])

while len(parents) != len(parents_set):
    parent2 = random.randint(0, len(population) - 1)

print("Parent 1")
print(population[parent1].test_suite)
print("Length : " + str(len(population[parent1].test_suite)))
print("--------------------------------------------------")

print("Parent 2")
print(population[parent2].test_suite)
print("Length : " + str(len(population[parent2].test_suite)))
print("--------------------------------------------------")

offsprings1 = one_point_crossover([population[parent1], population[parent2]], configurations)
offsprings2 = uniform_crossover([population[parent1], population[parent2]], configurations)

print("First Offspring")
for i in offsprings1:
    print("Offspring")
    print(i.test_suite)
    print("-------")
print("--------------------------------------------------")

print("Second Offspring")
for i in offsprings2:
    print(i.test_suite)
print("--------------------------------------------------")

print("------------------------")


#first_list, second_list = select(population, population_fitness, int(configurations.tournament_size.value), configurations.selection_type.value)
#population = rlt_adjustment(population, max(population_fitness))

#print("Test Suites Population")
#for i in range(len(population)):
#    print("-------------------------------------")
#    print("Test Suite - " + str(population[i].test_suite))
#    print("Fitness - " + str(population[i].fitness))
#print("-----------------------------------")