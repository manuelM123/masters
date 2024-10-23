# Master's Dissertation

## Using Genetic Algorithms to Automatically Generate Unit Tests

Automatic approach for the generation of unit tests from an individual code snippet using genetic algorithms for the Python programming language.
Genetic algorithms and optimizations to the genetic process (population, selection, crossover and mutation) are implemented.
Benchmarks are also performed between the genetic algorithms to assess the performance of the automated process and the quality of the generated unit tests.

## Implementation Structure

### Class Under Test

Calorie Intake Calculation using three equations for RDEE and TDEE

Mifflin StJeor Equation - M. D. Mifflin, S. T. S. Jeor, L. A. Hill, B. J. Scott, S. A. Daugherty, and Y. O. Koh,
“A new predictive equation for resting energy expenditure in healthy individuals.” The
American journal of clinical nutrition, vol. 51 2, pp. 241–7, 1990. [Online]. Available:
https://api.semanticscholar.org/CorpusID:45348378

Katch Mcardle Equation - W. D. McArdle, F. I. Katch, and V. L. Katch, Exercise physiology: Nutrition, energy,
and human performance. Lippincott Williams & Wilkins, 2010. 48

TDEE Calculation - R. MacPherson, “Energy expenditure: Tdee definition and calculator,” https://
www.verywellfit.com/what-is-energy-expenditure-3496103, October 2022, (Accessed on
04/11/2024). 49

### Representation Scheme

The JSON format enabled a proper organization of the CUT constructor and methods into
different objects with different properties or key-value pairs. This distinct separation into
different objects made it easier to access the necessary data to create the individuals of
the genetic algorithm. The metadata of the CUT is divided into the following objects and
key-value pairs:
  • constructor: representing the constructor of the class and the inherent attributes associated to it. It is divided into name and parameters key-value pairs:
                    – name: key that represents the name of the CUT;
                    – parameters: key that contains each attribute of the constructor, being an array of objects where each object represents each constructor’s attribute. Each object of the array has a corresponding type key and keys associated to a predefined range of values.
  • other_functions: key that contains a set of objects, which are the CUT methods, comprising getters, setters, and other functions. Each object of the array has a corresponding name (name of the method) and type (if it is a getter, setter, or another function) keys. There are some objects that include an additional key that contains parameters, which corresponds to an array that includes an object with corresponding key-value pairs that represent the parameters of the methods.

### Solution Structure

The population is a nested list involving a list of test suites where each test suite has a list of test cases and where each test case has a list of methods from the CUT.

