"""
Created on 24 Aug, 2021

@author : Sai Vikhyath
"""

import math

"""
Implementing Overriding in python
Define method with same name in super class and sub class
Method Overloading is an example of Compile time polymorphism.
More than one method of the same class shares same method name having different signatures.
Method overloading is used to add more to behaviour of methods and 
there is no need of more than one class for method overloading.
Note: Python does not support method overloading.
Overloading the methods only use latest defined method

Method overriding is an example of run time polymorphism
Implementation of method IN parent class is implemented and altered in child class

So to say, Parent Class Method is Customised in Child Class

Used to change the behaviour of existing methods and there is a need for at least two classes for
method overriding.
Method overriding, inheritance is required, it is done between parent class(superclass) and child
class(child class) methods
"""


class Shape:

    # Class constructor
    def __init__(self):
        print('call __init__ from shape class')

    def calculate_area(self):   # Method which will be overridden
        print('calling calculate_area() from shape class')
        return 0


class Circle(Shape):    # Sub class

    def __init__(self, r):
        print('call __init__ from circle class')
        self.r = r

    def calculate_area(self):   # Overriding Super class's method
        print('calling calculate_area() from circle class')
        return math.pi * self.r * self.r


class Rectangle(Shape):     # Sub class

    def __init__(self, l, w):
        print('call __init__ from rectangle class')
        self.l = l
        self.w = w

    def calculate_area(self):   # Overriding Super class's method
        print('calling calculate_area() from rectangle class')
        return self.l * self.w


a = Shape()     # Parent class object
area = a.calculate_area()
print('Area: ', area)

b = Circle(5)   # Child class object
area = b.calculate_area()
print('Area: ', area)

c = Rectangle(2, 3) # Child class object
area = c.calculate_area()
print('Area: ', area)
