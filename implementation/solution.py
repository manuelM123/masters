import random

# need to have a test suite where contains a set of test cases
# however a solution itself should be an array whose elements are the following [[type of method (constructor or other function), [parameters], [genetic operators]]]
# -1 for constructor, [0-total_number_functions] for other functions in respective order of the metadata

class Solution:
    '''
    Solution constructor to define the attributes of the solution
    '''
    def __init__(self):
        self.test_suite = []
        self.adaptive_crossover_rate = -1
        self.adaptive_mutation_rate = -1
        self.fitness = -1
        self.rank = -1
        self.mating_chance = -1
        self.adaptive_max_selections = 0
        self.remaining_lifetime = -1

    '''
    Function that generates a test case with constructor and other functions using the metadata from the class context

    Parameters:
    ----------
    metadata : dict
        The metadata of the class context

    max_number_functions : int
        The maximum number of other functions that can be generated

    Returns:
    -------
    test_case : list
        A list containing the test case in the structure [[identifier, [parameters], [genetic operators]]]
    '''
    def generate_test_case(self, metadata, max_number_functions):
        test_case = []

        # Generate constructor
        constructor = self.generate_constructor(metadata)
        test_case.append(constructor)

        # Generate a random number of other functions
        number_other_functions = random.randint(0, max_number_functions)

        for function in range(number_other_functions):
            # Generate other functions
            other_functions = self.generate_other_functions(metadata)
            test_case.append(other_functions)

        return test_case

    '''
    Function to generate a test suite with test cases using the metadata from the class context

    Parameters:
    ----------
    metadata : dict
        The metadata of the class context

    max_number_functions : int
        The maximum number of other functions that can be generated
        
    max_number_test_cases : int
        The maximum number of test cases that can be generated
    
    Returns:
    -------
    test_suite : list
        A list containing the test suite in the structure [[[identifier, [parameters], [genetic operators]]]]
    '''
    def generate_test_suite(self, metadata, max_number_functions, max_number_test_cases):
        # Generate a random number of test cases
        number_test_cases = random.randint(2, max_number_test_cases)
    
        for test_case in range(number_test_cases):
            # Generate test case
            self.test_suite.append(self.generate_test_case(metadata, max_number_functions))

    '''
    Function to generate a constructor using the metadata from the class context with random values specified in the metadata

    Parameters:
    ----------
    metadata : dict
        The metadata of the class context
    
    Returns:
    -------
    constructor : list
        A list containing the constructor in the structure [identifier, [parameters], [genetic operators]] when the constructor has the identifier -1
    '''
    def generate_constructor(self, metadata):
        constructor_parameters = []
        # Verify if metadata has a constructor attribute
        if 'constructor' in metadata:
            # Obtain parameters from constructor in metadata
            parameters = metadata['constructor']['parameters']

            for attribute in range(len(parameters)):
                #print(parameters[attribute])
                if 'min' in parameters[attribute] or 'max' in parameters[attribute]:
                    min = parameters[attribute]['min']
                    max = parameters[attribute]['max']

                    if 'int' in parameters[attribute]['type']:
                        constructor_parameters.append(random.randint(min, max))
                    else:
                        constructor_parameters.append(round(random.uniform(min, max),2))
                elif 'gender' in parameters[attribute]:
                    constructor_parameters.append(random.choice(parameters[attribute]['gender']))
                else:
                    constructor_parameters.append(random.choice(parameters[attribute]['intensity']))
        else:
            raise ValueError('Metadata does not contain a constructor')
        
        return [-1, constructor_parameters]

    '''
    Function to generate other functions using the metadata from the class context with random values specified in the metadata

    Parameters:
    ----------
    metadata : dict
        The metadata of the class context

    Returns:
    -------
    other_functions : list
        A list containing the other functions in the structure [identifier, [parameters], [genetic operators]] when the other functions have the identifier related 
        to the order they appear in the metadata
    '''
    def generate_other_functions(self, metadata):
        other_functions_parameters = []
        # Verify if metadata has a other_functions attribute
        if 'other_functions' in metadata:
            # Obtain parameters from other_functions in metadata
            parameters = metadata['other_functions']
            attribute = random.randint(0, len(parameters)-1)

            #print(parameters[attribute]['name'])

            if 'setter' in parameters[attribute]['type']:
                if 'min' in parameters[attribute]['parameters'][0] or 'max' in parameters[attribute]['parameters'][0]:
                    min = parameters[attribute]['parameters'][0]['min']
                    max = parameters[attribute]['parameters'][0]['max']
                    if 'age' in parameters[attribute]['name']:
                        other_functions_parameters.append(random.randint(min, max))
                    else:
                        other_functions_parameters.append(round(random.uniform(min, max),2))
                elif 'gender' in parameters[attribute]['parameters'][0]:
                    other_functions_parameters.append(random.choice(parameters[attribute]['parameters'][0]['gender']))
                else:
                    other_functions_parameters.append(random.choice(parameters[attribute]['parameters'][0]['intensity']))
        else:
            raise ValueError('Metadata does not contain other functions')
        
        return [attribute, other_functions_parameters]