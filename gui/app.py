import tkinter as tk
from gui.calculator import Calculator


class App:
    def __init__(self, master):
        self.master = master
        calculator = Calculator(self.master, 0, 0)

