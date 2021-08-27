"""
Created on 23 Aug, 2021

@author : Sai Vikhyath
"""

"""
Demonstrating string operations
"""

# Taking input from the user
name = input('What is your name?')
print('Hello ' + name)

user_ip = input('What is you ID?')
usr_id = int(user_ip)   # Casting user input to string

print(type(user_ip), type(usr_id))

print('Id is ' + str(usr_id))

str1 = "hello world"
str2 = "python"

# Concatenating
print(str1 + " " + str2)
print(str1, str2)
print("%s %s" % (str1, str2))
print("{} {}".format(str1, str2))
print("{} {}".format(str2, str1))

# String to Numeric
a = "2"
b = "6.8"

num1 = int(a)
print(num1, type(num1))
num2 = float(b)
print(num2, type(num2))

# Numeric to String
a = 6
b = 8.56
str1 = str(a)
print(str1, type(str1))
str2 = str(b)
print(str2, type(str2))

# Parsing
msg = "Berlin;Amsterdam;London;Tokyo;2020-12-31"
cities = msg.split(";")
print(cities, type(cities))
for city in cities:
    print(type(city), city)

# String Operations
msg = "Hello world, Python!"

# To Upper and To Lower
print("Hello world, Python!, msg.upper():", msg.upper())
print("Hello world, Python!, msg.lower():", msg.lower())

# Copy
print("", msg[5:])
print("Hello world, Python!:", msg[:5])
print("Hello world, Python!:", msg[-3:])
print("Hello world, Python!:", msg[:-3])
print("Hello world, Python!:", msg[2:6])
print("Hello world, Python!:", msg[5:8])

# Get Length of String
length = len(msg)
print("Hello world, Python!:", msg, length)


# Using format map
class Default(dict):

    def __missing__(self, key):
        return key


print('{name} was born in {country}'.format_map(Default(name='Guido')))
print('{name} was born in {country}'.format_map(Default(name='Guido', country='Sweden')))

symbol = "~`!@#$%^&*()_-+={}[]:>;',</?*-+"
psswd = "abc@123*"
for i in psswd:
    if i in symbol:
        print(i)

# Using stacked methods
encryptThis = 'The Text to be Encrypted'
print(encryptThis.replace('a', 'h').replace('e', 'l').replace('i', 'p').replace('o', 'v').replace('u', 'b'))

import time

# Alternately using Fernet module as encryptor
# pip install cryptography
from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)

print("Going to pause execution for 5 seconds")
time.sleep(5)
print(key)

# For better control, create your own key

'''
Base65 is encoding binary data to printable ASCII characters and decoding such encodings back to binary data
base64 => 26 UpperCase + 26 LowerCase + 0 to 9 (10 numbers) + '+' and '/' (for new lines)
Converting any Base64 character to Binary => each Character = 6 bits

P.S. = Base64 Application
suitable for encoding binary data to be sent by email, used as parts of
URLs, or included as part of an HTTP POST request, As Suggested By Many
not an encryption algorithm, and should not be used for security purposes
'''

import base64
import os

enCod = base64.urlsafe_b64encode(os.urandom(32))
print(enCod)

'''
Base64 Working
0. A to Z = 0 to 25 ## a to z = 26 to 51 ## 0 to 9 = 52 - 61 ## +, / = 62, 63
1. Take ASCII value of each character in string, say ABc
2. Calculate 8-bit binary equivalent of ASCII values, ABc = 0, 1, 28
    ==> ABc in Binary =
3. Convert 8-bit chunks into chunks of 6 bits by re-grouping  digits
Convert the 6-bit binary groups to their respective decimal values.
Using a base64 encoding table, assign the respective base64 character for each decimal value.
'''

ferNt = Fernet(key=key)

# Next encrypt your data
token = ferNt.encrypt(b"Latitude Longitude Zip Code 19.038850 73.017350 400708")
print(token)
time.sleep(5)
token = ferNt.encrypt(b"Latitude Longitude Zip Code 19.038850 73.017350 400708")
print(token)

strEx2 = 'She sells seashells by the seashore'
print(strEx2.count('s'))
print(strEx2.lower().count('s'))
# print(strEx2.count('s').lower())  # Prompts Error, as sequence of stacked methods is misplaced

# Escape Characters
print('doesn\'t')
print('Andrew said "Yes"')
print("Andrew said 'Yes'")
# print("Andrew said "Yes"") # Prompts Syntax Error Double Quote inside Double Quote

print('line one\nline two\n\tline three')

# Using str and repr
aStr = "Hello Python !"
print(str(aStr))
# repr adds string quotes and backlash
print(repr(aStr))
aStr = "Hello Python !\n"
bStr = repr(aStr)
print(bStr)
print(repr(bStr))
