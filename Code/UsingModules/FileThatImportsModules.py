"""
Created on 25 Aug, 2021

@author : Sai Vikhyath
"""

import UsingModules.ModulesForExport.FileToImport as fit

"""
Demonstrate module import in python
var3 is a variable assigned in FileToImport
var3 will be accessed in this file by importing the module 
"""

var1 = 100
var2 = 200
var3 = fit.var3


def methodOne(var1, var2, var3):
    print(var1, var2, var3)


methodOne(var1, var2, var3)