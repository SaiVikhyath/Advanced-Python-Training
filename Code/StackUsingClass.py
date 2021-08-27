"""
Created on 24 Aug, 2021

@author: Sai Vikhyath
"""


class Stack:
    """A Data Structure"""

    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        x = self.items[-1]
        del self.items[-1]
        return x

    def empty(self):
        return len(self.items) == 0


stack = Stack()
print("Stack empty? : ", stack.empty())
print("Pushing.....")
stack.push(10)
stack.push(20)
stack.push(30)
print("Stack after push : ", stack.items)
print("Stack empty? : ", stack.empty())
print("Popping.....")
stack.pop()
stack.pop()
stack.pop()
print("Stack after pop : ", stack.items)
print("Stack empty? : ", stack.empty())