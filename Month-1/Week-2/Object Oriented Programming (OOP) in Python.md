# Object Oriented Programming
Python is a multi-paradigm programming language. It supports different programming approaches.

One of the popular approaches to solve a programming problem is by creating objects. This is known as Object-Oriented Programming (OOP).

An object has two characteristics:

* attributes
* behavior
### Let's take an example:

A parrot is an object, as it has the following properties:

name, age, color as attributes
singing, dancing as behavior
The concept of OOP in Python focuses on creating reusable code. This concept is also known as DRY (Don't Repeat Yourself).

#### In Python, the concept of OOP follows some basic principles:

## Class
A class is a blueprint for the object.
We can think of class as a sketch of a parrot with labels. It contains all the details about the name, colors, size etc.
````python
class Parrot:
    pass
````
## Object
An object (instance) is an instantiation of a class. When class is defined, only the description for the object is defined. Therefore, no memory or storage is allocated.

### The example for object of parrot class can be:
````python
obj = Parrot()
````
## Example 1: Creating Class and Object in Python
````python
class Parrot:

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the attributes
print("First Parrot name is " + str((blu.name)) + " and is " + str((blu.age)) + " years old." )
print("Second Parrot name is " + str((woo.name)) + " and is " + str((woo.age)) + " years old." )

````
## Methods
Methods are functions defined inside the body of a class. They are used to define the behaviors of an object.
## Example 2 : Creating Methods in Python

````python
class Parrot:
    
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def sing(self, song):
        return (str(self.name)) + " sings " + str((song))
    
    def dance(self):
        return (str(self.name)) + " is now dancing. "     
# instantiate the object
blu = Parrot("Blu", 10)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())
````
## Inheritance
Inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).
## Example 3: Use of Inheritance in Python

````python
# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.run()
#calling Parent Function
peggy.swim()
````
In the above program, we created two classes i.e. Bird (parent class) and Penguin (child class). The child class inherits the functions of parent class. We can see this from the swim() method.Again, the child class modified the behavior of the parent class. We can see this from the whoisThis() method. Furthermore, we extend the functions of the parent class, by creating a new run() method.

## Encapsulation
Using OOP in Python, we can restrict access to methods and variables. This prevents data from direct modification which is called encapsulation. In Python, we denote private attributes using underscore as the prefix i.e single _ or double __.
## Example 4: Data Encapsulation in Python

````python
class Computer:

    def __init__(self):
      #private Attribute
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: " + str(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()
````
In the above program, we defined a Computer class.
We used __init__() method to store the maximum selling price of Computer.Here, we have tried to modify the value of __maxprice outside of the class. However, since __maxprice is a private variable, this modification is not seen on the output.As shown, to change the value, we have to use a setter function i.e setMaxPrice() which takes price as a parameter.

## Polymorphism
Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).
Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle). However we could use the same method to color any shape. This concept is called Polymorphism.
## Example 5: Using Polymorphism in Python

````python
class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def swim_test(bird):
    bird.swim()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
swim_test(blu)
swim_test(peggy)
````
In the above program, we defined two classes Parrot and Penguin. Each of them have a common fly() method. However, their functions are different.
To use polymorphism, we created a common interface i.e flying_test() function that takes any object and calls the object's fly() method. Thus, when we passed the blu and peggy objects in the flying_test() function, it ran effectively.
