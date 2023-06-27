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

Metaheuristic algorithms implement a search procedure to find the best solution possible within a search space (referred normally as "search budget") while also obeying a restrict time limit. They are also a powerful aid to ensure the search of a near-optimal solution with incomplete ou imperfect information with the available resources [9]. 

Optimization problems can be found diversily in search-based software testing. One pratical example of this situation

The application of metaheuristic algorithms in conjunction 























