"""
Created on 23 Aug, 2021

@author : Sai Vikhyath
"""

"""
Demonstration of Python lists
List is a collection of data(homogeneous or heterogeneous)
Lists are mutable
Lists are possibly the most useful data structure in Python!
"""

# Declare lists
print('Declare lists')
numbers = []
a = [2, 7, 10, 8]
cities = ['Berlin', 'Seattle', 'Tokyo', 'Moscow']
b = [10, 3, 'Apple', 6, 'Strawberry']   # Python list can have heterogeneous data
c = range(1, 10, 2)  # range method in python creates a list
"""
range(start, stop, step)
"""

# Print(lists)
print('Print lists')
print(a)
for city in cities:  # for loop with in can be used to iterate lists
    print(city)

print(b)
print(c)

# Lists are defined by square brackets
new_list = [3, 4, 5, 6]
print("new_list is: ", new_list, " line 56 ", type(new_list))

# Just like strings, we can index & slice them
print("new_list[2] is:", new_list[2])
print("new_list[0:2] is:", new_list[0:2])

# And iterate through them:
for item in new_list:
    print(item)

# Lists, however, are mutable! So, if we want we can change the value of one element

new_list[2] = 100
print("new_list is:", new_list)

# Or, add on a new element with append:
new_list.append(87)
print("new_list is:", new_list)

# Or, insert
new_list.insert(0, 200)  # insert at position 0 the element 200
print("new_list is:", new_list)

# Or, even delete an element using remove
new_list.remove(100)  # Write in the item that you want to remove from the list
print("new_list is:", new_list)

# Get length of lists
print('Get length of lists')
print(len(a))   # len method gives the length of any data structure in python
print(len(cities))

# Add item into list
print('Add item')
numbers.append(10)  # Append to the list. i.e. Add the element to the end of the list(At last index)
numbers.append(5)
cities.append('London')

for i in numbers:
    print(i)

for city in cities:
    print(city)

# Get specific item
print('Get specific item')
print(cities[2])    # Indexing can be used in lists
print(a[3])

# Sorting
print(a.sort(key=None, reverse=False))  # sort method is provided by the lists

# Edit item
print('Edit item. Lists are mutable')
cities[2] = 'New City'  # Lists are mutable
for city in cities:
    print(city)

# Remove item
print('Remove item')
a.remove(8)  # Remove by value
del cities[2]  # Remove by index
for city in cities:
    print(city)
