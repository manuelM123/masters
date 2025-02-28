import os
import json
import utilities as util
import operations.fitness_functions as ff

population_control = ['True', 'False']
selection_types = ['random', 'roulette_wheel', 'adaptive', 'rank', 'tournament']
crossover_types = ['deterministic_ilc', 'deterministic_dhc', 'self-adaptive', 'adaptive', 'uniform']
mutation_types = ['add_test_case', 'delete_test_case', 'deterministic_ilm', 'deterministic_dhm', 'adaptive', 'self-adaptive', 'change_parameters']
optimized_genetic_algorithms = ['tga', 'asga', 'sacga', 'oga']

'''
Function to create the necessary folders for the evaluation results
'''
def folder_setup():
    if not os.path.exists('results_evaluation'):
        os.makedirs('results_evaluation')

    if not os.path.exists('results_evaluation/methods_execution'):
        os.makedirs('results_evaluation/methods_execution')

    if not os.path.exists('results_evaluation/algorithms_execution'):
        os.makedirs('results_evaluation/algorithms_execution')

    if not os.path.exists('results_evaluation/methods_execution/time_execution'):
        os.makedirs('results_evaluation/methods_execution/time_execution')

    if not os.path.exists('results_evaluation/algorithms_execution/time_execution'):
        os.makedirs('results_evaluation/algorithms_execution/time_execution')

'''
Function to calculate the mean of the data for the different methods according to the type of data 

Parameters:
    genetic_parameters: list
        List of the genetic parameters to evaluate

    type_method: string
        Type of method to evaluate

    number_iterations: int
        Number of iterations to evaluate    

    type_data: string
        Type of data to evaluate    

    json_key: string
        Key to evaluate in the generation data json file 

'''
def mean_data_methods(genetic_parameters, type_method, number_iterations, type_data, json_key):
    mean_data = []
    success_rate = []
    for parameter in genetic_parameters:
        iteration_data = []
        for iteration in range(1, number_iterations + 1):
            if parameter != 'tga' and parameter != 'asga' and parameter != 'sacga' and parameter != 'oga':
                element_data = util.read_generations_stats_file_type(type_method + '_' + parameter + '_' + str(iteration), type_method, json_key)
            else:
                element_data = util.read_generations_stats_file_type(parameter + '_' + str(iteration), type_method, json_key)
            if type_data == 'best_fitness' or type_data == 'fitness_values':
                iteration_data.append(ff.mean_best_fitness(element_data))
                if max(element_data) >= 0.87:
                    success_rate.append([parameter, max(element_data)])
            elif type_data == 'time_execution':
                iteration_data.append(element_data)
            elif type_data == 'generation_number':
                iteration_data.append(max(element_data))

        if type_data == 'best_fitness' or type_data == 'fitness_values':
            mean_best_fitness_parameter = ff.mean_best_fitness(iteration_data)
            if parameter != 'tga' and parameter != 'asga' and parameter != 'sacga' and parameter != 'oga':
                mean_data.append([type_method + '_' + parameter, mean_best_fitness_parameter, util.standard_deviation(iteration_data)])
            else:
                mean_data.append([parameter, mean_best_fitness_parameter, util.standard_deviation(iteration_data)])
        elif type_data == 'time_execution':
            mean_time_parameter = util.mean_time_execution(iteration_data)
            if parameter != 'tga' and parameter != 'asga' and parameter != 'sacga' and parameter != 'oga':
                mean_data.append([mean_time_parameter, type_method + '_' + parameter])
            else:
                mean_data.append([mean_time_parameter, parameter])
        elif type_data == 'generation_number':
            mean_number_generation = util.mean_generations_execution(iteration_data)
            if parameter != 'tga' and parameter != 'asga' and parameter != 'sacga' and parameter != 'oga':
                mean_data.append([type_method + '_' + parameter, mean_number_generation])
            else:
                mean_data.append([parameter, mean_number_generation])

    return mean_data, success_rate

