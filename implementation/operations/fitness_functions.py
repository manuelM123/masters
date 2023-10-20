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
        test_suite.fitness = round(int(process.stdout.split("\n")[2].split()[3].replace("%",""))/100,2)

    elif(type == 'branch_coverage'):
        subprocess.run(['coverage', 'run', '--branch', '-m', 'pytest', 'results/intermediate_test_suite'])
        process = subprocess.run(['coverage', 'report'], capture_output=True, text=True)
        test_suite.fitness = round(int(process.stdout.split("\n")[2].split()[5].replace("%",""))/100,2)

    else:
        raise ValueError('Fitness function type is not specified correctly')