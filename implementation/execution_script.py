import os
import shutil
import subprocess
import resource
import configparser
import utilities as util
from enum import Enum
from operations.population_control import *

population_control = ['True', 'False']
selection_types = ['random', 'roulette_wheel', 'adaptive', 'rank', 'tournament']
crossover_types = ['deterministic', 'self-adaptive', 'adaptive', 'uniform']
mutation_types = ['add_test_case', 'delete_test_case', 'deterministic', 'adaptive', 'self-adaptive', 'change_parameters']
genetic_algorithms = ['tga', 'asga', 'sacga', 'oga']
time_execution_values = []

'''
Class that contains the configurations of the genetic algorithm

It is used to store the configurations of the genetic algorithm, genetic operators, genetic algorithm optimizations and file paths
'''
class configurations(Enum):
    # Genetic algorithm configurations
    max_number_functions = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "max_number_functions")
    max_number_test_cases = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "max_number_test_cases")
    fitness_function_type = util.obtain_configuration("config.ini", "genetic_algorithm_configurations", "fitness_function_type")

    # Genetic operators configurations
    population_size = util.obtain_configuration("config.ini", "genetic_operators_configurations", "population_size")

    # File paths
    intermediate_test_suite_path = util.obtain_configuration("config.ini", "file_paths", "intermediate_test_suite")
    generation_stats_history_path = util.obtain_configuration("config.ini", "file_paths", "generation_stats_history")

    # Scripts
    execution_script = util.obtain_configuration("config.ini", "scripts", "execution_script")
    execution_optimizations = util.obtain_configuration("config.ini", "scripts", "execution_optimizations")

# Configuration file path
path_configuration_file = 'config.ini'

# Read the metadata file
metadata_file = util.read_metadata(util.obtain_configuration("config.ini", "metadata", "metadata_location"))

'''
Function to execute a subprocess and measure the time of execution

Parameters:
----------------
command: list
    List with the command to be executed

Returns:
----------------
elapsed_time: float
    Elapsed time of the subprocess execution

'''
def run_subprocess(command):
    start_time = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
    subprocess.run(command)
    end_time = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
    elapsed_time = end_time - start_time
    return elapsed_time

'''
Function to change the configurations of the genetic algorithm

Parameters:
----------------

genetic_algorithm_values: list
    List with the values to be changed in the genetic algorithm configurations

genetic_operators_values: list
    List with the values to be changed in the genetic operators configurations

genetic_algorithm_optimizations_values: list
    List with the values to be changed in the genetic algorithm optimizations configurations

file_paths_values: list
    List with the values to be changed in the file paths configurations
'''
def change_configurations(genetic_algorithm_values, genetic_operators_values, genetic_algorithm_optimizations_values, file_paths_values, scripts_values):
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

    if scripts_values != None:
        for config in scripts_values:
            scripts[config[0]] = config[1]

'''
Function to adjust the configurations of the genetic algorithm

Parameters:
----------------
config_path: str
    Path of the configuration file

genetic_algorithm_configurations: dict
    Dictionary with the genetic algorithm configurations

genetic_operators_configurations: dict
    Dictionary with the genetic operators configurations

genetic_algorithm_optimizations_configurations: dict
    Dictionary with the genetic algorithm optimizations configurations

file_paths: dict
    Dictionary with the file paths configurations
'''
def configuration_update(config_path, metadata, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths):
    # Write the configuration file for the genetic algorithm
    config = configparser.ConfigParser()
    config['metadata'] = metadata
    config['genetic_algorithm_configurations'] = genetic_algorithm_configurations
    config['genetic_operators_configurations'] = genetic_operators_configurations
    config['genetic_algorithm_optimizations_configurations'] = genetic_algorithm_optimizations_configurations
    config['file_paths'] = file_paths
    config['scripts'] = scripts
    with open(config_path, 'w') as configfile:
        config.write(configfile)

