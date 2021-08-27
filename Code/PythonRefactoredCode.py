"""
Created on 25 Aug, 2021

@author : Sai Vikhyath
"""

import time

"""
Refactored code for the PythonCodeRefactoring.py
"""

def top():
    print('  ______')
    print(' /       \\')
    print('/         \\')


def bottom():
    print('\         /')
    print(' \_______/')


def line():
    print("+--------+")


def stop():
    print("|  STOP   |")


t1  = time.time()
for i in range(1000):
    top()
    bottom()
    print()
    bottom()
    print()
    line()
    print()
    top()
    stop()
    top()
    line()

t2 = time.time()
print('Time elasped : ', t2 - t1)