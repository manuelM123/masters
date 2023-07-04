## Links:

- https://dl.acm.org/doi/pdf/10.1145/3511430.3511433 (Human-based Test Design versus Automated Test Generation: A Literature Review and Meta-Analysis) [1]
- https://ieeexplore.ieee.org/document/8816768 (On the Effectiveness of Manual and Automatic Unit Test Generation: Ten Years Later) [2]
- https://ieeexplore.ieee.org/document/8367053 (How Do Automatically Generated Unit Tests Influence Software Maintenance?) [3]
- https://dl.acm.org/doi/10.1145/2771783.2771801 (Automated unit test generation during software development: a controlled experiment and think-aloud observations) [4]
- https://ieeexplore.ieee.org/document/7372009 (Do Automatically Generated Unit Tests Find Real Faults? An Empirical Study of Effectiveness and Challenges (T)) [5]
- https://pythonistaplanet.com/difference-between-statically-and-dynamically-typed-languages/ [6]
- https://arxiv.org/abs/2111.05003 (An Empirical Study of Automated Unit Test Generation for Python) [7]
- https://ieeexplore.ieee.org/abstract/document/5954405 (Search-Based Software Testing: Past, Present and Future) [8]
- https://www.informs.org/Publications/OR-MS-Tomorrow/Metaheuristics-in-Optimization-Algorithmic-Perspective [9]
- https://arxiv.org/abs/2110.13575 (Automated Support for Unit Test Generation A Tutorial Book Chapter) [10]
- https://www.sciencedirect.com/science/article/abs/pii/S0950584901001896 (Search-based software engineering) [11]
- https://onlinelibrary.wiley.com/doi/abs/10.1002/stvr.1701 (Choosing The Fitness Function for the Job: Automated Generation of Test Suites that Detect Real Faults) [12]
- https://www.hindawi.com/journals/jcnc/2019/7983583/ (The Characteristics of Metaheuristic Method in Selection of Path Pairs on Multicriteria Ad Hoc Networks) [13]
- https://www.baeldung.com/cs/heuristics-vs-meta-heuristics-vs-probabilistic-algorithms [14]
- https://www.researchgate.net/publication/220516273_Search-based_software_test_data_generation_a_survey_Research_Articles (Search-based software test data generation: a survey) [15]
- https://www.mygreatlearning.com/blog/an-introduction-to-hill-climbing-algorithm/ [16]
- https://link.springer.com/article/10.1007/s11042-020-10139-6 (A review on genetic algorithm: past, present, and future) [17]
- https://ieeexplore.ieee.org/document/488968 (Particle swarm optimization) [18]
- https://www.researchgate.net/publication/261741691_Genetic_Algorithms_Data_Structures_Evolution_Programs_by_Z_Michalewicz (Genetic Algorithms + Data Structures = Evolution Programs) [19]
- https://ieeexplore.ieee.org/document/4129846 (Ant colony optimization) [20]
- https://warin.ca/ressources/books/2015_Book_IntroductionToEvolutionaryComp.pdf (Introduction to Evolutionary Computing) [21]

## Automated and Manual Testing

The generation of unit tests reveals as it being one of the most important aspects of software development. Creating unit tests to evaluate the behavior of the different units within the system is a vital procedure to ensure the system works as intended. However, one must take into account how this procedure can be done. 

Two different methods to create unit tests are known. They can be generated using human effort, in a manual manner or can be generated automatically through the use of state-of-the-art unit test generation algorithms. This last sentence brings forth a relevant question, "Which of them should be used over the other?". This work does not elaborate on this question, however certain points can be said about their differences.

- Scaling problems:
    - Manual generation can be an exhaustive and a time-consuming process. It scales with the size of the project. Projects with a great amount of parts require even more unit tests to be created. Manually creating these tests can hinder the development speed of the software;
    - Automated generation, being an automated process, can help reduce the time needed to perform this process. A manual procedure tends to be more time-consuming than a automated one [1].

- Coverage values and mutation scores:
    - According to studies that evaluate manual and automated test generation coverage values ([1],[2],[3]), automated generation of unit tests proves to have a higher capability of achieving better coverage values than the manual approach. The ability to identify mutants in unit tests (identification of allocated defects) is generally better in unit tests generated automatically [2].

