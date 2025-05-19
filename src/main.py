import tkinter as tk
from tkinter import messagebox

class SimpleCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Калькулятор")

        self.entry1 = tk.Entry(master, width=10, font='Arial 14')
        self.entry1.grid(row=0, column=0, padx=5, pady=5)

        self.entry2 = tk.Entry(master, width=10, font='Arial 14')
        self.entry2.grid(row=0, column=2, padx=5, pady=5)

        self.result_label = tk.Label(master, text="Результат:", font='Arial 14')
        self.result_label.grid(row=1, column=0, columnspan=3, pady=5)

        self.create_buttons()

    def create_buttons(self):
        tk.Button(self.master, text='+', font='Arial 14', command=self.add).grid(row=2, column=0)
        tk.Button(self.master, text='-', font='Arial 14', command=self.subtract).grid(row=2, column=1)
        tk.Button(self.master, text='*', font='Arial 14', command=self.multiply).grid(row=2, column=2)
        tk.Button(self.master, text='/', font='Arial 14', command=self.divide).grid(row=3, column=1)

    def get_inputs(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Помилка", "Введіть коректні числа")
            return None, None

    def add(self):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            result = num1 + num2
            self.result_label.config(text=f"Результат: {result}")

    def subtract(self):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            result = num1 - num2
            self.result_label.config(text=f"Результат: {result}")

    def multiply(self):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            result = num1 * num2
            self.result_label.config(text=f"Результат: {result}")

    def divide(self):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            if num2 == 0:
                messagebox.showerror("Помилка", "Ділення на нуль!")
            else:
                result = num1 / num2
                self.result_label.config(text=f"Результат: {result}")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = SimpleCalculator(root)
    root.mainloop()
