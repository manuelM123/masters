import subprocess
import configparser

selection_types = ['random', 'roulette_wheel', 'tournament', 'rank', 'adaptive']
crossover_types = ['one_point', 'uniform', 'deterministic', 'adaptive', 'self-adaptive']
mutation_types = ['add_test_case', 'delete_test_case', 'change_parameters', 'deterministic', 'adaptive', 'self-adaptive']

# Metadata path 
metadata = {
    'metadata_location': 'metadata.json'
}

# Configuration of the genetic algorithm
genetic_algorithm_configurations = {
    'max_number_functions': 3,
    'max_number_test_cases': 8,
    'tournament_size': 2,
    'max_number_generations': 5,
    'fitness_max_stagnation_period': 4,
    'max_number_fitness_evaluations': 1000,
    'fitness_function_type': 'branch_coverage',
    'fitness_iteration_limit': 3
}

# Configuration of the genetic operators
genetic_operators_configurations = {
    'population_size': 10,
    'population_control': 'True',
    'selection_type': 'tournament',
    'crossover_type': 'uniform',
    'crossover_rate': 0.6,
    'crossover_rate_adjustment_type': 'ilc',
    'mutation_type': 'add_test_case',
    'mutation_rate': 0.25,
    'mutation_rate_adjustment_type': 'dhm'
}

# Configuration of the genetic algorithm optimizations
genetic_algorithm_optimizations_configurations = {
    'population_decrease_rate': 0.2,
    'uniform_number_crossover': 0.5,
    'lt_max': 10,
    'lt_min': 1
}

# File paths
file_paths = {
    'fuzzy_membership_functions': 'results/fuzzy_membership_functions',
    'intermediate_test_suite': 'results/intermediate_test_suite',
    'generation_stats': 'results/generations_stats',
    'best_generated_test_suite': 'results/best_generated_test_suite'
}

# Configuration file path
path_configuration_file = 'config.ini'

# genetic_algoritm_values = [['max_number_functions', 3], ['max_number_test_cases', 8]]
def change_configurations(genetic_algorithm_values, genetic_operators_values, genetic_algorithm_optimizations_values, file_paths_values):
    if genetic_algorithm_values != None:
        for config in genetic_algorithm_values:
            genetic_algorithm_configurations[config[0]] = config[1]

    if genetic_operators_values != None:
        for config in genetic_operators_values:
            genetic_operators_configurations[config[0]] = config[1]

    if genetic_algorithm_optimizations_values != None:
        for config in genetic_algorithm_optimizations_values:
            genetic_algorithm_optimizations_configurations[config[0]] = config[1]

    if file_paths_values != None:
        for config in file_paths_values:
            file_paths[config[0]] = config[1]

def genetic_algorithm_execution(config_path, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths):
    # Write the configuration file for the genetic algorithm
    config = configparser.ConfigParser()
    config['metadata'] = metadata
    config['genetic_algorithm_configurations'] = genetic_algorithm_configurations
    config['genetic_operators_configurations'] = genetic_operators_configurations
    config['genetic_algorithm_optimizations_configurations'] = genetic_algorithm_optimizations_configurations
    config['file_paths'] = file_paths
    with open(config_path, 'w') as configfile:
        config.write(configfile)

genetic_algorithm_execution(path_configuration_file, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
subprocess.run(['python3', 'genetic_algorithm.py'])

change_configurations([['max_number_generations', 5], ['fitness_max_stagnation_period', 5]],
                      [['population_size', 5], ['selection_type', 'adaptive'], ['crossover_type', 'deterministic'], ['mutation_type', 'change_parameters'], ['mutation_rate', 0.3]], None, [['generation_stats', 'results/generation_stats_1']])
genetic_algorithm_execution(path_configuration_file, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
subprocess.run(['python3', 'genetic_algorithm.py'])

change_configurations([['max_number_generations', 10], ['fitness_max_stagnation_period', 5]],
                      [['population_size', 10], ['selection_type', 'tournament'], ['crossover_type', 'adaptive'], ['mutation_type', 'adaptive'], ['mutation_rate', 0.3]], None, [['generation_stats', 'results/generation_stats_2']])
genetic_algorithm_execution(path_configuration_file, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
subprocess.run(['python3', 'genetic_algorithm.py'])
