"""
Created On 23 Aug, 2021

@author : Sai Vikhyath
"""

"""
Demonstration of Dictionary Comprehensions in Python
"""

# WITHOUT Dictionary comprehensions
input_list = [1, 2, 3, 4, 5, 6, 7]
output_dict = {}
# Using loop for constructing output dictionary
for var in input_list:
    if var % 2 != 0:
        output_dict[var] = var ** 3
print("Output Dictionary using for loop:", output_dict)

# Using Dictionary Comprehension
output_dict_comp = {var: var ** 3 for var in input_list if var % 2 != 0}
print("Using dictionary comprehension : ", output_dict_comp, type(output_dict_comp))

# Constructing dictionary from lists using for loop
state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['GandhiNagar', 'Mumbai', 'Jaipur']
output_dict = {}
# Using loop for constructing output dictionary
for (key, value) in zip(state, capital):
    output_dict[key] = value
print("Output Dictionary using for loop:", output_dict)

# Using dictionary comprehension to construct dictionary
output_dict_sc = {key: value for (key, value) in zip(state, capital)}
print("Using dictionary comprehension : ", output_dict_sc)
