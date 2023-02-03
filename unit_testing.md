# Unit Testing - Masters

Sources: 

[1] (last searched: 17/1/2023) https://www.guru99.com/unit-testing-guide.html

[2] (last searched: 2/3/2023)
https://livebook.manning.com/book/unit-testing/chapter-1/6

[3] (last searched: 17/1/2023)
https://thevaluable.dev/fighting-software-entropy/

[4] (last searched: 26/1/2023)
http://xunitpatterns.com/

[5] (last searched: 31/1/2023)
https://8thlight.com/insights/tdd-from-the-inside-out-or-the-outside-in

[6] (last searched: 2/3/2023)
https://enterprisecraftsmanship.com/posts/when-to-mock/

## What is a Unit Test

### Definition

Unit testing can be defined as an activity which the main objective is to perform quick tests in small segments of code in a isolated state, separated from the rest of the constituent parts of the system. More concretly, a unit test must follow three requeriments:

* Verifies a single unit of behavior;
* Performs it quickly;
* Isolated from other tests.

The realm of unit testing is a highly multifaceted theme, where differing perspectives and interpretations are commonplace. Amongst the various approaches, two stand out as prominent - the Classical school approach and the London school of unit testing. These approaches, while both focused on unit testing, possess distinct variations in their understanding and handling of the concept of "isolation" within a unit test. 


### London School of Unit Testing

This approach considers isolating the SUT from its collaborators, which means if a certain class is our SUT (System Under Test) and it has a dependency on another class, then this dependency must be substitued by a *test double*. In this way, the behavior of the class under test won't be affected by any external influence. 

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

### Classical School Approach

The classical school approach defends that unit tests must be in a isolated state regarding the rest of the system. Additionally each unit test must be independent from each other as to not exist external interference in the behavior of unit tests.

Unit tests can exercise a set of classes at once, however these must not reach a shared state, they must not interfere each other. A example of shared state is a out-of-process dependency like a database for example [2].

In cases where multiple tests are executed in parallel, the use of shared resources can lead to unexpected and undesirable behavior. For instance, imagine two unit tests that are designed to perform different actions on a shared database, one adding a record and the other removing a record. If these tests are run concurrently, and the second test completes before the first, the first test may fail not due to any issue within the test itself, but rather due to the interference caused by the second test altering the state of the shared resource.

This highlights the possible dangers of shared dependencies within unit testing. Some can cause undesirable behaviors because of interference as the unit tests are not isolated. Types of dependencies that can affect unit testing are as follows:

* ***Shared dependency***: dependency shared between tests providing means for the tests to affect each other's behavior;
* ***Private dependency***: dependency that isn't shared with tests, it only exists internally within the unit being tested;
* ***Out-of-process dependency***: dependency that runs outside a application execution process. It can usually correspond to a shared dependency but not always. A database, for example, is both shared and out-of-process, it runs outside of the tests scope and is used by the tests to alter data. However, a read-only database, is only out-of-process because it can't be used by the tests to alter data and consecutively tests can't affect each others behavior [2].

These dependencies situations are handled differently in the classical school approach. In this approach, only shared dependencies are replaced and private ones are maintained as the figure X.XX shows. 

