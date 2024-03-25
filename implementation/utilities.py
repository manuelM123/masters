import os
import json
import configparser 
import numpy as np
import matplotlib.pyplot as plt

'''
Function to read metadata in a genotype format from a file

Parameters:
----------
file : str
    The file to read the metadata from

Returns:
-------
metadata : dict
    The metadata in a dictionary format
'''
def read_metadata(file):
    if os.path.exists(file):
        with open(file, 'r') as f:
            metadata = json.load(f)

        f.close()
        return metadata
    else:
        raise FileNotFoundError('File does not exist')
       
''' 
Function to write the generated test suite to a file in a phenotype format
test suite has the following structure:
[ [test_case_1], [test_case_2], ... ] 
test_case_i has the following structure:
[ [identifier, [parameters], [genetic operators]] ]

Parameters:
----------
path : str
    The path to write the test suite to
test_suite : list
    The test suite to write to a file
metadata : dict
    The metadata of the class context

'''
def write_metadata(path, test_suite, metadata, method_iteration):
    # If the path does not exist, create it
    if not os.path.exists(path):
        os.makedirs(path)

    if method_iteration == None:
        # If the file in the path does not exist, create it
        if not os.path.exists(path + "/test_cases.py"):
            f = open(path + "/test_cases.py", "w+")

        f = open(path + "/test_cases.py", "a+")
        f.truncate(0)

    else:
        # If the file in the path does not exist, create it
        if not os.path.exists(path + "/test_cases_" + str(method_iteration) + ".py"):
            f = open(path + "/test_cases_" + str(method_iteration) + ".py", "w+")
    
        f = open(path + "/test_cases_" + str(method_iteration) + ".py", "a+")
        f.truncate(0)

    f.write("from cut import *" + "\n" + "\n")

    # Write the test_suite to a file
    for position_test_suite in range(len(test_suite)):
        # Write def test_case to file
        f.write("def test_case_" + str(position_test_suite) + "():\n")
        for test_case in range(len(test_suite[position_test_suite])): 
            test_case_type = test_suite[position_test_suite][test_case][0]
            test_case_parameters = test_suite[position_test_suite][test_case][1]   
            # Write the constructor to file
            if test_case_type == -1:
                f.write("\tcut"+ " = " + metadata['constructor']['name'] + "(" + str(test_case_parameters[0]))
                for parameter in range(1, len(test_case_parameters)):
                    if type(test_case_parameters[parameter]) is not str:
                        f.write("," + str(test_case_parameters[parameter]))
                    else:
                        f.write("," + "'" + test_case_parameters[parameter] + "'") 
                f.write(")\n")
            # Write a setter method to file
            elif 'setter' in metadata['other_functions'][test_case_type]['type']:
                if type(test_case_parameters[0]) is not str: 
                    f.write("\tcut"+ "." + metadata['other_functions'][test_case_type]['name'] + " = " + str(test_case_parameters[0]) + "\n")
                else:
                    f.write("\tcut"+ "." + metadata['other_functions'][test_case_type]['name'] + " = " + "'" + str(test_case_parameters[0]) + "'" + "\n")
            # Write a method to file
            else:
                f.write("\tresult_" + metadata['other_functions'][test_case_type]['name'] + " = cut"+ "." + metadata['other_functions'][test_case_type]['name'] + "()" + "\n")
        f.write("\n")
    f.close()

'''
Function to read the configuration file for the genetic algorithm and select a particular configuration

Parameters:
----------
file : str
    The file to read the configuration from

Returns:
-------
config : list
    Configuration requested 
'''
def obtain_configuration(file, type, configuration_name):
    if os.path.exists(file):
        config = configparser.ConfigParser()
        config.read(file)
        return config.get(type, configuration_name)
    else:
        raise FileNotFoundError('File does not exist')
    
