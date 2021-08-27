"""
Created on 24 Aug, 2021

@author : Sai Vikhyath
"""

"""
Create a simple program demonstrating Overriding
"""


class Parent:
    def printValue(self):
        a = 10; return a


class Child(Parent):
    def printValue(self):
        a = 30; return a


p = Parent()
c = Child()
print(p.printValue())
print(c.printValue())