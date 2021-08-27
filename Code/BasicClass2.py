"""
Created on 24 Aug, 2021

@author: Sai Vikhyath
"""

"""
class ClsOne: # Class Header { bk1
    clsVar = 10 # Class Variable

    def __init__(self):


    def methodOne(self, param1, param2): # Method Header { ck1
        localVar = 10 # local variable
        return localVar * 23
    # } ck1 - Method Body

    clsVar2 = 20 # Class Variable
# } bk1 - Class Body
"""


class ClsTwo:  # Class declaration
    def methodTwo(self):
        pass


class ClsOne:
    def set_age(self, num):
        return lambda num: num >= 18, print("allowed to vote")  # Lambda function


x = ClsOne()  # Class Instance, Object
x.set_age(23)


class Dog:
    clsVar1 = 20
    clsVar2 = 40

    def __init__(self, breed, available):  # Class constructor
        self.breed = breed
        self.available = available

    def show(self):
        print("Breed {0} is available: {1} ".format(self.breed, self.available))


pitBull = Dog("Pit Bull", False)
germanShepherd = Dog("German Shepherd", True)

pitBull.clsVar1 = 75
germanShepherd.clsVar1 = 100

print(Dog.clsVar1)

pitBull.show()
germanShepherd.show()


# self in Python is similar to this
# self is accessible inside a class
class ScopeOfSelf:
    def __init__(self, fullName):
        self.name = fullName

    def get_full_name(self):
        return self.name

    def get_age(self, age):
        return self.name, age


scopeSelf = ScopeOfSelf("John Doe")
print(scopeSelf.get_full_name())
print(scopeSelf.get_age(32), type(scopeSelf.get_age(32)))


# Accessing attributes and methods
class student:
    def __init__(self, fullName, age):
        self.full_name = fullName
        self.age = age

    def get_age(self):
        return self.age


studentObject = student("Jane Doe", 23)
# print(studentObject.full_name)  # Accessing attribute
# print(studentObject.get_age())  # Accessing method

# When name of an attribute or method is only given at run time
print(getattr(studentObject, "full_name"))
print(getattr(studentObject, "get_age"))
print(getattr(studentObject, "get_age")())  # call it
# print(getattr(studentObject, "get_birthday"))
print(hasattr(studentObject, "get_birthday"))

print("done")
