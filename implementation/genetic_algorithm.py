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
    alpha = util.obtain_configuration("config.ini", "genetic_algorithm_optimizations_configurations", "alpha")

    # File paths
    fuzzy_membership_path = util.obtain_configuration("config.ini", "file_paths", "fuzzy_membership_functions")
    intermediate_test_suite_path = util.obtain_configuration("config.ini", "file_paths", "intermediate_test_suite")
    generation_stats_path = util.obtain_configuration("config.ini", "file_paths", "generation_stats")
    best_generated_test_suite = util.obtain_configuration("config.ini", "file_paths", "best_generated_test_suite")
    generation_data_path = util.obtain_configuration("config.ini", "file_paths", "generation_data")

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
    crossover_rate_values = []
    mutation_rate_values = []

    return new_population, first_parents_list, second_parents_list, population_fitness, crossover_rate_values, mutation_rate_values

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
def update_genetic_algorithm_attributes(population, new_population, current_number_generation, old_best_fitness, generations_without_fitness_improvement, best_fitness_seen, configurations):
    # If the new population is not empty, the population is updated
    if len(new_population) > 0:
        population = new_population
    population_fitness = obtain_fitness_values(population)
    current_best_fitness = obtain_best_fitness(population_fitness)
    current_number_generation += 1
    if current_best_fitness > best_fitness_seen:
        best_fitness_seen = current_best_fitness
        generations_without_fitness_improvement = 0
    else:
        generations_without_fitness_improvement += 1

    population = rlt_setting(population, population_fitness, int(configurations.lt_max.value), int(configurations.lt_min.value), None)
    print("Old best fitness: " + str(old_best_fitness))
    old_best_fitness = current_best_fitness

    return population, current_number_generation, current_best_fitness, old_best_fitness, generations_without_fitness_improvement, best_fitness_seen

'''
Function to print the generation stats

Parameters:
----------
current_number_generation : int
    The current number of the generation

current_best_fitness : int
    The best fitness value of the current generation

population : list
    The population of the genetic algorithm
'''
def generation_stats(current_number_generation, old_best_fitness, current_best_fitness, best_fitness_seen, population, average_crossover_rate_value, average_mutation_rate_value):
    print("------------------------ GENERATION STATS ------------------------")
    print("Generation: " + str(current_number_generation) + " - Old best fitness: " + str(old_best_fitness) + " - Best fitness: " + str(current_best_fitness) + " - Best fitness seen: " + str(best_fitness_seen) + " - Average fitness: " + str(round(calculate_average_fitness(population),2)) 
          + " - Generations without fitness improvement: " + str(generations_without_fitness_improvement) + " - Population size: " + str(len(population)))
    print("------------------------------------------------------------------")

    generation_number_values.append(current_number_generation)
    population_size_values.append(len(population))
    generation_fitness_values.append(current_best_fitness)
    crossover_rate_generations.append(average_crossover_rate_value)
    mutation_rate_generations.append(average_mutation_rate_value)

# --------------------------------------------------------------

# Initializing parameters and variables for the genetic algorithm
metadata = util.read_metadata(util.obtain_configuration("config.ini", "metadata", "metadata_location"))
population = create_population(metadata, int(configurations.population_size.value), configurations)
population_fitness = obtain_fitness_values(population)
initial_best_fitness = obtain_best_fitness(population_fitness)
current_best_fitness = 0
old_best_fitness = 0
best_fitness_seen = population[0].fitness
current_number_generation = 0
iteration_number_population_control = 1
generations_without_fitness_improvement = 0
crossover_rate = float(configurations.crossover_rate.value)
mutation_rate = float(configurations.mutation_rate.value)
individual_suspended = None
mutated_individual_index = None
generation_number_values = []
population_size_values = []
generation_fitness_values = []
crossover_rate_values = []
mutation_rate_values = []
crossover_rate_generations = []
mutation_rate_generations = []
title_crossover_rate = None
title_mutation_rate = None
# ----------------------------------------------

