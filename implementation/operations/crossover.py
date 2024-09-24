import random
from operations.population_control import *
from operations.fuzzy_system import *
from operations.mutation import *

'''
Function that selects the crossover operator to generate offsprings from two parents

Parameters:
----------
parents : list
    The parents to generate the offspring

metadata : dict
    The metadata of the class context

current_iteration_number : int
    The current generation number of the algorithm

inputs : dict
    The inputs for the fuzzy system

configurations : dict
    The configurations of the algorithm

type : string
    The type of crossover operator to select

Returns:
----------

offsprings : list
    A list containing the two offsprings generated from the parents
    
or

crossover_rate : float
    The crossover rate adjusted using the deterministic rule

'''
def crossover(parents, metadata, current_iteration_number, inputs, configurations, type):
    if type == 'one_point':
        return one_point_crossover(parents, configurations, metadata)
    elif type == 'uniform':
        return uniform_crossover(parents, configurations, metadata)
    elif type == 'deterministic':
        return deterministic_crossover_adjustment(current_iteration_number, int(configurations.max_number_generations.value), configurations.crossover_rate_adjustment_type.value)
    elif type == 'adaptive':
        return adaptive_crossover_adjustment(inputs, configurations, 'crossover')
    elif type == 'self-adaptive':
        return self_adaptive_crossover_adjustment(parents, metadata, current_iteration_number, inputs, configurations)
    else:
        raise ValueError('Crossover type is not specified correctly')
    
'''
Crossover operator to generate offsprings from two parents using the one point crossover
Parameters:
----------
parents : list
    The parents to generate the offspring 

configurations : dict
    The configurations of the algorithm

metadata : dict
    The metadata of the class context

Returns:
-------
offsprings : list
    A list containing the two offsprings generated from the parents
'''
# split position is considered as the index of the test case to be replaced
# test suite = [test case 1, test case 2, test case 3, test case 4]
# split position = 2
# new test suite = [0, 1, 2, 3] if split position is 2 then former positions 0 and 1 are kept and the rest are replaced with the latter positions 2 and 3 of the other parent

def one_point_crossover(parents, configurations, metadata):
    if len(parents[0].test_suite) > len(parents[1].test_suite):
        split_position = random.randint(1, len(parents[1].test_suite) - 1)
    else:
        split_position = random.randint(1, len(parents[0].test_suite) - 1)

    print("Split position " + str(split_position))

    offspring1 = create_offspring(parents[0].test_suite[:split_position] + parents[1].test_suite[split_position:], configurations, metadata)
    offspring2 = create_offspring(parents[1].test_suite[:split_position] + parents[0].test_suite[split_position:], configurations, metadata)
    offsprings = [offspring1, offspring2]

    return offsprings

'''
Crossover operator to generate offsprings from two parents using the uniform crossover

Parameters:
----------
parents : list
    The parents to generate the offspring

configurations : dict
    The configurations of the algorithm

metadata : dict
    The metadata of the class context

Returns:
-------
offsprings : list
    A list containing the two offsprings generated from the parents
'''
def uniform_crossover(parents, configurations, metadata):
    random_values = []
    offsprings = []
    uniform_number_crossover = float(configurations.uniform_number_crossover.value)

    if len(parents[0].test_suite) > len(parents[1].test_suite):
        for i in range(len(parents[1].test_suite)):
            random_values.append(random.uniform(0, 1))
    else:
        for i in range(len(parents[0].test_suite)):
            random_values.append(random.uniform(0, 1))

    print("Random values")
    for i in range(len(random_values)):
        print(str(random_values[i]) + "|")

    for position in range(2):
        test_suite = []
        for i in range(len(random_values)):
            if random_values[i] < uniform_number_crossover:
                if(position == 0):
                    test_suite.append(parents[0].test_suite[i])
                else:
                    test_suite.append(parents[1].test_suite[i])
            else:
                if(position == 0):
                    test_suite.append(parents[1].test_suite[i])
                else:
                    test_suite.append(parents[0].test_suite[i])
        offsprings.append(create_offspring(test_suite, configurations, metadata))

    return offsprings


'''
Crossover rate adjustment using a deterministic rule by increasing or decreasing the crossover rate linearly with the number of generations based on the work of Hassanat, 
Almohammadi, Alkafaween, Abunawas, Hammouri and Prasath in "Choosing Mutation and Crossover Ratios for Genetic Algorithms — A Review with a New Dynamic Approach"

Parameters:
----------
current_iteration_number : int
    The current generation number of the algorithm

max_generations : int
    The maximum number of generations of the algorithm

type : string
    Type of crossover rate adjustment, either to increase or decrease the crossover rate linearly with the number of generations

Returns:
-------
crossover_rate : float
    The crossover rate adjusted using the deterministic rule
'''
def deterministic_crossover_adjustment(current_iteration_number, max_generations, type):
    if type == 'ilc':
        return float(current_iteration_number/max_generations)
    elif type == 'dhc':
        return float(1 - (current_iteration_number / max_generations))
    
    raise Exception("Invalid crossover rate adjustment type")

