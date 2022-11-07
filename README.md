# masters
Master's work

...

# 4 Search-Based Test Generation

**UUT** - unit under testing

- Things to look for when performing test cases:
    - Exceptions in the unit under testing;
    - Code coverage => cover all the lines of a code;
    - Verifying every outcome possible (identifying inputs for every possible output value or most);
    - Executing a wide variety of inputs and determine which set has the highest diversity.

- Process of Test Generation using Metaheuristic algorithms:

    1. Use of fitness functions to evaluate certain solutions (tests suites with one or more unit tests);
    2. Use of metaheuristic algorithms to take those solutions and come up with a improved solution;
    3. Repeat the process until a certain threshold.

## 4.1 Solution Representation

- To solve a certain problem in this context we need a set of unit tests in order to obtain a specific answer.
- Identifying a set of unit tests.
- This problem groups a test suite (collection of test cases).
- Steps do solve this problem:
    - Solution is a test suite
    - Test suites can have one or more test cases (individual methods of a single test class)
    - Solution interacts with UUT which is a Python class with one or more methods
    - Each test case calls the constructor of the UUT
    - Each test case can have one or more calls of methods inherent to the UUT
    - Each calls and initializations can have zero or more parameteres

In search-based generation, two solutions can be in two different forms:

![](https://i.imgur.com/OYTDVb3.png)

- **Phenotype (right) Representation:** Solution that is presented in human-readable format.
- **Genotype (left) Representation:** Solution that has properties relevant to the search algorithm (elements can be manipulated directly).

Using **phenotype** form is useful for testers to read however this isn't the ideal representation for metaheuristic search algorithms because it can't be manipulated. As for these problems the **genotype** form is the most important and crucial to use.

The **genotype** representation associated with a fitness function can improve to it's representation by the scores given by the latter. A **genotype** can be a bad solution in it's early stages however over time and with usage of a fitness function it can improve.

## 4.2 Fitness Functions

- Fundamental element for search-based test generation.
- It takes a solution candidate and evaluates it based on a score.
- With this function we want a representation of how close the solution came to resolve the problem at hand (every time it is applied).
- Mainly it helps arriving to a final solution with the use of the metaheuristic algorithm (score helps the algorithm).
- Returns a numeric score (can be percentage or a raw number).
- Depending on the type of algorithm applied, one or multiple fitness functions can be optimised at once.

Fitness function needs to:
- **Not return a boolean value**: almost no feedback provided by this type;
- **Provide continuous scores**: it helps the metaheuristic algorithms with clearer feedback;
- **Offer indication of quality and distance to a optimal quality**: In it's vast majority, it should indicate how close the solution is to the optimal one and not measure if the solution did everything right to a certain problem.

One of the most important aspects to apply to a fitness function is **code coverage**. The most common criteria to measure coverage is **statement coverage**. Measures the percentage of executable lines that have been triggered, at least once, by the test suite. Higher the coverage higher the possibility to **identify a fault**. Using this encorages the metaheuristic algorithm to explore, in depth, the structure of the code and it can branch all of the elements of that code.

Formula of fitness function calculation:
$fitness(solution) = statement coverage(solution) − bloat penalty(solution)$

**$bloatpenalty$** is a small penalty to the score to control the size of the produced solution in two aspects:
the number of test methods and the number of actions in each test.

A large test suite can contain redudant elements. Long sequences of actions can deteriotate debug of the code and identification of faults. Therefore this is penalty is used to encourage the metaheuristic algorithm to produce small but effective test suites.

This penalization can be adjusted by the test however it shouldn't be done heavily because it will penalize the optimization of the test suites (finding smaller solutions).