- Fault detection:
    - While automated generation proves to be superior in terms of code coverage and mutation scores, there is less consistency in favor of automated methods when it comes to fault detection [2],[5]. Manual generation seems to perform comparatively better in this regard.

(verificar se é possivel colocar algo mais aqui)

## Dynamic vs Static Languages

One important point to address is to determine if the programming language used in the generation is statically or dynamically typed. This is vital as each one possess different characteristics that can either be an advantage or disadvantage for the automated generation of unit tests. 

In order to further contextualize this topic, a definition about type checking is presented. Type checking is a process that consists in verifying/checking the type of a construct (list, array, variable among others) and its usage [6]. This process can happen during compile-time (static checking) or during run-time (dynamic checking) of a program. A programming language can be defined as a **statically typed language if the type checks happen at compile time** and as a **dynamically typed language if the type checks happen at run-time**. Moreover, in statically typed languages the variable and data types are known before run time however in dynamically typed languages the variable and data types are only known in run time. This can cause a larger execution time for programs as the types are determined during the execution process.

Automated test generation is affected if the used language is statically or dynamically typed. The process is negatively affected it the chosen language is dynamic as the latter requires the types to be specified previously in order provide enough type context for generation of tests. When the generation process is under execution, the functions to be created do not know the required types for their parameters [7].

This work delves this important characteristic by applying automated generation of unit tests in a statically typed language (Java) and a dynamically typed language (Python) in order to show how impactful can type information be for the generation of tests.

### Type inference (verificar mais tarde se relevante)

## Search-Based Test Generation

Test creation, as mentioned previously, can be a rather tedious/intensive task to be executed manually. It requires selecting sequences of program input as well as oracles to evaluate if the given test is executing as expected. Automating this process can effectively reduce this intensive and time-consuming task being this possible by applying a automated test creation technique called Search-Based Test Generation.

Search-Based Test Generation consists in a technique to seek the best test suites for a given SUT, with the use of metaheuristic search algorithms within a restricted time limit. When generating test cases certain goals must be met such as achieving the best code coverage, triggering assertions within the SUT or even finding possible faults. The principal objective is to generate tests to meet certain goals as this can be considered as a search problem all together [11]. A search is being made to find the best possible solutions (test suites) that achieve specific goals. 

The generation is obtained by executing a segment of code, being this process guided by cost functions, in other terms "fitness functions", to achieve the best test data possible [8]. This process is also aided with the application of metaheuristic algorithms, which provide a solution for optimization problems found within unit test generation. 

### Fitness Functions

Fitness functions play a crucial role in search-based test generation. These functions are responsible for determining the quality of a given test case. They evaluate the generated test cases, suggest improvements, and indicate how close they are to achieving a desired goal [10]. Fitness functions must adhere to the following requirements:

- Return **continuous scores** as to offer better feedback for the metaheuristic algorithms;
- Return **only numeric values** in order to properly evaluate the generation of test cases each time;
- Indication of how close the generation was to being optimal. It should not indicate quality but a distance to optimal quality [10]. 

Fitness functions serve as a guiding principle for the metaheuristic algorithms, as they take the attributed score for the generated tests to reformulate them for the next iteration of the generation process [12].


#### Desired Goals

As previously mentioned, the fitness function gives a scores for each generation attempt which can detail how close the generated tests are to achieving a specific goal. What is this goal concretely? When generating tests, one must ensure the tests are properly adequate. It's not entirely sure if a generated test is always relevant for the content in the SUT. A adequacy criteria must be deployed to ensure the test represents the necessary testing rationale for the SUT. 

Common methods to measure adequacy are coverage of structural elements of the software including executions of statements, flow of branches and boolean conditional statements. These were already previously mentioned in section "Code Coverage Metrics", where different metrics for code coverage - such as branch, statement or conditional coverage - can prove to be a good adequacy criteria for the fitness function. For example, a fitness function can return a score for a generated test given its fullfillment of a adequacy criteria (coverage metric). This can guide the generation process providing enough detail to help differentiate candidate solutions and always aim for optimal candidate solutions [12].

### Metaheuristic algorithms

