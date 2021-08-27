"""
Created on 23 Aug, 2021]

@author : Sai Vikhyath
"""

from math import sqrt

"""
Program that calculates distance of a point from origin
Demonstrates usage of lists and math module
Demonstrated map and lambda
"""

points = [(2, 1, 3), (5, 7, -3), (2, 4, 0), (9, 6, 8)]  # Tuples inside a list


def distance(point):    # Method to calculate distance
    x, y, z = point
    return sqrt(x ** 2 + y ** 2 + z ** 2)


distances = list(map(distance, points))
print(distances)

point = 2

result = list(map(lambda point: point[0], points))
print(result)
