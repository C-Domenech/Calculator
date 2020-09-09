from gui.app import App
import tkinter as tk


def main():
    root = tk.Tk()
    app = App(root)
    root.title('Calculator')
    # root.iconbitmap('calculator.ico')
    root.mainloop()


if __name__ == '__main__':
    main()
