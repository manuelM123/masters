# Unit Testing - Masters

Sources: 

[1] (last searched: 17/1/2023) https://www.guru99.com/unit-testing-guide.html

[2] (last searched: 26/1/2023)
https://livebook.manning.com/book/unit-testing/chapter-1/6

[3] (last searched: 17/1/2023)
https://thevaluable.dev/fighting-software-entropy/

[4] (last searched: 26/1/2023)
http://xunitpatterns.com/

## What is a Unit Test

### Definition

Unit testing can be defined as an activity which the main objective is to perform tests in segments of code in a isolated state, separated from the rest of the constituent parts of the system. The realm of unit testing is a highly multifaceted theme, where differing perspectives and interpretations are commonplace. Amongst the various approaches, two stand out as prominent - the Classical approach and the London school of unit testing. These approaches, while both focused on unit testing, possess distinct variations in their understanding and handling of the concept of "isolation" within a unit test. 

### Classical Approach
...

### London School of Unit Testing

This approach considers isolating the unit test from its collaborators, which means if a certain class is our SUT (System Under Test) and it has a dependency on another class, then this dependency must be substitued by a *test double*. In this way, the behavior of the class under test won't be affected by any external influence. 

*Test Double* - operation used in unit testing to replace a object or component present in the system under test. It acts and looks similar to the object/component replaced but its a lot less complex and facilitates testing in the SUT. 

Figure ... shows the isolation in this approach is achieved by replacing SUT dependencies by test doubles:

