"""
Created on 25 Aug, 2021

@author : Sai Vikhyath
"""

"""
Fibonacci Series with Refactoring Does and Don't
Fibonacci Series Pre Refactoring => Basic Code Implementation
"""


# Basic version of fibonacci series code
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


result = fibonacci(20)
print(result)


# First draft of refactored code using while loop
a, b = 0, 1
num1 = int(input("Enter first number: "))  # get number to generate Fibonacci series

while b < num1:
    print(b)
    a, b = b, (a + b)
print("Done")


# Fibonacci Series With Final Version After Refactoring
# Using Python's in-built recursion supported 'Generator"

def fibonacci_sequence():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


generator = fibonacci_sequence()
for i in range(20):
    print(next(generator))
