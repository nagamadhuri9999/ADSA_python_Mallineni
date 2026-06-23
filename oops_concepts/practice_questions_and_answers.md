# 50 Object-Oriented Programming (OOP) Practice Questions & Answers

## Core Concepts (Classes & Objects)

**1. What is Object-Oriented Programming (OOP)?**
**Answer:** OOP is a programming paradigm based on the concept of "objects", which can contain data (attributes or properties) and code (methods or functions). It aims to bind data and the functions that operate on them together.

**2. What is a Class?**
**Answer:** A class is a blueprint or template for creating objects. It defines a set of attributes and methods that the created objects will have.

**3. What is an Object?**
**Answer:** An object is an instance of a class. It represents a specific entity with its own state (data) and behavior (methods) as defined by its class.

**4. What are the four main principles of OOP?**
**Answer:** The four main principles are Encapsulation, Inheritance, Polymorphism, and Abstraction.

**5. What is the difference between a class and an object?**
**Answer:** A class is a logical construct (a blueprint), whereas an object is a physical reality that occupies memory in the system.

**6. What is a Constructor?**
**Answer:** A constructor is a special method used to initialize objects when they are created. In Python, the constructor is `__init__`.

**7. What is a Destructor?**
**Answer:** A destructor is a special method called when an object is destroyed or garbage collected. In Python, it is `__del__`.

**8. What is the `self` keyword (in Python) or `this` (in Java/C++)?**
**Answer:** It is a reference to the current instance of the class and is used to access variables and methods that belong to the class.

**9. What are instance variables?**
**Answer:** Instance variables are variables whose value is specific to a particular instance (object) of a class.

**10. What are class variables?**
**Answer:** Class variables are shared across all instances of a class. They belong to the class itself rather than any specific object.

## Encapsulation & Access Modifiers

**11. What is Encapsulation?**
**Answer:** Encapsulation is the bundling of data and methods that operate on that data within a single unit (class), and restricting direct access to some of the object's components.

**12. Why is Encapsulation useful?**
**Answer:** It prevents accidental modification of data, promotes data hiding, and allows internal implementation to be changed without affecting other parts of the code.

**13. What are Access Modifiers?**
**Answer:** Access modifiers are keywords that set the accessibility (visibility) of classes, methods, and other members. Common types are Public, Private, and Protected.

**14. What is a Public member?**
**Answer:** A public member is accessible from anywhere outside the class.

**15. What is a Private member?**
**Answer:** A private member is accessible only within the class where it is declared. In Python, it is denoted by a double underscore prefix `__`.

**16. What is a Protected member?**
**Answer:** A protected member is accessible within the class and its subclasses. In Python, it is conventionally denoted by a single underscore prefix `_`.

**17. What are Getter and Setter methods?**
**Answer:** They are methods used to safely read (getter) and update (setter) the private attributes of a class.

**18. What is a Property in Python?**
**Answer:** A property is a built-in function/decorator that allows you to define methods that can be accessed like attributes, often used for getters and setters.

**19. What is Name Mangling?**
**Answer:** Name mangling is a mechanism in Python where an interpreter changes the name of private variables (prefixed with `__`) to avoid naming collisions in subclasses.

**20. What is Data Hiding?**
**Answer:** Data hiding is an aspect of encapsulation where internal object data is hidden from the outside world to protect its integrity.

## Inheritance

**21. What is Inheritance?**
**Answer:** Inheritance is a mechanism where a new class (child/subclass) derives properties and behavior (methods) from an existing class (parent/superclass).

**22. What are the benefits of Inheritance?**
**Answer:** It promotes code reusability, establishes a natural relationship between classes, and reduces code redundancy.

**23. What is Single Inheritance?**
**Answer:** When a class inherits from only one parent class.

**24. What is Multiple Inheritance?**
**Answer:** When a single class inherits from more than one parent class.

**25. What is Multilevel Inheritance?**
**Answer:** When a class is derived from a class which is also derived from another class (e.g., A -> B -> C).

