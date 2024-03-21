import os
import shutil
import subprocess
import resource
import configparser
import utilities as util

population_control = ['True', 'False']
selection_types = ['random', 'roulette_wheel', 'adaptive', 'rank', 'tournament']
crossover_types = ['deterministic', 'self-adaptive', 'adaptive', 'uniform']
mutation_types = ['add_test_case', 'delete_test_case', 'deterministic', 'adaptive', 'self-adaptive', 'change_parameters']

# [[population methods], [selection methods], [crossover methods], [mutation methods]]
execution_activities = [
    population_control,
    selection_types,
    crossover_types,
    mutation_types 
]

time_execution_values = []

# Metadata path 
metadata = {
    'metadata_location': 'metadata.json'
}

# Configuration of the genetic algorithm
genetic_algorithm_configurations = {
    'max_number_functions': 4,
    'max_number_test_cases': 3,
    'tournament_size': 2,
    'max_number_generations': 3,
    'fitness_max_stagnation_period': 2,
    'max_number_fitness_evaluations': 1000,
    'fitness_function_type': 'branch_coverage',
    'fitness_iteration_limit': 1
}

# Configuration of the genetic operators
genetic_operators_configurations = {
    'population_size': 5,
    'population_control': 'True',
    'selection_type': 'tournament',
    'crossover_type': 'uniform',
    'crossover_rate': 0.5,
    'crossover_rate_adjustment_type': 'ilc',
    'mutation_type': 'change_parameters',
    'mutation_rate': 0.15,
    'mutation_rate_adjustment_type': 'dhm'
}

# Configuration of the genetic algorithm optimizations
genetic_algorithm_optimizations_configurations = {
    'population_decrease_rate': 0.2,
    'uniform_number_crossover': 0.5,
    'lt_max': 10,
    'lt_min': 1,
    'alpha': 0.5
}

# File paths
file_paths = {
    'fuzzy_membership_functions': 'results/fuzzy_membership_functions',
    'intermediate_test_suite': 'results/intermediate_test_suite',
    'generation_stats': 'results/generations_stats',
    'best_generated_test_suite': 'results/best_generated_test_suite',
    'generation_data': 'results/generation_data',
    'benchmark': 'results/benchmarks'
}

# Configuration file path
path_configuration_file = 'config.ini'

