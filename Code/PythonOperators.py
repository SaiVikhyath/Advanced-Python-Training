"""
Created on 23 Aug, 2021

@author : Sai Vikhyath
"""
# Always try avoiding *
# This affects performance as it imports all the modules and functions
from math import *
import cmath

"""
Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
"""

num1 = 2
num2 = 58.7

var1 = 10

var2 = 'as '
var3 = " string"

var4 = str(var1) + var2 + var3  # Cast and use a number in a string
print(var4)

var4 = var2 + var3  # Concatenation
print(var4)

var5 = 3.14
var4 = var1 + var5
print(var4)

''' Arithmetic Operations '''
print("Arithmetic Operations")
print(num1 + var1)
print(num1 + num2)
print(num1 * num2)
print(num1 / var1)
print(num2 / var1)

''' Mathematical Functions '''
print("Mathematical Functions included in math module")
print(pow(var1, num1))  # Exponential function
print(pow(num1, num2))

print(sqrt(num1))   # Square root
print(sqrt(num2))
print(sqrt(pow(var1, num1)))

print(sin(num2))    # Sine function

print(pi)   # Value of PI = 3.142

num3 = 10 + 5j  # Complex number
print(num3)
print("Real part of complex number is " + str(num3.real))
print("Imaginary part of complex number is " + str(num3.imag))

global gVar  # Global variable
gVar = 10
print(gVar)

''' Assignment Operations '''
print("Assignment Operations")
print("Increment and Decrement")

print("Assign First")
num1 = +1
num2 = -2
print(num1)
print(num2)

print("Solve First")
num1 += 1
num2 -= 2
print(num1)
print(num2)

num1 = 10
num2 = 5
print("Modulo OR Remainder")
print("Modulo of {1} and {0} is {2}, {3}".format(num1, num2, num2 % num1, type(num2 % num1)))

print("Floor Division")
print("line87", -2 // 5)

print("Floor division of {0} by {1} is {2}".format(5, -2, 5 // -2))

''' Comparison and Logical Operations '''
a = 3
b = 8

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

print("Using Conditionals in Python")


def do_fn1():
    print("Inside fn1")


def do_fn2():
    print("Inside fn2")


def do_fn3():
    print("Inside fn3")


def do_fnDefault():
    print("Inside Default Function")


num10 = 45
if num10 == 1: do_fn1()
elif num10 == 2: do_fn2()
elif num10 == 3: do_fn3()
else: do_fnDefault()


def do_fnResultsDefault():
    print("line 127 Result Not Released, Contact Registrar")


if(num10 is not None) and (num10 < 30): print("line 129 fail")
elif(num10 >= 30) and (num10 < 45): print("pass")
elif(num10 >= 45) and (num10 < 60): print("2nd Class")
elif(num10 >= 60) and (num10 < 75): print("1ST Class")
elif num10 >= 75: print("Distinction")
else: do_fnResultsDefault()

backLogStatus = "No"
num10 = 28
if(num10 == 29) and (backLogStatus != "Yes"): print("promoted")

''' Identity Operations '''


def funcChkIdentity(argOne, *argv):
    for arg in argv:
        if argOne is arg:
            print("{0} has same identity as {1}".format(argOne, arg))
        elif argOne is not arg:
            print("{0} does not have same identity as {1}".format(argOne, arg))
        else:
            print("{0} could not be compared to {1}".format(argOne, arg))


funcChkIdentity(10, 20, 30, 10, -10)

''' Membership Operations '''


def funcChkMembership(argOne, *argv):
    for arg in argv:
        if argOne in arg:
            print("{0} is contained in {1}".format(argOne, arg))
        elif argOne not in arg:
            print("{0} is not contained in {1}".format(argOne, arg))
        else:
            print("{0} could not be checked for existence in {1}".format(argOne, arg))


funcChkMembership(10, [20, 30, 10, -10], {30, 20, 40})
funcChkMembership('H', 'Hello World', {"30", "20", "40"})

''' Bitwise Operations '''

print("Bitwise shift")
print(5 << 2)  # Shift to left by 5 bits
print(bin(5 << 2))
print(bin(5 * 2 ** 2))
print(5 >> 2)  # Shift to right by 5 bits)
print(bin(5 >> 2))
print(bin(int(5 / 2 ** 2)))

aVar = 60  # binary of 60 = 0011 1100
bVar = 13  # binary of 13 = 0000 1101
cVar = 0
print(aVar, bVar, cVar)
# & copies a bit to the result if the bit exists in both operands
cVar = aVar & bVar  # Bitwise AND
print("{a} & {b} = {c} ".format(a=bin(aVar), b=bin(bVar), c=bin(cVar)))

# | copies a bit to the result if the bit exists in either operands
cVar = aVar | bVar  # Bitwise OR
print("{a} | {b} = {c} ".format(a=bin(aVar), b=bin(bVar), c=bin(cVar)))

# ^ copies the bit if it is set in one operand but not both
cVar = aVar ^ bVar  # Bitwise BI-IMPLICATION
print("{a} ^ {b} = {c} ".format(a=bin(aVar), b=bin(bVar), c=bin(cVar)))

# ~ Unary operator and flips bits
cVar = ~aVar
print("{c} ~ {a} ".format(a=bin(aVar), b=bin(bVar), c=bin(cVar)))

# << Binary Left Shift
cVar = aVar << 2
print("cVar is {c} = (aVar) {a} << {b} ".format(a=bin(aVar), b=2, c=bin(cVar)))

# >> Binary Right Shift
cVar = aVar >> 2
print("{c} = {a} >> {b} ".format(a=bin(aVar), b=2, c=bin(cVar)))


'''
Find roots of a quadratic equation
'''

print("Hello!  This is my quadratic equation program.")

a = int(input("What is a? "))
b = int(input("What is b? "))
c = int(input("What is c? "))

# Calculate the discriminant
d = (b ** 2) - (4 * a * c)

# Find the roots
root1 = (-b - cmath.sqrt(d)) / (2 * a)
root2 = (-b + cmath.sqrt(d)) / (2 * a)
print('The solution are {0} and {1}'.format(root1, root2))
print('Real part :', root1.real)
print('Imag part :', root1.imag)
print('Real part :', root2.real)
print('Imag part :', root2.imag)

num3 = 10 + 5 * cmath.sqrt(-1)  # complex number
print(num3)
print("real part of complex number is " + str(num3.real))
print("imaginary part of complex number is " + str(num3.imag))
