"""
Created on 25 Aug, 2021

@author : Sai Vikhyath
"""

"""
Demonstration of iterators
"""

tupleA = ("ele1", "ele2", "ele3")

# Store tuple using iter
it_tupleA = iter(tupleA)
print(type(it_tupleA))

print(it_tupleA)
print(next(it_tupleA))
print(next(it_tupleA))
print(next(it_tupleA))
# print(next(it_tupleA))    # Prompts an error because out of index.

it_tupleB = iter(tupleA)
for iEle in tupleA:
    print(iEle)


nums = [1, 2, 3]
iter(nums)  # <list_iterator object at 0x7fc1997ed690>
nums.__iter__()  # <list_iterator object at 0x7fc1997ed710>
it = iter(nums)
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it)) # Prompt StopIteration

print((i for i in nums))  # <generator object <genexpr> at 0x7fc199585150>
print([i for i in nums])  # [1, 2, 3]
print(list(i for i in nums))  # [1, 2, 3]
print({i for i in range(3)})  # {0, 1, 2}
print({i: i ** 2 for i in range(3)})  # {0: 0, 1: 1, 2: 4}