def run_subprocess(command):
    start_time = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
    subprocess.run(command)
    end_time = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
    elapsed_time = end_time - start_time
    return elapsed_time

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
                change_configurations(None, [['population_control', method]], None, [['generation_stats', 'results/generation_stats/' + 'population_' + method]])
                genetic_algorithm_execution(path_configuration_file, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
                subprocess.run(['python3', 'genetic_algorithm.py'])

        ## Selection methods
        elif execution_activities.index(activity) == 1:
            for method in activity:
                change_configurations(None, [['selection_type', method]], None, [['generation_stats', 'results/generation_stats/' + 'selection_' + method]])
                genetic_algorithm_execution(path_configuration_file, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
                subprocess.run(['python3', 'genetic_algorithm.py'])

        # Crossover methods
        elif execution_activities.index(activity) == 2:
            for method in activity: 
                if method == 'deterministic':
                    for deterministic_type in deterministic_crossover_adjustment_types:
                        change_configurations(None, [['crossover_type', method], ['crossover_rate_adjustment_type', deterministic_type]], None, [['generation_stats', 'results/generation_stats/' + 'crossover_' + method + "_" + deterministic_type]])
                        genetic_algorithm_execution(path_configuration_file, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
                        subprocess.run(['python3', 'genetic_algorithm.py'])
                else:
                    change_configurations(None, [['crossover_type', method]], None, [['generation_stats', 'results/generation_stats/' + 'crossover_' + method]])
                    genetic_algorithm_execution(path_configuration_file, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
                    subprocess.run(['python3', 'genetic_algorithm.py'])

        # Mutation methods
        elif execution_activities.index(activity) == 3:
            for method in activity:
                if method == 'deterministic':
                    for deterministic_type in deterministic_mutation_adjustment_types:
                        change_configurations(None, [['mutation_type', method], ['mutation_rate_adjustment_type', deterministic_type]], None, [['generation_stats', 'results/generation_stats/' + 'mutation_' + method + "_" + deterministic_type]])
                        genetic_algorithm_execution(path_configuration_file, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
                        subprocess.run(['python3', 'genetic_algorithm.py'])
                else:
                    change_configurations(None, [['mutation_type', method]], None, [['generation_stats', 'results/generation_stats/' + 'mutation_' + method]])
                    genetic_algorithm_execution(path_configuration_file, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
                    subprocess.run(['python3', 'genetic_algorithm.py'])

def population_execution(iteration):
    population_methods = []
    for method in population_control:
        change_configurations(None, [['population_control', method]], None, [['generation_stats', 'results/generation_stats/population/' + 'population_' + method + "_" + str(iteration)], ['generation_data', 'results/generation_data/population/' + 'population_' + method + "_" + str(iteration)]])
        genetic_algorithm_execution(path_configuration_file, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
        time = run_subprocess(['python3', 'genetic_algorithm.py'])
        time_execution_values.append([time, 'population_' + method])

        population_methods.append('population_' + method + "_" + str(iteration))
        util.write_metadata('results/best_generated_test_suite/population', util.read_best_generated_test_suite_data('results/best_generated_test_suite'),
                            util.read_metadata(util.obtain_configuration("config.ini", "metadata", "metadata_location")), method + "_" + str(iteration))


    util.time_execution_histogram(time_execution_values, 'population', 'results/benchmarks/time_execution/population', iteration)

    time_execution_values.clear()

    return population_methods

def selection_execution(iteration):
    selection_methods = []
    for method in selection_types:
        change_configurations(None, [['selection_type', method]], None, [['generation_stats', 'results/generation_stats/selection/' + 'selection_' + method + "_" + str(iteration)], ['generation_data', 'results/generation_data/selection/' + 'selection_' + method + "_" + str(iteration)]])
        genetic_algorithm_execution(path_configuration_file, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
        time = run_subprocess(['python3', 'genetic_algorithm.py'])
        time_execution_values.append([time, 'selection_' + method])
    
        selection_methods.append('selection_' + method + "_" + str(iteration))
        util.write_metadata('results/best_generated_test_suite/selection', util.read_best_generated_test_suite_data('results/best_generated_test_suite'),
                            util.read_metadata(util.obtain_configuration("config.ini", "metadata", "metadata_location")), method + "_" + str(iteration))

    util.time_execution_histogram(time_execution_values, 'selection', 'results/benchmarks/time_execution/selection', iteration)

    time_execution_values.clear()

    return selection_methods

def crossover_execution(iteration):
    crossover_methods = []
    deterministic_crossover_adjustment_types = ['dhc', 'ilc']
    for method in crossover_types:
        if method == 'deterministic':
            for deterministic_type in deterministic_crossover_adjustment_types:
                change_configurations(None, [['crossover_type', method], ['crossover_rate_adjustment_type', deterministic_type]], None, [['generation_stats', 'results/generation_stats/crossover/' + 'crossover_' + method + "_" + deterministic_type + "_" + str(iteration)], ['generation_data', 'results/generation_data/crossover/' + 'crossover_' + method + "_" + deterministic_type + "_" + str(iteration)]])
                genetic_algorithm_execution(path_configuration_file, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
                time = run_subprocess(['python3', 'genetic_algorithm.py'])
                time_execution_values.append([time, 'crossover_' + method + "_" + deterministic_type])
            
                crossover_methods.append('crossover_' + method + "_" + deterministic_type + "_" + str(iteration))
                util.write_metadata('results/best_generated_test_suite/crossover', util.read_best_generated_test_suite_data('results/best_generated_test_suite'),
                            util.read_metadata(util.obtain_configuration("config.ini", "metadata", "metadata_location")), method + "_" + deterministic_type + "_" + str(iteration))
        else:
            change_configurations(None, [['crossover_type', method]], None, [['generation_stats', 'results/generation_stats/crossover/' + 'crossover_' + method + "_" + str(iteration)], ['generation_data', 'results/generation_data/crossover/' + 'crossover_' + method + "_" + str(iteration)]])
            genetic_algorithm_execution(path_configuration_file, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
            time = run_subprocess(['python3', 'genetic_algorithm.py'])
            time_execution_values.append([time, 'crossover_' + method])

            crossover_methods.append('crossover_' + method + "_" + str(iteration))
            util.write_metadata('results/best_generated_test_suite/crossover', util.read_best_generated_test_suite_data('results/best_generated_test_suite'),
                            util.read_metadata(util.obtain_configuration("config.ini", "metadata", "metadata_location")), method + "_" + str(iteration))

    util.time_execution_histogram(time_execution_values, 'crossover', 'results/benchmarks/time_execution/crossover', iteration)

    time_execution_values.clear()

    return crossover_methods

def mutation_execution(iteration):
    mutation_methods = []
    deterministic_mutation_adjustment_types = ['dhm', 'ilm']
    for method in mutation_types:
        if method == 'deterministic':
            for deterministic_type in deterministic_mutation_adjustment_types:
                change_configurations(None, [['mutation_type', method], ['mutation_rate_adjustment_type', deterministic_type]], None, [['generation_stats', 'results/generation_stats/mutation/' + 'mutation_' + method + "_" + deterministic_type + "_" + str(iteration)], ['generation_data', 'results/generation_data/mutation/' + 'mutation_' + method + "_" + deterministic_type + "_" + str(iteration)]])
                genetic_algorithm_execution(path_configuration_file, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
                time = run_subprocess(['python3', 'genetic_algorithm.py'])
                time_execution_values.append([time, 'mutation_' + method + "_" + deterministic_type])

                mutation_methods.append('mutation_' + method + "_" + deterministic_type + "_" + str(iteration))
                util.write_metadata('results/best_generated_test_suite/mutation', util.read_best_generated_test_suite_data('results/best_generated_test_suite'),
                            util.read_metadata(util.obtain_configuration("config.ini", "metadata", "metadata_location")), method + "_" + deterministic_type + "_" + str(iteration))
        else:
            change_configurations(None, [['mutation_type', method]], None, [['generation_stats', 'results/generation_stats/mutation/' + 'mutation_' + method + "_" + str(iteration)], ['generation_data', 'results/generation_data/mutation/' + 'mutation_' + method + "_" + str(iteration)]])
            genetic_algorithm_execution(path_configuration_file, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
            time = run_subprocess(['python3', 'genetic_algorithm.py'])
            time_execution_values.append([time, 'mutation_' + method])

            mutation_methods.append('mutation_' + method + "_" + str(iteration))
            util.write_metadata('results/best_generated_test_suite/mutation', util.read_best_generated_test_suite_data('results/best_generated_test_suite'),
                            util.read_metadata(util.obtain_configuration("config.ini", "metadata", "metadata_location")), method + "_" + str(iteration))

    util.time_execution_histogram(time_execution_values, 'mutation', 'results/benchmarks/time_execution/mutation', iteration)

    time_execution_values.clear()

    return mutation_methods

def folder_setup():
    # Verify if folder benchmarks exists
    if not os.path.exists('results/benchmarks'):
        os.makedirs('results/benchmarks')  # Create the directory if it doesn't exist
    else:
        try:
            shutil.rmtree('results/benchmarks')
            os.makedirs('results/benchmarks')
        except OSError as e:
            print("Error: %s : %s" % ('results/benchmarks', e.strerror))

    # Verify if folder benchmarks/time_execution exists
    if not os.path.exists('results/benchmarks/time_execution'):
        os.makedirs('results/benchmarks/time_execution')
    else:
        try:
            shutil.rmtree('results/benchmarks/time_execution')
            os.makedirs('results/benchmarks/time_execution')
        except OSError as e:
            print("Error: %s : %s" % ('results/benchmarks/time_execution', e.strerror))

    method_folders = ['population', 'selection', 'crossover', 'mutation']

    for folder in method_folders:
        # Verify if folder generation_data exists for each method
        if not os.path.exists('results/generation_data/' + folder):
            os.makedirs('results/generation_data/' + folder)  # Create the directory if it doesn't exist
        else:
            try:
                shutil.rmtree('results/generation_data/' + folder)
                os.makedirs('results/generation_data/' + folder)
            except OSError as e:
                print("Error: %s : %s" % ('results/generation_data/' + folder, e.strerror))

        # Verify if folder generations_stats exists for each method
        if not os.path.exists('results/generation_stats/' + folder):
            os.makedirs('results/generation_stats/' + folder)  # Create the directory if it doesn't exist
        else:
            try:
                shutil.rmtree('results/generation_stats/' + folder)
                os.makedirs('results/generation_stats/' + folder)
            except OSError as e:
                print("Error: %s : %s" % ('results/generation_stats/' + folder, e.strerror))

        # Verify if the folder for each method exists
        if not os.path.exists('results/benchmarks/' + folder):
            os.makedirs('results/benchmarks/' + folder)
        else:
            try:
                shutil.rmtree('results/benchmarks/' + folder)
                os.makedirs('results/benchmarks/' + folder)
            except OSError as e:
                print("Error: %s : %s" % ('results/benchmarks/' + folder, e.strerror))
        
        # Verify if folder time_execution exists for each method
        if not os.path.exists('results/benchmarks/time_execution/' + folder):
            os.makedirs('results/benchmarks/time_execution/' + folder)
        else:
            try:
                shutil.rmtree('results/benchmarks/time_execution/' + folder)
                os.makedirs('results/benchmarks/time_execution/' + folder)
            except OSError as e:
                print("Error: %s : %s" % ('results/benchmarks/time_execution/' + folder, e.strerror))

        # Verify if folder time_execution exists for each method
        if not os.path.exists('results/best_generated_test_suite/' + folder):
            os.makedirs('results/best_generated_test_suite/' + folder)
        else:
            try:
                shutil.rmtree('results/best_generated_test_suite/' + folder)
                os.makedirs('results/best_generated_test_suite/' + folder)
            except OSError as e:
                print("Error: %s : %s" % ('results/best_generated_test_suite/' + folder, e.strerror))
                
def generate_benchmarks(benchmark_type, generations_methods, generations_data, path):
    generations = []
    populations_size = []
    generations_fitness = []
    crossover_rates = []
    mutation_rates = []
    best_fitness_seen = []

    for method in range(len(generations_methods)):
        for data in range(len(generations_data[0])):
            data_type = generations_data[method][data][0]
            data_values = generations_data[method][data][1]

            if data_type == 'generation_number_values':
                generations.append(data_values)
            elif data_type == 'population_size_values':
                populations_size.append(data_values)
            elif data_type == 'generation_fitness_values':
                generations_fitness.append(data_values)
            elif data_type == 'crossover_rate_values':
                crossover_rates.append(data_values)
            elif data_type == 'mutation_rate_values':
                mutation_rates.append(data_values)
            elif data_type == 'best_fitness_seen_values':
                best_fitness_seen.append(data_values)

    # Verify if the folder exists
    benchmark_result = path + benchmark_type
    if not os.path.exists(benchmark_result):
        os.makedirs(benchmark_result)
    else:
        try:
            shutil.rmtree(benchmark_result)
            os.makedirs(benchmark_result)
        except OSError as e:
            print("Error: %s : %s" % (benchmark_result, e.strerror))

    util.population_size_graph(populations_size, generations, benchmark_result, generations_methods)
    util.fitness_values_graph(generations_fitness, generations, benchmark_result, generations_methods)
    util.best_fitness_seen_graph(best_fitness_seen, generations, benchmark_result, generations_methods)
    if 'crossover' in benchmark_type:
        util.crossover_rate_values_graph(crossover_rates, generations, 'Average Crossover Rate', benchmark_result, generations_methods)
    elif 'mutation' in benchmark_type:
        util.mutation_rate_values_graph(mutation_rates, generations, 'Average Mutation Rate', benchmark_result, generations_methods)

# Execute the folder setup
folder_setup()

for iteration in range(1,3):
    # Execute the population methods
    population_methods = population_execution(iteration)
    population_generations_data = util.read_generation_stats_file(population_methods, 'population')
    print("Population Generations Data")
    print(population_generations_data)
    print("------------------------------------------")
    generate_benchmarks('population_' + str(iteration), population_methods, population_generations_data, 'results/benchmarks/population/')

    # Execute the selection methods
    selection_methods = selection_execution(iteration)
    selection_generations_data = util.read_generation_stats_file(selection_methods, 'selection')
    print("Selection Generations Data")
    print(selection_generations_data)
    print("------------------------------------------")
    generate_benchmarks('selection_' + str(iteration), selection_methods, selection_generations_data, 'results/benchmarks/selection/')
    
    # Execute the crossover methods
    crossover_methods = crossover_execution(iteration)
    print(crossover_methods)
    crossover_generations_data = util.read_generation_stats_file(crossover_methods, 'crossover')
    print("Crossover Generations Data")
    print(crossover_generations_data)
    print("------------------------------------------")
    generate_benchmarks('crossover_' + str(iteration), crossover_methods, crossover_generations_data, 'results/benchmarks/crossover/')
    
    # Execute the mutation methods
    mutation_methods = mutation_execution(iteration)
    mutation_generations_data = util.read_generation_stats_file(mutation_methods, 'mutation')
    print("Mutation Generations Data")
    print(mutation_generations_data)
    print("------------------------------------------")
    generate_benchmarks('mutation_' + str(iteration), mutation_methods, mutation_generations_data, 'results/benchmarks/mutation/')

# Execute the genetic algorithm              
#general_execution()