# Genetic algorithm population remaining life time (RLT) calculation for individuals
population = rlt_setting(population, population_fitness, int(configurations.lt_max.value), int(configurations.lt_min.value), None)

# ---- Genetic algorithm execution ----
while current_number_generation < int(configurations.max_number_generations.value) and generations_without_fitness_improvement < int(configurations.fitness_max_stagnation_period.value):
    
    new_population, first_parents_list, second_parents_list, population_fitness, crossover_rate_values, mutation_rate_values = initialize_generation(population)

    print("Generation number: " + str(current_number_generation))
    print("---------------------------------------------------------------")

    while len(new_population) < len(population) and len(population) > 1:
        # ------------------------ Selection Operations -------------------

        if configurations.selection_type.value == "adaptive":
            # ------------ ADAPTIVE SELECTION METHOD ------------

            first_parents_list, second_parents_list = select(population, population_fitness, None, configurations.selection_type.value)
            # Adaptive selection method does not implement mutation operations
            if len(first_parents_list) > 0 and len(second_parents_list) > 0: 
                new_population = adaptive_selection_method_lists(first_parents_list, second_parents_list, population, population_fitness, configurations, new_population, metadata)
                print("New population size: " + str(len(new_population)))
            else:
                print("No parents selected for the adaptive selection method")
                break

            # ------------ END ADAPTIVE SELECTION METHOD ------------
        else:
            parents_selected = select(population, population_fitness, int(configurations.tournament_size.value), configurations.selection_type.value)

            # Consider self_adaptive crossover suspended individual
            if individual_suspended != None:
                print("Suspended individual in selection operation: " + str(individual_suspended.test_suite) + " - Fitness: " + str(individual_suspended.fitness) + " - Remaining life time: " + str(individual_suspended.remaining_lifetime))
                parents_selected.pop(random.randint(0, len(parents_selected) - 1))
                parents_selected.append(individual_suspended)

            print("# ----------- Parents selected ----------- #")
            for i in parents_selected:
                print("Parent: " + str(i.test_suite) + " - Fitness: " + str(i.fitness) + " - Remaining life time: " + str(i.remaining_lifetime) + " - Adaptive max selections: " + str(i.adaptive_max_selections))
            print("-------------------------------------------")

            # Stop the genetic algorithm if there are no parents selected
            if len(parents_selected) < 1:
                break

        # ------------------------ End Selection Operations -------------------

            # ------------------------ Crossover Operations ------------------------

            inputs = [obtain_best_fitness(population_fitness), iteration_number_population_control, stats.variance(population_fitness)]
            if configurations.crossover_type.value == 'self-adaptive':
                # ------------ SELF-ADAPTIVE CROSSOVER METHOD ------------

                offsprings = crossover(parents_selected, metadata, current_number_generation, inputs, configurations, configurations.crossover_type.value, configurations.mutation_type.value)
                individual_suspended = offsprings[2]
                mutated_individual_index = offsprings[3]
                if mutated_individual_index != -1 and mutated_individual_index != None:
                    print("Offsprings before rlt setting self_adaptive: ")
                    print("Offspring 1: " + str(offsprings[0].remaining_lifetime))
                    print("Offspring 2: " + str(offsprings[1].remaining_lifetime))
                    print("#----------------------------------------------------------------#")

                    offspring = rlt_setting(population, population_fitness, int(configurations.lt_max.value), int(configurations.lt_min.value), offsprings[mutated_individual_index])

                    print("Offsprings after rlt setting self_adaptive: ")
                    print("Offspring 1: " + str(offsprings[0].remaining_lifetime))
                    print("Offspring 2: " + str(offsprings[1].remaining_lifetime))
                    print("#----------------------------------------------------------------#")
                    new_population.append(offspring)

                elif mutated_individual_index == -1 or mutated_individual_index == None:
                    print("Offsprings before rlt setting self_adaptive: ")
                    print("Offspring 1: " + str(offsprings[0].remaining_lifetime))
                    print("Offspring 2: " + str(offsprings[1].remaining_lifetime))
                    print("#----------------------------------------------------------------#")

                    for position in range(0, len(offsprings) - 2):
                        offsprings[position] = rlt_setting(population, population_fitness, int(configurations.lt_max.value), int(configurations.lt_min.value), offsprings[position])

                    print("Offsprings after rlt setting self_adaptive: ")
                    print("Offspring 1: " + str(offsprings[0].remaining_lifetime))
                    print("Offspring 2: " + str(offsprings[1].remaining_lifetime))
                    print("#----------------------------------------------------------------#")
                    new_population.append(offsprings[0])
                    new_population.append(offsprings[1])
                
                # ------------ END SELF-ADAPTIVE CROSSOVER METHOD ------------
                    
            else:
                # ------------ DETERMINISTIC AND ADAPTIVE CROSSOVER METHOD ------------ 

                if configurations.crossover_type.value == 'deterministic' or configurations.crossover_type.value == 'adaptive':
                    crossover_rate = crossover(parents_selected, metadata, current_number_generation, inputs, configurations, configurations.crossover_type.value, configurations.mutation_type.value)
                    print("Crossover rate before applying crossover: " + str(crossover_rate))
                    crossover_rate_values.append(crossover_rate)

                    if crossover_rate > random.random():
                        offsprings = uniform_crossover(parents_selected, configurations, metadata)

                    else:
                        print("Crossover operation was not performed")
                        offsprings = parents_selected

                # ------------ END DETERMINISTIC AND ADAPTIVE CROSSOVER METHOD ------------
                        
                # ------------ OTHER CROSSOVER METHODS ------------
                else:
                    if float(configurations.crossover_rate.value) > random.random():
                        offsprings = crossover(parents_selected, metadata, current_number_generation, inputs, configurations, configurations.crossover_type.value, configurations.mutation_type.value)

                    else:
                        print("Crossover operation was not performed")
                        offsprings = parents_selected 

                # ------------ END OTHER CROSSOVER METHODS ------------
                    
                # ------------------------ End Crossover Operations ------------------------       

                # ------------------------ Mutation Operations ------------------------        

                # ------------ DETERMINISTIC AND ADAPTIVE MUTATION METHOD ------------
                        
                if configurations.mutation_type.value == 'deterministic' or configurations.mutation_type.value == 'adaptive':
                    mutation_rate = mutation(None, None, current_number_generation, inputs, configurations, configurations.mutation_type.value)
                    print("Mutation rate before applying mutation: " + str(mutation_rate))	
                    mutation_rate_values.append(mutation_rate)
                    maximum_mutation_rate = 1.0

                    if configurations.mutation_type.value == 'adaptive':
                        maximum_mutation_rate = 0.1

                    if mutation_rate > random.random(0, maximum_mutation_rate):
                        print("Mutation applied to offspring 1 using " + configurations.mutation_type.value + " method | Offspring 1: " + str(offsprings[0].test_suite))
                        offsprings[0] = mutation(offsprings[0], metadata, current_number_generation, inputs, configurations, random.choice(['add_test_case', 'delete_test_case', 'change_parameters']))
                        print("Offspring 1 after mutation: " + str(offsprings[0].test_suite))
                    if mutation_rate > random.random(0, maximum_mutation_rate):
                        print("Mutation applied to offspring 2 using " + configurations.mutation_type.value + " method | Offspring 2: " + str(offsprings[1].test_suite))
                        offsprings[1] = mutation(offsprings[1], metadata, current_number_generation, inputs, configurations, random.choice(['add_test_case', 'delete_test_case', 'change_parameters']))
                        print("Offspring 2 after mutation: " + str(offsprings[1].test_suite))
                
                # ------------ END DETERMINISTIC AND ADAPTIVE MUTATION METHOD ------------

                # ------------ SELF-ADAPTIVE MUTATION METHOD ------------

                elif configurations.mutation_type.value == 'self-adaptive':
                    print("Offspring 1 adaptive mutation rate before adaptive method: " + str(offsprings[0].adaptive_mutation_rate))
                    print("Offspring 2 adaptive mutation rate before adaptive method: " + str(offsprings[1].adaptive_mutation_rate))
                    
                    offsprings[0].adaptive_mutation_rate = mutation(offsprings[0], metadata, current_number_generation, inputs, configurations, configurations.mutation_type.value)
                    offsprings[1].adaptive_mutation_rate = mutation(offsprings[1], metadata, current_number_generation, inputs, configurations, configurations.mutation_type.value)
                    print("Offspring 1 adaptive mutation rate: " + str(offsprings[0].adaptive_mutation_rate))
                    print("Offspring 2 adaptive mutation rate: " + str(offsprings[1].adaptive_mutation_rate))

                    mutation_rate_values.append(offsprings[0].adaptive_mutation_rate)
                    mutation_rate_values.append(offsprings[1].adaptive_mutation_rate)

                    if offsprings[0].adaptive_mutation_rate > random.random():
                        print("Mutation applied to offspring 1 using self-adaptive method | Offspring 1: " + str(offsprings[0].test_suite))
                        offsprings[0] = mutation(offsprings[0], metadata, current_number_generation, inputs, configurations, random.choice(['add_test_case', 'delete_test_case', 'change_parameters']))
                        print("Offspring 1 after mutation: " + str(offsprings[0].test_suite))
                    if offsprings[1].adaptive_mutation_rate > random.random():
                        print("Mutation applied to offspring 2 using self-adaptive method | Offspring 2: " + str(offsprings[1].test_suite))
                        offsprings[1] = mutation(offsprings[1], metadata, current_number_generation, inputs, configurations, random.choice(['add_test_case', 'delete_test_case', 'change_parameters']))
                        print("Offspring 2 after mutation: " + str(offsprings[1].test_suite))

                # ------------ END SELF-ADAPTIVE MUTATION METHOD ------------
                        
                else:
                    if float(configurations.mutation_rate.value) > random.random():
                        print("Mutation applied to offspring 1 using other method | Offspring 1: " + str(offsprings[0].test_suite))
                        offsprings[0] = mutation(offsprings[0], metadata, current_number_generation, inputs, configurations, configurations.mutation_type.value)
                        print("Offspring 1 after mutation: " + str(offsprings[0].test_suite))
                    if float(configurations.mutation_rate.value) > random.random():
                        print("Mutation applied to offspring 2 using other method | Offspring 2: " + str(offsprings[1].test_suite))
                        offsprings[1] = mutation(offsprings[1], metadata, current_number_generation, inputs, configurations, configurations.mutation_type.value)
                        print("Offspring 2 after mutation: " + str(offsprings[1].test_suite))

                # ------------------------ End Mutation Operations ------------------------

                # Updating RLT for offsprings after crossover and mutation operations
                print("Offsprings before rlt setting: ")
                print("Offspring 1: " + str(offsprings[0].remaining_lifetime))
                print("Offspring 2: " + str(offsprings[1].remaining_lifetime))
                print("#----------------------------------------------------------------#")

                for offspring in offsprings:
                    offspring = rlt_setting(population, population_fitness, int(configurations.lt_max.value), int(configurations.lt_min.value), offspring)

                print("Offsprings after rlt setting: ")
                print("Offspring 1: " + str(offsprings[0].remaining_lifetime))
                print("Offspring 2: " + str(offsprings[1].remaining_lifetime))
                print("#----------------------------------------------------------------#")

                            
                # Adding offsprings to the new population
                new_population.append(offsprings[0])
                new_population.append(offsprings[1])

    # ------------ POPULATION CONTROL METHOD ------------

    if eval(configurations.population_control.value):
        print("Old population size: " + str(len(population)))
        print("New population size: " + str(len(new_population)))
        print("------------------------------------------------------------------")
        if len(new_population) > 1:
            new_population_fitness = obtain_fitness_values(new_population)
            current_best_fitness = obtain_best_fitness(new_population_fitness)
            new_population, iteration_number_population_control = population_resizing(new_population, current_best_fitness, old_best_fitness, 
                                                                                  initial_best_fitness, current_number_generation, iteration_number_population_control,
                                                                                  metadata, configurations)
    else:
        if current_best_fitness > old_best_fitness:
            iteration_number_population_control = 0
        else:
            iteration_number_population_control += 1

    # ------------ END POPULATION CONTROL METHOD ------------

    # Reset population and iterations
    population, current_number_generation, current_best_fitness, old_best_fitness, generations_without_fitness_improvement, best_fitness_seen = update_genetic_algorithm_attributes(population, new_population, 
                                                                                                                                            current_number_generation, old_best_fitness, 
                                                                                                                                            generations_without_fitness_improvement, best_fitness_seen, configurations)
    
    # Print generation stats
    average_crossover_rate_value, title_crossover_rate = average_crossover_rate(crossover_rate_values, configurations.crossover_type.value, title_crossover_rate)
    average_mutation_rate_value, title_mutation_rate = average_mutation_rate(population, mutation_rate_values, configurations.mutation_type.value, title_mutation_rate)
    generation_stats(current_number_generation, old_best_fitness, current_best_fitness, best_fitness_seen, population, average_crossover_rate_value, average_mutation_rate_value)
    print("Population size values: " + str(population_size_values) + " - Generation number values: " + str(generation_number_values) + " - Generation fitness values: " + str(generation_fitness_values) 
          + " - Crossover rate values: " + str(crossover_rate_generations) + " - Mutation rate values: " + str(mutation_rate_generations) + " - Iteration number population control: " + str(iteration_number_population_control))
    print("------------------------------------------------------------------")
            
