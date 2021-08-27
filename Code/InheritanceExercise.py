"""
Created on 24 Aug, 2021

@author : Sai Vikhyath
"""

"""
Refactoring code whenever possible
Implementing inheritance
"""


class Employee:  # Base class

    def get_details(self):
        details = {'hours': 40, 'baseSalary': 40000, 'vacationDays': 10, 'vacationForm': "Yellow"}
        return details

    # Refactoring performed by avoiding multiple methods

    # def get_hours(self):
    #   return 40  # works 40 hours / week

    # def get_salary(self):
    #    return 40000.0  # Rs40,000.00 / year

    # def get_vacation_days(self):
    #    return 10  # 2 weeks' paid vacation

    # def get_vacation_form(self):
    #    return "yellow"  # use the yellow form


class Secretary(Employee):  # Child class

    # Refactoring the code because the methods already exist in Parent class

    # def get_details(self):
    #    hours, salary, vaccinationDays, vaccinationForm = 50, 40000, 10, "yellow"
    #    return hours, salary, vaccinationDays, vaccinationForm

    # def get_hours(self):
    #    return 50  # works 40 hours / week

    # def get_salary(self):
    #    return 40000.0  # $40,000.00 / year

    # def get_vacation_days(self):
    #    return 10  # 2 weeks' paid vacation

    # def get_vacation_form(self):
    #    return "yellow"  # use the yellow form

    def take_dictation(self, text):
        print("Taking dictation of text: " + text)


class LegalSecretary(Employee):  # Child class

    def fileShares(self):
        return "Filed shares!!"

    def publishYearlyReport(self):
        return "Published reports for current year!!"


class SalesPerson(Employee):    # Child class

    def get_salary(self, sales):
        details = super().get_details()
        return details['baseSalary'] + (0.3 * sales)    # Computing Sales person's salary


sales1 = SalesPerson()  # Sales person object
print("\nSalary of sales person is {0}".format(sales1.get_salary(10000)))

# e = Employee()
# s = Secretary()
# s1 = e
# print(Employee().get_hours())
# print(Secretary().get_hours())
# print("======")
# print(e.get_hours())
# print(s.get_details())
# print(s1.get_hours())
