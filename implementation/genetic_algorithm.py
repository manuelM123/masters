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


# ------------ Genetic algorithm auxiliary functions ------------
    
'''
Function to initialize each generation during the genetic algorithm execution

Returns:
-------
new_population : list
    A list containing the new population of the genetic algorithm

first_parents_list : list
    A list containing the first parents selected for the crossover operation

second_parents_list : list
    A list containing the second parents selected for the crossover operation

population_fitness : list	
    A list containing the fitness values of the population
'''
def initialize_generation(population):
    new_population = []
    first_parents_list = []
    second_parents_list = []
    population_fitness = obtain_fitness_values(population)
    
    return new_population, first_parents_list, second_parents_list, population_fitness    

'''
Function to update the genetic algorithm attributes after each generation

Parameters:
----------
new_population : list
    The new population of the genetic algorithm

current_number_generation : int
    The current number of the generation

old_best_fitness : int
    The best fitness value of the previous generation

generations_without_fitness_improvement : int
    The number of generations without fitness improvement

configurations : dict
    The configurations of the genetic algorithm

Returns:
-------
population : list
    The population of the genetic algorithm

population_fitness : list
    A list containing the fitness values of the population

current_number_generation : int
    The current number of the generation

old_best_fitness : int
    The best fitness value of updated for the next generation

generations_without_fitness_improvement : int
    The number of generations without fitness improvement
'''
def update_genetic_algorithm_attributes(population, new_population, current_number_generation, old_best_fitness, generations_without_fitness_improvement, configurations):
    # If the new population is not empty, the population is updated
    if len(new_population) > 1:
        population = new_population
    population_fitness = obtain_fitness_values(population)
    current_best_fitness = obtain_best_fitness(population_fitness)
    current_number_generation += 1
    if current_best_fitness > old_best_fitness:
        generations_without_fitness_improvement = 0
    else:
        generations_without_fitness_improvement += 1

    population = rlt_setting(population, population_fitness, int(configurations.lt_max.value), int(configurations.lt_min.value), None)
    print("Old best fitness: " + str(old_best_fitness))
    old_best_fitness = current_best_fitness

    return population, population_fitness, current_number_generation, old_best_fitness, generations_without_fitness_improvement

# --------------------------------------------------------------

# Initializing parameters and variables for the genetic algorithm
metadata = util.read_metadata(util.obtain_configuration("config.ini", "metadata", "metadata_location"))
population = create_population(metadata, int(configurations.population_size.value), configurations)
population_fitness = obtain_fitness_values(population)
initial_best_fitness = obtain_best_fitness(population_fitness)
current_best_fitness = 0
old_best_fitness = 0
current_number_generation = 1
iteration_number_population_control = 1
generations_without_fitness_improvement = 0
crossover_rate = float(configurations.crossover_rate.value)
mutation_rate = float(configurations.mutation_rate.value)
individual_suspended = None
mutated_individual_index = None
# ----------------------------------------------

# Genetic algorithm population remaining life time (RLT) calculation for individuals
population = rlt_setting(population, population_fitness, int(configurations.lt_max.value), int(configurations.lt_min.value), None)

