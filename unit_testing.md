# Unit Testing - Masters

Sources: 

[1] (last searched: 17/1/2023) https://www.guru99.com/unit-testing-guide.html

[2] (last searched: 17/1/2023)
https://livebook.manning.com/book/unit-testing/chapter-1/6

[3] (last searched: 17/1/2023)
https://thevaluable.dev/fighting-software-entropy/

## Definition

Unit testing can be defined as an activity which main objective is to perform tests in segments of code in a isolated state, separated from the rest of the constituent parts of the system. 

## Purpose 

This operation can ensure a higher probability of detection of faults within a system while ensuring a general testing of every part that composes a system.  These tests are performed to verify it the implemented functionalities are in accordance to the system requirements defined in early stages of development.
In another words, it's used to verify the correctness of a certain segment of code.

The identification of possible faults in the early stages of development is more important than to find at later stages. The correction of a fault is minimized when found at early stages of development where it's located at a certain unit. When a system runs and a fault occurs, it's more time-consuming and costly to correct it at system level than at the unit level where is isolated from the rest of the system.

Despite the identification of faults, unit testing can lead to code reuse. In this case, a portion of the testing done can be used again in a different system when the objectives/functionalities are similiar between the different systems.

The application of unit testing can enable a sustainable growth of a software project. In a really early stage of development, there is a low quantity of code to be worried about, enabling a rapid development and progress in the creation of the product. However, as time goes by, more code is created, more architeture ideas are developed and the probability of finding a fault is higher [2].

This latter causes the development speed to be much slower, when performed in it's raw form without tests  in the code. This can reach points where progress is halted due to higher complexity when creating the software.

![](https://i.imgur.com/dntV9bq.png) [2]

This decrease in the development can be called as **software entropy**. **Entropy** is a mathematical concept that states, for a closed, independent system, the amount of disorder doesn't decrease overtime. It can increase or be stable [3]. 

This concept can be applied in software regarding the code built. As the development of the product goes on, more code is created and the quantity of disorder, or entropy, increases.


## Overall Structure

## Automated and Manual Testing

## Techniques
These kinds of faults can be found through a wide variety of techniques, all specified within the scope of unit testing.

These techniques can be listed as follows: 
* **Black Box Testing**
* **White Box Testing**
* **Gray Box Testing**

### Black Box Testing

### White Box Testing

### Gray Box Testing

#### Code Coverage Techniques
* Line Coverage
* Statement Coverage
* Branch Coverage
* Condition Coverage
* Decision Coverage

(coverage and such)





