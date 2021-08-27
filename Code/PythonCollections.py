"""
Created on 23 Aug, 2021

@author : Sai Vikhyath
"""

"""
Demonstrating Python Collections
Lists - List is a collection of homogeneous or heterogeneous data. Lists are mutable
Sets  - Set is a ordered collection of data. No duplicates. Sets do not support indexing
Tuples - Tuple is a immutable collection of data
Dictionaries - Dictionary comprises of a key, value pair of data.
"""

# List creation
l = [2, 3, 4]
print(l[0])  # 2

# Append - Insert at the end of the list
l.append(7)  # [1, 2, 3, 7]
l.append(["d", "e", "f"])  # [2, 3, 4, 7, ['d', 'e', 'f']]

# Extend - Append another list
l.extend(["d", "e", "f"])  # [2, 3, 4, 7, ['d', 'e', 'f'], 'd', 'e', 'f’]

# Insert - Insert at an index
l.insert(6, "x")  # [2, 3, 4, 7, ['d', 'e', 'f'], 'd', 'x', 'e', 'f']

# Remove - Remove the element
l.remove("x")  # [2, 3, 4, 7, ['d', 'e', 'f'], 'd', 'e', 'f']

# Pop - Remove last element
l.pop()  # f

# Index - Return the index
print(l.index("d"))  # 5
print(l[4])  # ['d', 'e', 'f']
print(l[4][0])  # 'd'
print(l[4][1])  # 'e'
print(l[5])  # 'd'

# Count - Count the occurrence
l.count("d")  # 1

# Sort - Sort the list
# l.sort() # Error - Must be homogeneous
# l.sort(reverse=True) # Error - Must be homogeneous

# Reverse - Reverse the list
l.reverse()  # ['e', 'd', ['d', 'e', 'f'], 7, 4, 3, 2]

# Extend or + serves the same purpose
l += [2]  # ['e', 'd', ['d', 'e', 'f'], 7, 4, 3, 2, 2]

# * => to create similar values list
l_new = [1, 2]  # [1, 2]
l_new = l_new * 2  # [1, 2, 1, 2]

# Slicing
# list[first index:last index:step]
list_new = [1, 2, 3, 4, 5]  # [1, 2, 3, 4, 5]
list[:]
list_new[2:]  # [3, 4, 5]
list_new[:2]  # [1, 2]
list_new[1:1]  # []
list_new[1:2]  # [2]
list_new[:]  # [1, 2, 3, 4, 5]

# Comprehension
# Without comprehension
evens = []
for i in range(10):
    if i % 2 == 0:
        evens.append(i)
evens  # [0, 2, 4, 6, 8]

# With comprehension - Always efficient practice
[i for i in range(10) if i % 2 == 0]  # [0, 2, 4, 6, 8]

# Filtering Lists
li = [3, 7]
[e * 2 for e in li if e > 2]  # [6, 14]

# List as Queue (FIFO)
lque = ['a', 'b', 'c', 'd', 'e']  # ['a', 'b', 'c', 'd']
lque.pop()  # 'e’

# List as Stack (LIFO)
lstak = ['a', 'b', 'c', 'd', 'e', 'f']  # ['a’, 'b', 'c', 'd']
lstak.pop()  # 'f'
lstak  # ['a', 'b', 'c', 'd', 'e']
lstak.pop()  # 'e'
lstak  # ['a', 'b', 'c', 'd']

"""
Shallow copy - List objects refer to same memory
So, changing one list affects the other list.
Deep copy - List objects have different copies
So, changing one list does not affect the other list.
"""
# Copy a list
# Shallow copy => nested objects not copied
a = [1, 2, [3, 4]]
b = a[:]  # [1, 2, [3, 4]]
a[2][0] = 10  # [1, 2, [10, 4]]
b  # [1, 2, [10, 4]]

import copy

a = [1, 2, [3, 4]]
b = copy.deepcopy(a)  # [1, 2, [3, 4]]  # Deep copy
a[2][0] = 10  # [1, 2, [10, 4]]
b  # [1, 2, [3, 4]]


