"""
Created on 24 Dec 2020

@author: rameshsrao
"""

"""To illustrate Parametrised Constructor and use of Default and Keyword arguments"""


class Person(object):

        def __init__(self, fname=" John", lname=" Doe", age=" 40"):     # Default parameters
                self.fname = fname
                self.lname = lname
                self.age = age

        def talk(self):
                print("Hi, I am ", self.fname + self.lname + self.age)

        def __str__(self):
                return "Hi, I am " + self.fname + self.lname + self.age


withParametersPassed = Person(age=" forever 20", fname="Peter ")
print(withParametersPassed)
print(Person())

noParametersPassed = Person()
print(noParametersPassed)

print(Person(lname="Parker", fname="Peter ", age=" forever 20"))
print(Person(age="asd", fname="dfg", lname="hjk"))