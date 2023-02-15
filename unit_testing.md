# Unit Testing - Masters

Sources: 

[1] (last searched: 17/1/2023) 
https://www.guru99.com/unit-testing-guide.html

[2] (last searched: 15/2/2023 => **book**)
https://livebook.manning.com/book/unit-testing/chapter-1/6

[3] (last searched: 17/1/2023)
https://thevaluable.dev/fighting-software-entropy/

[4] (last searched: 26/1/2023)
http://xunitpatterns.com/

[5] (last searched: 31/1/2023)
https://8thlight.com/insights/tdd-from-the-inside-out-or-the-outside-in

[6] (last searched: 3/2/2023)
https://enterprisecraftsmanship.com/posts/when-to-mock/

[7] (last searched: 15/2/2023)
https://www.softwaretestinghelp.com/black-box-testing/

[8] (last searched: 15/2/2023)
https://www.softwaretestinghelp.com/guide-to-functional-testing/

[9] (last searched: 15/2/2023)
https://www.softwaretestinghelp.com/white-box-testing-techniques-with-example/

[10] (last searched: 15/2/2023)
https://www.browserstack.com/guide/code-coverage-vs-test-coverage

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

Figure X.XX shows how the isolation in this approach is achieved by replacing SUT dependencies by test doubles:

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

This approach is also heavily associated with the use of mock objects to simulate the behavior of dependencies.

### Classical School Approach

The classical school approach defends that unit tests must be in a isolated state regarding the rest of the system. Additionally each unit test must be independent from each other as to not exist external interference in the behavior of unit tests.

Unit tests can exercise a set of classes at once, however these must not reach a shared state, they must not interfere each other. A example of shared state is a out-of-process dependency like a database for example [2].

In cases where multiple tests are executed in parallel, the use of shared resources can lead to unexpected and undesirable behavior. For instance, imagine two unit tests that are designed to perform different actions on a shared database, one adding a record and the other removing a record. If these tests are run concurrently, and the second test completes before the first, the first test may fail not due to any issue within the test itself, but rather due to the interference caused by the second test altering the state of the shared resource.

This highlights the possible dangers of shared dependencies within unit testing. Some can cause undesirable behaviors because of interference as the unit tests are not isolated. Types of dependencies that can affect unit testing are as follows:

* ***Shared dependency***: dependency shared between tests providing means for the tests to affect each other's behavior;
* ***Private dependency***: dependency that isn't shared with tests, it only exists internally within the unit being tested;
* ***Out-of-process dependency***: dependency that runs outside a application execution process. It can usually correspond to a shared dependency but not always. A database, for example, is both shared and out-of-process, it runs outside of the tests scope and is used by the tests to alter data. However, a read-only database, is only out-of-process because it can't be used by the tests to alter data and consecutively tests can't affect each others behavior [2].

These dependencies situations are handled differently in the classical school approach. In this approach, only shared dependencies are replaced and private ones are maintained as the figure X.XX shows. 