# ---- Genetic algorithm execution ----
while current_number_generation <= int(configurations.max_number_generations.value) and generations_without_fitness_improvement <= int(configurations.fitness_max_stagnation_period.value):
    
    new_population, first_parents_list, second_parents_list, population_fitness = initialize_generation(population)

    while len(new_population) < len(population):
        # ------------------------ Selection operations -------------------

        if configurations.selection_type.value == "adaptive":
            # ------------ ADAPTIVE SELECTION METHOD ------------
            first_parents_list, second_parents_list = select(population, population_fitness, int(configurations.tournament_size.value), configurations.selection_type.value)
            # Adaptive selection method does not implement mutation operations
            if len(first_parents_list) > 0 and len(second_parents_list) > 0: 
                new_population = adaptive_selection_method_lists(first_parents_list, second_parents_list, population, population_fitness, configurations, new_population, metadata)
                print("New population size: " + str(len(new_population)))
            else:
                break
            # ---------------------------------------------

        else:
            parents_selected = select(population, population_fitness, int(configurations.tournament_size.value), configurations.selection_type.value)

            # Consider self_adaptive crossover suspended individual
            if individual_suspended != None:
                parents_selected.pop(random.randint(0, len(parents_selected) - 1))
                parents_selected.append(individual_suspended)

            print("Parents selected: ")
            for i in parents_selected:
                print("Parent: " + str(i.test_suite) + " - Fitness: " + str(i.fitness) + " - Remaining life time: " + str(i.remaining_lifetime) + " - Adaptive max selections: " + str(i.adaptive_max_selections))
            print("-------------------------------------------")

        # ----------------------------------------------------------------

            # --- Crossover operations ---
            inputs = [current_best_fitness, iteration_number_population_control, stats.variance(population_fitness)]
            offsprings = crossover(parents_selected, metadata, current_number_generation, inputs, configurations, configurations.crossover_type.value)
            if configurations.crossover_type.value == 'self_adaptive':
                individual_suspended = offsprings[2]
                mutated_individual_index = offsprings[3]
                offspring = rlt_setting(population, population_fitness, int(configurations.lt_max.value), int(configurations.lt_min.value), offsprings[mutated_individual_index])
                if mutated_individual_index != -1:
                    new_population.append(offsprings[mutated_individual_index])
                else:
                    new_population.append(offsprings[0])
                    new_population.append(offsprings[1])
            else:
                if configurations.crossover_type.value == 'deterministic' or configurations.crossover_type.value == 'adaptive':
                    crossover_rate = crossover(parents_selected, metadata, current_number_generation, inputs, configurations, configurations.crossover_type.value)

                    if crossover_rate > random.random():
                        offsprings = uniform_crossover(parents_selected, configurations, metadata)
                    else:
                        offsprings = parents_selected
                else:
                    if crossover_rate > random.random():
                        offsprings = crossover(parents_selected, metadata, current_number_generation, inputs, configurations, configurations.crossover_type.value)
                    else:
                        offsprings = parents_selected 
                    
                # ----------------------------

                # Mutation operations

                # NOTE: IN SELF_ADAPTIVE CROSSOVER OPERATION, THE MUTATION OPERATION CAN CALL THE ADAPTIVE MUTATION METHOD THAT DOES NOT RETURN A INDIVIDUAL, FIX THIS BY PERFORMING A MUTATION METHOD AFTER THE MUTATION RATE ADJUSTMENT
                pass

                # ----------------------------
                new_population.append(offsprings[0])
                new_population.append(offsprings[1])

        print("Current Population")
        for i in range(len(population)):
            print("-------------------------------------")
            print("Test Suite - " + str(population[i].test_suite))
            print("Fitness - " + str(population[i].fitness))
            print("Adaptive Max Selections - " + str(population[i].adaptive_max_selections))
            print("Remaining Life Time - " + str(population[i].remaining_lifetime))
            print("-----------------------------------")

    # ------------ POPULATION CONTROL METHOD ------------
    if bool(configurations.population_control.value):
        print("Old population size: " + str(len(population)))
        print("New population size: " + str(len(new_population)))
        if len(new_population) > 1:
            new_population_fitness = obtain_fitness_values(new_population)
            current_best_fitness = obtain_best_fitness(new_population_fitness)
            new_population, iteration_number_population_control = population_resizing(new_population, current_best_fitness, old_best_fitness, 
                                                                                  initial_best_fitness, current_number_generation, iteration_number_population_control,
                                                                                  metadata, configurations)
    # ---------------------------------------------

    # Reset population and iterations
    print("New population size: " + str(len(new_population)))
    print("New population individuals")
    #for i in new_population:
        #print("New individual:" + str(i.test_suite))

    print("------------------------------------------------------------------")

    population, population_fitness, current_number_generation, old_best_fitness, generations_without_fitness_improvement = update_genetic_algorithm_attributes(population, new_population, 
                                                                                                                                                               current_number_generation, old_best_fitness, 
                                                                                                                                                               generations_without_fitness_improvement, configurations)
    
    print("Generation: " + str(current_number_generation) + " - Best fitness: " + str(current_best_fitness) + " - Average fitness: " + str(round(calculate_average_fitness(population),2)) 
          + " - Generations without fitness improvement: " + str(generations_without_fitness_improvement))
    
    '''
    print(" ------- Current population ------- ")
    for i in population:
        print("Individual: " + str(i.test_suite) + " - Fitness: " + str(i.fitness) + " - Remaining life time: " + str(i.remaining_lifetime) + " - Adaptive max selections: " + str(i.adaptive_max_selections))
    '''
          
# ---------------------------------------------------------------

# Print the new population
print("-----------------------------------")
print("New Population")
for i in range(len(new_population)):
    print("-------------------------------------")
    print("Test Suite - " + str(new_population[i].test_suite))
    print("Fitness - " + str(new_population[i].fitness))
    print("Crossover Rate - " + str(new_population[i].adaptive_crossover_rate))
    print("Mutation Rate - " + str(new_population[i].adaptive_mutation_rate))
    print("Adaptive Max Selections - " + str(new_population[i].adaptive_max_selections))
    print("Remaining Life Time - " + str(new_population[i].remaining_lifetime))
