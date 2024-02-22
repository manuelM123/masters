import subprocess
import configparser

population_control = ['False', 'True']
selection_types = ['random', 'roulette_wheel', 'adaptive', 'rank', 'tournament']
crossover_types = ['uniform', 'deterministic', 'self-adaptive', 'adaptive']
mutation_types = ['add_test_case', 'delete_test_case', 'change_parameters', 'deterministic', 'adaptive', 'self-adaptive']

# [[population methods], [selection methods], [crossover methods], [mutation methods]]
execution_activities = [
    population_control,
    selection_types,
    crossover_types,
    mutation_types 
]

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
    'fitness_max_stagnation_period': 3,
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

def general_execution():
    deterministic_crossover_adjustment_types = ['ilc', 'dhc']
    deterministic_mutation_adjustment_types = ['ilm', 'dhm']

    for activity in execution_activities:
        # Population methods
        if execution_activities.index(activity) == 0:
            for method in activity:
                change_configurations(None, [['population_control', method]], None, [['generation_stats', 'results/generation_stats_' + 'population_' + method]])
                genetic_algorithm_execution(path_configuration_file, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
                subprocess.run(['python3', 'genetic_algorithm.py'])

        # Selection methods
        elif execution_activities.index(activity) == 1:
            for method in activity:
                change_configurations(None, [['selection_type', method]], None, [['generation_stats', 'results/generation_stats_' + 'selection_' + method]])
                genetic_algorithm_execution(path_configuration_file, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
                subprocess.run(['python3', 'genetic_algorithm.py'])

        # Crossover methods
        elif execution_activities.index(activity) == 2:
            for method in activity: 
                if method == 'deterministic':
                    for deterministic_type in deterministic_crossover_adjustment_types:
                        change_configurations(None, [['crossover_type', method], ['crossover_rate_adjustment_type', deterministic_type]], None, [['generation_stats', 'results/generation_stats_' + 'crossover_' + method + "_" + deterministic_type]])
                        genetic_algorithm_execution(path_configuration_file, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
                        subprocess.run(['python3', 'genetic_algorithm.py'])
                else:
                    change_configurations(None, [['crossover_type', method]], None, [['generation_stats', 'results/generation_stats_' + 'crossover_' + method]])
                    genetic_algorithm_execution(path_configuration_file, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
                    subprocess.run(['python3', 'genetic_algorithm.py'])

        # Mutation methods
        elif execution_activities.index(activity) == 3:
            for method in activity:
                if method == 'deterministic':
                    for deterministic_type in deterministic_mutation_adjustment_types:
                        change_configurations(None, [['mutation_type', method], ['mutation_rate_adjustment_type', deterministic_type]], None, [['generation_stats', 'results/generation_stats_' + 'mutation_' + method + "_" + deterministic_type]])
                        genetic_algorithm_execution(path_configuration_file, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
                        subprocess.run(['python3', 'genetic_algorithm.py'])
                else:
                    change_configurations(None, [['mutation_type', method]], None, [['generation_stats', 'results/generation_stats_' + 'mutation_' + method]])
                    genetic_algorithm_execution(path_configuration_file, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
                    subprocess.run(['python3', 'genetic_algorithm.py'])
       

# Execute the genetic algorithm              
general_execution()