![](https://i.imgur.com/Vf4o1vU.png)

Shared dependencies are shared *between unit tests*, not between SUTs (units). In this way of thinking, a dependency is not shared if it's possible to create a new instance of it for each test. If there is only one instance of a dependency in production code, then this latter is shared between all unit tests in the SUT as a shared dependency.

Replacing shared dependecies proves to be quite useful regarding the increase of test execution speeds. Calls to shared dependencies take more time than calls to the privates ones, because the shared dependencies are out of execution process of the tests. Unit testing requires the execution of **quick tests** being this an important aspect taking into account.

The use of dependencies is part of the realm of unit testing and integration testing. The way every every unit of the system interacts with the use of dependencies is a very important theme to provide a correct process of creation of a system. The actual use of dependencies and its impact on the general behaviour of a system are talked more in depth in the subsection **"Relationship between Unit and Integration Testing"**.


### How the approaches handle the dependencies

Both schools handle differently the dependencies according their ideals. The London school allows immutable dependencies to be used in their original form. These kind of dependencies possess a content that cannot be changed. This fact does not introduce a problem regarding the change in the behavior of a certain SUT and because of this it's not incorrect to leave this type of dependency as it is.

These immutable dependencies or immutable objects are called ***value objects*** or ***values***. These objects do not possess any kind of behavior or state and are simply used to represent a certain value that is being passed on to a testing method. A immutable object can be instanciated a reasonable amount of times without ever being a problem because these instances have the same content being interchangeable.

Resuming the point in section "*Classical School Approach*", a dependency can be of three types: *shared*, *private* or *out-of-process*. *Shared* dependencies can only be mutable, its content is being changed by other parts of the system. 

*Private* dependencies can either be mutable or immutable. A instance that is only available to the unit being tested can possess a content that is changed within the scope of the SUT (mutable nature). A private instance can also be immutable representing, for example, a value that is only being used for certain methods. 

A simpler example would be having two instances regarding a store themed application. A *Store* and a *Product* instances being both only available to a SUT (private dependencies). The *Store* manages different aspects of the products such as: quantity, price and amount sold. The *Product* only has description, type and name associated to a product. The *Product* instance can be considered a immutable object as the *Store* instance can be a mutable object. The *Store* content will be constantly changed as the *Product* content only represents values (being a *value object*).

Classical school considers all shared dependencies to be replaced as these interferes with the behavior of unit tests.

A representation of how each schools handles the dependencies can be visualized in the figure X.XX:

![](https://i.imgur.com/SylakSZ.png) [2]

Often times the term *collaborator* is used for the London School approach to mention the dependencies, however this term needs to be explained as it posseses a different meaning. **Collaborator** is a dependency of a shared or mutable nature. Taking the example of the *Store* and *Product* instances mentioned above, *Store* can be considered as a collaborator because its content can be changed (mutable nature) while the *Product* can't be considered as such (immutable nature).

Another aspect to take into account is where a *out-of-process* dependencies blends in all this rationale. Not all dependencies of this type are *out-of-process*, it depends on certain situations:

* *Shared* and *out-of-process*: an example of this is a database. It is used by tests (shared) and it's out of the main process (out-of-process);
* *Shared* and non *out-of-process*: a singleton is a good example for this. Being reused by tests (shared) but it is not out of the main process of the tests (non *out-of-process*);
* Non *Shared* and *out-of-process*: an API service can be an example of this type of situation. Tests can't modify the API and therefore can't interfere in each other's behavior (non *shared*) while being out of the main process (*out-of-process*).


### Differences between approaches (see section 2.3)

The root diference between the two approaches is the isolation attribute of a unit test. Classical approach defends the isolation must be between the unit tests themselves on the contrary, London school says that the isolation must be done for the SUT, separating the latter from its collaborators. A summary of the principal differences between each approach can be found in the following table:


|  | Isolation of | Unit test | Test doubles for |
| -------- | -------- | -------- | -------- |
| ***London school***     | Units (SUT)     | Is a class     | All but immutable dependencies     |
| ***Classical school***     | Unit tests     | Is a class or set of classes     | Shared dependencies     |

Both approaches possess different benefits according their specific use. Overall a group of points can be made regarding the choice of each approach:

* **Granularity**: the tests following the London approach are more fine-grained and check only one class at time instead of the Classical approach who can more than one class in certain situations. Checking once at a time reduces the complexity to resolve certain erroneous situations when they happen. Code being fine-grained allows easier testing of units, making it easier to write focused tests for specific units; 
* **Testing in a large amount**: when testing with a grand quantity of interconnected classes (lots of shared dependencies in a unit), it can be troublesome to design a specific test that comprehends the problem domain of the unit being tested. The classical approach only replaces the shared dependencies as the London approach replaces all the dependencies (except for the immutable ones) with the use of mock objects referred in section X.XX. This provides a reduction in complexity reducing substantially the amount of preparation necessary for a unit test;
* **Bug location**: when applying a London approach, only tests whose SUT has the bug will fail. With the London approach is easier to track the location of the bug. When applying a Classical approach, all the tests that target clients of the defective class will all be affected, this situation tends to provoke failures across the parts of the system. With the Classical approach, various parts of the system will fail, and it is extremely complex to find the location of the bug. However this latter reveals itself favorable in certain situations. Failures happening in lots of tests is a good indication that the altered code, that provoked the failures, is important for the overall functionality of the system being a useful information to keep in mind when adjusting the code [2].
* **Test-driven development (TDD)**: London and Classical approaches have different types to apply TDD: 
    * **Classical Approach**: applies a inside-out TDD (Bottom Up approach). With this approach, each part (i.e. an individual class or module) is created sequentially until the overall system is built up. Building up a part at a time reduces the complexity of the work to be done [5]. Tests are created for simpler levels of the system (initial parts) in a sequential manner being added more tests as the system develops; 
    * **London Approach**: applies a outside-in TDD (Top Down approach). With this approach, higher-level tests are made that set expectations for the whole functionality of the system. The tests are based on user scenarios, and all the parts are interconnected at the start [5]. Initial tests that cover interactions between parts are made and sequentially more tests will be created covering more specifically each constituent part of the system;
    * **Over-specification**: this entails the coupling of tests to a SUT implementation. The London approach tends to produce tests that couple to the implementation more often than the classical approach because of the use of test doubles [2]. This higher coupling can lead to tests that are fragile and prone to failures when the implementations changes. Higher the coupling, higher the chances to occur test failures when changes are made to the SUT implementation.

### Mocks and Test Fragility

The use of mocks can introduce some fragility to the SUT being tested. Replacing certain dependencies with mocks can add dissonances when the SUT in question is changed. These fragilities can be caused by a set of factors who will be explained in the following sections.

#### Communications between systems

Communications within a application is a important aspect to take into account as this is directly correlated to the use of mock objects. It's necessary to distinguish two types of communication: **Intra-system communication** and **Inter-system communication**.

Intra-system communications consist in communications between classes within the application. Inter-system communications encompass all the external communications between a application and external applications.

The intra-system communications are the implementation details within a application because the classes themselves communicate in the application domain in order to perform an operation. Coupling to these collaborations between classes can induce fragile tests [2].

The inter-system communications describe the way a application or system talks to external entities which forms an observable behavior of the system (result of output according a certain input.)

Mocks can be used for intra and inter communications. It can be used to verify internal and external communications within a system however, as stated before, verifying communications between classes in a system results in tests that couple more to the implementation details leading to fragile tests. In this situation, unit tests with low resistance to refactoring are created.

The figure X.XX demonstrates a visual representation a example of each type of communication between a communication, it's constituent parts and external entities. 

![](https://i.imgur.com/v63LZTI.png) [6]

#### Classical and London Approaches on Mocks

The approaches refered in sections X.XX and X.XX, have different ways to apply mocks (test doubles) to replace dependencies within a system.



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

## Unit Test Quality

(ver secção 4 - 4.3)

## Relationship between Unit and Integration Testing (TODO)
...

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





