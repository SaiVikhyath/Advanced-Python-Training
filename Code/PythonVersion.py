"""
Created on 23 Aug, 2021

@author : Sai Vikhyath
"""

"""
Prints the version of Python installed
"""

import sys

print("\nVersion : ", sys.version)
print("\nVersion", sys.version_info)  # returns mixed tuple

import platform

print("\nPython version : ", platform.python_version())  # returns string
print("\nPython version : ", platform.python_version_tuple())  # returns string tuple