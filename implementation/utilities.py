import os
import json
import configparser 
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline 
import matplotlib.ticker as ticker

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
def write_metadata(path, test_suite, metadata):
    # If the path does not exist, create it
    if not os.path.exists(path):
        os.makedirs(path)

    # If the file in the path does not exist, create it
    if not os.path.exists(path + "/test_cases.py"):
        f = open(path + "/test_cases.py", "w+")
    
    f = open(path + "/test_cases.py", "a+")
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
def population_size_graph(population_size_values, generation_number_values, path):
    if plt.get_fignums():
            plt.close('all')

    x = np.linspace(min(generation_number_values), max(generation_number_values), 500)
    k = min(3, len(generation_number_values) - 1)
    x_y_spline = make_interp_spline(generation_number_values, population_size_values, k=k)
    y = x_y_spline(x)

    plt.plot(generation_number_values, population_size_values)
    plt.xlabel('Generation')
    plt.ylabel('Population Size')
    plt.title('Population Size per Generation')

    plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

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
def fitness_values_graph(generation_fitness_values, generation_number_values, path):
    if plt.get_fignums():
            plt.close('all')
    
    x = np.linspace(min(generation_number_values), max(generation_number_values), 500)
    k = min(3, len(generation_number_values) - 1)
    x_y_spline = make_interp_spline(generation_number_values, generation_fitness_values, k=k)
    y = x_y_spline(x)

    plt.plot(generation_number_values, generation_fitness_values)
    plt.xlabel('Generation')
    plt.ylabel('Best Fitness Value')
    plt.title('Best Fitness Value per Generation')

    plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

    plt.savefig(path + '/fitness_values_graph.png')
    