**26. What is Hierarchical Inheritance?**
**Answer:** When more than one child class is derived from a single parent class.

**27. What is Hybrid Inheritance?**
**Answer:** A combination of two or more types of inheritance (e.g., mixing multiple and hierarchical inheritance).

**28. What is the `super()` function?**
**Answer:** The `super()` function returns a temporary object of the superclass, allowing you to call its methods, most commonly used within the child class's constructor.

**29. What is Method Resolution Order (MRO)?**
**Answer:** MRO is the order in which a programming language resolves a method or attribute in a class hierarchy, especially important in multiple inheritance.

**30. What is the Diamond Problem?**
**Answer:** An ambiguity that arises in multiple inheritance when two classes B and C inherit from A, and class D inherits from both B and C. If D calls a method defined in A (and overridden in B and C), it's ambiguous which method to execute. MRO solves this.

## Polymorphism

**31. What is Polymorphism?**
**Answer:** Polymorphism means "many forms". It allows methods to do different things based on the object it is acting upon.

**32. What is Method Overloading?**
**Answer:** Defining multiple methods with the same name but different parameters (number or type) within the same class. (Note: Python doesn't support this natively like Java/C++, but handles it via default arguments).

**33. What is Method Overriding?**
**Answer:** When a child class provides a specific implementation for a method that is already defined in its parent class.

**34. What is Compile-time (Static) Polymorphism?**
**Answer:** Polymorphism resolved during compilation, such as method overloading and operator overloading.

**35. What is Run-time (Dynamic) Polymorphism?**
**Answer:** Polymorphism resolved during program execution, typically achieved through method overriding.

**36. What is Operator Overloading?**
**Answer:** Giving extended meaning beyond their predefined operational meaning to operators (like +, -, *) to work with user-defined objects.

**37. What are Magic/Dunder Methods in Python?**
**Answer:** Special methods surrounded by double underscores (e.g., `__init__`, `__str__`, `__add__`) that define how objects behave with built-in operations.

**38. What is Duck Typing?**
**Answer:** A concept (common in Python) where the type or the class of an object is less important than the methods it defines. "If it walks like a duck and quacks like a duck, it must be a duck."

**39. How do you implement Polymorphism with functions?**
**Answer:** By writing a function that can take any object as a parameter and call a specific method that is expected to be implemented by all passed objects.

**40. What is the difference between Overloading and Overriding?**
**Answer:** Overloading occurs in the same class with different parameters; overriding occurs in a child class with the exact same method signature as the parent.

## Abstraction & Advanced Concepts

**41. What is Abstraction?**
**Answer:** Abstraction is the process of hiding the complex implementation details and showing only the essential features of the object.

**42. How is Abstraction achieved?**
**Answer:** Through abstract classes and interfaces.

**43. What is an Abstract Class?**
**Answer:** A class that cannot be instantiated on its own and may contain one or more abstract methods. It is meant to be subclassed.

**44. What is an Abstract Method?**
**Answer:** A method that has a declaration but no implementation. It must be overridden by concrete subclasses.

**45. What is an Interface?**
**Answer:** A completely "abstract class" that is used to group related methods with empty bodies. (In Python, this is often implemented using abstract base classes with only abstract methods).

**46. What is the difference between an Abstract Class and an Interface?**
**Answer:** An abstract class can have both abstract and concrete methods, and can hold state. An interface generally only has abstract methods and no state.

**47. What is Composition?**
**Answer:** A "has-a" relationship where an object contains another object. If the parent object is destroyed, the child object ceases to exist (strong relationship).

**48. What is Aggregation?**
**Answer:** A "has-a" relationship like composition, but the child object can exist independently of the parent object (weak relationship).

**49. What is Association?**
**Answer:** A general relationship where all objects have their own lifecycle and there is no owner.

**50. What are SOLID principles in OOP?**
**Answer:** A set of five design principles: Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion, which make object-oriented designs more understandable, flexible, and maintainable.