'''
Function to execute the population methods

Parameters:
----------------
iteration: int
    Iteration number

Returns:
----------------
population_methods: list
    List with the population methods executed
'''
def population_execution(iteration):
    population_methods = []
    for method in population_control:
        change_configurations(None, [['population_control', method]], None, [['generation_stats', 'results/generation_stats/population/' + 'population_' + method + "_" + str(iteration)], ['generation_data', 'results/generation_data/population/' + 'population_' + method + "_" + str(iteration)]], None)
        configuration_update(path_configuration_file, metadata, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
        time = run_subprocess(['python3', 'genetic_algorithm.py'])
        time_execution_values.append([time, 'population_' + method])

        population_methods.append('population_' + method + "_" + str(iteration))
        util.write_metadata('results/best_generated_test_suite/population', util.read_best_generated_test_suite_data('results/best_generated_test_suite'),
                            util.read_metadata(util.obtain_configuration("config.ini", "metadata", "metadata_location")), method + "_" + str(iteration))
        util.write_best_generated_test_suite_data('results/best_generated_test_suite/population', util.read_best_generated_test_suite_data('results/best_generated_test_suite'), method + "_" + str(iteration))
        util.write_data_file('results/generation_data/population/' + 'population_' + method + "_" + str(iteration), time, 'time_execution')
    util.time_execution_histogram(time_execution_values, 'population', 'results/benchmarks/time_execution/population', iteration)

    time_execution_values.clear()

    return population_methods

'''
Function to execute the selection methods

Parameters:
----------------
iteration: int

Returns:
----------------
selection_methods: list
    List with the selection methods executed
'''
def selection_execution(iteration):
    selection_methods = []
    for method in selection_types:
        change_configurations(None, [['selection_type', method]], None, [['generation_stats', 'results/generation_stats/selection/' + 'selection_' + method + "_" + str(iteration)], ['generation_data', 'results/generation_data/selection/' + 'selection_' + method + "_" + str(iteration)]], None)
        configuration_update(path_configuration_file, metadata, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
        time = run_subprocess(['python3', 'genetic_algorithm.py'])
        time_execution_values.append([time, 'selection_' + method])
    
        selection_methods.append('selection_' + method + "_" + str(iteration))
        util.write_metadata('results/best_generated_test_suite/selection', util.read_best_generated_test_suite_data('results/best_generated_test_suite'),
                            util.read_metadata(util.obtain_configuration("config.ini", "metadata", "metadata_location")), method + "_" + str(iteration))
        util.write_best_generated_test_suite_data('results/best_generated_test_suite/selection', util.read_best_generated_test_suite_data('results/best_generated_test_suite'), method + "_" + str(iteration))
        util.write_data_file('results/generation_data/selection/' + 'selection_' + method + "_" + str(iteration), time, 'time_execution')
    util.time_execution_histogram(time_execution_values, 'selection', 'results/benchmarks/time_execution/selection', iteration)

    time_execution_values.clear()

    return selection_methods

'''
Function to execute the crossover methods

Parameters:
----------------    
iteration: int

Returns:
----------------
crossover_methods: list
    List with the crossover methods executed
'''
def crossover_execution(iteration):
    crossover_methods = []
    deterministic_crossover_adjustment_types = ['dhc', 'ilc']
    for method in crossover_types:
        if method == 'deterministic':
            for deterministic_type in deterministic_crossover_adjustment_types:
                change_configurations(None, [['crossover_type', method], ['crossover_rate_adjustment_type', deterministic_type]], None, [['generation_stats', 'results/generation_stats/crossover/' + 'crossover_' + method + "_" + deterministic_type + "_" + str(iteration)], ['generation_data', 'results/generation_data/crossover/' + 'crossover_' + method + "_" + deterministic_type + "_" + str(iteration)]], None)
                configuration_update(path_configuration_file, metadata, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
                time = run_subprocess(['python3', 'genetic_algorithm.py'])
                time_execution_values.append([time, 'crossover_' + method + "_" + deterministic_type])
            
                crossover_methods.append('crossover_' + method + "_" + deterministic_type + "_" + str(iteration))
                util.write_metadata('results/best_generated_test_suite/crossover', util.read_best_generated_test_suite_data('results/best_generated_test_suite'),
                            util.read_metadata(util.obtain_configuration("config.ini", "metadata", "metadata_location")), method + "_" + deterministic_type + "_" + str(iteration))
                util.write_best_generated_test_suite_data('results/best_generated_test_suite/crossover', util.read_best_generated_test_suite_data('results/best_generated_test_suite'), method + "_" + deterministic_type + "_" + str(iteration))
                util.write_data_file('results/generation_data/crossover/' + 'crossover_' + method + "_" + deterministic_type + "_" + str(iteration), time, 'time_execution')
        else:
            change_configurations(None, [['crossover_type', method]], None, [['generation_stats', 'results/generation_stats/crossover/' + 'crossover_' + method + "_" + str(iteration)], ['generation_data', 'results/generation_data/crossover/' + 'crossover_' + method + "_" + str(iteration)]], None)
            configuration_update(path_configuration_file, metadata, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
            time = run_subprocess(['python3', 'genetic_algorithm.py'])
            time_execution_values.append([time, 'crossover_' + method])

            crossover_methods.append('crossover_' + method + "_" + str(iteration))
            util.write_metadata('results/best_generated_test_suite/crossover', util.read_best_generated_test_suite_data('results/best_generated_test_suite'),
                            util.read_metadata(util.obtain_configuration("config.ini", "metadata", "metadata_location")), method + "_" + str(iteration))
            util.write_best_generated_test_suite_data('results/best_generated_test_suite/crossover', util.read_best_generated_test_suite_data('results/best_generated_test_suite'), method + "_" + str(iteration))
            util.write_data_file('results/generation_data/crossover/' + 'crossover_' + method + "_" + str(iteration), time, 'time_execution')

    util.time_execution_histogram(time_execution_values, 'crossover', 'results/benchmarks/time_execution/crossover', iteration)

    time_execution_values.clear()

    return crossover_methods

'''
Function to execute the mutation methods

Parameters:
----------------
iteration: int

Returns:
----------------
mutation_methods: list
    List with the mutation methods executed
'''
def mutation_execution(iteration):
    mutation_methods = []
    deterministic_mutation_adjustment_types = ['dhm', 'ilm']
    for method in mutation_types:
        if method == 'deterministic':
            for deterministic_type in deterministic_mutation_adjustment_types:
                change_configurations(None, [['mutation_type', method], ['mutation_rate_adjustment_type', deterministic_type]], None, [['generation_stats', 'results/generation_stats/mutation/' + 'mutation_' + method + "_" + deterministic_type + "_" + str(iteration)], ['generation_data', 'results/generation_data/mutation/' + 'mutation_' + method + "_" + deterministic_type + "_" + str(iteration)]], None)
                configuration_update(path_configuration_file, metadata, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
                time = run_subprocess(['python3', 'genetic_algorithm.py'])
                time_execution_values.append([time, 'mutation_' + method + "_" + deterministic_type])

                mutation_methods.append('mutation_' + method + "_" + deterministic_type + "_" + str(iteration))
                util.write_metadata('results/best_generated_test_suite/mutation', util.read_best_generated_test_suite_data('results/best_generated_test_suite'),
                            util.read_metadata(util.obtain_configuration("config.ini", "metadata", "metadata_location")), method + "_" + deterministic_type + "_" + str(iteration))
                util.write_best_generated_test_suite_data('results/best_generated_test_suite/mutation', util.read_best_generated_test_suite_data('results/best_generated_test_suite'), method + "_" + deterministic_type + "_" + str(iteration))
                util.write_data_file('results/generation_data/mutation/' + 'mutation_' + method + "_" + deterministic_type + "_" + str(iteration), time, 'time_execution')
        else:
            change_configurations(None, [['mutation_type', method]], None, [['generation_stats', 'results/generation_stats/mutation/' + 'mutation_' + method + "_" + str(iteration)], ['generation_data', 'results/generation_data/mutation/' + 'mutation_' + method + "_" + str(iteration)]], None)
            configuration_update(path_configuration_file, metadata, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
            time = run_subprocess(['python3', 'genetic_algorithm.py'])
            time_execution_values.append([time, 'mutation_' + method])

            mutation_methods.append('mutation_' + method + "_" + str(iteration))
            util.write_metadata('results/best_generated_test_suite/mutation', util.read_best_generated_test_suite_data('results/best_generated_test_suite'),
                            util.read_metadata(util.obtain_configuration("config.ini", "metadata", "metadata_location")), method + "_" + str(iteration))
            util.write_best_generated_test_suite_data('results/best_generated_test_suite/mutation', util.read_best_generated_test_suite_data('results/best_generated_test_suite'), method + "_" + str(iteration))
            util.write_data_file('results/generation_data/mutation/' + 'mutation_' + method + "_" + str(iteration), time, 'time_execution')

    util.time_execution_histogram(time_execution_values, 'mutation', 'results/benchmarks/time_execution/mutation', iteration)

    time_execution_values.clear()

    return mutation_methods

def optimized_genetic_algorithms_execution(iteration):
    algorithms = []

    for genetic_algorithm in genetic_algorithms:

        if genetic_algorithm == 'tga':
            change_configurations(None, [['population_control', 'False'], ['selection_type', 'tournament'], ['crossover_type', 'uniform'], ['mutation_type', 'change_parameters']], None, [['generation_stats', 'results/generation_stats/optimized_genetic_algorithms/' + genetic_algorithm + "_" + str(iteration)], ['generation_data', 'results/generation_data/optimized_genetic_algorithms/' + genetic_algorithm + "_" + str(iteration)], ['generation_stats_history', 'results/generation_stats_history/optimized_genetic_algorithms/' + genetic_algorithm + "_" + str(iteration)]], None)
        elif genetic_algorithm == 'asga':
            change_configurations(None, [['population_control', 'True'], ['selection_type', 'adaptive']], None, [['generation_stats', 'results/generation_stats/optimized_genetic_algorithms/' + genetic_algorithm + "_" + str(iteration)], ['generation_data', 'results/generation_data/optimized_genetic_algorithms/' + genetic_algorithm + "_" + str(iteration)], ['generation_stats_history', 'results/generation_stats_history/optimized_genetic_algorithms/' + genetic_algorithm + "_" + str(iteration)]], None)
        elif genetic_algorithm == 'sacga':
            change_configurations(None, [['population_control', 'True'], ['crossover_type', 'self-adaptive']], None, [['generation_stats', 'results/generation_stats/optimized_genetic_algorithms/' + genetic_algorithm + "_" + str(iteration)], ['generation_data', 'results/generation_data/optimized_genetic_algorithms/' + genetic_algorithm + "_" + str(iteration)], ['generation_stats_history', 'results/generation_stats_history/optimized_genetic_algorithms/' + genetic_algorithm + "_" + str(iteration)]], None)
        elif genetic_algorithm == 'oga':
            change_configurations(None, [['population_control', 'True'], ['selection_type', 'rank'], ['crossover_type', 'adaptive'], ['mutation_type', 'self-adaptive']], None, [['generation_stats', 'results/generation_stats/optimized_genetic_algorithms/' + genetic_algorithm + "_" + str(iteration)], ['generation_data', 'results/generation_data/optimized_genetic_algorithms/' + genetic_algorithm + "_" + str(iteration)], ['generation_stats_history', 'results/generation_stats_history/optimized_genetic_algorithms/' + genetic_algorithm + "_" + str(iteration)]], None)

        configuration_update(path_configuration_file, metadata, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)
        time = run_subprocess(['python3', 'genetic_algorithm.py'])
        time_execution_values.append([time, genetic_algorithm])

        algorithms.append(genetic_algorithm + "_" + str(iteration))
        util.write_metadata('results/best_generated_test_suite/optimized_genetic_algorithms/' + genetic_algorithm, util.read_best_generated_test_suite_data('results/best_generated_test_suite'),
                    util.read_metadata(util.obtain_configuration("config.ini", "metadata", "metadata_location")), genetic_algorithm + "_" + str(iteration))
        util.write_best_generated_test_suite_data('results/best_generated_test_suite/optimized_genetic_algorithms/' + genetic_algorithm, util.read_best_generated_test_suite_data('results/best_generated_test_suite'), genetic_algorithm + "_" + str(iteration))
        util.write_data_file('results/generation_data/optimized_genetic_algorithms/' + genetic_algorithm + "_" + str(iteration), time, 'time_execution')

    util.time_execution_histogram(time_execution_values, "genetic_algorithms", 'results/benchmarks/time_execution/optimized_genetic_algorithms/', iteration)

    time_execution_values.clear()

    return algorithms

'''
Function to setup the folders for the genetic algorithm execution results
'''
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

    method_folders = ['population', 'selection', 'crossover', 'mutation', 'optimized_genetic_algorithms']

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

        # Verify if folder best_generated_test_suite exists for each method
        if not os.path.exists('results/best_generated_test_suite/' + folder):
            os.makedirs('results/best_generated_test_suite/' + folder)
        else:
            try:
                shutil.rmtree('results/best_generated_test_suite/' + folder)
                os.makedirs('results/best_generated_test_suite/' + folder)
            except OSError as e:
                print("Error: %s : %s" % ('results/best_generated_test_suite/' + folder, e.strerror))

        # Verify if folder generation_stats_history exists for each method
        if not os.path.exists('results/generation_stats_history/' + folder):
            os.makedirs('results/generation_stats_history/' + folder)
        else:
            try:
                shutil.rmtree('results/generation_stats_history/' + folder)
                os.makedirs('results/generation_stats_history/' + folder)
            except OSError as e:
                print("Error: %s : %s" % ('results/generation_stats_history/' + folder, e.strerror))

        

'''
Function to generate the benchmarks

Parameters:
----------------
benchmark_type: str
    Type of the benchmark

generations_methods: list
    List with the methods executed

generations_data: list
    List with the data of the generations

path: str
    Path of the benchmark
'''            
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
    elif 'population' not in benchmark_type and 'selection' not in benchmark_type: 
        util.crossover_rate_values_graph(crossover_rates, generations, 'Average Crossover Rate', benchmark_result, generations_methods)
        util.mutation_rate_values_graph(mutation_rates, generations, 'Average Mutation Rate', benchmark_result, generations_methods)

def obtain_configuration():
    # Read file
    config = configparser.ConfigParser()
    config.read('config.ini')
    # Obtain the dictionary
    return config['metadata'], config['genetic_algorithm_configurations'], config['genetic_operators_configurations'], config['genetic_algorithm_optimizations_configurations'], config['file_paths'], config['scripts']

metadata, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths, scripts = obtain_configuration()

# Execute the folder setup
folder_setup()

population = create_population(metadata_file, int(configurations.population_size.value), configurations)
# Write population in current directory
util.write_population_data_file(os.getcwd(), population)

change_configurations(None, None, None, None, [['execution_script', 'True']])
configuration_update(path_configuration_file, metadata, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)

for iteration in range(1,3):
    if eval(configurations.execution_optimizations.value):
        algorithms = optimized_genetic_algorithms_execution(iteration)
        print(algorithms)
        algorithms_generations_data = util.read_generation_stats_file(algorithms, 'optimized_genetic_algorithms')
        print("Optimized Genetic Algorithms Generations Data")
        print(algorithms_generations_data)
        print("------------------------------------------")
        generate_benchmarks(str(iteration), algorithms, algorithms_generations_data, 'results/benchmarks/optimized_genetic_algorithms/')
    else: 
        # Execute the population methods
        population_methods = population_execution(iteration)
        print(population_methods)
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

change_configurations(None, None, None, None, [['execution_script', 'False']])
configuration_update(path_configuration_file, metadata, genetic_algorithm_configurations, genetic_operators_configurations, genetic_algorithm_optimizations_configurations, file_paths)


'''
[metadata]
metadata_location = metadata.json

[genetic_algorithm_configurations]
max_number_functions = 5
max_number_test_cases = 5
tournament_size = 2
max_number_generations = 1000
fitness_max_stagnation_period = 100
fitness_function_type = branch_coverage
fitness_iteration_limit = 5

[genetic_operators_configurations]
population_size = 55
population_control = False
selection_type = tournament
crossover_type = uniform
crossover_rate = 0.5
crossover_rate_adjustment_type = ilc
mutation_type = change_parameters
mutation_rate = 0.15
mutation_rate_adjustment_type = dhm

[genetic_algorithm_optimizations_configurations]
population_decrease_rate = 0.2
uniform_number_crossover = 0.5
lt_max = 20
lt_min = 4
alpha = 0.7

[file_paths]
fuzzy_membership_functions = results/fuzzy_membership_functions
intermediate_test_suite = results/intermediate_test_suite
generation_stats = results/generation_stats/population/population_True_1
best_generated_test_suite = results/best_generated_test_suite
generation_data = results/generation_data/population/population_True_1
benchmark = results/benchmarks

[scripts]
execution_script = False
execution_optimizations = True
'''