# Insert into sorted List
# bisect => supported in bisect methods
lstak = ['f, l', 'g', 'a', 'e']  # ['f, l', 'g', 'a', 'e']
lstak.sort()  # ['a', 'e', 'f, l', 'g']
lstak = ['f', 'l', 'g', 'a', 'e']

lstak = ['f', 'l', 'g', 'a', 'e']  # ['f’, 'l', 'g', 'a', 'e']
lstak.sort()  # ['a', 'e', 'f', 'g', 'l']
import bisect

bisect.insort(lstak, 'c')  # ['a', 'c', 'e', 'f', 'g', 'l']
bisect.bisect(lstak, 'c')  # 2
lstak  # ['a', 'c', 'e', 'f', 'g', 'l']


# Set creation
l = {2, 3, 4}
mySet = set('2')
mySet = set(['2', 3])  # {3, '2'}
# l[0] # Not Supported, Indexing & Slicing

# Add
l.add(7)  # [2, 3, 4, 7]
# l.add(["d", "e", "f"]) # Error - unhashable type: 'list'

# Remove, Clear
# l.remove("4") # {2, 3, 7}
l.discard(3)  # {2, 7}
l = {1, 2, 3, 4}
l.pop()  # 1

l.clear()  # set()

# len, in
len(l)  # 3
print(3 in l)  # True

# Transform set into ordered values
l = {10, 20, 50, 30}
l  # {10, 20, 50, 30}
sorted(l)  # [10, 20, 30, 50]
sorted(l, reverse=True)  # [50, 30, 20, 10]

# Union, Intersection, Unique, Disjoint
l = {2, 3, 4};
l2 = {3, 7, 5}
l.union(l2)  # {2, 3, 4, 5, 7}
print(l | l2)  # {2, 3, 4, 5, 7}

l.intersection(l2)  # {3}
print(l & l2)  # {3}

print(l.difference(l2))  # {2, 4}
print(l - l2)  # {2, 4}
print(l2 - l)  # {5, 7}
print(l.symmetric_difference(l2))  # {2, 4, 5, 7} (l ^ l2)
print(l.issuperset(l2))  # False (l > l2 or l >= l2)
print(l.symmetric_difference(l2))  # {2, 4, 5, 7}
print(l.isdisjoint(l2))  # False
print(l.issubset(l2))  # False (l <= l2 or l < l2)

# Tuple is immutable

# Similar to List but faster
t = (2, 3, 4)  # (2, 3, 4)
print(t[0])  # 2
t_new = 2, 3, 4  # (2, 3, 4)
print(t_new[0])  # 2

# Single Element Tuple
t_singlevalue = (7)  # 7
print(type(t_singlevalue))  # <class 'int’>
t_singlevalue = (7,)  # 7
t_singlevalue = (7,)  # (7,)
print(type(t_singlevalue))  # <class 'tuple'>

# Repeat tuple element with multiplication
t = (7,) * 5  # (7, 7, 7, 7, 7)

# Concat Tuple element
tconcat = (8,)  # (8,)
tconcat += (2, 3, 9)  # (8, 2, 3, 9)
tconcat += 2, 3, 9  # (8, 2, 3, 9, 2, 3, 9)  # appends
tconcat *= (2)  # (8, 2, 3, 9, 2, 3, 9, 8, 2, 3, 9, 2, 3, 9)  # duplicates

# Tuple
# methods - index, count, len
print(tconcat.count(8))  # 2
print(tconcat.count(9))  # 4
# tconcat.index(0) # ValueError: tuple.index(x): x not in tuple
print(tconcat.index(9))  # 3
print(len(t))  # 5

# Tuple methods - count duplicates
tconcat  # (8, 2, 3, 9, 2, 3, 9, 8, 2, 3, 9, 2, 3, 9)


# Using List Comprehension
def dups(lst, item):
    return [i for i, x in enumerate(lst) if x == item]


