"""
Created on 27 Aug, 2021

@author : Sai Vikhyath
"""

"""
Basic arithmetic calculator
"""

from functools import partial

import toga  # toga widget toolkit
from toga.style.pack import COLUMN, ROW, Pack
# from toga.style import pack
# import Pack, COLUMN, ROW


class Calculator(toga.App):  # Each Toga application has a single toga.App instance
    # App may manage multiple windows
    # For simple applications, there will be a single main window

    def __init__(
            self,
            formal_name=None,
            app_id=None,
            app_name=None,
            id=None,
            icon=None,
            author=None,
            version=None,
            home_page=None,
            description=None,
            startup=None,
            on_exit=None,
            factory=None,
    ):
        super().__init__(formal_name, app_id, app_name, id, icon, author, version, home_page, description, startup,
                         on_exit, factory)
        self.name_input = toga.TextInput(style=Pack(flex=1))

    def startup(self):
        # All Code Goes Here
        """
        Calculator has 6 Rows
        Row 0 =       Display
        Row 1 =     7   8   9   +
        Row 2 =     4   5   6   -
        Row 3 =     1   2   3   *
        Row 4 =     .   0   C   /
        Row 5 =       Calculate
        :return:
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))

        # Step 1 Create the Boxes
        row0_box1 = toga.Box(style=Pack(direction=ROW, padding=5))
        row1_box1 = toga.Box(style=Pack(direction=ROW, padding=5))
        row2_box1 = toga.Box(style=Pack(direction=ROW, padding=5))
        row3_box1 = toga.Box(style=Pack(direction=ROW, padding=5))
        row4_box1 = toga.Box(style=Pack(direction=ROW, padding=5))
        row5_box1 = toga.Box(style=Pack(direction=ROW, padding=5))

        # Step 2 Make the TextInput
        # Row 0 =       Display
        self.name_input.style.padding_top = 5
        self.name_input.style.width = 150

        # Step 3 Make the Row Buttons
        # Step 7 Add on_press functionality

        # Row 1 =     7   8   9   +
        button7 = toga.Button('7', on_press=partial(self.enter_data, number='7'), style=Pack(padding=5))
        button7.style.padding_top = 20
        button8 = toga.Button('8', on_press=partial(self.enter_data, number='8'), style=Pack(padding=5))
        button8.style.padding_top = 20
        button9 = toga.Button('9', on_press=partial(self.enter_data, number='9'), style=Pack(padding=5))
        button9.style.padding_top = 20
        buttonPlus = toga.Button('+', on_press=partial(self.enter_data, number='+'), style=Pack(padding=5))
        buttonPlus.style.padding_top = 20

        # Row 2 =     4   5   6   -
        button4 = toga.Button('4', on_press=partial(self.enter_data, number='4'), style=Pack(padding=5))
        button4.style.padding_top = 20

        button5 = toga.Button('5', on_press=partial(self.enter_data, number='5'), style=Pack(padding=5))
        button5.style.padding_top = 20

        button6 = toga.Button('6', on_press=partial(self.enter_data, number='6'), style=Pack(padding=5))
        button6.style.padding_top = 20

        buttonMinus = toga.Button('-', on_press=partial(self.enter_data, number='-'), style=Pack(padding=5))
        buttonMinus.style.padding_top = 20

        # Row 3 =     1   2   3   *
        button1 = toga.Button('1', on_press=partial(self.enter_data, number='1'), style=Pack(padding=5))
        button1.style.padding_top = 20

        button2 = toga.Button('2', on_press=partial(self.enter_data, number='2'), style=Pack(padding=5))
        button2.style.padding_top = 20

        button3 = toga.Button('3', on_press=partial(self.enter_data, number='3'), style=Pack(padding=5))
        button3.style.padding_top = 20

        buttonMultiply = toga.Button('*', on_press=partial(self.enter_data, number='*'), style=Pack(padding=5))
        buttonMultiply.style.padding_top = 20

        # Row 4 =     .   0   C   /
        buttonDot = toga.Button('.', on_press=partial(self.enter_data, number='.'), style=Pack(padding=5))
        buttonDot.style.padding_top = 20

        button0 = toga.Button('0', on_press=partial(self.enter_data, number='0'), style=Pack(padding=5))
        button0.style.padding_top = 20

        buttonClear = toga.Button('C', on_press=partial(self.enter_data, number='C'), style=Pack(padding=5))
        buttonClear.style.padding_top = 20

        buttonDivide = toga.Button('/', on_press=partial(self.enter_data, number='/'), style=Pack(padding=5))
        buttonDivide.style.padding_top = 20

        # Row 5 =       Calculate
        # Step 8 Add on_press functionality
        buttonCalculate = toga.Button('=', on_press=self.calculate, style=Pack(padding=5))
        buttonCalculate.style.padding_top = 5
        buttonCalculate.style.width = 130

        # Step 4 Add the Buttons to a Toga Box
        row0_box1.add(self.name_input)

        row1_box1.add(button7)
        row1_box1.add(button8)
        row1_box1.add(button9)
        row1_box1.add(buttonPlus)

        row2_box1.add(button4)
        row2_box1.add(button5)
        row2_box1.add(button6)
        row2_box1.add(buttonMinus)

        row3_box1.add(button1)
        row3_box1.add(button2)
        row3_box1.add(button3)
        row3_box1.add(buttonMultiply)

        row4_box1.add(buttonDot)
        row4_box1.add(button0)
        row4_box1.add(buttonClear)
        row4_box1.add(buttonDivide)

        row5_box1.add(buttonCalculate)

        # Step 5 Add Row_Buttons to Toga Main Window
        main_box.add(row0_box1)
        main_box.add(row1_box1)
        main_box.add(row2_box1)
        main_box.add(row3_box1)
        main_box.add(row4_box1)
        main_box.add(row5_box1)

        self.main_window = toga.MainWindow(title=self.formal_name)

        self.main_window.content = main_box
        self.main_window.show()

    # Step 6 displaying to the UI the pressed number
    def enter_data(self, widget, number):
        if number == 'C':
            self.name_input.value = ''
        else:
            self.name_input.value = self.name_input.value + number

    # Step 8 Calculate and display the result on pressing "="
    def calculate(self, widget):
        result = eval(self.name_input.value)  # evaluate string data
        self.main_window.info_dialog('Result = ', str(result))


def main():
    return Calculator()

# Use Terminal from Pycharm to run application
#   cd to project folder
#   run "briefcase dev"

# To activate virtual environment
#   cd to main folder
#   run activate beeware venv script

# Further documentation and support to make mobile app
# https://docs.beeware.org/en/latest/tutorial/tutorial-2.html
