import subprocess
import os

'''
Function to calculate the fitness of a test suite
The fitness is calculated using the coverage module
A specification of each type of coverage is needed

Parameters:
----------
test_suite : list
    The test suite to calculate the fitness of

type : str
    The type of coverage to calculate the fitness of the test suite

Returns:
-------
fitness : int
    The fitness of the test 
'''
def calculate_coverage_fitness(test_suite, type):
    if type == 'statement_coverage':
        subprocess.run(['coverage', 'run', '--timid', '-m', 'pytest', '-q', 'results/intermediate_test_suite'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        process = subprocess.run(['coverage', 'report'], capture_output=True, text=True)
        lines = process.stdout.split("\n")
        for line_number, line in enumerate(lines):
            if 'cut.py' in line:
                test_suite.fitness = int(process.stdout.split("\n")[line_number].split()[3].replace("%",""))/100

    elif type == 'branch_coverage':
        subprocess.run(['coverage', 'run', '--timid', '--branch', '-m', 'pytest', '-q', 'results/intermediate_test_suite'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        process = subprocess.run(['coverage', 'report'], capture_output=True, text=True)
        lines = process.stdout.split("\n")
        for line_number, line in enumerate(lines):
            if 'cut.py' in line:
                test_suite.fitness = int(process.stdout.split("\n")[line_number].split()[5].replace("%",""))/100
    else:
        raise ValueError('Fitness function type is not specified correctly')
    
    # Remove the .coverage file if it exists
    if os.path.exists('.coverage'):
        os.remove('.coverage')

'''
Function to obtain the fitness values of a population and insert them into a list for easier manipulation

Parameters:
----------
population : list
    The population to obtain the fitness values from

Returns:
-------
individuals_fitness : list
    A list containing the fitness values of each individual in the population
'''
def obtain_fitness_values(population):
    individuals_fitness = []
    for individual in population:
        individuals_fitness.append(individual.fitness)
    return individuals_fitness

'''
Function to calculate the average fitness of a population

Parameters:
----------
population : list
    The population to calculate the average fitness of

Returns:
-------
average_fitness : float
    The average fitness of the population
'''
def calculate_average_fitness(population):
    average_fitness = 0
    for individual in population:
        average_fitness += individual.fitness

    return average_fitness/len(population)

'''
Function to obtain the best fitness value of a population

Parameters:
----------
fitness_values : list
    The fitness values of the population

Returns:
-------
best_fitness : float
    The best fitness value of the population
'''
def obtain_best_fitness(fitness_values):
    return max(fitness_values)

'''
Function to obtain the mean fitness value from a set of fitness values

Parameters:
----------
fitness_values : list
    A list of fitness values

Returns:
-------
mean_fitness : float
    The mean fitness value of the fitness values
'''
def mean_best_fitness(fitness_values):
    return sum(fitness_values)/len(fitness_values)