print(dups(tconcat, 9))  # [3, 6, 10, 13]
print(dups(tconcat, 8))  # [0, 7]

# Using more_itertools.locate with lambda
from more_itertools import locate

list(locate(tconcat, lambda a: a == 9))  # [3, 6, 10, 13]

# Tuples in Dictionary
dictT = dict([('jan', 1), ('feb', 2), ('dec', 12)])
print(dictT['dec'])  # 12

# Single Value \ Single Assigned
(a, b, c, r1, r2) = (14, 2, 2, 1, 2)
a  # 14
r2  # 2

# Tuple Unpacking
quadEqn = (22, 2, 2, 4, 7)
(a, b, c, r1, r2) = quadEqn
print(a)  # 22
print(r1)  # 4
print(r2)  # 7


# Tuple for swap
def swap(r1, r2):
    (r1, r2) = (r2, r1)


print(r1)  # 7
print(r2)  # 4
swap(r1, r2)  # r1: 7;    r2: 4
# pass by value NOT reference

# Using Tuple
(r1, r2) = (r2, r1)  # r1: 4;    r2: 7

# Tuple to string
print(str(r1))  # '4’

# Tuple comparison
print(max(tconcat))  # 9, min is available

# Tuples more methods
print(len(tconcat))  # 28 # length of tuple

print(len(tconcat[2:]))  # 26 # slicing tuple w/o data change

t  # (7, 7, 7, 7, 7)
print(t_new)  # (2, 3, 4)
t = t_new
print(t)  # (2, 3, 4) # copying using = assignment

t = (1, 2, 3, 4, 5)
t_new = t[2:]  # (3, 4, 5) # copy with slicing

# Tuple Immutable !!
t = (2, 3, [4, 5])  # (2, 3, [4, 5])
# t[0] = 9  # error: 'tuple' object does not support item assignment
t[2][0] = 9  # (2, 3, [9, 5])

# Dictionary
d = {'jan': 1, 'feb': 2, 'dec': 12}  # {'jan’: 1, 'feb': 2, 'dec': 12}
print(d.keys())  # dict_keys(['jan', 'feb', 'dec'])
print(d.values())  # dict_values([1, 2, 12])
print(d['jan'])  # 1
print(d.items())  # dict_items([('jan’, 1), ('feb', 2), ('dec', 12)])

if 'dec' in d: print(d['dec'])  # 12

print(d.get('feb'))  # 2
print(d.pop('feb'))  # 2 # removes mentioned item not LIFO
print(d)  # {'jan': 1, 'dec': 12}

# Duplicate keys not allowed
# Order of elements NOT supported

# popitem
d = {'first': 'string value', 'second': [1, 2], 'third': a}
d.popitem()  # ('third’, 22)
print(d)  # {'first': 'string value', 'second': [1, 2]}
d.popitem()  # ('second', [1, 2])
print(d)  # {'first': 'string value’}

# Create new Dictionary
d1 = {'a': [1, 2]}
d2 = d1  # {'a': [1, 2]}
print(d1)  # {'a': [1, 2]}
print(d2['a'])  # [1, 2]
d2['a'] = [1, 2, 3, 4]
print(d1)  # {'a': [1, 2, 3, 4]} # Dictionaries are objects
print(d2)  # {'a': [1, 2, 3, 4]}

# Dictionary create new object =>
# copy, shallow copy, deep copy
# copy
d1 = {'a': [1, 2]}
d2 = d1
print(d1)  # {'a’: [1, 2]}
print(d2)  # {'a': [1, 2]}
print(id(d2) == id(d1))  # True
print(id(d2['a']) == id(d1['a']))  # True

# shallow copy; change in copy changes original
import copy

d2 = copy.copy(d1)
d2  # {'a': [1, 2]}
print(id(d2) == id(d1))  # False, d2 is new object
print(id(d2['a']) == id(d1['a']))  # True, a is same object

