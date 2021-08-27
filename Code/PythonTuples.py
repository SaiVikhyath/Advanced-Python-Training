"""
Created on 23 Aug, 2021

@author : Sai Vikhyath
"""

"""
Demonstrating tuples in python
"""

# Tuple declaration
a = ()
b = (3, 5, 7)
c = ('Ford', 'BMW', 'Toyota')
d = (3, (5, 'London'), 12)

# Print tuples
print("a: ", a)
print("b: ", b)
print("c: ", c)
print("d: ", d)

# Get length of tuples
print("len(a): ", len(a))
print("len(b): ", len(b))
print("len(c): ", len(c))
print("len(d): ", len(d))

# Get item in tuple
print("b[2]: ", (b[2]))
print("c[1]: ", (c[1]))

# Get index of item in tuple
print("b.index(7): ",b.index(7))
print("c.index('Toyota'): ", c.index('Toyota'))
print("d.index('London'): ", d[1].index('London'))
print("d[1][0]: ", d[1][0])
