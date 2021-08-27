"""
Created on 24 Aug, 2021

@author : Sai Vikhyath
"""

"""
Demonstrate nested classes
"""


class Parent:  # Define parent class
    parentAttr = 100

    def __init__(self):
        print("Call parent constructor")
        self.inner = self.Inner()

    def parentMethod(self):
        print('Call parent method')

    def reveal(self):
        self.inner.childMethod("Call Inner Class's Function from Outer Class")

    class Inner:  # Define Inner class

        def __init__(self):
            print("Called inner class's constructor")

        def childMethod(self, msg):
            print(msg)


p = Parent()
p.reveal()  # Instance of child
# c.childMethod()  # Prompts AttributeError, childMethod is hidden
Parent().Inner().childMethod("Less Efficient -> Parent to Inner to Inner's method")
c2 = p.inner    # Instance of child
c2.childMethod("Child c2!")