The population for the different genetic algorithms will be composed of a set of solutions, where each of them is composed by the following elements:
      • Test suite: each solution has only one test suite, which contains a set of two or more test cases. Each test case is composed of a set of methods that must contain a constructor and can contain zero or more functions (according to CUT structure). These inherent methods also have a structure of their own:
          – Method identifier: each method has an identifier that determines which type of method was selected from the CUT. The constructor has the identifier of value −1 and the other functions have corresponding identifiers in the interval [0, number of class attributes[ according to their position index in the metadata file;
          – Method parameters: each method has a list that contains the parameters associated to it. These parameters differ in regard to the type of method that was chosen during the initial random generation of solutions.

      • Attributes: a solution is composed of an additional set of attributes that are necessary for the genetic algorithm execution and respective optimizations. These attributes are:
          – Encoded crossover rate: each solution has a self-encoded crossover rate that is randomly generated within the interval [0, 1] during the initial generation of the solution. It’s used in the self-adaptive crossover rate optimization when the self-encoded crossover rate is compared to a random number in the interval [0, 1] to decide which genetic operator (crossover, mutation or even both) to apply to the solution. This method was presented in the work “An Emperical Study on GAs “Without Parameters””;
          – Encoded mutation rate: each solution has a self-encoded mutation rate that is randomly generated within the interval [0, 1] during the initial generation of the solution. It’s used in the self-adaptive mutation rate optimization, alongside other data, to calculate a new mutation rate for the solution, adjusting its mutation rate across the genetic algorithm execution. This method was proposed by the work ”Intelligent Mutation Rate Control in Canonical Genetic Algorithms”;
          - Fitness score: each solution has a fitness score value associated to it. This value is pre-defined at the beginning and updated across the genetic algorithm run either during the initial generation or through genetic operations;
          - Rank score: a pre-defined rank score is attributed to a solution during the initial generation. This score is then updated when rank-based selection is used during the evolution process;
          - Mating chance: a mating chance is calculated for each solution during the adaptive selection method execution. It’s the probability for the solution to be inserted into the mating lists for further reproduction. This attribute is done solely for the adaptive method described in the work ”Adaptive selection routine for evolutionary algorithms”;
          - Maximum selections: maximum number of selections of the solution to be inserted into the mating lists. Each solution can be selected up to two times in order to avoid early convergence. This was implemented in the adaptive selection method proposed by the work ”Adaptive selection routine for evolutionary algorithms”;
          - Lifetime value: value that determines the remaining lifetime of a solution. This is used in the population optimization method to control the size of the population during the genetic algorithm execution. This attribute is mostly used to evaluate if the individual needs to be removed from the population according to the remaining lifetime it has. This method was presented by the work ”APOGA: An Adaptive Population Pool Size based Genetic Algorithm”. 

### Fitness Evaluation

The implementation process of fitness evaluation is composed of two activities, being running the generated tests and evaluate them according to a desired code coverage metric. This is possible due to the use of two Python modules which are:
- Pytest: testing framework that provides enough tools for the creation and execution
of tests in Python. It requires Python’s version 3.7 or above in order to be used. The Pytest testing framework runs any file of the form test_∗.py or ∗_test.py in the current directory and respective subdirectories;
- Coverage module:  it measures code coverage in Python, measuring which code wasexecuted and analyses the source code that could have been executed. It requires
Python’s version 3.8 or above in order to be used. The Coverage module executes a test suite and gathers data that can be visualized in different formats. The tool measuresthe coverage, by default, using the statement coverage metric, however it can be alsoset up to measure coverage using the branch coverage metric. The coverage module needs a test runner to executethe tests first in order to have information about which parts of the code were executed. The tool works with Pytest, Unittest and Nosetest test runners. After the execution of the tests, the tool is able to calculate the code coverage according to the coverage metric chosen. https://coverage.readthedocs.io/en/latest/index.html

### Configuration File

A configuration file was created to hold a set of different attributes for easier execution of the different \ac{GA}s. The configuration file is a Windows and MS-DOS initialization file that bears the \texttt{INI} format extension. This \texttt{INI} file has different set of configurations divided in five sections:

- Metadata: section that contains the field metadata_location to specify the location of the metadata file that holds the necessary CUT information;

- Configurations for the GA: section that contains a wide set of basic configurations for the GA execution. This section is divided into the following fields:
  
  max_number_functions: this field is used to determine the maximum number of CUT functions an individual can have in its test cases. For the first benchmark, this field was set with value 10. For the second benchmark, this field was set with the value 4;

  max_number_test_cases: this field is used to determine the maximum number of test cases an individual can have in its test suite composition. For the first benchmark, this field was set with value 10. For the second benchmark, this field was set with the value 4;

  tournament_size: this field specifies the tournament size for the tournament selection method. The GA was designed with the standard two individuals in mind, which means that operations like crossover were designed for two individuals, so the used and recommended value for this field is 2;

  max_number_generations: this field specifies the maximum number of generations by which the GA can run. For the first benchmark, this field was set with the value 100. For the second benchmark, this field was set with the value 1000;

  fitness_max_stagnation_period: this field specifies the maximum stagnation period (number of generations) by which the GA can run without fitness improvement (stagnation of the best fitness score). For the first benchmark, this field was set with the value 30. For the second benchmark, this field was set with the value 100;

  fitness_function_type: this field specifies the type of fitness function used in the \ac{GA}. This can range between two types of coverage according to the \texttt{Coverage} module limitations, as the only available coverage metrics are the branch coverage and statement coverage metrics. For both benchmarks, this field was set with branch coverage;

  fitness_iteration_limit}}: this field specifies the iteration limit by which the \ac{GA} can run without fitness improvement. This field has a different purpose than the fitness_max_stagnation_period as it's used for the population size control optimization. For the first benchmark, this field was set with the value 2. For the second benchmark, this field was set with the value 5. 
    
