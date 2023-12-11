from solution import *
from operations.fuzzy_system import *

'''
Function that selects the mutation operator to generate offsprings from one parent

Parameters:
----------
individual : Solution
    The individual to generate the offspring

metadata : dict
    The metadata of the class context

configurations : dict
    The configurations of the algorithm

type : str
    The type of mutation to be performed

Returns:
-------
individual : Solution
    The offspring generated from the parent
'''
def mutation(individual, metadata, inputs, configurations, type):
    solution = Solution()
    if type == 'add_test_case':
        return add_test_case(individual, metadata, configurations, solution)
    elif type == 'delete_test_case':
        return delete_test_case(individual)
    elif type == 'change_parameters':
        return change_parameters(individual, metadata, solution)
    elif type == 'deterministic':
        return deterministic_mutation_adjustment(configurations.current_iteration_number, configurations.max_generations, configurations.mutation_rate_adjustment_type)
    elif type == 'adaptive':
        return adaptive_mutation_adjustment(inputs, 'mutation')
    elif type == 'self-adaptive':
        return self_adaptive_mutation_adjustment()
    else:
        raise ValueError('Mutation type is not specified correctly')

'''
Function to add a test case to the individual

Parameters:
----------
individual : Solution
    The individual to add the test case to

metadata : dict
    The metadata of the class context

configurations : dict
    The configurations of the algorithm

solution : Solution
    The solution to generate the test case from

Returns:
-------
individual : Solution
    The individual with the new test case added
'''
def add_test_case(individual, metadata, configurations, solution):
    new_test_case = []

    while len(new_test_case) < 2:
        new_test_case = solution.generate_test_case(metadata, int(configurations.max_number_functions.value))

    print("New test case " + str(new_test_case))

    individual.append(new_test_case[1:])
    return individual

'''
Function to delete a test case from the individual

Parameters:
----------
individual : Solution
    The individual to delete the test case from

Returns:
-------
individual : Solution
    The individual with the test case deleted
'''
def delete_test_case(individual):
    if len(individual) > 1:
        position = random.randint(1, len(individual) - 1)
        individual.pop(position)
        return individual
    else:
        return individual
    
'''
Function to change the parameters of a test case from the individual

Parameters:
----------
individual : Solution
    The individual to change the parameters from

metadata : dict
    The metadata of the class context

solution : Solution
    The solution to generate the new parameters from

Returns:
-------
individual : Solution
    The individual with the new parameters
'''
def change_parameters(individual, metadata, solution):
    position_test_case = random.randint(0, len(individual) - 1)   
    test_case = individual[position_test_case] 
    position_method = random.randint(0, len(test_case) - 1)
    method = test_case[position_method]
    
    # constructor
    if method[0] == -1:
        print("Constructor")
        individual[position_test_case][position_method] = solution.generate_constructor(metadata)
    # other function
    else:
        print("Function " + str(method[0]))
        individual[position_test_case][position_method] = solution.generate_other_functions(metadata)

    return individual   

'''
Mutation rate adjustment using a deterministic rule by increasing or decreasing the mutation rate linearly with the number of generations based on the work of Hassanat, 
Almohammadi, Alkafaween, Abunawas, Hammouri and Prasath in "Choosing Mutation and Crossover Ratios for Genetic Algorithms — A Review with a New Dynamic Approach"

Parameters:
----------
current_iteration_number : int
    The current iteration number of the algorithm

max_generations : int
    The maximum number of generations of the algorithm

type : string
    Type of mutation rate adjustment, either to increase or decrease the mutation rate linearly with the number of generations

Returns:
-------
mutation_rate : float
    The mutation rate adjusted using the deterministic rule
'''
def deterministic_mutation_adjustment(current_iteration_number, max_generations, type):
    if type == 'ilm':
        return current_iteration_number / max_generations
    elif type == 'dhm':
        return 1 - (current_iteration_number / max_generations)
    
    raise Exception("Invalid mutation rate adjustment type")

'''
Mutation rate adaptive adjustment using a fuzzy expert system based upon the work of Shi, Eberhart and 
Chen in "Implementation of Evolutionary Fuzzy Systems"

Parameters:
----------
inputs : list
    The inputs of the fuzzy system

genetic_operator : string
    The type of genetic operator to adjust

Returns:
-------
mutation_rate : float
    The mutation rate adjusted using the fuzzy system
'''
def adaptive_mutation_adjustment(inputs, genetic_operator):
    fuzzy_system = Fuzzy_system()
    mutation_rate = fuzzy_system.fuzzy_control_system(fuzzy_system.rules, inputs, genetic_operator)
    return mutation_rate


def self_adaptive_mutation_adjustment():
    pass