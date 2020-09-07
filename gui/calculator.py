import tkinter as tk
from logic.controller import Controller


class Calculator:

    def __init__(self, parent=None, x=None, y=None):
        self.parent = parent
        self.container = tk.Frame(self.parent)
        self.container.grid(row=x, column=y)
        self.ctrl = Controller(self.container)
        self.ctrl.entry(0, 0)
        self.create_buttons()

    def create_buttons(self):
        buttons = {
            "(": (1, 0, lambda: self.ctrl.normal_button('(')),
            ")": (1, 1, lambda: self.ctrl.normal_button(')')),
            "C": (1, 2, self.ctrl.clear_button),
            "«": (1, 3, self.ctrl.erase_button),
            "7": (2, 0, lambda: self.ctrl.normal_button('7')),
            "8": (2, 1, lambda: self.ctrl.normal_button('8')),
            "9": (2, 2, lambda: self.ctrl.normal_button('9')),
            "/": (2, 3, lambda: self.ctrl.normal_button('/')),
            "4": (3, 0, lambda: self.ctrl.normal_button('4')),
            "5": (3, 1, lambda: self.ctrl.normal_button('5')),
            "6": (3, 2, lambda: self.ctrl.normal_button('6')),
            "*": (3, 3, lambda: self.ctrl.normal_button('*')),
            "1": (4, 0, lambda: self.ctrl.normal_button('1')),
            "2": (4, 1, lambda: self.ctrl.normal_button('2')),
            "3": (4, 2, lambda: self.ctrl.normal_button('3')),
            "-": (4, 3, lambda: self.ctrl.normal_button('-')),
            "0": (5, 0, lambda: self.ctrl.normal_button('0')),
            ".": (5, 1, lambda: self.ctrl.normal_button('.')),
            "=": (5, 2, self.ctrl.equal_button),
            "+": (5, 3, lambda: self.ctrl.normal_button('+')),
        }

        for char, pos in buttons.items():
            self.button(char, pos[0], pos[1], pos[2])

    def button(self, char, x, y, func):
        self.my_button = tk.Button(self.container, text=char, width=6, height=1, cursor='hand2', font=('Arial', 15),
                                   command=func)
        self.my_button.grid(row=x, column=y, padx=5, pady=5)



