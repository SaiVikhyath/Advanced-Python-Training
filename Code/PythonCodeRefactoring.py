"""
Created on 25 Aug, 2021

@author : Sai Vikhyath
"""

"""
This code must be refactored
Refactored code in PythonRefactoredCode.py
"""

import time

def main():
 print('  ______')
 print(' /       \\')
 print('/         \\')
 print('\         /')
 print(' \_______/')
 print()
 print('\        /')
 print(' \______/')
 print("+--------+")
 print()
 print("  ______")
 print(" /       \\")
 print("/         \\")
 print("|  STOP   |")
 print("\         /")
 print(" \_______/")
 print()
 print("  ______")
 print(" /      \\")
 print("/        \\")
 print("+--------+")


t1 = time.time()
for i in range(1000):
 main()
t2 = time.time()
print('Time elasped : ', t2 - t1)