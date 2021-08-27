"""
Created on 24 Aug, 2021

@author : Sai Vikhyath
"""

"""
Demonstrating operator overloading in python
Python doesn't support method overloading
Python does support operator overloading
Python allows to overload all existing operators but not create a new operator
Python provides special functions that is auto invoked that it is associated with that particular operator
Example, when using + operator, __add__ is automatically invoked
Changing the behaviour of operator is as simple as changing behaviour of method or function
"""


# Overload an binary + operator
class ClassOne:

    def __init__(self, initObj1):
        self.initObj1 = initObj1

    # Adding two objects
    def __add__(self, addObj1):
        # ToDo
        return self.initObj1 + addObj1.initObj1


binOp1 = ClassOne(32)
binOp2 = ClassOne(100)
binOp3 = ClassOne("Dr. Gru")
binOp4 = ClassOne(" Stole the Moon")

print(binOp1 + binOp2)  # Addition is performed
print(binOp3 + binOp4)  # Concatenation is performed


# Overload an addition + operator to perform complex number addition
class ClassTwo:

    def __init__(self, initObj1, initObj2):
        self.initObj1 = initObj1
        self.initObj2 = initObj2

    # Adding two objects
    def __add__(self, addObj1):
        return self.initObj1 + addObj1.initObj1, self.initObj2 + addObj1.initObj2

    def __str__(self):
        return self.initObj1, self.initObj2


cmpOp1 = ClassTwo(10, (10 + 5j))
cmpOp2 = ClassTwo(10, (20 + 3j))
cmpOp3 = cmpOp1 + cmpOp2

print(cmpOp3)   # Addition of complex number through operator overloading

cmp1 = 10 + (10 + 20j)
cmp2 = 30 + (20 + 30j)
print(cmp1 + cmp2)  # Complex numbers addition


# Overload comparison operators
class ClassThree:

    def __init__(self, initObj1):
        self.initObj1 = initObj1

    def __gt__(self, cmpr1):  # Greater Than Special Method Of Python
        if self.initObj1 > cmpr1.initObj1:
            return True
        else:
            return False

    def __lt__(self, cmpr1):  # Less Than Special Method Of Python
        if self.initObj1 < cmpr1.initObj1:
            return "cmpr1 is less than cmpr2"
        else:
            return False

    def __eq__(self, cmpr1):  # Equality  Special Method Of Python
        if self.initObj1 == cmpr1.initObj1:
            return 1
        else:
            return 0


cmpr1 = ClassThree(300)
cmpr2 = ClassThree(30)

if cmpr1 > cmpr2:
    print("cmpr1 is greater than cmpr2")
elif cmpr1 < cmpr2:
    print("cmpr1 is lesser than cmpr2")
else:
    if cmpr1 == cmpr2:
        print("cmpr1 is equal to cmpr2")