![](https://i.imgur.com/Vf4o1vU.png) [2]

Shared dependencies are shared *between unit tests*, not between SUTs (units). In this way of thinking, a dependency is not shared if it's possible to create a new instance of it for each test. If there is only one instance of a dependency in production code, then this latter is shared between all unit tests in the SUT as a shared dependency.

Replacing shared dependecies proves to be quite useful regarding the increase of test execution speeds. Calls to shared dependencies take more time than calls to the privates ones, because the shared dependencies are out of execution process of the tests. Unit testing requires the execution of **quick tests** being this an important aspect taking into account.

:::warning
**(usar na secção unit and integration testing???)**

The use of dependencies is part of the realm of unit testing and integration testing. The way every every unit of the system interacts with the use of dependencies is a very important theme to provide a correct process of creation of a system. The actual use of dependencies and its impact on the general behaviour of a system are talked more in depth in the subsection **"Relationship between Unit and Integration Testing"**.
:::


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

* ***Shared* and *out-of-process***: an example of this is a database. It is used by tests (shared) and it's out of the main process (out-of-process);
* ***Shared* and non *out-of-process***: a singleton is a good example for this. Being reused by tests (shared) but it is not out of the main process of the tests (non *out-of-process*);
* **Non *Shared* and *out-of-process***: an API service can be an example of this type of situation. Tests can't modify the API and therefore can't interfere in each other's behavior (non *shared*) while being out of the main process (*out-of-process*).


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

#### Communications in a system

Communications within a application is a important aspect to take into account as this is directly correlated to the use of mock objects. It's necessary to distinguish two types of communication: **Intra-system communication** and **Inter-system communication**.

Intra-system communications consist in communications between classes within the application. Inter-system communications encompass all the external communications between a application and external applications.

The **intra-system communications** are the implementation details within a application because the classes themselves communicate in the application domain in order to perform an operation. Coupling to these collaborations between classes can induce fragile tests [2].

The **inter-system communications** describe the way a application or system talks to external entities which forms an observable behavior of the system (result of output according a certain input.)

Mocks can be used for intra-system and inter-system communications. It can be used to verify internal and external communications within a system however, as stated before, verifying communications between classes (at a internal level) in a system results in tests that couple more to the implementation details leading to fragile tests. In this situation, unit tests with low resistance to refactoring are created. This latter attribute refers to the degree to which a test can sustain refactoring without introducing any kind of error (failing). Tests that are thightly coupled to the implementation tend to be fragile tests, as a constant maintenance is needed as the SUT changes. Mocks are mostly recommended for external communications or in this case inter-system communications. 

The figure X.XX demonstrates a visual representation a example of each type of communication between a communication, it's constituent parts and external entities. 

![](https://i.imgur.com/v63LZTI.png) [6]

#### Classical and London Approaches Revisited

London approach, as mentioned in section X.XX, defends the use of test doubles to replace all but immutable dependencies and because of this it doesn't differentiate between intra-system and inter-system communications. It's main purpose is to simulate behavior of the dependencies and verify the SUT. As a result, these tests verify the communications between classes as much they verify the communications between external entities.

Classical approach, as referred in section X.XX, it only replaces the shared dependencies between unit tests. This approach prevents the unit tests in SUT from running in parallel and consecutively it doesn't allow for tests to interfere with each other's executions. However as it deals with the internal scope of a aplication, it is not ideal for inter-system communications.

In cases for the non out-of-process shared dependencies, they can be prevented by instanciating them on each test run. In situations where this type of dependency is out-of-process, testing gets harder because instanciating out-of-process elements before each test execution is not correct (instanciating a new database for example) as this slows down the test suite. For these types of cases, replacing the dependencies with test doubles such as mocks objects is more correct. London school approach is known to use test doubles to replace the dependencies with the use of mocks. But as stated in section "Communications in a system", mocks can lead to fragile tests. 

#### Proper use of Mocks
One way to eliminate the fragility of the mocks is to use them for ***unmanaged dependencies***. Interactions with this type of dependency are observed *externally*. Interactions produce an observable behavior of the system that communicates with a external system. There is a clear distinction between *unmanaged dependencies* and *managed dependencies* and it's the ability to have control over them. *Managed* refers to dependencies that are only acessible through a application (application has full control over them) as *Unmanaged*  refers to dependencies that a application cannot control completely. One example of an unmanaged dependency would be a SMTP server, the ability to send emails is not controlled by the application but by a external service. A example of a managed dependency would be a database, as this latter is acessed by the application through the use of APIs.

Dependencies are an essential part of an application domain being extremely important for communications at an internal state (intra-system) or at an external level (inter-system). Mocks should be used for *unmanaged dependencies* as these ones maintain it's functionality no matter any type of refactoring done at the system's internal level. With this, prevention is made regarding fragile tests as the main reason mocks are fragile correlates to the resistance-to-factoring metric already mentioned in section "Communications in a system".

### Unit and Integration Testing 

Unit testing isn't the only operation necessary to contribute for a well working system as this latter only verifies the behavior of a individual component of the system. In order to provide a thorough verification of the  behavior between system components, a operation called ***Integration Testing*** is needed. This operation verifies the behavior of the constituent parts of a system, how they communicate and behave with each other. 
Unit tests and integration tests are correlated regarding their main objective that is to provide a well working system by in a first instance test early layers of the system in a individual scope (executed by unit testing) and afterwards test if the units that compose the system, behave as expected (executed by integration testing).

#### Dependencies usage

The use of dependencies is part of the realm of unit testing and integration testing. The way every every unit of the system interacts with the use of dependencies is a very important theme to provide a correct process of creation of a system. For example a certain SUT, that represents a part of the system, is chosen to be tested to verify if the implementation behaves according expectation. This latter can possibily necessitate to use a dependency in order to perform its operations. In the realm of unit testing, the objective is to verify the SUT behavior in isolation, as in the realm of integration testing is to verify the communications and interactions between units of a system. However as stated before, to test certain units some dependencies are needed to perform the SUT operations. According to the different approaches on unit testing, Classical and London approaches, dependencies are treated differently  however the main objective remains and that is to perform tests on components of a system. 

The themes of unit testing and integration testing are deeply connected in this dependency topic. An example could be a shared dependency that is used in unit testing to provide necessary inputs or services for the SUT and in integration testing used to verify communications between units of a system. These types of dependencies, as well other types spoken in section "How the approaches handle dependencies", are a major component for unit tests and integration tests as they help testing components of the system in different situations. This dependencies theme is part of the communications between a system theme already mentioned in section "Communications in a system".

#### Differences between operations

Despite being correlated to favor a well-designed and implemented system, unit and integration testing have a set of differences that distinguish them between one another. These can be viewed in the following table: 


| Unit Test | Integration Test |
| -------- | -------- | 
| Test a component of a system in a isolated form, separated from the rest of the system to verify its correctfulness     | Test and verify communications and behaviors between constituent parts of the system to ensure they are functioning as expected|
| Can be performed at any time | Can be performed after unit testing but before system testing
| Focuses on a single module | Checks integration between two or more modules
| Kind of white-box testing | Kind of black-box testing
| Scope-limited, as it covers a piece of code | Wide scope, as it covers more parts of the system
| Internal structure of the application is known | Almost no internal structure of the application is known


The main difference between Unit and Integration testing lies in their primary objectives. Unit testing focuses on testing individual units or components of code in isolation to verify their behavior, while Integration testing examines how the different parts of a system work together and interact with each other to assess the overall system correctness.


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

For a unit test to be considered of high quality it must follow four attributes being:
* Protection against regressions;
* Resistant to refactoring operations;
* Provide fast feedback;
* Maintainability.

A unit test can be evaluated according to these attributes as all tests exhibits some degree of each attribute. Each of these attributes possess different particularities, being this explained in order of appearance.

### Protection against regressions

In the scope of software, *regression* is when a feature stops working as intented after a certain event was done [2]. The term *regression* can also be called *software bug*.

Regression is more likely to appear when a project possesses a large code base. As more functionalities are developed, higher the chances *software bugs* will appear and because of this a much needed protection must be present in order to sustain a project in the long run. A test can be measured regarding its protection against regressions according to three metrics:

1. **How much code is executed during the test;**
2. **Complexity of the code executed;**
3. **How important the code is for the intended domain.**

- For point **1**, higher the amount of code executed, higher the chances the test will reveal a presence of a regression. Testing large amounts of code can help determine how well the latter is protected against possible regressions;

 - For point **2**, complex code is better than trivial code. It's rare to occur regressions in trivial code rather than complex code as it is more simple. Simpler code sometimes does not possess complex elements, like libraries or frameworks for example, that increase the overall complexity of the code and can introduce an higher chance of occurrence of *sofware bugs*;

- For point **3**, code that is not relevant for the problem domain is not even worthwhile to measure its protection against regressions. Only code that targets the domain problem should be measured.

### Resistance to refactoring

This attribute refers how much a test can sustain refactoring operations without being compromised or in another words, keeping its functionality without failing. Refactoring is an operation that consists in changing existing code without altering its observable behavior being normally done for code improvements. In order to evalue how good a test is resistant to refactoring operations, a term must be introduced being this the ***false positive*** term. The lower the false positives, higher the resistance the test possesses and vice-versa.

#### False Positive

When refactoring operations are made in a working system, often times after these operations are made, certain tests accuse failures on their execution. These failures do not accuse anything wrong with the system features as these continue to work as intended despite the failures from the tests. The problem here is that the tests are tightly coupled to the implementation details of the SUT and with SUT changes, that were made by refactoring operations, these tests accuse a failure raising a false alarm. This type of situation is referred as a ***false positive*** [2]. The test fails however the functionality it covers works as intended.

False positives often appear in refactoring situations, where a change is made in the implementation but the observable behavior is kept intact. They can be devastating for the overall development of a project as it can damage the perceptivity of the overall correctness of the latter. Initially developers take test failures as a serious matter dealing with them accordingly. However if a constant sequence of failures is presented, developers tend to ignore them more each time and this is because of previous false alarms they had (provoked by false positives). Eventually a released software will possess a good amount of bugs lowering the value of the latter. This is why false positives can be damaging and the tests should not couple too much to the implementation details of the unit they are testing. 

In order to reduce the brittleness of the tests, these need verify the end result of the SUT and not couple too much to the implementation details within [2]. A verification of the result can provide more resistance to refactoring operations, the test is not too concerned about which steps were necessary to do something, it's concerned about the end result of the SUT and if this corresponds to the expected result.

### Fast Feedback

A unit test that produces a faster feedback is always more advantageous that one that does not. Faster tests enable faster feedback which then can be used to fix bugs rapidly in case they appear. Slower tests produce a slower feedback, increasing the period of time to correct a certain bug and thus increasing overall time of correction of successive bugs that appear in the long run. Slower tests can also cause a "discouragement" effect for the developer, these take to much time to run and most of these tests will be ignored due to the extensive time they take to execute, compromising the quality of the software in the end.

### Maintainability

Regarding the maintainability aspect, this metric corresponds to what extent a unit test can suffer modifications to be modified, improved or updated without introducing bugs or issues. A unit that is maintainable is better that one who is not. This attribute can be divided in two important aspects:

* ***Is it hard to understand the test**?*: this question is correlated to the size of test. A test with a huge amount of lines of code, the less readable it is and it's harder to modify. A test with fewer amount of code should always be the priority as it's more easier to read and to modify it. The reduction of the size should always be sought out without compromising the quality of the unit test;
* ***Is it hard to run the test?***: this question corresponds to the complexity of execution of the test. A test that is harder to run, requires more time or more effort that ones that are simpler. Tests that uses out-of-process dependencies, for example, need much more effort and time to execute than one that does not. Such tests are harder to modify.

### Test Accuracy

The attributes mentioned in section "Protection against regressions" and "Resistance to refactoring" are related regarding the accuracy of a unit test. Both of them contribute for the accuracy in different forms as the main objective it's to try maximize the latter.

When speaking about test accuracy, three additional terms must be explained as the *false positive* term was already introduced in section "Resistance to refactoring". These terms can be shown in the following table:

|             | Correct Functionality | Broken Functionality 
| ----------- | --------------------- | --------------------
| Test Passes | Correct inference (True negative) | False negative |
| Test Fails  | False positive | Correct inference (True positive) |

* ***True negative***: a test passes and the behavior of the SUT occurs as expected;
* ***True positive***: a test fails and the correspondent functionality of the SUT is broken. It's expected for the test to fail if the functionality is broken;
* ***False negative***: the test passes and the functionality does not present a expected behavior. This is associated with the *Protection against regressions* attribute. Tests with good protection against regressions help avoid *false negatives*;
* ***False positive***: the test fails but the functionality occurs as expected. This is associated with the *Resistance to refactoring* attribute. Tests that have a good resistance to refactoring help avoid *false positives*.

The accuracy of a unit test can be measured according the probability of *false positives* and *false negatives*. The lower the probability, higher the accuracy of the test. As mentioned above, each of these correspond to two important attributes for a good unit test being *protection against regressions* (*false negatives*) and *resistance to refactoring* (*false positives*). The accuracy is measured on how good the test indicates the presence of bugs (lack of *false negatives*, *protection against regressions*) and how good the test indicates the absence of bugs (*lack of false positives*, *resistance to refactoring*) [2].

(info adicional em baixo)

:::info

**Absence of Bugs**

The absence of bugs in the SUT is directly related to false positives in a unit test because if there are no bugs in the SUT, the test should not report any failures or errors. If the unit test reports failures or errors in this scenario, it is a false positive and the test is not accurate. On the other hand, if a unit test correctly reports the absence of bugs in the SUT, it is considered accurate, and this means that it is less prone to false positives. The accuracy of a unit test in indicating the absence of bugs is an important metric to measure the quality of the test and its usefulness in detecting real problems in the SUT.

**Presence of Bugs**

False negatives occur when a unit test fails to catch a bug that exists in the system under test (SUT). If a bug is present in the SUT, the unit test should detect it and indicate failure. If the test passes but the bug is still present, this is a false negative and the bug can go unnoticed and cause problems later on. The presence of bugs in the SUT and the resulting false negatives can negatively impact the reliability and confidence in the results of the unit tests, leading to a lack of trust in the test suite.
:::

Another way to perform a accuracy measure of a unit test can be demonstrated in the following formula [2]:

$Test \ accuracy = Signal \ (number \ of \ bugs \ found) \ / \ Noise \ (number \ of \ false \ alarms \ raised)$

The formula uses a signal-noise ratio to measure how a accurate a unit test can be. A accurate unit test must possess a higher *signal* (higher numerator which indicates the test is capable of finding regressions) and a lower *noise* (lower denominator which indicates the test is better at not raising false alarms). A test that can't find bugs but does not raise false alarms (lower numerator and lower denominator) is not of any use. The same can be said in the opposite situation, a test that can find bugs but raises false alarms (higher numerator and higher denominator) is not of any use either. These situations are useful to measure how a accurate a test can be relatively to finding regressions and raising false alarms. 

#### Best attribute ratio

A good unit test, as mentioned in the beginning of the section "Unit Test Quality", must follow four attributes being *protection against regressions*, *resistance to refactoring*, *fast feedback* and *maintainability*. However it's extremely difficult to achieve a unit test that excels in *protection against regressions*, *resistance to refactoring* and *fast feedback* at the same time [2]. In this case, excelling in a certain attribute comes at a cost of lacking in another.

There's multiple praticle examples of types of tests that prove the point being:

* ***End-to-end tests***: these tests are focused in the user's perspective, they emulate users interactions in a system. This type of test is well protected against regressions as exercises a large amount of code (including libraries, frameworks, and another related applications) and *false positives* are generally less common as these tests verify the behavior of the system as a whole making it less likely to react to refactoring operations (if refactoring is done correctly and does not change interactions between components). However it does not fare well in the *fast feedback* attribute, as it exercises a large amount of code being specially slow. It's a hassle to apply when developing a software to be fast delivered;

* ***Trivial tests***: simple tests that check if a basic functionality of a SUT works as expected. These tests fare well in the *fast feedback* attribute as they are simple tests that provide fast responses. They also are less prone to produce *false positives* as they verify the end result of the SUT rather than the implementation details. This means if the end result stays the same after refactoring operations, these tests will pass even after a change in the internal details of a SUT. For these reasons, they are more resistant to refactoring and less prone to fragile tests. However these are not protected against regressions, being simple tests they are almost meaningless, they test the basic functionality of the SUT not covering important parts and thus not able to detect possible bugs to occur;

* ***Brittle tests***: these tests are known to be fragile because they are not resistant to refactoring operations. They are very prone to *false positives*, the tests will acuse failures after refactoring operations. A slight chance on the implementation details of a SUT can accuse a failure from the test even if the functionality remains as expected. Despite this, these tests fare well in the *protection against regressions* and *fast feedback* attributes as they typically detect changes in the system and as they are not too complex, they provide a fast response when executed.

#### Balance between attributes

It's especially hard to create a unit test that has a perfect score for the *protection against regressions*, *resistance to refactoring* and *fast feedback* attributes. A unit test, can excel in two attributes at the cost of one of them as demonstrated in the previous section. A unit test should possess a healthy balance between these three attributes without letting any of them behind. 
It's nearly impossible to create a ideal test that maximizes these three attributes [2], the necessity to apply trade-offs for the attributes is a harsh reality. In accordance to the three attributes, each one of them must be viewed with different levels of malleability.
For the *resistance to refactoring* attribute, this is one is a very important one because a test either has resistance or it does not, there is almost no stages in between [2]. A test can't concede between a much or less resistance, either it has resistance or none at all. The trade-off comes regarding the remaining two attributes *protection against regressions* and *fast feedback* as these two are more malleable. A test can be less or more quick to respond as the same can be said for a test that can protect more against bugs or one that does not protect as much. A balanced choice must be made between these attributes in order for them to not be less impactful than the other.

Regarding the maintainability attribute, while not being correlated to the first three, a code must be as maintainable as possible. A test that is large in size, like a end-to-end test, that exercises a large amount of code it's necessary an effort to keep everything operational in the long run.

### Code Coverage Metrics

Another way to measure if a unit test is of good quality is to use code coverage metrics. These can be divided in various types with different objectives, however this topic of *coverage metric* needs to be viewed carefully.

For starters, a *coverage metric* can be defined as a operation to show how code was executed. This operation is primarely used in the realm of unit testing with the main objective to perform an assessment of quality of unit tests [10]. *Coverage metric* can be measured in a percentage value, i.e, from none to 100% that represents percentage of code covered for example. In this situation, a higher value is perceived as a good indicator however, in reality, it's not that simple. A higher code coverage value does not represent if a code is of quality or not, it only means the test was able coverage a *x* amount of code. It can be said for lower values that the test is not exercing enough code however a higher amount cannot guarantee a good-quality unit test.

(continue)

* Line Coverage
* Statement Coverage
* Branch Coverage
* Condition Coverage
* Decision Coverage

(coverage and such)

## Automated and Manual Testing (TODO)
...

## Techniques (TODO)
Faults in a software can be found through a wide variety of techniques, all specified within the scope of unit testing.

These techniques can be listed as follows: 
* **Black Box Testing**
* **White Box Testing**
* **Gray Box Testing**

### Black Box Testing (see section 4.5.2 and correlate / see links [7] e [8])

*Black Box Testing* is a software testing method that analyzes the functionality of the software without knowing almost nothing about its internal structure. It derives tests through the specification of requirements  of the software to be tested, being a test driven development operation where all tests are elaborated according a expected result for a functionality of the software. 

Black Box testing can be divided in two principal types being *Functional Testing* and *Non-Functional Testing*. 

*Functional Testing* can be defined as a kind of black-box testing method that is used to perform a functionality verification of a system to assess if it acts as expected [8].

*Non-Functional Testing* is a software testing method for non-functional requeriments, it covers the aspects that are not covered by the *functional testing* [9]. This type of testing is normally done to assess non-functional attributes of a system like execution speed, load limit and failure recovery for example.

### White Box Testing (see section 4.5.2 and correlate / see links [7] e [9])

*White Box Testing* is a software testing method that evaluates the code and the internal structure of a software. Emphasizes code evaluation, measuring a multitude of attributes within the structure of the latter in order to verify if it obeys to the specifications made [9]. Opposite to the *Black Box Testing* method, tests are created to verify the internal structure of the code and are not made from the specification of requirements.

(continue)

### Gray Box Testing






