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

## 4.3 Metaheuristic Algorithms

After the representation of a possible solution and a fitness function to evaluate it, it's necessary to apply a metaheuristic algorithm that will produce the best possible solution within a time limit or a certain threshold.

Before utilizing the metaheuristic algorithm there is **specific data that this algorithm will use** for it's operation. This data refers to a **metadata file** that will list every detail of the **UUT** subdividing it's elements in:

- file: python file that contains UUT;
- location: path to the file;
- class: name of the UUT;
- constructor: information about the parameters of the UUT;
- actions: information about each action inherent to the UUT:
    - name: name of the action (or this case name of the method or variable);
    - type: type of action (if it is a "method" or "assing" => refering to a variable);
    - parameters: information about each parameter of the action:
        - type: datatype of the parameter;
        - min: **optional** minimum value for the parameter;
        - max: **optional** max value for the parameter.

**UUT Metadata file**: this file provides all the information about the UUT to the metaheuristic algorithm in this way the algorithm can interact with the UUT. This information compreends methods, constructor and respective parameters as well class variables. The information is presented in a JSON format.

This file provides certain ranges for the values specified. In this way the metaheuristic algorithm does not need to guess for values outside our desired range.

The metaheuristic algorithm makes guesses to try to find a better solution. This action is designated by **Random Test Generation**. However in order for the algorithm to not provide infinite solutions we need to specify certain limits to this action:

- **Maximum number of test cases:** define a limit for the number of test cases to be applied. This maximum number will then be chosen and added to the test suite (group of test cases);
- **Maximum number of actions:** define the biggest test case. In this case we chose a specifir max number of actions for a certain test case.

(by default the value 20 provides enough coverages)

Finally the metaheuristic algorithm needs it's search activities to limited. This is called **Search budget**. In this case it refers to the time given for the metaheuristic to find the best solution possible. Basically is the **maximum number of generations** of work that can be completed, before returning the best solution possible, in the time limit defined.

Search budget is **expressed as a number of generations** which are **cycles of exploration of the search space that has the test inputs**.

### Hill Climber

Metaheuristic algorithm that performs guess and check processes. In summary, it starts by a making a initial random guess for the solution and tries to improve it by making small changes to it (process of **mutation**). Everytime he guesses better than the last one, he adopts it as the current best solution to use and continues to make the respective changes. It continues to do this until we reach the maximum number of tries and maximum number of restarts (search resets).


**Mutation process:**

