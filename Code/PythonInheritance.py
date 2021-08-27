"""
Created on 24 Aug, 2021

@author : Sai Vikhyath
"""

"""
Base class / Super class: A class on which another can depend; it is inherited by a derived class
Derived class inherits base class
"""


# Base class or Super class
class Animal:
    def __init__(self, name):  # Constructor
        self.name = name

    def get_name(self):
        return self.name


# Derived class or Child class inheriting Animal super class
class Cat(Animal):
    def talk(self):
        return 'Meow!'


# Derived class or Child class inheriting Animal super class
class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'


animals = [Cat('Pussy'), Cat('Spots'), Dog('Johnny')]   # Class objects

for animal in animals:
    print(animal.talk() + ' I am ' + animal.get_name())
