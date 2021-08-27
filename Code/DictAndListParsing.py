"""
Created on 23 Aug, 2021

@author: Sai Vikhyath
"""

"""
Demonstration of parsing and iterating through Lists, Dictionaries and Nested Lists and Dictionaries
"""

myList = [11111111, 22222222, 33333333, 44444444]
myDict = {0: "1", 1: "22", 2: "333", 3: "44444"}
myNestedListDict = [[[{0: "1"}, {1: "22"}, {2: "333"}, {3: "44444"}],
                     [{4: "4"}, {5: "22"}, {6: "333"}, {7: "44"}]],
                    [[{0: "1"}, {1: "22"}, {2: "333"}, {3: "44444"}],
                     [{8: "44"}, {9: "22"}, {10: "333"}, {11: "444"}]]]

# Iterating through myList
for i in range(len(myList)):
    for x in myList:
        print(x)
print("================")
for x in myList:
    print(x)
print("================")
# Iterating through myDict
for y in myDict:
    print(myDict[y])
print("================")
# Iterating through myNestedListDict
for z in myNestedListDict:
    for x in z:
        for y in x:
            print(y)
            for _, v in y.items():
                print(v)
