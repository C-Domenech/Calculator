import tkinter as tk


class Controller:
    def __init__(self, container):
        self.complete_text = ''
        self.container = container

    def normal_button(self, text):
        self.complete_text = '' + self.complete_text + text
        self.display_text(self.complete_text)

    def equal_button(self):
        try:
            result = eval(self.complete_text)
            self.display_text(result)
            self.complete_text = str(result)
        except:
            error = 'ERROR'
            self.display_text(error)
            self.complete_text = ''

    def erase_button(self):
        self.complete_text = '' + self.complete_text[0:-1]
        self.display_text(self.complete_text)

    def clear_button(self):
        self.display_text('')
        self.complete_text = ''

    def entry(self, x, y):
        self.my_entry = tk.Text(self.container, height=0, width=20, font=('Arial', 20), state=tk.DISABLED)
        self.my_entry.grid(row=x, column=y, columnspan=4, padx=5, pady=5)

    def display_text(self, text):
        self.my_entry.config(state=tk.NORMAL)
        self.my_entry.delete('1.0', tk.END)
        self.my_entry.insert('1.0', text)
        self.my_entry.config(state=tk.DISABLED)