'''
Function to plot the population size variation per generation

Parameters:
----------
population_size_values: list
    The population size values per generation

generation_number_values: list
    The generation number values

path: str
    The path to save the graph
'''
def population_size_graph(population_size_values, generation_number_values, path, benchmarks):
    if plt.get_fignums():
            plt.close('all')

    if benchmarks == None:
        plt.plot(generation_number_values, population_size_values)
        plt.xlabel('Generation')
        plt.ylabel('Population Size')
        plt.title('Population Size per Generation')
    else:
        fig, ax = plt.subplots()
        for benchmark in range(len(benchmarks)):
            if 'test' in benchmarks[benchmark]:
                benchmark_label = benchmarks[benchmark].split('_')[0].capitalize() + ' ' + benchmarks[benchmark].split('_')[1] + ' ' + benchmarks[benchmark].split('_')[2] + ' ' + benchmarks[benchmark].split('_')[3]
            elif 'deterministic' in benchmarks[benchmark] or 'change' in benchmarks[benchmark]:
                benchmark_label = benchmarks[benchmark].split('_')[0].capitalize() + ' ' + benchmarks[benchmark].split('_')[1] + ' ' + benchmarks[benchmark].split('_')[2]
            else:
                benchmark_label = benchmarks[benchmark].split('_')[0].capitalize() + ' ' + benchmarks[benchmark].split('_')[1]

            ax.plot(generation_number_values[benchmark], population_size_values[benchmark], label=benchmark_label)
        
        ax.set_xlabel('Generation')
        ax.set_ylabel('Population Size')
        ax.set_title('Population Size per Generation')
        ax.legend()

    plt.savefig(path + '/population_size_graph.png')

'''
Function to plot the best fitness value variation per generation

Parameters:
----------
generation_fitness_values: list
    The best fitness value per generation

generation_number_values: list
    The generation number values

path: str
    The path to save the graph
'''
def fitness_values_graph(generation_fitness_values, generation_number_values, path, benchmarks):
    if plt.get_fignums():
            plt.close('all')
        
    if benchmarks == None:
        plt.plot(generation_number_values, generation_fitness_values)
        plt.xlabel('Generation')
        plt.ylabel('Fitness Value')
        plt.title('Best Fitness Value per Generation')
    else:
        fig, ax = plt.subplots()
        for benchmark in range(len(benchmarks)):
            if 'test' in benchmarks[benchmark]:
                benchmark_label = benchmarks[benchmark].split('_')[0].capitalize() + ' ' + benchmarks[benchmark].split('_')[1] + ' ' + benchmarks[benchmark].split('_')[2] + ' ' + benchmarks[benchmark].split('_')[3]
            elif 'deterministic' in benchmarks[benchmark] or 'change' in benchmarks[benchmark]:
                benchmark_label = benchmarks[benchmark].split('_')[0].capitalize() + ' ' + benchmarks[benchmark].split('_')[1] + ' ' + benchmarks[benchmark].split('_')[2]
            else:
                benchmark_label = benchmarks[benchmark].split('_')[0].capitalize() + ' ' + benchmarks[benchmark].split('_')[1]

            ax.plot(generation_number_values[benchmark], generation_fitness_values[benchmark], label=benchmark_label)

        ax.set_xlabel('Generation')
        ax.set_ylabel('Fitness Value')
        ax.set_title('Best Fitness Value per Generation')
        ax.legend()

    plt.savefig(path + '/fitness_values_graph.png')


'''
Function to plot the crossover rate variation per generation

Parameters:
----------
crossover_rate_values: list
    The crossover rate values per generation

generation_number_values: list
    The generation number values

title: str
    The title of the graph

path: str
    The path to save the graph 
'''
def crossover_rate_values_graph(crossover_rate_values, generation_number_values, title, path, benchmarks):
    if plt.get_fignums():
            plt.close('all')
    
    if benchmarks == None:
        plt.plot(generation_number_values, crossover_rate_values)
        plt.xlabel('Generation')
        plt.ylabel('Crossover rate')
        plt.title(title)

    else:
        fig, ax = plt.subplots()
        for benchmark in range(len(benchmarks)):
            if 'deterministic' in benchmarks[benchmark]:
                benchmark_label = benchmarks[benchmark].split('_')[0].capitalize() + ' ' + benchmarks[benchmark].split('_')[1] + ' ' + benchmarks[benchmark].split('_')[2]
            else:
                benchmark_label = benchmarks[benchmark].split('_')[0].capitalize() + ' ' + benchmarks[benchmark].split('_')[1]

            ax.plot(generation_number_values[benchmark], crossover_rate_values[benchmark], label=benchmark_label)

        ax.set_xlabel('Generation')
        ax.set_ylabel('Crossover rate')
        ax.set_title(title)
        ax.legend()

    plt.savefig(path + '/crossover_rate_values_graph.png')

