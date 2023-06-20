# Unit Test Generation - Masters

## Links:

- https://dl.acm.org/doi/pdf/10.1145/3511430.3511433 (Human-based Test Design versus Automated Test Generation: A Literature Review and Meta-Analysis) [1]
- https://ieeexplore.ieee.org/document/8816768 (On the Effectiveness of Manual and Automatic Unit Test Generation: Ten Years Later) [2]
- https://ieeexplore.ieee.org/document/8367053 (How Do Automatically Generated Unit Tests Influence Software Maintenance?) [3]
- https://dl.acm.org/doi/10.1145/2771783.2771801 (Automated unit test generation during software development: a controlled experiment and think-aloud observations) [4]
- https://ieeexplore.ieee.org/document/7372009 (Do Automatically Generated Unit Tests Find Real Faults? An Empirical Study of Effectiveness and Challenges (T)) [5]
- https://pythonistaplanet.com/difference-between-statically-and-dynamically-typed-languages/ [6]
- https://arxiv.org/abs/2111.05003 (An Empirical Study of Automated Unit Test Generation for Python) [7]

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


This work delves this important characteristic by applying automated generation of unit tests in a statically typed language (Java) and a dynamically typed language (Python).

















