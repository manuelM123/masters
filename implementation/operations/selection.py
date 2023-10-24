import random
import utilities as util

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
            return self.rank_selection(population)
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
        random_number = random.uniform(0, sum(selection_probabilities))

        print("Random number: " + str(random_number))
        print(selection_probabilities)

        while len(parents_selection) < 2:
            for i in range(len(population)):
                selection_probabilities_sum += selection_probabilities[i]

                if selection_probabilities_sum >= random_number:
                    parents_selection.append(population[i])
                    random_number = random.uniform(0, sum(selection_probabilities))
                    print("Random number: " + str(random_number))
                    selection_probabilities_sum = 0
                    break 
            
            if len(parents_selection) > 1 and parents_selection[0] == parents_selection[1]:
                print("Parents are the same")
                print(parents_selection[0].test_suite + " " + parents_selection[1].test_suite)
                parents_selection.pop(1)

        return parents_selection
    
    '''
    Rank selection to select two parents from the population
    The individuals are sorted in ascending order according to their fitness
    The individuals are assigned a rank according to their position in the sorted list
    The parents are selected by choosing two individuals at random and comparing their ranks 
    The individual with the higher rank is selected as a parent and the process is repeated until two parents are selected

    Parameters:
    ----------
    population : list
        The population to select the parents from

    Returns:
    -------
    parents_selection : list
        A list containing the two parents selected from the population
    '''
    def rank_selection(self, population):
        parents_selected = []
        sorted_population_fitness = sorted(population, key=lambda x:x.fitness)

        print("Sorted Fitness")
        for i in range(len(sorted_population_fitness)):
            sorted_population_fitness[i].rank = i + 1
            print(sorted_population_fitness[i].fitness, end="|")

        while len(parents_selected) < 2 :
            individuals_selection = random.choices(sorted_population_fitness, k=2)
            print("Individuals selection: " +  str(individuals_selection[0].rank) + "|" + str(individuals_selection[1].rank))
            if individuals_selection[0] != individuals_selection[1]:
                if individuals_selection[0].rank > individuals_selection[1].rank:
                    parents_selected.append(individuals_selection[0])
                else:
                    parents_selected.append(individuals_selection[1])

            if len(parents_selected) > 1 and parents_selected[0] == parents_selected[1]:
                parents_selected.pop(1)
            
        return parents_selected

    def tournament_selection(self, population, fitness):
        pass

    def adaptive_selection(self, population, fitness):
        pass
