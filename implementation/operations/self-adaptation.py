import random
from utilities import *
from operations.crossover import *
from operations.mutation import *
import numpy as np

'''
Function that implements the self-adaptive crossover operator to generate offsprings from two parents according to
the mechanism proposed by Back, Eiben and Vaart in the work An empirical study on GAs "without parameters".

The individual that is suspended from the crossover operation will be set on hold and will be used in the next iteration where only one parent will be selected and this
will be used to generate the offspring with the other individual chosen in the selection process.

Parameters:
----------
individuals : list
    The parents to generate the offspring

metadata : dict
    The metadata of the class context

inputs : dict
    The inputs for the fuzzy system

configurations : dict
    The configurations of the algorithm

mutation_type : str
    The type of mutation to be performed

Returns:
-------
individuals : list
    A list containing the two offsprings generated from the parents

individual_suspended : Solution
    The individual that was suspended from the crossover operation
'''
def self_adaptive_crossover_operation(individuals):
    individual_suspended = []
    individuals[0], first_decision = self_adaptive_crossover_decision(individuals[0]) 
    individuals[1], second_decision = self_adaptive_crossover_decision(individuals[1])

    if first_decision and second_decision:
        individuals = uniform_crossover(individuals)
    elif first_decision and not second_decision:
        individual_suspended = individuals[0]
    elif not first_decision and second_decision:
        individual_suspended = individuals[1]

    return individuals, individual_suspended
    
'''
Function that decides whether the crossover operator will be performed or not according to the mechanism proposed by Back, Eiben and Vaart 
in the work An empirical study on GAs "without parameters".

Parameters:
----------
individual : Solution
    The individual to decide whether the crossover operator will be performed or not

metadata : dict
    The metadata of the class context

inputs : dict
    The inputs for the fuzzy system

configurations : dict
    The configurations of the algorithm

mutation_type : str
    The type of mutation to be performed

Returns:
-------
individual : Solution
    The individual that was used to decide whether the crossover operator will be performed or not

decision : bool
    A boolean value indicating whether the crossover operator will be performed or not
'''
def self_adaptive_crossover_decision(individual):
    random_number = random.uniform(0, 0.99)
    if random_number < individual.adaptive_crossover_rate:
        return individual, True
    else:
        individual = mutation(individual)
        return individual, False
    

'''
Function that implements the self-adaptive mutation operator to mutate the individuals according to the mechanism proposed by Back, Eiben and Vaart
in the work An empirical study on GAs "without parameters".

Parameters:
----------
individuals : list
    The individuals to mutate

Returns:
-------
individuals : list
    A list containing the two offsprings generated from the parents
'''
def self_adaptive_mutation_operation(individuals):
    for i in individuals:
        i.adaptive_mutation_rate = (1 + ((1 - i.adaptive_mutation_rate) / i.adaptive_mutation_rate) * ((-0.22) * np.random.normal(0, 1))) ** (-1)

    return individuals