d2['a'] = [1, 2, 3, 4]
print(d1)  # {'a': [1, 2]}
print(id(d2['a']) == id(d1['a']))  # False
print(d2.values())  # dict_values([[1, 2, 3, 4]])
print(d1.values())  # dict_values([[1, 2]])

# deep copy, deep copied dictionary has no impact on original dictionary because its a deep copy
d2 = copy.deepcopy(d1)
print(id(d2) == id(d1))  # False, new object
print(id(d2['a']) == id(d1['a']))  # False, new object
print(d2)  # {'a': [1, 2]}
d2['a'] = [1, 2, 3, 4]
print(d1)  # {'a': [1, 2]}
print(d2)  # {'a': [1, 2, 3, 4]}

# Dictionary create new object =>
# copy, shallow copy, deep copy
# copy
d1 = {'a': [1, 2]}
d2 = d1
print(d1)  # {'a’: [1, 2]}
print(d2)  # {'a': [1, 2]}
print(id(d2) == id(d1))  # True
print(id(d2['a']) == id(d1['a']))  # True

# shallow copy; change in copy changes original
import copy

d2 = copy.copy(d1)
d2  # {'a': [1, 2]}
print(id(d2) == id(d1))  # False, d2 is new object
print(id(d2['a']) == id(d1['a']))  # True, a is same object

d2['a'] = [1, 2, 3, 4]
print(d1)  # {'a': [1, 2]}
print(id(d2['a']) == id(d1['a']))  # False
print(d2.values())  # dict_values([[1, 2, 3, 4]])
print(d1.values())  # dict_values([[1, 2]])

# deep copy, deep copied dictionary has no impact on original dictionary because its a deep copy
d2 = copy.deepcopy(d1)
print(id(d2) == id(d1))  # False, new object
print(id(d2['a']) == id(d1['a']))  # False, new object
print(d2)  # {'a': [1, 2]}
d2['a'] = [1, 2, 3, 4]
print(d1)  # {'a': [1, 2]}
print(d2)  # {'a': [1, 2, 3, 4]}

# Dictionary more methods
# clear, removes all elements
print(d2)  # {'a': [1, 2, 3, 4]}
d2.clear()  # {}
d2 = d1

# delete, deletes one item pair
d2 = {'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8]}
d2  # {'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8]}
del d2['a']  # {'b': [5, 6, 7, 8]}

# combine dictionaries
d1 = {'a': [1, 2, 4, 8], 'b': [2, 4, 6, 8]}  # {'a’: [1, 2, 4, 8], 'b': [2, 4, 6, 8]}
d2 = {'a': [1, 2, 3, 4], 'b': [2, 4, 6, 8]}  # {'a’: [1, 2, 3, 4], 'b': [2, 4, 6, 8]}
d2.update(d1)  # d2 update to d1
print(d2)  # {'a': [1, 2, 4, 8], 'b': [2, 4, 6, 8]}
print(d1)  # {'a': [1, 2, 4, 8], 'b': [2, 4, 6, 8]}

# iterators
[x for x in d1.values()]  # [[1, 2, 4, 8], [2, 4, 6, 8]]
[x for x in d1.keys()]  # ['a’, 'b']
[x for x in d1.items()]  # [('a’, [1, 2, 4, 8]), ('b', [2, 4, 6, 8])]

# Dictionary more methods
# compare dictionaries, compares by key
d1 = {'a': [1, 2, 4, 8], 'b': [2, 4, 6, 8]}
d2 = {'a': [1, 2, 4, 8], 'b': [2, 4, 6, 8]}
d1 == d2  # True
d2['b'] = [3, 6, 9, 12]
print(d2)  # {'a': [1, 2, 4, 8], 'b': [3, 6, 9, 12]}
print(d1)  # {'a': [1, 2, 4, 8], 'b': [2, 4, 6, 8]}
print(d1 == d2)  # False
d1 = {'b': [2, 4, 6, 8], 'a': [1, 2, 4, 8]}
d2 = {'a': [1, 2, 4, 8], 'b': [2, 4, 6, 8]}
print(d1 == d2) # True
