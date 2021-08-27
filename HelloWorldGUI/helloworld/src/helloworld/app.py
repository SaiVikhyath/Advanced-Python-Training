"""
Created on 27 Aug, 2021

@author : Sai Vikhyath
"""

"""
Hello World application, says hello to the user on a button click
"""
from functools import partial

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class HelloWorld(toga.App):

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
        self.name_input.style.update(height=100)

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        # Step 1 create rows
        row0 = toga.Box(style=Pack(direction=ROW, padding=35))
        row1 = toga.Box(style=Pack(direction=ROW, padding=25))

        # Step 2 create TextInput
        # Created in constructor
        self.name_input.style.padding_top = 15
        self.name_input.style.width = 200
        self.name_input.style.update(height=100)

        # Step 3 create hello button
        helloBtn = toga.Button('Click Me!!!', on_press=partial(self.enterData),
                               style=Pack(padding=0, height=30, width=100))
        helloBtn.style.padding_top = 20

        # Step 4 add buttons to a Toga Box
        row0.add(self.name_input)
        row1.add(helloBtn)

        # Step 5 add rows to main window
        main_box.add(row0)
        main_box.add(row1)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def enterData(self, widget):
        self.name_input.value = "Hello!!!"


def main():
    return HelloWorld()
