# 50 OOPs Practice Problems & Code Solutions (Python)

This document contains 50 practical coding problems and their solutions, covering all major Object-Oriented Programming (OOP) concepts in Python.

## Section 1: Classes and Objects

**Problem 1: Create a basic `Person` class and instantiate an object.**
```python
class Person:
    pass

p = Person()
print(type(p))
```

**Problem 2: Add `__init__` constructor to initialize `name` and `age`.**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)
print(p.name, p.age)
```

**Problem 3: Create an instance method to display person details.**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

p = Person("Bob", 30)
p.display()
```

**Problem 4: Define and use a class variable (e.g., `species`).**
```python
class Person:
    species = "Homo Sapiens"
    def __init__(self, name):
        self.name = name

p1, p2 = Person("Alice"), Person("Bob")
print(p1.species, p2.species)
```

**Problem 5: Modify a class variable using the class name.**
```python
Person.species = "Human Being"
print(p1.species) # Output: Human Being
```

**Problem 6: Modify an instance variable after object creation.**
```python
p1.name = "Alicia"
print(p1.name) # Output: Alicia
```

**Problem 7: Implement the `__str__` magic method for string representation.**
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"'{self.title}' by {self.author}"

b = Book("1984", "George Orwell")
print(b) # Uses __str__
```

**Problem 8: Implement the `__repr__` method for developer representation.**
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(2, 3)
print(repr(p))
```

**Problem 9: Create multiple objects and store them in a list.**
```python
points = [Point(1, 2), Point(3, 4), Point(5, 6)]
for pt in points:
    print(pt)
```

**Problem 10: Delete an object property and the object itself.**
```python
class Temp:
    def __init__(self, val):
        self.val = val

t = Temp(10)
del t.val # Deletes property
del t     # Deletes object
```

## Section 2: Encapsulation & Access Modifiers

**Problem 11: Create a class with public attributes.**
```python
class Student:
    def __init__(self, name):
        self.name = name # Public

s = Student("John")
print(s.name)
```

**Problem 12: Create a class with a protected attribute (convention).**
```python
class Student:
    def __init__(self, name):
        self._name = name # Protected

s = Student("John")
print(s._name) # Accessible, but indicates it shouldn't be touched directly
```

**Problem 13: Create a class with a private attribute.**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # Private

acc = BankAccount(100)
# print(acc.__balance) # Raises AttributeError
```

**Problem 14: Access a private attribute using name mangling.**
```python
print(acc._BankAccount__balance) # Output: 100
```

**Problem 15: Create a getter method for a private attribute.**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance

acc = BankAccount(150)
print(acc.get_balance())
```

**Problem 16: Create a setter method to modify a private attribute.**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount

acc = BankAccount(100)
acc.set_balance(200)
```

**Problem 17: Use the `@property` decorator for getters.**
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius

t = Temperature(25)
print(t.celsius) # Accessed like an attribute
```

**Problem 18: Use the `@property.setter` decorator.**
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
        
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value

t = Temperature(25)
t.celsius = 30
```

**Problem 19: Create a read-only property (no setter).**
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def area(self):
        return 3.14159 * (self.radius ** 2)

c = Circle(5)
print(c.area)
# c.area = 100 # Raises AttributeError
```

**Problem 20: Use `@property.deleter` to handle attribute deletion.**
```python
class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
        
    @name.deleter
    def name(self):
        print("Deleting name...")
        del self._name

p = Person("Alice")
del p.name
```

## Section 3: Inheritance

**Problem 21: Implement Single Inheritance.**
```python
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    pass

d = Dog()
print(d.speak()) # Inherited method
```

**Problem 22: Override a method from the parent class.**
```python
class Dog(Animal):
    def speak(self):
        return "Woof!"

d = Dog()
print(d.speak())
```

**Problem 23: Use `super()` in the `__init__` method.**
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

d = Dog("Buddy", "Golden Retriever")
print(d.name, d.breed)
```

**Problem 24: Use `super()` to extend an overridden method.**
```python
class Employee:
    def work(self):
        print("Doing basic tasks.")

class Manager(Employee):
    def work(self):
        super().work()
        print("Managing the team.")

m = Manager()
m.work()
```

**Problem 25: Implement Multiple Inheritance.**
```python
class Flyer:
    def fly(self):
        return "Flying"

class Swimmer:
    def swim(self):
        return "Swimming"

class Duck(Flyer, Swimmer):
    pass

duck = Duck()
print(duck.fly(), duck.swim())
```

**Problem 26: Implement Multilevel Inheritance.**
```python
class Vehicle:
    def start(self): print("Vehicle started")

class Car(Vehicle):
    def drive(self): print("Car driving")

class ElectricCar(Car):
    def charge(self): print("Car charging")

ec = ElectricCar()
ec.start(); ec.drive(); ec.charge()
```

**Problem 27: Implement Hierarchical Inheritance.**
```python
class Shape:
    def draw(self): print("Drawing shape")

class Circle(Shape): pass
class Square(Shape): pass

