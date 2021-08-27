"""
Created on 23 Aug, 2021

@author : Sai Vikhyath
"""

"""
Conditional statements if, elif and else are demonstrated 
"""

# Simple if statements
var1 = 1
if var1:
    print("True")
    print(var1)

var1 = 0
if var1:
    print("True")
    print(var1)

# If, elif and else statements
x = 5
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')

print("Using Conditionals in Python")


# Invoking functions inside conditional blocks
def do_fn1():
    print("Inside fn1")


def do_fn2():
    print("Inside fn2")


def do_fn3():
    print("Inside fn3")


def do_fnDefault():
    print("Inside Default Function")


num10 = 15
if num10 == 1:
    do_fn1()
elif num10 == 2:
    do_fn2()
elif num10 == 3:
    do_fn3()
else:
    do_fnDefault()


def do_fnResultsDefault():
    print("Result Not Released, Contact Registrar")


if (num10 is not None) and (num10 < 30):
    print("Fail")
elif (num10 >= 30) and (num10 < 45):
    print("Pass")
elif (num10 >= 45) and (num10 < 60):
    print("2nd Class")
elif (num10 >= 60) and (num10 < 75):
    print("1st Class")
elif num10 >= 75:
    print("Distinction")
else:
    do_fnResultsDefault()

# Single Statement Suites
backLogStatus = "Yes"
num10 = 29
if (num10 == 29) and (backLogStatus == "Yes"): print("not promoted")
