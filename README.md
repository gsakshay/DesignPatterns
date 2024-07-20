## Design Patterns

Focuses on usage and need for Design Pattern. Before diving in, lets understand that 
- Code is not an asset, it's a liability
- A genius admires simplicity while not sacrificing - readability, performance, maintainability, testability and reusability

**Why Design Patterns?**

* **Beyond Code:**  Effective code goes beyond functionality. It should be:
    * **Readable:** Easy to understand for you and other developers.
    * **Maintainable:** Simple to modify and extend as your project evolves.
    * **Testable:** Verifiable to ensure it works as expected.
    * **Reusable:** Adaptable for use in different contexts.

**A Pattern for Every Problem**

Design patterns come in three main categories, each addressing specific coding scenarios:

1. **Creational Patterns:** Focus on creating objects in a flexible and efficient way.
2. **Behavioral Patterns:**  Deal with how objects interact and communicate with each other.
3. **Structural Patterns:**  Emphasize how classes and objects are structured to form larger systems.

**Choosing the Right Tool**

Once you've identified a relevant category, ask yourself these questions to narrow down to the most suitable pattern:

**Creational Patterns:**

* **Singleton:**  Do you need a single instance of a class throughout your application?
* **Abstract Factory:**  Are you creating families of related objects?
* **Builder:**  Is object creation complex, involving many optional parameters?

**Behavioral Patterns:**

* **Strategy:**  Do you need interchangeable algorithms or behaviors for a particular operation?
* **Command:**  Are you implementing undo/redo functionality, or want to encapsulate requests as objects?
* **State:**  Do you need to manage the internal state of an object and how it changes its behavior?

**Structural Patterns:**

* **Adapter:**  Are you trying to make incompatible interfaces work together seamlessly?
* **Decorator:**  Do you want to add new functionalities to existing objects dynamically?
* **Facade:**  Do you have a complex subsystem with many dependencies? A facade can simplify its interaction with other parts of your code.

There are many more patterns based on different use-cases.