"""
Created on 25 Aug, 2021

@author: Sai Vikhyath
"""

"""
Demonstrating Map, Filter and Reduce along with Lambda's
"""


def square(x): return x * x  # Square method


def callerToFunc(q, x): return q(x)


# Python is a first class citizen
print(callerToFunc(square, 25))  # Method name can be passed as parameter

n = 0


def make_incrementor(n):
    return lambda x: x + n  # Lambda's are used when different values are to be returned


f = make_incrementor(42)
print(f(0))
# print(f(1))
print(f(5))


# Without using lambdas
def starts_with_A(s):
    return s[0] == "A"


fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange", '123']
map_object = map(starts_with_A, fruit)

print(list(map_object))

# With using lambdas
lambda s: s[0] == "A"
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]

# Map
map_object = map(lambda s: s[0] == "A", fruit)
print("map", list(map_object))

# Filter
# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(lambda s: s[0] == "A", fruit)
print("filter", list(filter_object))

nums = [0, 4, 7, 2, 1, 0, 9, 3, 5, 6, 8, 0, 3]
nums = list(filter(lambda x: x != 0, nums))
print(nums)  # [4, 7, 2, 1, 9, 3, 5, 6, 8, 3]

from functools import reduce  # Importing reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8]
nums = list(reduce(lambda x, y: (x, y), nums))
print(nums)  # (((((((1, 2), 3), 4), 5), 6), 7), 8)

# Reduce
list1 = [2, 4, 7, 3]
print(reduce(lambda x, y: x + y, list1))
print("With an initial value: " + str(reduce(lambda x, y: x + y, list1, 10)))


def add1(x): return x + 1


def odd(x): return x % 2 == 1


def add(x, y): return x + y


print(list(map(add1, [1, 2, 3, 4])))  # [2, 3, 4, 5]
# map(+,[1,2,3,4],[100,200,300,400]) #map(+,[1,2,3,4],[100,200,300,400]) SyntaxError: invalid syntax
print(list(map(add, [1, 2, 3, 4], [100, 200, 300, 400])))  # [101, 202, 303, 404]
print(reduce(add, [1, 2, 3, 4]))  # 10
print(list(filter(odd, [1, 2, 3, 4])))  # [1, 3]