Metaheuristic algorithms implement a search procedure to find the best solution possible within a search space (referred normally as "search budget") while also obeying a restrict time limit. They are also a powerful aid to ensure the search of a near-optimal solution with incomplete ou imperfect information with the available resources [9]. The objective - behind these algorithms - is to find new strategies to resolve a problem as they use heuristics for that matter. 

The major distinction between a metaheuristic and a heuristic is that the latter needs to be tailored to a specific problem. A metaheuristic is a general algorithm which can be used in different types of problems being an problem-independent algorithm [14] being generally associated to a black-box technique. In context of search-based test generation this can be exemplified regarding coverage metrics. The same heuristic cannot be used for two different coverage problems as the heuristic needs to be tailored to a specific coverage problem, however the use of a metaheuristic proves to be better as it can take a problem in a general context, i.e, does not need to be specified for a specific problem.

Applying metaheuristic algorithms in conjunction with fitness functions can aid in the stable and efficient search for near-optimal solutions in the context of search-based test generation. The process of generating test cases can be seen as an optimization problem, where the objective is to search within a space of possible inputs and improve the quality of the solutions over time. The use of fitness functions in this optimization process is crucial. Fitness functions assign scores to individual test cases based on their adherence to specific adequacy criteria, such as coverage metrics or other relevant quality measures. These scores guide the metaheuristic algorithms to explore the search space and find better, more optimized solutions with each iteration.

By leveraging the power of metaheuristic algorithms and fitness functions, search-based test generation aims to continuously improve the quality of generated test cases within the constraints of a given search budget. The process involves iteratively evaluating and refining the solutions based on their fitness scores, ultimately leading to test suites that better achieve a specific goal.

#### Hill Climber

Hill Climber is a metaheuristic algorithm that focuses in searching a local optimal solution within a search space. The algorithm starts with a single initial solution chosen randomly and makes continuous searches around its neighbourhood to find better solutions. If a better solution is found - within that neighbourhood - then the current solution is replaced by the better solution. This last process is repeated continously until the search budget is reached or if no improved neighbours can be found. It is considered as a single-solution based metaheuristic [17].

This algorithm is essentially a local search algorithm. It tries to find a local optima, i.e, trying to find the local maximum within the search space, which represents the state who maximizes the value of a objective function (fitness function). This however is a limitation to the algorithm as it may not achieve the most desired score which is the global maximum, which represents the highest objective score. 

During the search, a local maximum can be found and limit the search as it is not possible to find a better neighbour within that search scope (further "climbing" is not made) because the neighbours values are worse than the current found solution [16]. Another problem is that the search may lead to search spaces where the solution cannot be improved any further because of the neighbours sharing the same objective score, i.e, there is a high quantity of values that are equal to the current solution. All these equal values are designated as "flat" local maximums. A problem that also associated to these "flat" values is the **shoulder problem**. This identifies a range of equal objective values which prevents founding the best solution within that search space. The regions where all neighbours have the same values are called **plateau** regions.

Despite all the problems listed above, the major limitation behind this algorithm lies upon the starting solution. If a bad solution is chosen to start the search, there is a higher chance that the search scope can be very limited not providing enough good solutions. In this case, the best solution can be found almost imediately which is a bad indicator for the search as it means the starting solution was not a good choice and the peak - within the search space of the starting solution - was almost instantly achieved.

