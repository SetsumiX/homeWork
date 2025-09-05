import sqlite3
import tkinter
from tkinter import ttk, messagebox

class Calculator:
    def __init__(self, db = "calculDB.db"):
        self.db = db
        # self.create_table()

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("300x400")
        self.calculator = Calculator()
        self.create_widgets()
        # self.creat_menu()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.grid(row=0, column=0, sticky=(tkinter.W, tkinter.E, tkinter.N, tkinter.S))

        self.notebook = ttk.Notebook(main_frame)
        self.notebook.grid(row=1, column=0, columnspan=2, sticky=(tkinter.W, tkinter.E, tkinter.N, tkinter.S))

        self.creat_calc_tab()

    def creat_calc_tab(self):
        add_frame = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(add_frame, text="Калькулятор")

        self.nums_entry = ttk.Entry(add_frame, width=20)
        self.nums_entry.grid(row=0, column=4)
        clmn = 0
        for x in range(1,4):
            self.button = ttk.Button(add_frame, text=str(x), width=5)
            self.button.grid(row=4, column=clmn, sticky=(tkinter.W, tkinter.E, tkinter.N, tkinter.S))
            clmn += 1
        clmn = 0
        for x in range(4,7):
            self.button = ttk.Button(add_frame, text=str(x), width=5)
            self.button.grid(row=3, column=clmn, sticky=(tkinter.W, tkinter.E, tkinter.N, tkinter.S))
            clmn += 1
        clmn = 0
        for x in range(7,10):
            self.button = ttk.Button(add_frame, text=str(x), width=5)
            self.button.grid(row=2, column=clmn, sticky=(tkinter.W, tkinter.E, tkinter.N, tkinter.S))
            clmn += 1



def main():
    root = tkinter.Tk()
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()