![](https://i.imgur.com/zCRweHL.png)

(see algorithm: https://github.com/Greg4cr/PythonUnitTestGeneration/blob/main/src/hill_climber.py)

### Genetic Algorithm

Another metaheuristic algorithm that can be used to find better solutions is the **Genetic Algorithm**. In this case this algorithm models the evolution of a population over time. It has the same idea of the **Hill Climber** algorithm with two major differences. 

- It manages a **population** of different solutions instead of evolving a single solution;
- It uses a **selection process** to choose the best individuals in a population and uses a **crossover process** that produces new solutions by **merging test cases ("genes") of parent solutions ("chromossomes").** 

After the **crossover** operation further **mutations** can be applied in the resulting children in order to further improve the solutions that the children have. If any of the children are better (measured by **fitness functions**) than the current solution then the latter is overwrited by the better child. There may be times where no improvement can be seen which leads to **stagnation**. If this happens the process is stopped to lower computacional cost.

![](https://i.imgur.com/9Fy0FfX.png)

## 4.4 Examining the resulting test suites 
**(see paper)**

# 5. Advanced Concepts

## 5.1 Distance-Based Coverage Fitness Function

:::info
ver papers mencionados
::: 


**Distance-Based Coverage Fitness Function** is a an advanced type of **search-based input generation** technique. This inherently uses a more complex fitness function. **The principal objective of this technique is to determain how close a test suite came to cover the outcomes of the code.**

**Branch coverage** - measure the number of outcomes that are performed by the test case.

The branch mentioned is divided into a **set of goals/combinations of coverage**.


## 5.2 Multiple and Many Objectives 

When defining certain test cases we have some goals that need to be achieved. This goals are important because they define the objectives we have for the creation of test cases.

For multiple objectives we can considerer merging all of them into a single fitness function and optimize it returning a single score. However in this case some of the goals can compete with each other and the returned value can not be what we are hoping for. A huge problem for this situation is to decide which objectives should be prioritized against others. 

An alternative and better way to do this is to keep each goal with it's specific fitness function and try to optimize each of them while taking account the optimization of the others (balance the optimizations). **Multi-objective optimizations** does not refer to a single best solution but to a set of solutions that are balanced or have good trade-offs between the objectives. In summary it represents a set of objectives that each have their importance and neither of them are more important in comparison with another objectives.

(see paper)


## 5.3 Human-readable Tests

Typically generated test cases by automation don't look similar to what developers and tests would write leading up to situations of misunderstanding. This can be hard to use future test cases by humans. So generating readable test cases is one important aspect regarding automated test generation. Combining AI techniques with multi-objective optimzation can automatically generate readable test cases.

## 5.4 Finding Input Boundaries

Choosing input boundaries for tests is a importante aspect. This has the objective to identify values at the boundary between diferent program behaviours. This boundary can demonstrate faults by minor mistakes/errors (small input values at the boundary can lead to faults depending on the program behaviour to that input).

**Program derivative** measures how sensible a program is to behaviour changes for differents sets of inputs. Conveys how function values (output) change when varying independent variables (input). We can detect boundary values when we see major output differences when applying similar inputs.

Similarity between input and output is measured using distance functions. **Low distance values** indicate that input and output are similar to each other. **High distance values** indicate that input and ouput are really different from each other.

For the program derivative:
- High derivative values (high numerator) indicates dissimilar output with similar inputs (low denominator) reveals sets of input values that are more sensitive to changes in program behaviour.
- High numerator values and low denominator values => indicate high sensibility
- Low numerator values and high denominator values => indicate low sensibility or almost non-existent.

(see paper)

## Finding Diverse Test Suites

When executing test cases to a certain system we want them to cover most of the behaviour of our system. However certain behaviours can not be found if we rerun the same set of tests or even very similar tests. For this problem we want to choose a test suite that adequates this situations. We want to a find a **Diverse Test Suite**. With this we can have a more controled view about possible behaviours of the system and even have better coverage and better chances to find faults within the system.

(see paper)

## Oracle Generation and Specification Mining

Automating oracle generation is a very difficult task to do. The previous chapters focused on how to automate generation of test inputs and actions for test cases however we can't judge faithfully if the behaviour of the system under test is correct.



(see paper)

## Other AI Techniques ==> SEE PAPER TO BE USED LATER


---
# Abstract of paper

Title: Automated Unit Test Generation Using Machine Learning Techniques

One of the most important aspects regarding the development process of a software it's the process of unit testing. Unit testing focuses on testing a segment of the code in a isolated state from the rest of the system. A framework utilized for this purpose and discussed in this paper, is the pytest framework responsible for unit testing in Python. 

The creation of unit tests is proven to be an intensive process regarding time and effort with many of it's elements being made manually. The need for automatization is a crucial point regarding this current thematic. The introduction of AI can support this need through the use of search-based unit test generation. This paper introduces this technique comprising fitness functions and respective metaheuristic algorithms. The algorithms mentioned generate unit tests in a pytest format with the objective to obtain coverage of code statements. 
More complex AI and Machine Learning techniques are applied in this paper to generate more unit tests. This paper includes the analysis of results obtained by applying metaheuristic algorithms and AI techniques mentioned. This work concludes by specifying the importance of the automatization when generating units tests and discussing conclusions obtained with the development of this work.