'''
Function to plot the mutation rate variation per generation

Parameters:
----------
mutation_rate_values: list
    The mutation rate values per generation

generation_number_values: list
    The generation number values

title: str
    The title of the graph

path: str
    The path to save the graph 
'''
def mutation_rate_values_graph(mutation_rate_values, generation_number_values, title, path, benchmarks):
    if plt.get_fignums():
            plt.close('all')
    
    if benchmarks == None:
        plt.plot(generation_number_values, mutation_rate_values)
        plt.xlabel('Generation')
        plt.ylabel('Mutation rate')
        plt.title(title)
    else:
        fig, ax = plt.subplots()
        for benchmark in range(len(benchmarks)):
            if 'test' in benchmarks[benchmark]:
                benchmark_label = benchmarks[benchmark].split('_')[0].capitalize() + ' ' + benchmarks[benchmark].split('_')[1] + ' ' + benchmarks[benchmark].split('_')[2] + ' ' + benchmarks[benchmark].split('_')[3]
            elif 'deterministic' in benchmarks[benchmark] or 'change' in benchmarks[benchmark]:
                benchmark_label = benchmarks[benchmark].split('_')[0].capitalize() + ' ' + benchmarks[benchmark].split('_')[1] + ' ' + benchmarks[benchmark].split('_')[2]
            else:
                benchmark_label = benchmarks[benchmark].split('_')[0].capitalize() + ' ' + benchmarks[benchmark].split('_')[1]

            ax.plot(generation_number_values[benchmark], mutation_rate_values[benchmark], label=benchmark_label)

        ax.set_xlabel('Generation')
        ax.set_ylabel('Mutation rate')
        ax.set_title(title)
        ax.legend()
    
    plt.savefig(path + '/mutation_rate_values_graph.png')

'''
Function to plot the average time of execution per generation method

Parameters:
----------
time_execution_values: list
    The average time of execution per generation method

type: str
    The type of the generation method

path: str
    The path to save the graph
'''
def time_execution_histogram(time_execution_values, type, path, iteration):
    if plt.get_fignums():
            plt.close('all')

    fig, ax = plt.subplots()
    for time_execution in time_execution_values:
        generation_method_name = time_execution[1].split('_')[0].capitalize()
        for word in range(1, len(time_execution[1].split('_'))):
            generation_method_name += ' ' + time_execution[1].split('_')[word]

        # in each bar make a space to prevent overlapping
        ax.bar(generation_method_name, time_execution[0])

    ax.set_xlabel('Generation Method')
    ax.set_ylabel('Average Time of Execution (s)')
    ax.set_title('Average Time of Execution for ' + type.capitalize() + ' Methods')

    plt.xticks(rotation=90, ha='right')
    plt.savefig(path + '/' + type + '_time_execution_histogram_' + str(iteration) + '.png', bbox_inches='tight')

'''
Function to plot the mean best fitness of a generation method

Parameters:
----------
mean_best_fitness_values: list
    The mean best fitness values of a generation method

type: str
    The type of the generation method

path: str
    The path to save the graph
'''
def mean_best_fitness_histogram(mean_best_fitness_values, type, path):
    if plt.get_fignums():
            plt.close('all')
    
    fig, ax = plt.subplots()
    for mean_best_fitness in mean_best_fitness_values:
        generation_method_name = mean_best_fitness[0].split('_')[0].capitalize()
        for word in range(1, len(mean_best_fitness[0].split('_'))):
            generation_method_name += ' ' + mean_best_fitness[0].split('_')[word]

        # in each bar make a space to prevent overlapping
        ax.bar(generation_method_name, mean_best_fitness[1], yerr=mean_best_fitness[2],
               align='center', ecolor='black', capsize=10)
        
    ax.set_xlabel('Generation Method')
    ax.set_ylabel('Mean Best Fitness')
    ax.set_title('Mean Best Fitness for ' + type.capitalize() + ' Methods')

    plt.xticks(rotation=90, ha='right')
    plt.savefig(path + '/' + type + '_mean_best_fitness_histogram.png', bbox_inches='tight')