![](https://i.imgur.com/2JCxKGC.png) [2]

One of the major advantages of this approach is shown in an eventual case of failure when testing. In these situations, is easy to identify where the failure occurred, having it happen in the system under test. The failure couldn't happen at any other place, the SUT neighbours are test doubles. 

When a unit test is executed, the test double replaces the dependencies of the SUT by simpler objects. The test double is configured to provide certain inputs and outputs or to record information about how it was called by the SUT. These provide the ability to control the behavior of the SUT and to verify if the behavior occured as expected. 

The test doubles can be used in a multitude of ways, it can be done manually or by using a testing library that provides this sort of functionality. A wide range of types of test doubles exists and they can be divided in the following points:

* ***Dummy Object***: it acts as a placeholder object that is passed to the SUT as an argument but is never used[4];
* ***Test Stub*** : objects that replaces a component of the SUT. In this way, the test can control the indirect inputs of the SUT, making it exercise certain paths of the code he otherwise would not;
* ***Test Spy***: advanced version of a *Test Stub* which records information about how it was called. Used for inspections of interactions between the SUT and the test double;
* ***Mock Object***: object replacing a component that the SUT depends on. Records information about how it was called, allows the specification on how it should be called and is used to stimulate the behavior of the replaced component;
* ***Fake Object***: objects replacing the functionality of the replaced component with a different implementation for the functionality[4].

This approach also defends the creation of a set of classes for each unit being tested. This enables the testing of a unit at a time comprising a well structured unit test suite.

![](https://i.imgur.com/aSbVYD4.png) [2]

### Differences between approaches
...

## Purpose 

### Faults 
This operation can ensure a higher probability of detection of faults within a system while ensuring a general testing of every part that composes a system.  These tests are performed to verify it the implemented functionalities are in accordance to the system requirements defined in early stages of development.
In another words, it's used to verify the correctness of a certain segment of code.

The identification of possible faults in the early stages of development is more important than to find at later stages. The correction of a fault is minimized when found at early stages of development where it's located at a certain unit. When a system runs and a fault occurs, it's more time-consuming and costly to correct it at system level than at the unit level where is isolated from the rest of the system.

### Re-Use
Despite the identification of faults, unit testing can lead to code reuse. In this case, a portion of the testing done can be used again in a different system when the objectives/functionalities are similar between the different systems. 

A unit test can be used for refactoring. The unit test can be updated according the code developed for the application. In this way, unit tests are constantly updated to accompany the evolution of code in the system. 

### Development Speed
The application of unit testing can enable a sustainable growth of a software project. In a really early stage of development, there is a low quantity of code to be worried about, enabling a rapid development and progress in the creation of the product. However, as time goes by, more code is created, more architeture ideas are developed and the probability of finding a fault is higher [2].

This latter causes the development speed to be much slower, when performed in it's raw form without tests  in the code. This can reach points where progress is halted due to higher complexity when creating the software.

![](https://i.imgur.com/dntV9bq.png) [2]

This decrease in the development can be called as **software entropy**. **Entropy** is a mathematical concept that states, for a closed, independent system, the amount of disorder doesn't decrease overtime. It can increase or be stable [3]. In software, the more changes are made, more its the disorder of the latter and its entropy increases.

This concept can be applied in software regarding the code built. As the development of the product goes on, more code is created and the quantity of disorder, or entropy, increases [2]. As the code increases so does the complexity of the system and higher the chance to occur bugs in the software. Fixing bugs in a complex system, which possesses a great variety of functions and relationships between components, can prove to be very difficult. Altering a part of the software can affect others negatively, fixing a bug can introduce other bugs that were hidden. It is harder for a system to maintain its stability in this situation.

Unit testing can help reduce this problem. By applying tests in a specific component of the system is easier to verify it's correctfulness when the software is evolving. As more code is built, more testing is applied on specific units to make sure the latter were not affected negatively by new code or refactoring operations. This can ensure quicker development speed because a constant testing and verification in units is made as the system is evolving. Time and progress are achieved with better results when performing a constant testing in units as the new code or new functionalities are added in the software to be developed. Without tests, more time would be spent trying to find and fix bugs as a continuous verification is not made and because of this, it's more difficult to solve errors and inconsistencies in the system.

## Unit Test Structure


### Arrange, Act, Assert Pattern (AAA)

A unit test can be created using a the **AAA (Arrange, Act, Assert)** pattern. This pattern is divided in three parts, which can be clarified below:

* **Arrange** - Identifiying the segment of code to be under test. In another words, a part of the system is chosen to apply tests, being this part the SUT (system under test);
* **Act** - Deciding which tests to perform in the SUT. A test example would be making method or constructor calls;
* **Assert** - Verifying the output result of the test performed. In this phase, the output of the test is compared to the expected output in order to determine the overall correctness. It's made an evaluation of the expected behaviour, ultimately deciding if a test passes or fails.

An example of the use of the AAA pattern to create a unit test is presented in the following figure:

:::info
public class DivisionTest {

    @Test
    void Division() {
     // Arrange section
     var div_operation = new Division();
     
     // Act section
     var result = div_operation.divide(4,2);
     
     // Assert section
     assertEquals(2,result);
    }
}
:::

In the above example, Arrange, Act and Assert phases are implemented. It possesses a class that contains the set of tests to apply. The unit test with the name "Division" will test a simple division operation divided into three sections being the Arrange, Act and Assert sections respectively. 

:::info
The **Arrange section** holds the class to be tested. In this case, the constructor of the class division is called. This will be the SUT.

The **Act section** is intended to perform an "action" on the SUT chosen. A method call of the Division class is performed and the result is stored in a variable.

The **Assert section** verifies the outcome from the Act section. A verification will be made to see if the value of the variable from the previous section corresponds to the expected result. This determines if the test passes or 
fails.
:::

Another possible pattern that is used for the creation of unit tests is the **Give-When-Then** pattern [2]. This one is similar to the **AAA pattern** and also defends the division of the unit test in three parts:

* **Given** - describes the initial context of the test (correlates to the arrange phase)
* **When** -  describes the action or method being tested (correlates to the act phase)
* **Then** - describes the expected outcome (correlates to the assert phase)

Both patterns have the same of goal of testing a certain part of the system. Their only difference is how they structure each phase of testing as demonstrated above.

In order to design a unit test, according the AAA pattern, the arrange section can be the first step. There is need to specify first which section of the system will be under test before performing the act and assert phases. However this approach could not be the best when performing a Test Driven Development (TDD). 

In a TDD, the tests are created before any code is done, in other words, tests are developed before any type of functionality is created and formulation of the functionalities is done taking into account the tests, hence the term TDD. In this situation, it's best to start with the assertion phase where a set of evaluations is performed continuously with code writing. After a set of continuous steps, a unit test that meets the expectation can be achieved.

### Teardown Phase

This phase can be an additional section to unit testing. Its purpose comprehends the cleaning of resources and other tasks after the unit tests are created. It can be viewed as a "non strictly necessary" section, a unit test has an independent nature and as such it doesn't talk to out-of-process dependencies. The implementation of this phase is heavily associated as part of an integration testing instead of unit testing.


## Automated and Manual Testing
...

## Techniques
These kinds of faults can be found through a wide variety of techniques, all specified within the scope of unit testing.

These techniques can be listed as follows: 
* **Black Box Testing**
* **White Box Testing**
* **Gray Box Testing**

### Black Box Testing

#### Test-Driven Development

### White Box Testing

### Gray Box Testing

#### Code Coverage Metrics
* Line Coverage
* Statement Coverage
* Branch Coverage
* Condition Coverage
* Decision Coverage

(coverage and such)





