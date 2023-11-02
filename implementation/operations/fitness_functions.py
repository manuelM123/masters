import subprocess

'''
Function to calculate the fitness of a test suite
The fitness is calculated using the coverage module
A specification of each type of coverage is needed
Parameters:
----------
test_suite : list
    The test suite to calculate the fitness of
Returns:
-------
fitness : int
    The fitness of the test 
'''
# Using coverage module within a subprocess to calculate the fitness of a test suite 
def calculate_coverage_fitness(test_suite, type):
    if(type == 'statement_coverage'):
        subprocess.run(['coverage', 'run', '-m', 'pytest', 'results/intermediate_test_suite'])
        process = subprocess.run(['coverage', 'report'], capture_output=True, text=True)
        lines = process.stdout.split("\n")
        for line_number, line in enumerate(lines):
            if 'cut.py' in line:
                test_suite.fitness = round(int(process.stdout.split("\n")[line_number].split()[3].replace("%",""))/100,2)

    elif(type == 'branch_coverage'):
        subprocess.run(['coverage', 'run', '--branch', '-m', 'pytest', 'results/intermediate_test_suite'])
        process = subprocess.run(['coverage', 'report'], capture_output=True, text=True)
        lines = process.stdout.split("\n")
        for line_number, line in enumerate(lines):
            if 'cut.py' in line:
                test_suite.fitness = round(int(process.stdout.split("\n")[line_number].split()[5].replace("%",""))/100,2)
    else:
        raise ValueError('Fitness function type is not specified correctly')

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
average_fitness : int
    The average fitness of the population
'''
def calculate_average_fitness(population):
    average_fitness = 0
    for individual in population:
        average_fitness += individual.fitness

    return average_fitness/len(population)