"""
Created on 24 Aug, 2021

@author: Sai Vikhyath
"""

"""
Variables at the class level are referred to as class variables
Variables at the object level are called instance variables
"""


# Instances and Data Attributes
class Teacher:
    def __init__(self, full_name):
        self.full_name = full_name

    def print_name(self):
        print(self.full_name)


obj = Teacher("John Doe")
print(obj.print_name())


# Class Attributes
class BasicClass:  # Class Name
    # Class Variables Go Here
    clsVar1 = 100
    print("In class variable definition section", clsVar1)

    # A sample method        # Class Method
    def func(self, aStr=""):  # aStr is an Instance variable
        # Variables local to method Go here
        methodVar1 = 200
        print("Hello")
        print(aStr)  # is
        print(self.clsVar1)  # Access Class Variable

        print(methodVar1)  # Accessing method variable locally

        print(clsVar)

        print(self.clsVar1)


clsVar = 33
print(clsVar)
obj = BasicClass()  # Create Object / Instance of Class
obj.func()  # Use the Instance of the Class to Call method inside the Class
obj.func("Hello Python")  # Access Instance Variables

# print(BasicClass.func(""))

# print(methodVar1)  # Prompts Undefined Variable
print("In class but accessibility section", BasicClass.clsVar1)  # Prompts Undefined Variable
