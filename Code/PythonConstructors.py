"""
Created on 24 Aug, 2021

@author: Sai Vikhyath
"""

"""
__init__ is a reserved method in python classes
It is called as a constructor in object oriented terminology
The method is called when an object is created from a class
and it allows the class to initialize the attributes of the class
'self' keyword represents the instance of a class
The 'self' keyword allows to access the attributes and methods of the class in python
"""


class Rectangle:

    def __init__(self, length, breadth, unit_cost=10):
        self.length = length
        self.breadth = breadth
        self.unit_cost = unit_cost

    def get_area(self):
        return self.length * self.breadth

    def calculate_cost(self):
        # area = self.get_area()
        return self.get_area() * self.unit_cost


rect = Rectangle(120, 100)
print(rect.get_area())
print(rect.calculate_cost())