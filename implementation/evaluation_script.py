import os
import json
import utilities as util
import operations.fitness_functions as ff

population_control = ['True', 'False']
selection_types = ['random', 'roulette_wheel', 'adaptive', 'rank', 'tournament']
crossover_types = ['deterministic_ilc', 'deterministic_dhc', 'self-adaptive', 'adaptive', 'uniform']
mutation_types = ['add_test_case', 'delete_test_case', 'deterministic_ilm', 'deterministic_dhm', 'adaptive', 'self-adaptive', 'change_parameters']

'''
Function to create the necessary folders for the evaluation results
'''
def folder_setup():
    if not os.path.exists('results_evaluation'):
        os.makedirs('results_evaluation')

    if not os.path.exists('results_evaluation/methods_execution'):
        os.makedirs('results_evaluation/methods_execution')

    if not os.path.exists('results_evaluation/algorithm_execution'):
        os.makedirs('results_evaluation/algorithm_execution')

    if not os.path.exists('results_evaluation/methods_execution/time_execution'):
        os.makedirs('results_evaluation/methods_execution/time_execution')

'''
Function to obtain the mean best fitness of a set of genetic parameters

Parameters:
----------
genetic_parameters : list
    The genetic parameters to evaluate

type : str
    The type of genetic algorithm element to evaluate

number_iterations : int
    The number of iterations to evaluate

Returns:
-------
genetic_parameter_mbf : list
    A list containing the mean best fitness of each genetic parameter evaluated
'''
def mean_best_fitness_methods(genetic_parameters, type, number_iterations):
    genetic_parameter_mbf = []
    for parameter in genetic_parameters:
        iteration_data = []
        for iteration in range(1, number_iterations + 1):
            element_data = util.read_generations_stats_file_type(type + '_' + parameter + '_' + str(iteration), type, 'best_fitness_seen_values')
            mean_best_fitness = ff.mean_best_fitness(element_data)
            iteration_data.append(mean_best_fitness)

        mean_best_fitness_parameter = ff.mean_best_fitness(iteration_data)
        genetic_parameter_mbf.append([type + '_' + parameter, mean_best_fitness_parameter, util.standard_deviation(iteration_data)])

    return genetic_parameter_mbf

def mean_time_execution_methods(genetic_parameters, type, number_iterations):
    time_execution_data = []
    for parameter in genetic_parameters:
        iteration_data = []
        for iteration in range(1, number_iterations + 1):
            element_data = util.read_generations_stats_file_type(type + '_' + parameter + '_' + str(iteration), type, 'time_execution')
            iteration_data.append(element_data)

        mean_time_parameter = util.mean_time_execution(iteration_data)
        time_execution_data.append([mean_time_parameter, type + '_' + parameter])

    return time_execution_data

folder_setup()

mbf_population = mean_best_fitness_methods(population_control, 'population', 2)
time_execution_population = mean_time_execution_methods(population_control, 'population', 2)
util.mean_best_fitness_histogram(mbf_population, 'population', 'results_evaluation/methods_execution')
util.mean_time_execution_histogram(time_execution_population, 'Population', 'results_evaluation/methods_execution/time_execution')
print('Population: ' + str(mbf_population))
print('Population Time Execution: ' + str(time_execution_population) + "\n")

mbf_selection = mean_best_fitness_methods(selection_types, 'selection', 2)
time_execution_selection = mean_time_execution_methods(selection_types, 'selection', 2)
util.mean_best_fitness_histogram(mbf_selection, 'selection', 'results_evaluation/methods_execution')
util.mean_time_execution_histogram(time_execution_selection, 'Selection', 'results_evaluation/methods_execution/time_execution')
print('Selection: ' + str(mbf_selection))
print('Selection Time Execution: ' + str(time_execution_selection) + "\n")

mbf_crossover = mean_best_fitness_methods(crossover_types, 'crossover', 2)
time_execution_crossover = mean_time_execution_methods(crossover_types, 'crossover', 2)
util.mean_best_fitness_histogram(mbf_crossover, 'crossover', 'results_evaluation/methods_execution')
util.mean_time_execution_histogram(time_execution_crossover, 'Crossover', 'results_evaluation/methods_execution/time_execution')
print('Crossover: ' + str(mbf_crossover))
print('Crossover Time Execution: ' + str(time_execution_crossover) + "\n")

mbf_mutation = mean_best_fitness_methods(mutation_types, 'mutation', 2)
time_execution_mutation = mean_time_execution_methods(mutation_types, 'mutation', 2)
util.mean_best_fitness_histogram(mbf_mutation, 'mutation', 'results_evaluation/methods_execution')
util.mean_time_execution_histogram(time_execution_mutation, 'Mutation', 'results_evaluation/methods_execution/time_execution')
print('Mutation: ' + str(mbf_mutation))
print('Mutation Time Execution: ' + str(time_execution_mutation) + "\n")