'''
Crossover rate adaptive adjustment using a fuzzy expert system based upon the work of Shi, Eberhart and 
Chen in "Implementation of Evolutionary Fuzzy Systems"

Parameters:
----------
inputs : list
    The inputs of the fuzzy system

configurations : dict
    The configurations of the algorithm

genetic_operator : string
    The type of genetic operator to adjust

Returns:
-------
crossover_rate : float
    The crossover rate adjusted using the fuzzy system
'''
def adaptive_crossover_adjustment(inputs, configurations, genetic_operator):
    fuzzy_system = Fuzzy_system(configurations.fuzzy_membership_path.value)
    crossover_rate = fuzzy_system.fuzzy_control_system(fuzzy_system.rules, inputs, genetic_operator)
    return crossover_rate

'''
Function that implements the self-adaptive crossover operator to generate offsprings from two parents according to
the mechanism proposed by Back, Eiben and Vaart in the work "An empirical study on GAs "without parameters"".

The individual that is suspended from the crossover operation will be set on hold and will be used in the next iteration where only one parent will be selected and this
will be used to generate the offspring with the other individual chosen in the selection process.

Parameters:
----------
individuals : list
    The parents to generate the offspring

metadata : dict
    The metadata of the class context

current_iteration_number : int
    The current generation number of the algorithm

inputs : dict
    The inputs for the fuzzy system

configurations : dict
    The configurations of the algorithm

Returns:
-------
individuals : list
    A list containing the two offsprings generated from the parents, the individual that was suspended from the crossover operation and the index of the individual that was mutated
'''
def self_adaptive_crossover_adjustment(individuals, metadata, current_iteration_number, inputs, configurations):
    individual_suspended = None
    mutated_individual_index = None
    individuals[0], first_decision = self_adaptive_crossover_decision(individuals[0], metadata, current_iteration_number, inputs, configurations) 
    individuals[1], second_decision = self_adaptive_crossover_decision(individuals[1], metadata, current_iteration_number, inputs, configurations)

    if first_decision and second_decision:
        individuals = uniform_crossover(individuals, configurations, metadata)
        for individual in individuals:
            individual = mutation(individual, metadata, current_iteration_number, inputs, configurations, random.choice(['add_test_case', 'delete_test_case', 'change_parameters']))

    elif not first_decision and second_decision:
        individual_suspended = individuals[1]
        mutated_individual_index = 0
        
    elif first_decision and not second_decision:
        individual_suspended = individuals[0]
        mutated_individual_index = 1

    else:
        mutated_individual_index = -1

    print("Individuals" + str(individuals[0].test_suite) + "|" + str(individuals[1].test_suite) + "|" + "Individual suspended " + str(individual_suspended) + "|" + "Mutated individual index " + str(mutated_individual_index))
    individuals.append(individual_suspended)
    individuals.append(mutated_individual_index)

    return individuals

'''
Function that decides whether the crossover operator will be performed or not according to the mechanism proposed by Back, Eiben and Vaart 
in the work "An empirical study on GAs "without parameters"".

Parameters:
----------
individual : Solution
    The individual to decide whether the crossover operator will be performed or not

metadata : dict
    The metadata of the class context

current_iteration_number : int
    The current generation number of the algorithm

inputs : dict
    The inputs for the fuzzy system

configurations : dict
    The configurations of the algorithm

Returns:
-------
individual : Solution
    The individual that was used to decide whether the crossover operator will be performed or not

decision : bool
    A boolean value indicating whether the crossover operator will be performed or not which means the individual will be mutated if the crossover operator is not performed in
    the current iteration of the algorithm
'''
def self_adaptive_crossover_decision(individual, metadata, current_iteration_number, inputs, configurations):
    random_number = random.uniform(0, 1)
    print("Random number: " + str(random_number))
    print("Crossover rate: " + str(individual.adaptive_crossover_rate))

    if random_number < individual.adaptive_crossover_rate:
        return individual, True
    
    else:
        individual = mutation(individual, metadata, current_iteration_number, inputs, configurations, random.choice(['add_test_case', 'delete_test_case', 'change_parameters']))
        return individual, False
    
'''
Function to determine the average crossover rate of the population

Parameters:
----------
crossover_rates : list
    The crossover rates of the population

crossover_type : str
    The type of crossover applied

title_crossover_rate : str
    The title of the crossover rate

Returns:
-------
average_crossover_rate : float
    The average crossover rate of the population

'''
def average_crossover_rate(crossover_rates, crossover_type, title_crossover_rate):
    if crossover_type == 'deterministic' and len(crossover_rates) > 0:
        title_crossover_rate = "Average Crossover Rate - Deterministic Method"
        return sum(crossover_rates)/len(crossover_rates), title_crossover_rate
    elif crossover_type == 'adaptive' and len(crossover_rates) > 0:
        title_crossover_rate = "Average Crossover Rate - Adaptive Method"
        return sum(crossover_rates)/len(crossover_rates), title_crossover_rate
    
    return 0, title_crossover_rate
