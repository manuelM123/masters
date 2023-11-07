import random
from operations.population_control import *

def crossover(parents, configurations, type):
    if type == 'one_point':
        return one_point_crossover(parents, configurations)
    elif type == 'uniform':
        return uniform_crossover(parents, configurations)
'''
Crossover operator to generate offsprings from two parents using the one point crossover
Parameters:
----------
parents : list
    The parents to generate the offspring 

configurations : dict
    The configurations of the algorithm

Returns:
-------
offsprings : list
    A list containing the two offsprings generated from the parents
'''
# split position is considered as the index of the test case to be replaced
# test suite = [test case 1, test case 2, test case 3, test case 4]
# split position = 2
# new test suite = [0, 1, 2, 3] if split position is 2 then former positions 0 and 1 are kept and the rest are replaced with the latter positions 2 and 3 of the other parent

def one_point_crossover(parents, configurations):
    if len(parents[0].test_suite) > len(parents[1].test_suite):
        split_position = random.randint(1, len(parents[1].test_suite) - 1)
    else:
        split_position = random.randint(1, len(parents[0].test_suite) - 1)

    print("Split position " + str(split_position))

    offspring1 = create_offspring(parents[0].test_suite[:split_position] + parents[1].test_suite[split_position:], configurations)
    offspring2 = create_offspring(parents[1].test_suite[:split_position] + parents[0].test_suite[split_position:], configurations)
    offsprings = [offspring1, offspring2]

    return offsprings

'''
Crossver operator to generate offsprings from two parents using the uniform crossover
Parameters:
----------
parents : list
    The parents to generate the offspring

configurations : dict
    The configurations of the algorithm

Returns:
-------
offsprings : list
    A list containing the two offsprings generated from the parents
'''

def uniform_crossover(parents, configurations):
    random_values = []
    offsprings = []
    uniform_number = float(configurations.uniform_number.value)

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
            if random_values[i] < uniform_number:
                if(position == 0):
                    test_suite.append(parents[0].test_suite[i])
                else:
                    test_suite.append(parents[1].test_suite[i])
            else:
                if(position == 0):
                    test_suite.append(parents[1].test_suite[i])
                else:
                    test_suite.append(parents[0].test_suite[i])
        offsprings.append(create_offspring(test_suite, configurations))

    return offsprings
    