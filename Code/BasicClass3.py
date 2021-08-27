"""
Created on 24 Aug, 2021

@author: Sai Vikhyath
"""

# Constructor is used for initialising instance members when object of a class is created


class ParentClass:

    # Constructor : To declare a constructor use def keyword, def stands for definition

    # A default constructor exists when it is not defined explicitly
    # Injected by python during program compilation or an empty constructor without a body can be created

    # def default_constructor(self):
    # Non-parameterised constructors exist
    # Parameterised constructors exist

    # Python does not have constructor overloading

    # __init__ is a non-parameterised constructor as below

    def __init__(self):

        # Below the def, all indented lines are the BODY of the Constructor
        # Initialising instance variable

        self.name = "Gru"

    # Some method
    def read_number(self):
        print(self.name)


# Creating object of class, invokes constructor
obj1 = obj2 = ParentClass()
# obj2 = ParentClass()

# calling the instance method using the object obj1
obj1.read_number()
obj2.read_number()
