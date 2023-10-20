import random

# Population contain test suites which are lists of test cases where each individual within the test suite is a test case
# structure of test suite: [ [test_case_1], [test_case_2], ... ]
# structure of test_case_i: [ [identifier, [parameters], [genetic operators]] ]

class Selection:

    def __init__(self, type):
        self.type = type

    def select(self, population, population_fitness):
        if self.type == 'random':
            pass
        if self.type == 'roulette_wheel':
            return self.roulette_wheel_selection(population, population_fitness)
        elif self.type == 'tournament':
            pass
        elif self.type == 'rank':
            pass
        else:
            raise ValueError('Selection type is not specified correctly')
    
    '''
    Random selection to select two parents from the population 

    Parameters:
    ----------
    population : list
        The population to select the parents from
    
    Returns:
    -------
    parents_selection : list
        A list containing the two parents selected from the population
    '''
    def random_selection(self, population):
        parents_selection = [random.randint(0, len(population) - 1), random.randint(0, len(population) - 1)]

        while parents_selection[0] == parents_selection[1]:
            parents_selection[1] = random.randint(0, len(population) - 1)
        
        return parents_selection

    '''
    Roulette wheel selection to select two parents from the population 
    Selection probability of an individual is calculated by dividing the individual's fitness by the sum of the fitness of the population
    A sum of each selection probability is calculated and a random number is generated in the interval [0, sum(population_fitness)]
    The individual whose selection probability sum is greater than the random number is selected as a parent
    The process is repeated until two parents are selected

    Parameters:
    ----------
    population : list
        The population to select the parents from
    population_fitness : list
        The fitness of each individual in the population
    
    Returns:
    -------
    parents_selection : list
        A list containing the two parents selected from the population
    '''
    def roulette_wheel_selection(self, population, population_fitness):
        # Calculate the selection probabilities for each individual
        # population_fitness is a list that holds every individual's fitness of the population 

        # When selecting a first individual, do the loop again with another random number to ensure
        # that the individual is not chosen in bias according the order of the sum of the selection probabilities 
        # Verify if the individuals selected are the same
    
        selection_probabilities = []
        for individual_fitness in population_fitness:
            selection_probabilities.append(round(individual_fitness / sum(population_fitness),2))

        parents_selection = []
        selection_probabilities_sum = 0
        random_number = random.randint(0, sum(population_fitness))

        while len(parents_selection) < 2:
            for i in range(len(population) - 1):
                selection_probabilities_sum += selection_probabilities[i]

                if selection_probabilities_sum >= random_number:
                    parents_selection.append(population[i])
                    random_number = random.randint(0, sum(population_fitness))
                    selection_probabilities_sum = 0
                    break 
            
            if len(parents_selection) > 1 and parents_selection[0] == parents_selection[1]:
                parents_selection.pop(1)

        return parents_selection
            
    def rank_selection(self, population, population_fitness):
        pass

    def tournament_selection(self, population, fitness):
        pass

    def adaptive_selection(self, population, fitness):
        pass
