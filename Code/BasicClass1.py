"""
Created on 24 Aug, 2021

@author: Sai Vikhyath
"""


# Create a simple class
class BasicClass:  # Class Name
    # Class Variables Go here
    a = 0       # Variable assignment
    var1: int   # Variable declaration

    # Class Method Go here
    def func(self, aStr="Hello Word"):
        a = "hello"
        # Variables local to method Go here
        print("Hello")
        print(aStr)
        print("line 19", self.a)

    def func2(self):
        print(self.a)

    print(a)


obj1 = BasicClass()  # Create Object / Instance of Class
obj2 = BasicClass()
print(type(obj1))

obj1.func()  # Use the Instance of the Class created to Access / Call a method inside the Class
obj1.func("Hello Python")

obj1.var1 = 20
obj2.var1 = 30
# print("LINE 40", obj1.var1)
# print("LINE 41", obj2.var1)
# print(BasicClass.var1)    # Class members can be accessed this way, but is not recommended

'''
The self

Class methods must have an extra first parameter in method definition
We do not give a value for this parameter when we call the method
Python provides it
If we have a method which takes no arguments, then we still have to have one argument – the self
See func() in above simple example.
This is similar to this pointer in C++ and 'this' reference in Java

What really happens
calling method obj.func() with no arguments auto converted in Python to
obj.func() ==> BasicClass.func(basicClass)

BasicClass.func(basicClass)
calling method obj.func(args) with  arguments auto converted in Python to BasicClass.func(basicClass, args)

'''
