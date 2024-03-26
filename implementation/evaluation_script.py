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
    iteration_data = []
    genetic_parameter_mbf = []
    for parameter in genetic_parameters:
        for iteration in range(1, number_iterations + 1):
            element_data = util.read_generations_stats_file_type(type + '_' + parameter + '_' + str(iteration), type, 'generation_fitness_values')
            mean_best_fitness = ff.mean_best_fitness(element_data)
            iteration_data.append(mean_best_fitness)

        mean_best_fitness_parameter = ff.mean_best_fitness(iteration_data)
        genetic_parameter_mbf.append([type + '_' + parameter, mean_best_fitness_parameter, util.standard_deviation(iteration_data)])

    return genetic_parameter_mbf

folder_setup()

mbf_population = mean_best_fitness_methods(population_control, 'population', 5)
util.mean_best_fitness_histogram(mbf_population, 'population', 'results_evaluation/methods_execution')
print('Population: ' + str(mbf_population))

mbf_selection = mean_best_fitness_methods(selection_types, 'selection', 5)
util.mean_best_fitness_histogram(mbf_selection, 'selection', 'results_evaluation/methods_execution')
print('Selection: ' + str(mbf_selection))

mbf_crossover = mean_best_fitness_methods(crossover_types, 'crossover', 5)
util.mean_best_fitness_histogram(mbf_crossover, 'crossover', 'results_evaluation/methods_execution')
print('Crossover: ' + str(mbf_crossover))

mbf_mutation = mean_best_fitness_methods(mutation_types, 'mutation', 5)
util.mean_best_fitness_histogram(mbf_mutation, 'mutation', 'results_evaluation/methods_execution')
print('Mutation: ' + str(mbf_mutation))