'''
Function to plot the best fitness value during the execution of the genetic algorithm

Parameters:
----------
best_fitness_values: list
    The best fitness value per generation

path: str
    The path to save the graph
'''
def best_fitness_seen_graph(best_fitness_values, generation_number_values, path, benchmarks):
    if plt.get_fignums():
            plt.close('all')

    if benchmarks == None:
        plt.plot(best_fitness_values)
        plt.xlabel('Generation')
        plt.ylabel('Best Fitness')
        plt.title('Best Fitness Seen')
    else:
        fig, ax = plt.subplots()
        for benchmark in range(len(benchmarks)):
            if 'test' in benchmarks[benchmark]:
                benchmark_label = benchmarks[benchmark].split('_')[0].capitalize() + ' ' + benchmarks[benchmark].split('_')[1] + ' ' + benchmarks[benchmark].split('_')[2] + ' ' + benchmarks[benchmark].split('_')[3]
            elif 'deterministic' in benchmarks[benchmark] or 'change' in benchmarks[benchmark]:
                benchmark_label = benchmarks[benchmark].split('_')[0].capitalize() + ' ' + benchmarks[benchmark].split('_')[1] + ' ' + benchmarks[benchmark].split('_')[2]
            else:
                benchmark_label = benchmarks[benchmark].split('_')[0].capitalize() + ' ' + benchmarks[benchmark].split('_')[1]

            ax.plot(generation_number_values[benchmark], best_fitness_values[benchmark], label=benchmark_label)
        
        ax.set_xlabel('Generation')
        ax.set_ylabel('Best Fitness')
        ax.set_title('Best Fitness Seen')
        ax.legend()

    plt.savefig(path + '/best_fitness_seen.png')

# generation_stats = [generation_number_values, population_size_values, generation_fitness_values, crossover_rate_generations, mutation_rate_generations]
'''
Function to write the generation stats into a json file

Parameters:
----------
generation_stats: list
    The generation stats to write into a json file

path: str
    The path to save the json file
'''
def write_generation_stats_file(generation_stats, path):
    print("Started writing list data into a json file")

    generation_stats_name = ['generation_number_values', 'population_size_values', 'generation_fitness_values', 'crossover_rate_values', 'mutation_rate_values', 'best_fitness_seen_values']

    for stat in range(len(generation_stats_name)):
        generation_data_path_stat = path + '/' + generation_stats_name[stat]

        with open(generation_data_path_stat + ".json", "w") as fp:
            json.dump(generation_stats[stat], fp)
            print("Done writing JSON data into .json file")

'''
Function to read the generation stats from a json file

Parameters:
----------
generation_methods: list
    The generation methods to read the generation stats from

type: str
    The type of the generation method

Returns:
-------
generations_data: list
    The generation stats read from the json file
'''
def read_generation_stats_file(generation_methods, type):
    print("Started reading list data from a json file")
    
    generation_stats_name = ['generation_number_values', 'population_size_values', 'generation_fitness_values', 'crossover_rate_values', 'mutation_rate_values', 'best_fitness_seen_values']
    generations_data = []
    
    for generation_method in range(len(generation_methods)):
        generation_data_read = []
        path = 'results/generation_data/' + type + "/" + generation_methods[generation_method]
        for stat in range(len(generation_stats_name)):
            # Verify if file exists
            if os.path.exists(path + '/' + generation_stats_name[stat] + '.json'):
                generation_read_path = path + '/' + generation_stats_name[stat]
                with open(generation_read_path + '.json', 'rb') as fp:
                    data = json.load(fp)
                    generation_data_read.append([generation_stats_name[stat], data])
        
        generations_data.append(generation_data_read)

    return generations_data


'''
Function to read the generation stats from a json file with a specific file type

Parameters:
----------
parameter_type: str
    The parameter type to read the generation stats from

type: str
    The type of the generation method   

Returns:
-------
generations_data_type: list
    The generation stats read from the json file
'''
def read_generations_stats_file_type(parameter_type, type, file_type):
    generations_data_type = []
    path = 'results/generation_data/' + type + "/" + parameter_type

    # Verify if file exists
    if os.path.exists(path + '/' + file_type + '.json'):
        generation_read_path = path + '/' + file_type
        with open(generation_read_path + '.json', 'rb') as fp:
            data = json.load(fp)

    return data

'''
Function to write the best generated test suite data into a json file

Parameters:
----------
path: str
    The path to save the json file

test_suite: list
    The best generated test suite to write into a json file

'''
def write_best_generated_test_suite_data(path, test_suite):
    print("Started writing list data into a json file")

    with open(path + "/best_generated_test_suite.json", "w") as fp:
        json.dump(test_suite, fp)
        print("Done writing JSON data into .json file")

'''
Function to read the best generated test suite data from a json file

Parameters:
----------
path: str
    The path to read the json file

Returns:
-------
data: list
    The best generated test suite read from the json file

'''
def read_best_generated_test_suite_data(path):
    print("Started reading list data from a json file")
    
    with open(path + '/best_generated_test_suite.json', 'rb') as fp:
        data = json.load(fp)
    
    return data

'''
Function to calculate the standard deviation of a population of values

Parameters:
----------
population: list
    The population of values to calculate the standard deviation of

Returns:
-------
standard_deviation: int
    The standard deviation of the population of values
'''
def standard_deviation(population):
    return np.std(population)