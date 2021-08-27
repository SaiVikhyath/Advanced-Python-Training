"""
Created on 23 Aug, 2021

@author: Sai Vikhyath
"""

"""
Demonstrating Python Dictionaries 
"""

a = {}  # Dictionary assignment
b = {2: 'Sea', 3: 'River', 8: 'Mountain'}   # Dictionary assignment
c = {2: {4: 'abcd', 5: 'hjkl'}, 3: 'vbnm'}  # Nested Dictionary
d = dict(name='elena', age='30', rolese=('manager', 'consultant'))  # Tuple nested in Dictionary
e = {1: 'elena', 2: '30', 3: {1: 'manager', 2: 'consultant'}}   # Dictionary nested in Dictionary

# Print dictionary
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
print("e:", e)

# Get Key values
print("b.keys(): ", b.keys())
print("b.values(): ", b.values())
print("b.items(): ", b.items())

# Get Key values
print("d.keys(): ", d.keys())
print("d.values(): ", d.values())
print("d.items(): ", d.items())

# Get Key values
print("e.keys(): ", e.keys())
print("e.values(): ", e.values())
print("e.items(): ", e.items())
print("e[3]: ", e[3])
print("e[3][1]: ", e[3][1])

# Add item to dictionary
a.setdefault(2, 'car')
a.setdefault(5, 'train')
a.setdefault(7, 'plane')
print("a: ", a)

# Check key
print("3 in b: ", 3 in b)
print("5 in b: ", 5 in b)