c, s = Circle(), Square()
c.draw(); s.draw()
```

**Problem 28: Check the Method Resolution Order (MRO).**
```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.mro())
```

**Problem 29: Use `isinstance()` to check object inheritance.**
```python
print(isinstance(duck, Duck))    # True
print(isinstance(duck, Flyer))   # True
print(isinstance(duck, Animal))  # False
```

**Problem 30: Use `issubclass()` to check class hierarchy.**
```python
print(issubclass(Dog, Animal)) # True
print(issubclass(Dog, Flyer))  # False
```

## Section 4: Polymorphism

**Problem 31: Implement polymorphism using an external function.**
```python
class Cat:
    def sound(self): return "Meow"
class Dog:
    def sound(self): return "Woof"

def make_sound(animal):
    print(animal.sound())

make_sound(Cat())
make_sound(Dog())
```

**Problem 32: Implement Polymorphism through a common interface.**
```python
shapes = [Circle(), Square()]
for shape in shapes:
    shape.draw() # Calls appropriate method based on object type
```

**Problem 33: Operator Overloading: Overload the `+` operator (`__add__`).**
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3.x, p3.y) # Output: 4 6
```

**Problem 34: Overload the equality operator `==` (`__eq__`).**
```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

print(Point(1, 2) == Point(1, 2)) # True
```

**Problem 35: Overload the less than `<` operator (`__lt__`).**
```python
class Student:
    def __init__(self, grade):
        self.grade = grade
    def __lt__(self, other):
        return self.grade < other.grade

print(Student(80) < Student(90)) # True
```

**Problem 36: Overload the `len()` function (`__len__`).**
```python
class Team:
    def __init__(self, members):
        self.members = members
    def __len__(self):
        return len(self.members)

t = Team(["Alice", "Bob", "Charlie"])
print(len(t)) # Output: 3
```

**Problem 37: Demonstrate Duck Typing.**
```python
class Airplane:
    def fly(self): print("Airplane is flying")

class Bird:
    def fly(self): print("Bird is flying")

def lift_off(entity):
    entity.fly() # Only cares if entity has 'fly' method

lift_off(Airplane())
lift_off(Bird())
```

**Problem 38: Simulate method overloading using default arguments.**
```python
class MathOp:
    def add(self, a, b, c=0):
        return a + b + c

m = MathOp()
print(m.add(2, 3))    # 5
print(m.add(2, 3, 4)) # 9
```

**Problem 39: Simulate method overloading using `*args`.**
```python
class MultiAdder:
    def add(self, *args):
        return sum(args)

ma = MultiAdder()
print(ma.add(1, 2, 3, 4, 5)) # 15
```

**Problem 40: Overload indexing (`__getitem__` and `__setitem__`).**
```python
class CustomList:
    def __init__(self):
        self.data = {}
    def __setitem__(self, index, value):
        self.data[index] = value
    def __getitem__(self, index):
        return self.data.get(index, None)

cl = CustomList()
cl[0] = "Python"
print(cl[0]) # Python
```

## Section 5: Abstraction, Class Methods, & Advanced OOP

**Problem 41: Create an Abstract Base Class (ABC).**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# s = Shape() # Raises TypeError: Can't instantiate abstract class
```

**Problem 42: Inherit from an Abstract Base Class.**
```python
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self): # Must implement area
        return self.side * self.side

sq = Square(4)
print(sq.area())
```

**Problem 43: Create a class method using `@classmethod`.**
```python
class Employee:
    company = "Tech Corp"
    
    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

Employee.change_company("InnoTech")
print(Employee.company)
```

**Problem 44: Create a static method using `@staticmethod`.**
```python
class MathUtils:
    @staticmethod
    def is_even(num):
        return num % 2 == 0

print(MathUtils.is_even(10)) # True, doesn't require instance or class reference
```

**Problem 45: Use `@classmethod` as an alternative constructor (Factory Method).**
```python
class Date:
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day
        
    @classmethod
    def from_string(cls, date_str):
        year, month, day = map(int, date_str.split('-'))
        return cls(year, month, day)

d = Date.from_string("2023-10-25")
print(d.year, d.month, d.day)
```

**Problem 46: Implement the Singleton Design Pattern.**
```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2) # True
```

**Problem 47: Implement Composition (Has-A relation).**
```python
class Engine:
    def start(self): print("Engine starts")

class Car:
    def __init__(self):
        self.engine = Engine() # Car strongly owns Engine
    def start(self):
        self.engine.start()

car = Car()
car.start()
```

**Problem 48: Implement Aggregation (Weak Has-A relation).**
```python
class Professor:
    def __init__(self, name): self.name = name

class Department:
    def __init__(self, prof):
        self.prof = prof # Department uses Professor, but Professor exists independently

prof = Professor("Dr. Smith")
cs_dept = Department(prof)
```

**Problem 49: Create a Custom Exception Class.**
```python
class NegativeAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeError("Age cannot be negative")
    print(f"Age is {age}")

try:
    set_age(-5)
except NegativeAgeError as e:
    print(e)
```

**Problem 50: Use `__call__` to make an object callable like a function.**
```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    def __call__(self, val):
        return val * self.factor

times_three = Multiplier(3)
print(times_three(10)) # Output: 30
```