![](https://hackmd.io/_uploads/BJkFJBndn.png) [16]


#### Genetic Algorithm

Not all metaheuristic algorithms delve onto the local search scope, as some of them also perform a global search and consider a wide set of candidate solutions within the search space. These algorithms are called "Population-based metaheuristics" and can maintain diversity in the population (set of solutions) while also prevent the search to be stuck in a local optima [17]. A few example of these algorithms are swarm optimization (PSO) [18], genetic algorithm (GA) [19] and ant colony optimization (ACO) [20]. 

For this work, genetic algorithm was implemented and as such, a much needed contextualization about evolutionary algorithms must be presented. An evolutionary algorithm is an algorithm who uses a search strategy to evolve candidate solutions using genetics and natural selections inspired operators [15]. A more detailed definition can be defined as: "**given a population of individuals within some environment that has limited resources, competition for those resources causes natural selection (survival of the fittest)**" mentioned by A.E. Eiben and J.E. Smith [21]. 

Evolutionary algorithms (EAs) are inspired by the Darwinian Evolution, where the solutions are identified as individual organisms in a population (set of solutions). Within that population, each individual is tested for fitness (how well they can resolve a problem) and a set of them are selected for reproduction, which includes crossover and mutation operators. Genetic algorithm is a class of the evolutionary algorithms and as such also employs bio-inspired operators for its generation of solutions.


##### Natural phenomena

A genetic algorithm is a optimization algorithm that uses bio-inspired operators for its generation of solutions. Being a population-based search algorith it employs the concept of survival of the fittest [19]. New populations are formed iteratively through genetic operators applied on the individuals of the present population. These genetic operators will alter the fittest individuals of the population and will apply crossover and mutation operations to them in order to generate even better individuals. This process is repeated until a certain budget is met and the population will contain the best generated individuals until then. The application of GA, with biological terms, can be explained in a simple step scheme:

1. **Population**: a set of $n$ chromossomes, where each one of them represents one individual, is initialized randomly;
2. **Selection**: operation that selects the fittest individuals of the current population. the $t$ chosen individuals (chromossomes) are selected through their fitness score value (the $t$ highest fitness score values are chosen);
3. **Crossover**: the chosen chromossomes undergo crossover operations, i.e, they exchange information between each other according the type of mutation specified. The newly created chromossomes are now reffered to as "offsprings";
4. **Mutation**: according to the type of mutation operator, small changes will be made to the offsprings in order to add more evolution/information;
5. **Adding offsprings**: after the mutation process, the offsprings are placed in a new population replacing the old population entirely. After this step the search will continue in the new population;
6. **Repetition of step 2 - 5**: the steps 2 through 5 are repeated until a certain limit or budget is reached within the generation process.

In biological terms, an individual or chromossome components are called genes, the values for each component are reffered to as alleles and their position within the sequence of the chromossome are called locus. In this work, these biological terms will be referred interchangeably between sections.

###### Selection operators

###### Crossover operators

###### Mutation operators


:::info
**Local vs Global Optima**

Local optima and global optima are concepts related to optimization problems, including those solved by hill climbers and genetic algorithms. Let's understand the distinctions:

Local Optima:

Local optima refer to solutions that are optimal within a specific region of the search space. These solutions may be the best in their local vicinity, but they are not necessarily the best solution globally across the entire search space.
In the context of optimization algorithms like hill climbers, when the algorithm starts from a specific point in the search space and iteratively explores its neighboring solutions, it may converge to a local optimum that is the best in that particular neighborhood.
The drawback of local optima is that they may prevent the algorithm from finding the overall best solution if that solution exists in a different region of the search space.
Global Optima:

Global optima, on the other hand, refer to the best possible solution across the entire search space. These are the optimal solutions that one would ideally like to find when solving an optimization problem.
In the context of optimization algorithms like genetic algorithms, which use a population of solutions and evolutionary processes, the algorithm aims to explore different regions of the search space and converge to the global optimum, i.e., the best possible solution overall.
Finding the global optimum can be challenging, especially in complex and high-dimensional search spaces, as the algorithm needs to overcome local optima to reach the best possible solution.
Distinction in Hill Climber and Genetic Algorithm:

Hill Climber:

Hill climbers are local search algorithms that start from a specific point in the search space and iteratively move to neighboring solutions that improve the objective function.
They are prone to getting stuck in local optima, as they focus on exploring the nearby solutions and may not venture far enough to find the global optimum.
Hill climbers are computationally efficient and work well for some simple optimization problems with a well-defined landscape.
Genetic Algorithm:

Genetic algorithms, on the other hand, are population-based metaheuristics that maintain a population of solutions and apply genetic operators (crossover, mutation, selection) to evolve the population over generations.
By maintaining a diverse population and applying genetic operators, genetic algorithms are more capable of exploring different regions of the search space, which helps them avoid getting trapped in local optima and increases the chance of finding the global optimum.
However, genetic algorithms might require more computational resources and can be slower compared to hill climbers, especially for problems with a large search space.
In summary, hill climbers are more prone to finding local optima due to their localized search strategy, while genetic algorithms are better suited to explore the search space globally and have a higher chance of finding global optima. However, genetic algorithms might require more computational resources and be computationally expensive compared to hill climbers, making the choice of optimization algorithm dependent on the specific problem characteristics and available resources.
:::

























