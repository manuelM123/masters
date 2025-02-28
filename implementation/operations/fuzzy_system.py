import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import utilities as util
import os

class Fuzzy_system:
    '''
    Fuzzy system constructor to define the antecedents, consequents, fuzzy sets and rules of the fuzzy system
    '''
    def __init__(self, fuzzy_membership_path):
        self.antecedents = self.define_antecedents()
        self.consequents = self.define_consequents()
        self.define_fuzzy_sets(self.antecedents, self.consequents)
        self.plot_fuzzy_sets(self.antecedents, self.consequents, fuzzy_membership_path)
        self.rules = self.define_fuzzy_rules(self.antecedents, self.consequents)

    '''
    Function to define the antecedents of the fuzzy system

    Returns:
        antecedents: list of antecedents
    '''
    def define_antecedents(self):
        best_fitness = ctrl.Antecedent(np.arange(0.0, 1.1, 0.1), 'best_fitness')
        number_generations_unchanged_best_fitness = ctrl.Antecedent(np.arange(0, 13, 1), 'number_generations_unchanged_best_fitness')
        variance_fitness = ctrl.Antecedent(np.arange(0.0, 0.21, 0.01), 'variance_fitness')
        antecedents = [best_fitness, number_generations_unchanged_best_fitness, variance_fitness]

        return antecedents

    '''
    Function to define the consequents of the fuzzy system

    Returns:
        consequents: list of consequents
    '''
    def define_consequents(self):
        crossover_rate = ctrl.Consequent(np.arange(0.48, 0.83, 0.01), 'crossover_rate')
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
    def define_fuzzy_sets(self, antecedents, consequents):
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
    def define_fuzzy_rules(self, antecedents, consequents):
        rule1 = ctrl.Rule(antecedents[0]['low'], consequents[1]['low'])
        rule1_2 = ctrl.Rule(antecedents[0]['low'], consequents[0]['high'])

        rule2 = ctrl.Rule(antecedents[0]['medium'] & antecedents[1]['low'], consequents[1]['low'])
        rule2_1 = ctrl.Rule(antecedents[0]['medium'] & antecedents[1]['low'], consequents[0]['high'])

        rule3 = ctrl.Rule(antecedents[0]['medium'] & antecedents[1]['medium'], consequents[1]['medium'])
        rule3_1 = ctrl.Rule(antecedents[0]['medium'] & antecedents[1]['medium'], consequents[0]['medium'])

        rule4 = ctrl.Rule(antecedents[1]['high'] & antecedents[2]['medium'], consequents[1]['high'])
        rule4_1 = ctrl.Rule(antecedents[1]['high'] & antecedents[2]['medium'], consequents[0]['low'])

        rule5 = ctrl.Rule(antecedents[0]['high'] & antecedents[1]['low'], consequents[1]['low'])
        rule5_1 = ctrl.Rule(antecedents[0]['high'] & antecedents[1]['low'], consequents[0]['high'])

        rule6 = ctrl.Rule(antecedents[0]['high'] & antecedents[1]['medium'], consequents[1]['medium'])
        rule6_1 = ctrl.Rule(antecedents[0]['high'] & antecedents[1]['medium'], consequents[0]['medium'])

        rule7 = ctrl.Rule(antecedents[1]['high'] & antecedents[2]['low'], consequents[1]['high'])
        rule7_1 = ctrl.Rule(antecedents[1]['high'] & antecedents[2]['low'], consequents[0]['low'])

        rule8 = ctrl.Rule(antecedents[1]['high'] & antecedents[2]['high'], consequents[1]['low'])
        rule8_1 = ctrl.Rule(antecedents[1]['high'] & antecedents[2]['high'], consequents[0]['low'])

        return [rule1, rule1_2, rule2, rule2_1, rule3, rule3_1, rule4, rule4_1, rule5, rule5_1, rule6, rule6_1, rule7, rule7_1, rule8, rule8_1]

    '''
    Function to define the fuzzy control system to compute the crossover and mutation rates

    Parameters:
    ----------
    rules: list of rules
        The rules of the fuzzy system
    
    inputs: list
        The inputs of the fuzzy system

    genetic_operator: string
        The type of genetic operator to adjust

    Returns:
    -------
    crossover_rate: float
        The crossover rate computed by the fuzzy system

    mutation_rate: float
        The mutation rate computed by the fuzzy system
    '''
    def fuzzy_control_system(self, rules, inputs, genetic_operator):
        fuzzy_control_system = ctrl.ControlSystem(rules)
        fuzzy_control = ctrl.ControlSystemSimulation(fuzzy_control_system)
        fuzzy_control.input['best_fitness'] = inputs[0]
        fuzzy_control.input['number_generations_unchanged_best_fitness'] = inputs[1]
        fuzzy_control.input['variance_fitness'] = inputs[2]

        fuzzy_control.compute()

        if(genetic_operator == 'crossover'):
            return fuzzy_control.output['crossover_rate']
        elif(genetic_operator == 'mutation'):
            return fuzzy_control.output['mutation_rate']
        else:
            raise ValueError('Genetic operator is not specified correctly')
        
    '''
    Function to plot the fuzzy sets of the fuzzy system 

    Parameters:
    ----------
    antecedents: skfuzzy.control.Antecedent
        The antecedents of the fuzzy system

    consequents: skfuzzy.control.Consequent
        The consequents of the fuzzy system

    path: string
        The path to save the visual representations of the fuzzy sets
    '''
    def plot_fuzzy_sets(self, antecedents, consequents, path):
        if plt.get_fignums():
            plt.close('all')

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