"""
Created on Aug 24, 2021

@author : Sai Vikhyath
"""

"""
Demonstrating lists and string in python
"""


# Reads temperatures from user, computes average and number of days above average.
def main():
    days = int(input("How many days' temperatures? "))
    # Declare a List and initialize the element values
    temps = [0] * days  # List to store days' temperatures
    print(type(temps))
    tempSum = 0

    for i in range(0, days):  # Read/Store each day's temperature
        temps[i] = int(input(("Day " + str(i + 1) + "'s high temperature: ")))
        tempSum += temps[i]

    average = tempSum / days
    print(temps)
    print(tempSum)

    count = 0  # See if each day is above average
    for i in range(0, days):
        if temps[i] > average:
            count += 1
    # Report results
    print("Average temp = " + str(average))
    print(str(count) + " days above average")


main()
