import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2

        elif operation == "-":
            result = num1 - num2

        elif operation == "*":
            result = num1 * num2

        elif operation == "/":
            if num2 == 0:
                messagebox.showerror(
                    "Error",
                    "Cannot divide by zero"
                )
                return

            result = num1 / num2

        result_label.config(
            text=f"Result: {result}"
        )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter valid numbers"
        )

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x300")

title = tk.Label(
    root,
    text="Calculator",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

tk.Label(root, text="First Number").pack()
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack(pady=5)

operation_var = tk.StringVar()
operation_var.set("+")

tk.Label(root, text="Select Operation").pack()

operations = ["+", "-", "*", "/"]

dropdown = tk.OptionMenu(
    root,
    operation_var,
    *operations
)
dropdown.pack(pady=5)

tk.Button(
    root,
    text="Calculate",
    command=calculate
).pack(pady=15)

result_label = tk.Label(
    root,
    text="Result:",
    font=("Arial", 12)
)
result_label.pack()

root.mainloop()