"""
Created on 25 Aug, 2021

@author : Sai Vikhyath
"""

"""
Illustration of decorators in Python
"""


def methodOneDecorator(fnToDecorate):
    def wrapperToMethodOne():  # Wrapper method
        print("Before the function runs")  # Code to setup and base
        fnToDecorate()
        print("After the function runs")  # Code to teardown and clean

    return wrapperToMethodOne


def methodOne():
    # ToDo
    print("Code not to be changed")


methodOne()
decoratedMethodOne = methodOneDecorator(methodOne)
decoratedMethodOne()
print("done")


# Using Decorator annotation
@methodOneDecorator
def myMethod():
    print("Inside myMethod - Code to receive pull some data")


myMethod()


# Decorator build-up
def methodOne(first, second):
    return first + second


def methodTwo(func, first):
    def methodTwoWrapper(second):
        return func(first, second)

    return methodTwoWrapper


func = methodTwo(methodOne, 1)  # Pass a function and argument(s)
print(func(2))  # Pass to the function a second argument

# Function is called thrice for one task

func2 = methodTwo(methodOne, 3)
print(func2(2))


def methodNewOne(someFunc):
    def wrapper_function():
        print("Inside methodNewOne Wrapper")
        someFunc()
    return wrapper_function


def methodNewTwo(someFunc):
    def wrapper_function():
        print("Inside methodNewTwo Wrapper")
        someFunc()
    return wrapper_function


@methodNewOne
@methodNewTwo
def myFunc():  # myFunc is Decorated with two Decorators (/ or annotations)

    print("Inside myFunc")


myFunc()


def methodNewOne(someFunc):
    def wrapper_function(aStr="Decorator"):
        print("Inside methodNewOne Wrapper")
        someFunc(aStr)

    return wrapper_function


@methodNewOne
def myFunc(aStr="Decorator"):
    print("Inside myFunc")
    if aStr:
        print("Hello " + aStr)
    else:
        print("Hi")


myFunc()
myFunc("John Doe")


# To illustrate use of decorators in functions
def decorator(func):
    def wrapper():  # wrapper is a closure over func
        print('in wrapper()')
        return func()

    return wrapper


@decorator
def my_function():
    print('in my_function()')


my_function()


# To illustrate use of decorators in class
class Decorator:

    def __init__(self, func):
        self.func = func

    def __call__(self):
        print('in __call__()')
        return self.func()


@Decorator
def my_function():
    print('in my_function()')


my_function()


# To illustrate use of decorators with arguments
def decorator(*args, **kwargs):
    def receiver(func):
        def wrapper():
            print('in wrapper()')
            print(args)
            print(kwargs)
            return func()

        return wrapper

    return receiver


@decorator(1, config='value')
def my_function():
    print('in my_function()')


my_function()