def data_evaluation(population_control, selection_types, crossover_types, mutation_types, optimized_genetic_algorithms, type):
    if type == 'optimizations':
        mbf_population, _ = mean_data_methods(population_control, 'population', 2, 'best_fitness', 'best_fitness_seen_values')
        mean_fitness_population, _ = mean_data_methods(population_control, 'population', 2, 'fitness_values', 'generation_fitness_values')
        time_execution_population, _ = mean_data_methods(population_control, 'population', 2, 'time_execution', 'time_execution')
        number_generations_population, _ = mean_data_methods(population_control, 'population', 2, 'generation_number', 'generation_number_values')

        print('Population Mean Best Fitness: ' + str(mbf_population) + "\n")
        print('Population Generations Mean Best Fitness: ' + str(mean_fitness_population) + "\n")
        print('Population Time Execution: ' + str(time_execution_population) + "\n")
        print('Population Number Generations: ' + str(number_generations_population) + "\n")

        util.mean_fitness_histogram(mbf_population, 'population', 'results_evaluation/methods_execution', 'Mean Best Fitness')
        util.mean_fitness_histogram(mean_fitness_population, 'population', 'results_evaluation/methods_execution', 'Generations Mean Best Fitness')
        util.mean_time_execution_histogram(time_execution_population, 'population', 'results_evaluation/methods_execution/time_execution')
        util.mean_generations_histogram(number_generations_population, 'population', 'results_evaluation/methods_execution')
        print('Population Mean Best Fitness: ' + str(mbf_population) + "\n")
        print('Population Generations Mean Best Fitness: ' + str(mean_fitness_population) + "\n")
        print('Population Time Execution: ' + str(time_execution_population) + "\n")
        print('Population Number Generations: ' + str(number_generations_population) + "\n")

        mbf_selection, _ = mean_data_methods(selection_types, 'selection', 2, 'best_fitness', 'best_fitness_seen_values')
        mean_fitness_selection, _ = mean_data_methods(selection_types, 'selection', 2, 'fitness_values', 'generation_fitness_values')
        time_execution_selection, _ = mean_data_methods(selection_types, 'selection', 2, 'time_execution', 'time_execution')
        number_generations_selection, _ = mean_data_methods(selection_types, 'selection', 2, 'generation_number', 'generation_number_values')
        util.mean_fitness_histogram(mbf_selection, 'selection', 'results_evaluation/methods_execution', 'Mean Best Fitness')
        util.mean_fitness_histogram(mean_fitness_selection, 'selection', 'results_evaluation/methods_execution', 'Generations Mean Best Fitness')
        util.mean_time_execution_histogram(time_execution_selection, 'selection', 'results_evaluation/methods_execution/time_execution')
        util.mean_generations_histogram(number_generations_selection, 'selection', 'results_evaluation/methods_execution')
        print('Selection Mean Best Fitness: ' + str(mbf_selection) + "\n")
        print('Selection Generations Mean Best Fitness: ' + str(mean_fitness_selection) + "\n")
        print('Selection Time Execution: ' + str(time_execution_selection) + "\n")
        print('Selection Number Generations: ' + str(number_generations_selection) + "\n")

        mbf_crossover, _ = mean_data_methods(crossover_types, 'crossover', 2, 'best_fitness', 'best_fitness_seen_values')
        mean_fitness_crossover, _ = mean_data_methods(crossover_types, 'crossover', 2, 'fitness_values', 'generation_fitness_values')
        time_execution_crossover, _ = mean_data_methods(crossover_types, 'crossover', 2, 'time_execution', 'time_execution')
        number_generations_crossover, _ = mean_data_methods(crossover_types, 'crossover', 2, 'generation_number', 'generation_number_values')
        util.mean_fitness_histogram(mbf_crossover, 'crossover', 'results_evaluation/methods_execution', 'Mean Best Fitness')
        util.mean_fitness_histogram(mean_fitness_crossover, 'crossover', 'results_evaluation/methods_execution', 'Generations Mean Best Fitness')
        util.mean_time_execution_histogram(time_execution_crossover, 'crossover', 'results_evaluation/methods_execution/time_execution')
        util.mean_generations_histogram(number_generations_crossover, 'crossover', 'results_evaluation/methods_execution')
        print('Crossover Mean Best Fitness: ' + str(mbf_crossover) + "\n")
        print('Crossover Generations Mean Best Fitness: ' + str(mean_fitness_crossover) + "\n")
        print('Crossover Time Execution: ' + str(time_execution_crossover) + "\n")
        print('Crossover Number Generations: ' + str(number_generations_crossover) + "\n")

        mbf_mutation, _ = mean_data_methods(mutation_types, 'mutation', 2, 'best_fitness', 'best_fitness_seen_values')
        mean_fitness_mutation, _ = mean_data_methods(mutation_types, 'mutation', 2, 'fitness_values', 'generation_fitness_values')
        time_execution_mutation, _ = mean_data_methods(mutation_types, 'mutation', 2, 'time_execution', 'time_execution')
        number_generations_mutation, _ = mean_data_methods(mutation_types, 'mutation', 2, 'generation_number', 'generation_number_values')
        util.mean_fitness_histogram(mbf_mutation, 'mutation', 'results_evaluation/methods_execution', 'Mean Best Fitness')
        util.mean_fitness_histogram(mean_fitness_mutation, 'mutation', 'results_evaluation/methods_execution', 'Generations Mean Best Fitness')
        util.mean_time_execution_histogram(time_execution_mutation, 'mutation', 'results_evaluation/methods_execution/time_execution')
        util.mean_generations_histogram(number_generations_mutation, 'mutation', 'results_evaluation/methods_execution')
        print('Mutation Mean Best Fitness: ' + str(mbf_mutation) + "\n")
        print('Mutation Generations Mean Best Fitness: ' + str(mean_fitness_mutation) + "\n")
        print('Mutation Time Execution: ' + str(time_execution_mutation) + "\n")
        print('Mutation Number Generations: ' + str(number_generations_mutation) + "\n")

    elif type == 'optimized_genetic_algorithms':
        mbf_genetic_algorithm, success_rate_data = mean_data_methods(optimized_genetic_algorithms, 'optimized_genetic_algorithms', 10, 'best_fitness', 'best_fitness_seen_values')
        mean_fitness_genetic_algorithm, _ = mean_data_methods(optimized_genetic_algorithms, 'optimized_genetic_algorithms', 10, 'fitness_values', 'generation_fitness_values')
        time_execution_genetic_algorithm, _ = mean_data_methods(optimized_genetic_algorithms, 'optimized_genetic_algorithms', 10, 'time_execution', 'time_execution')
        number_generations_genetic_algorithm, _ = mean_data_methods(optimized_genetic_algorithms, 'optimized_genetic_algorithms', 10, 'generation_number', 'generation_number_values')
        util.mean_fitness_histogram(mbf_genetic_algorithm, 'optimized_genetic_algorithms', 'results_evaluation/algorithms_execution', 'Mean Best Fitness')
        util.mean_fitness_histogram(mean_fitness_genetic_algorithm, 'optimized_genetic_algorithms', 'results_evaluation/algorithms_execution', 'Generations Mean Best Fitness')
        util.mean_time_execution_histogram(time_execution_genetic_algorithm, 'optimized_genetic_algorithms', 'results_evaluation/algorithms_execution/time_execution')
        util.mean_generations_histogram(number_generations_genetic_algorithm, 'optimized_genetic_algorithms', 'results_evaluation/algorithms_execution')
        print('Mean Best Fitness: ' + str(mbf_genetic_algorithm) + "\n")
        print('Generations Mean Best Fitness: ' + str(mean_fitness_genetic_algorithm) + "\n")
        print('Time Execution: ' + str(time_execution_genetic_algorithm) + "\n")
        print('Number Generations: ' + str(number_generations_genetic_algorithm) + "\n")
        print('Success Rate: ' + str(success_rate_data) + "\n")

    else:
        raise Exception('Type not found')

folder_setup()

data_evaluation(population_control, selection_types, crossover_types, mutation_types, optimized_genetic_algorithms, 'optimized_genetic_algorithms')