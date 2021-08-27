"""
Created on 23 Aug, 2021

@author : Sai Vikhyath
"""

"""
Demonstration of list comprehensions
"""

# WITHOUT List comprehensions
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
output_list = []
# Using loop for constructing output list
for var in input_list:
    if var % 2 == 0:
        output_list.append(var)
print("Output List using for loop:", output_list)

# USING List comprehensions
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
list_using_comp = [var for var in input_list \
                   if var % 2 == 0]
print("list comprehensions:", list_using_comp)


# WITHOUT using list comprehensions
output_list = []
for var in range(1, 10):
    output_list.append(var ** 2)
print("Output List using for loop:", output_list)

# Using list comprehensions
listCmp = [var ** 2 for var in range(1, 10)]
print(listCmp)


# WITHOUT using list comprehensions
myString = "I have 2 apples"

for i in myString.split():
    if i.isnumeric():
        int(i)

# Using list comprehensions
extractedNum = [int(i) for i in myString.split() if i.isnumeric()]
print("Numbers list is: ", str(extractedNum))


# WITHOUT List comprehensions
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
output_list = []
# Using loop for constructing output list 
for var in input_list:
    if var % 2 == 0:
        output_list.append(var)
print("Output List using for loop:", output_list)

# USING List comprehensions
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
list_using_comp = [var for var in input_list if var % 2 == 0]
print("list comprehensions:", list_using_comp)


# Constructing output list using for loop
output_list = []
for var in range(1, 10):
    output_list.append(var ** 2)
print("Output List using for loop:", output_list)

# USING list comprehension
list_using_comp = [var ** 2 for var in range(1, 10)]
print("Output List using list comprehension:", list_using_comp)

# Extract Number from string
myString = "I have 2 apples"
extractedNum = [int(i) for i in myString.split() if i.isnumeric()]
print("Numbers list is: ", str(extractedNum))

# List comprehensions example
nums = [1, 2, 3]
oL = [n if n == 1 else (n + 1) if n == 2 else (n + 3) for n in nums]
print(oL)


# WITHOUT list comprehensions
lst = []
for iCnt in range(10):
    if iCnt == 6:
        for jCnt in range(3):
            if jCnt == 2:
                lst.append(iCnt)

print(lst)

# Using list comprehensions
print([iCnt for iCnt in range(10) if iCnt == 6 for jCnt in range(3) if jCnt == 2])
