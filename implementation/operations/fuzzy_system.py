import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import os

'''
Function to define the antecedents of the fuzzy system

Returns:
    antecedents: list of antecedents
'''
def define_antecedents():
    best_fitness = ctrl.Antecedent(np.arange(0.0, 1.1, 0.1), 'best_fitness')
    number_generations_unchanged_best_fitness = ctrl.Antecedent(np.arange(0, 21, 1), 'number_generations_unchanged_best_fitness')
    variance_fitness = ctrl.Antecedent(np.arange(0.0, 0.21, 0.01), 'variance_fitness')
    antecedents = [best_fitness, number_generations_unchanged_best_fitness, variance_fitness]

    return antecedents

'''
Function to define the consequents of the fuzzy system

Returns:
    consequents: list of consequents
'''
def define_consequents():
    crossover_rate = ctrl.Consequent(np.arange(0.40, 0.91, 0.01), 'crossover_rate')
    mutation_rate = ctrl.Consequent(np.arange(0.005, 0.105, 0.005), 'mutation_rate')
    consequents = [crossover_rate, mutation_rate]

    return consequents

'''
Function to define the fuzzy sets of the fuzzy system

Parameters:
----------
antecedents: skfuzzy.control.Antecedent
    The antecedents of the fuzzy system

consequents: skfuzzy.control.Consequent
    The consequents of the fuzzy system
'''
def define_fuzzy_sets(antecedents, consequents):
    antecedents[0]['low'] = fuzz.trimf(antecedents[0].universe, [0, 0, 0.7])
    antecedents[0]['medium'] = fuzz.trimf(antecedents[0].universe, [0.5, 0.7, 0.9])
    antecedents[0]['high'] = fuzz.trimf(antecedents[0].universe, [0.7, 1, 1])

    antecedents[1]['low'] = fuzz.trimf(antecedents[1].universe, [0, 0, 6])
    antecedents[1]['medium'] = fuzz.trimf(antecedents[1].universe, [3, 6, 9])
    antecedents[1]['high'] = fuzz.trimf(antecedents[1].universe, [6, 12, 12])

    antecedents[2]['low'] = fuzz.trimf(antecedents[2].universe, [0, 0, 0.12])
    antecedents[2]['medium'] = fuzz.trimf(antecedents[2].universe, [0.1, 0.12, 0.14])
    antecedents[2]['high'] = fuzz.trimf(antecedents[2].universe, [0.12, 0.2, 0.2])

    consequents[0]['low'] = fuzz.trimf(consequents[0].universe, [0.48, 0.48, 0.65])
    consequents[0]['medium'] = fuzz.trimf(consequents[0].universe, [0.55, 0.65, 0.75])
    consequents[0]['high'] = fuzz.trimf(consequents[0].universe, [0.65, 0.83, 0.83])

    consequents[1]['low'] = fuzz.trimf(consequents[1].universe, [0.005, 0.005, 0.015])
    consequents[1]['medium'] = fuzz.trimf(consequents[1].universe, [0.01, 0.015, 0.02])
    consequents[1]['high'] = fuzz.trimf(consequents[1].universe, [0.015, 0.1, 0.1])

'''
Function to define the fuzzy rules of the fuzzy system

Parameters:
----------
antecedents: skfuzzy.control.Antecedent
    The antecedents of the fuzzy system

consequents: skfuzzy.control.Consequent
    The consequents of the fuzzy system

Returns:
-------
rules: list of rules
'''
def define_fuzzy_rules(antecedents, consequents):
    rule1 = ctrl.Rule(antecedents[0]['low'], consequents[1]['low'] & consequents[0]['high'])
    rule2 = ctrl.Rule(antecedents[0]['medium'] & antecedents[1]['low'], consequents[1]['low'] & consequents[0]['high'])
    rule3 = ctrl.Rule(antecedents[0]['medium'] & antecedents[1]['medium'], consequents[1]['medium'] & consequents[0]['medium'])
    rule4 = ctrl.Rule(antecedents[1]['high'] & antecedents[2]['medium'], consequents[1]['high'] & consequents[0]['low'])
    rule5 = ctrl.Rule(antecedents[0]['high'] & antecedents[1]['low'], consequents[1]['low'] & consequents[0]['high'])
    rule6 = ctrl.Rule(antecedents[0]['high'] & antecedents[1]['medium'], consequents[1]['medium'] & consequents[0]['medium'])
    rule7 = ctrl.Rule(antecedents[1]['high'] & antecedents[2]['low'], consequents[1]['high'] & consequents[0]['low'])
    rule8 = ctrl.Rule(antecedents[1]['high'] & antecedents[2]['high'], consequents[1]['low'] & consequents[0]['low']) 

    return [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8]


'''
Function to plot the membership functions 

Parameters:
----------
antecedents: skfuzzy.control.Antecedent
    The antecedents of the fuzzy system

consequents: skfuzzy.control.Consequent
    The consequents of the fuzzy system
'''
def plot_fuzzy_sets(antecedents, consequents, path):
    if not os.path.exists(path):
        os.makedirs(path)  # Create the directory if it doesn't exist

    antecedents[0].view()
    plt.savefig(os.path.join(path, 'best_fitness.png'))
    antecedents[1].view()
    plt.savefig(os.path.join(path, 'number_generations_unchanged_best_fitness.png'))
    antecedents[2].view()
    plt.savefig(os.path.join(path, 'variance_fitness.png'))

    consequents[0].view()
    plt.savefig(os.path.join(path, 'crossover_rate.png'))
    consequents[1].view()
    plt.savefig(os.path.join(path, 'mutation_rate.png'))