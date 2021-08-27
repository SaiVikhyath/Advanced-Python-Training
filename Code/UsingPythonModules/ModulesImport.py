"""
Created on 25 Aug, 2021

@author : Sai Vikhyath
"""

import UsingPythonModules.ModulesExport.AirtelNumbers as numAirtel
import UsingPythonModules.ModulesExport.BSNL_Numbers as numBSNL
import UsingPythonModules.ModulesExport.VodafoneNumbers as numVodafone


"""
Create a program to import modules
"""

def usingModuleExport():
    numAirtel.Airtel()
    numBSNL.BSNL()
    numVodafone.Vodafone()
    print("Airtel number :", numAirtel.var3)


if __name__ == "__main__":
    usingModuleExport()