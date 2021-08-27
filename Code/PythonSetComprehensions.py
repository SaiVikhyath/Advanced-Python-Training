"""
Created on 23 Aug, 2021

@author : Sai Vikhyath
"""

"""
Demonstrating Set comprehensions
"""

# WITHOUT Set comprehensions
input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
output_set = set()
# Using loop for constructing output set
for var in input_list:
    if var % 2 == 0:
        output_set.add(var)
print("Output Set using for loop:", output_set)

# USING Set comprehensions
set_using_comp = {var for var in input_list if var % 2 == 0}
print("Output Set using set comprehensions:", set_using_comp)