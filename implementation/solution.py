import random

# need to have a test suite where contains a set of test cases
# however a solution itself should be an array whose elements are the following [[type of method (constructor or other function), [parameters], [genetic operators]]]
# -1 for constructor, [0-total_number_functions] for other functions in respective order of the metadata

class Solution:
    '''
    Solution class used to represent the solution of the unit test generation using the genetic algorithm
    '''
    def __init__(self):
        self.test_suite = []
        self.fitness = -1

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
        
        return [0, constructor_parameters, []]

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
            attribute  = random.randint(0, len(parameters)-1)

            print(parameters[attribute]['name'])

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
        
        return [attribute, other_functions_parameters, []]