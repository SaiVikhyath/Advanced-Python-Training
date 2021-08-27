"""
Created on 23 Aug, 2021

@author : Sai Vikhyath
"""

"""
Program that implements variables in Python
Covers the concept involved with Python variables
"""

import math

# Variable names are case-sensitive
age = 5
print(age)
# print(Age) # Prompts 'Undefined variable'


# To specify data type of a variable use casting
m = str(math.pi)
n = int(math.pi)
o = float(math.pi)
print(math.pi)
print(m, n, o)
print(type(m), type(n), type(o))

# Variable declaration rules
this_is_a_valid_variable_name = "value1"
# 9_this_is_a_invalid_variable_name = ""  # Prompts an error message
_this_is_a_valid_variable_name = "value2"  # Not recommended as it is used for protected variables
print(this_is_a_valid_variable_name)
print(_this_is_a_valid_variable_name)

# Variable declaration using different case-notations
this_is_snake_case = "this_is_snake_case"
thisIsCamelCase = "thisIsCamelCase"
ThisIsPascalCase = "ThisIsPascalCase"
print(this_is_snake_case)
print(thisIsCamelCase)
print(ThisIsPascalCase)

# Variables assignment
singleAssignment = "John"  # Single variable assignment
math = chem = bio = phy = minPassing = 35  # Multiple variables assignment
print(math, chem, bio, phy, minPassing)
# math, chem, bio, phy, minPassing = 35 # Prompts TypeError: cannot unpack non-iterable int object
# print(math, chem, bio, phy, minPassing)

# The BEST TECHNIQUE
math, chem, bio, phy, minPassing = (24,) * 5  # Prompts TypeError: cannot unpack non-iterable int object
print(math, chem, bio, phy, minPassing)

# Global Variables
fruit = "apple"  # Global variable


def myfunc():
    x = "super fast"  # Local variable
    print("Python is " + x)  # Local variable is given priority


myfunc()
# print("Python is " + x) # Prompt Undefined variable x

y = "Nothing"  # Global variable


def myfunc2():
    global y  # Global Keyword to declare variable inside method
    x = "fantastic"
    print(x, y)
    y = x  # Changes the value of global variable


myfunc2()
print("Python is " + y)

global z  # Does not support Assignment on same line
z = "Global Variable"


def myfunc3():
    print("Inside myFunc3 " + z)


myfunc3()
print("Outside myFunc3 " + z)

# Dynamic typing in Python
print("Python is a Dynamically typed language")
num1 = 2  # Integer assigned
num2 = 58.7  # Float assigned
var1 = 10  # Integer assigned
var2 = 'as '  # String assigned
var3 = " string"  # String assigned

print("Dynamically typed language do not require Data Type Declaration")

print("Multiple declaration of Mixed Data Types is also valid")
var4, var5, var6 = 20, ' as ', " string"  # Multiple variables declaration with multiple values

print("Printing Multiple variables of Mixed Data Types is also allowed")
print(var4, var5, var6)

print("Adding a Numeral variable to String is allowed by Casting")
var4 = str(var1) + var2 + var3  # Casting is performed on var1
print("var4 which is originally containing Numeral is reused to store string")
print(var4)

print("Auto promoting a Numeral to its higher order is supported")
var5 = 3.14
var4 = var1 + var5  # var1 is promoted to Float implicitly
print("var5 is a float, var1 is integer = ", var4)

var7 = "Python is EASY"
print("The data type of a value in a variable is found using type = ", type(var7))  # type method
print("Length of var7 string is = ", len(var7))  # len method
print("A use a single character in a string, use var[index] = ", var7[7])  # Indexing on strings
print("Index begins from 0")  # Index starts from 0 in python
print("To use character in reverse order, use var[index-index]", var7[0 - 3])  # Reverse indexes is possible

print("To capitalise ", var7.capitalize())  # capitalize method
print("capitalise() converts first character of string to uppercase letter and all others to lowercase")
print("centre = ", var7.center(len(var7) + 10))  # center method
print("centre takes two parameters, length and the character to fill")
print("centre(size, fill with *) = ", var7.center(len(var7) + 10, "^"))