# ---- End genetic algorithm execution ----
    
# ---- Genetic algorithm results ----
    
# If the path does not exist, create it
if not os.path.exists(configurations.generation_stats_path.value):
    os.makedirs(configurations.generation_stats_path.value)

util.population_size_graph(population_size_values, generation_number_values, configurations.generation_stats_path.value, None)
util.fitness_values_graph(generation_fitness_values, generation_number_values, configurations.generation_stats_path.value, None)
if configurations.crossover_type.value == 'deterministic' or configurations.crossover_type.value == 'adaptive': 
    util.crossover_rate_values_graph(crossover_rate_generations, generation_number_values, title_crossover_rate, configurations.generation_stats_path.value, None)
if configurations.mutation_type.value == 'deterministic' or configurations.mutation_type.value == 'adaptive' or configurations.mutation_type.value == 'self-adaptive':
    util.mutation_rate_values_graph(mutation_rate_generations, generation_number_values, title_mutation_rate, configurations.generation_stats_path.value, None)
# ---- End genetic algorithm results ----
    
# ---- Genetic algorithm data writing ----

# If the path does not exist, create it
if not os.path.exists(configurations.generation_data_path.value):
    os.makedirs(configurations.generation_data_path.value)   

util.write_generation_stats_file([generation_number_values, population_size_values, generation_fitness_values, crossover_rate_generations, mutation_rate_generations], configurations.generation_data_path.value)
    
# ---- End genetic algorithm data writing ----

# Obtain the best individual of the population and write it to a file
best_solution = obtain_best_individual(population)
print("Best solution: " + str(best_solution.test_suite) + " - Fitness: " + str(best_solution.fitness))
util.write_metadata(configurations.best_generated_test_suite.value, best_solution.test_suite, metadata)  
# ---------------------------------------------------------------

# Print the new population
print("-----------------------------------------------")
print("New Population After Genetic Algorithm Execution")
for i in range(len(new_population)):
    print("-------------------------------------")
    print("Test Suite - " + str(new_population[i].test_suite))
    print("Fitness - " + str(new_population[i].fitness))
    print("Crossover Rate - " + str(new_population[i].adaptive_crossover_rate))
    print("Mutation Rate - " + str(new_population[i].adaptive_mutation_rate))
    print("Adaptive Max Selections - " + str(new_population[i].adaptive_max_selections))
    print("Remaining Life Time - " + str(new_population[i].remaining_lifetime))