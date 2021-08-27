"""
Created on 25 Aug, 2021

@author : Sai Vikhyath
"""

"""
Illustrating file operation in python
Understanding and using With
With by default handles the closing of file without being mentioned
Dangling files are harmful. So, always prefer to use WITH
"""


# Without using WITH statement
file = open('File1.txt', 'w')
file.write('Hello World!')
file.close()

# Without using WITH statement. Using exceptions
file = open('File2.txt', 'w')
try:
    file.write('Hello World!')
finally:
    file.close()
#

# Using WITH statement
with open('File3.txt', 'w') as file:
    file.write('Hello World!')
