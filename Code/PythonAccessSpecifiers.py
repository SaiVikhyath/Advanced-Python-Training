"""
Created on 24 Aug, 2021

@author: Sai Vikhyath
"""

"""
PUBLIC - All data members and member functions of a class are public by default
PROTECTED - Data members and member functions declared as protected are accessible only to that class and children
PRIVATE - Data members and member functions declared as private are accessible to only that class
"""


class PublicClassEx:

    def __init__(self, name, age):
        # public data members
        self.publClassName = name
        self.publClassAge = age

    # public member function
    def displayAge(self):
        # accessing public data member
        print("Age: ", self.publClassAge)


# creating object of the class
obj = PublicClassEx("Dr. Gru", 20)

# accessing public data member
print("Name: ", obj.publClassName)

# calling public member function of the class
obj.displayAge()
print("Public Class End")

"""
PROTECTED - Protected are only accessible to a class derived from it
Declared by prefixing with a single underscore
"""


# super class or parent class
class ProtectedClassEx:  # Class for Object Student

    # Protected data members
    _name = None  # single underscore to declare member as protected
    _roll = None
    _branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch

    # Protected member function
    def _displayRollAndBranch(self):
        # accessing protected data members
        print("Roll: ", self._roll)
        print("Branch: ", self._branch)


# Derived class or inheriting class
class DeriveFromProtectedClassEx(ProtectedClassEx):

    # constructor
    def __init__(self, name, roll, branch):
        ProtectedClassEx.__init__(self, name, roll, branch)

    # Public member function
    def displayDetails(self):
        # accessing protected data members of super class
        print("Name: ", self._name)

        # accessing protected member functions of super class
        self._displayRollAndBranch()


# Creating objects of the derived class
obj = DeriveFromProtectedClassEx("Dr. Gru", 32, "Mechanical Engineering")

# Calling public member functions of the class
obj.displayDetails()

print("End of Protected")


"""
PRIVATE - Private are accessible within the class only, private access modifier is the most secure access modifier
Declared by prefixing with double underscore
"""


class PrivateClassEx:
    # Private members
    __name = None  # Double underscore to declare member as private
    __roll = None
    __branch = None

    # Constructor
    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch

    # Private member function
    def __displayDetails(self):
        # Accessing private data members
        print("Name: ", self.__name)
        print("Roll: ", self.__roll)
        print("Branch: ", self.__branch)

    # Public member function
    def accessPrivateFunction(self):
        # accessing private member function
        self.__displayDetails()


# Creating object
obj = PrivateClassEx("Dr. Gru", 32, "Mechanical Engineering")

# Calling public member function of the class
# obj.__displayDetails()    # No attribute error
# obj.__name    # No attribute error

print("Done")