- Configurations for genetic operators: section that contains a wide set of configurations related to the genetic operators. This includes configurations for the population, selection, crossover and mutation operations. This section is divided into the following fields:

    - population_size: this field specifies the population size for the initial population creation during the GAs execution. For the first benchmark, this field was defined with the value 25. For the second benchmark, this field was defined with the value 55;

    - population_control: this field specifies if the population control optimization method, referring to the work “APOGA: An Adaptive Population Pool Size based Genetic Algorithm”, can be activated during the GAs execution. The value of this field was set to True during the GAs population benchmark and to False for the remainder of the first benchmark. For the second benchmark, this field was only set to False for the TGA while for the other GAs this field was set to True;

    - selection_type: this field specifies the type of selection method to be used during the GAs execution. This selection type field can take one of the following values: random, roulette_wheel, adaptive, rank or tournament. The adaptive value applies the methodology of the research \cite{adaptive_selection_genetic_algorithms}. The standard value defined for this field is \texttt{tournament};

    - crossover_type: this field specifies the type of crossover method to be used during the GAs execution. This crossover type field can take one of the following values: deterministic, self-adaptive, adaptive, or uniform. The deterministic, self-adaptive, and adaptive values enable the methodologies of the researches “Choosing Mutation and Crossover Ratios for Genetic Algorithms — A Review with a New Dynamic Approach”, "An emperical study on gas “without parameters"", and "Implementation of evolutionary fuzzy systems" respectively. The standard value defined for this field is uniform;

    - crossover_rate: this field specifies the crossover rate to be used during the crossover operations. This field was set with the value 0.50. This was assigned based on a standard range of rates for this genetic operator which is [0.45, 0.95];

    - crossover_rate_adjustment_type: this field specifies the type of strategy to apply when the deterministic crossover method, proposed in “Choosing Mutation and Crossover Ratios for Genetic Algorithms — A Review with a New Dynamic Approach”, is applied during the GAs execution. This field can take one of the following values: ilc or dhc;

    - mutation_type: this field specifies the type of mutation method to be used during the GAs execution. This mutation type field can take one of the following values: add_test_case, delete_test_case, deterministic, adaptive, self-adaptive, or change_parameters. The deterministic, adaptive, self-adaptive values apply the methodologies of the researches “Choosing Mutation and Crossover Ratios for Genetic Algorithms — A Review with a New Dynamic Approach”, "Implementation of evolutionary fuzzy systems", and "Intelligent mutation rate control in canonical genetic algorithms" respectively. The standard value defined for this field is change_parameters;

    - mutation_rate: this field specifies the mutation rate to be used during the mutation operations. This field was set with the value 0.15. There is a high discrepancy in the literature related to the desired interval of mutation rates, as intervals such as [0.001, 0.01] or [0.001, 0.05] are suggested. This value was chosen to be a slightly higher than the standard values due to its low probability, however it was not increased too much in order to not disrupt the genetic information too often;

    - mutation_rate_adjustment_type: this field specifies the type of strategy to apply when the deterministic mutation method, proposed in “Choosing Mutation and Crossover Ratios for Genetic Algorithms - A Review with a New Dynamic Approach” “Choosing Mutation and Crossover Ratios for Genetic Algorithms — A Review with a New Dynamic Approach”, is applied during the GAs execution. This field can take one of the following values: ilm or dhm.

- Configurations for GAs optimizations: section that contains a wide set of configurations for the GAs optimizations. This section is divided into the following fields:

    - population_decrease_rate: decrease rate used in the population control method, proposed in the research “APOGA: An Adaptive Population Pool Size based Genetic Algorithm”, during stagnation of fitness improvement. This field was set with the value 0.20 as per parameter setting description in the research;

    - uniform_number_crossover: control variable for the implementation of the uniform crossover operation to decide which part of the genotype would be exchanged between the parents. This field was set with the value 0.5;

    - lt_max: maximum lifetime for the individuals in the population. This is used during the RLT mechanic of the population control method proposed in the work “APOGA: An Adaptive Population Pool Size based Genetic Algorithm”. For the first benchmark, this field was set with the value 10. For the second benchmark, this field was set with the value 20;

    - lt_min: minimum lifetime for the individuals in the population. This is used during the RLT mechanic of the population control method proposed in the work “APOGA: An Adaptive Population Pool Size based Genetic Algorithm”. For the first benchmark, this field was set with the value 1. For the second benchmark, this field was set with the value 4;

    - alpha: variable used in the population growth operation of the population control method, proposed in the research “APOGA: An Adaptive Population Pool Size based Genetic Algorithm” [apoga_population_size_optimization], during fitness improvement. For the first benchmark, this field was set with the value 0.7. For the second benchmark, this field was set with the value 0.5;

- File paths: section that contains a wide set of file locations for the GA execution. This section is divided into the following fields:

    - fuzzy_membership_functions: path for the files that will store a visual representation of the membership functions that compose the fuzzy system described in research “Implementation of evolutionary fuzzy systems”;

    - intermediate_test_suite: path for the files that will contain new test suites each time an individual generation occurs. These tests suites are written in phenotype format;

    - generations_stats: path for the files that will store graphs relative to generation results after the GA execution;

    - best_generated_test_suite: path for the files that will store the best generated test suite in phenotype format after the GA execution;

    - generation_data: path for the files that will store the data obtained from the generations after the GA execution;

    - benchmark: path for the files that will store a visual representation of the GAs performance comparison on a diverse set of evaluation metrics;

    - generations_stats_history: path for the files that will store the generation stats history for the GAs (data from each generation) in text format.

- Scripts: section that contains configurations for the execution of additional scripts. This section is divided into the following fields:

     - execution_script: this field is used as a control variable during the GA execution. This field is set to False by default and it's only set to True during the execution script. This is done to create an initial population at the beginning of the execution script, as this population is intended to be the same across the multiple GAs executions to avoid any type of advantage or disadvantage for the GAs. In the end of the execution script, this field is set to False. In cases where only the genetic algorithm script is executed, the population is created during the genetic algorithm script run;

     - execution_optimizations: this field is used as a control variable in order to determine which benchmark to execute. If it's set to True then the benchmark of the optimized GAs will be executed. If it's set to False then the benchmark for the optimizations of the GA genetic attributes will be executed instead.

### Execution 

- Run "genetic_algorithm.py" as is for a singular run of a GA with the configurations defined in the configuration file.
- Run "execution_script.py" to run a set of GA iterations. 
- Run "evaluation_script.py" after the "execution_script.py" run to obtain benchmarks after the algorithms runs. Change the value of iteration in method "mean_data_methods" if number of executions does not reflect the number of executions in the results directory
