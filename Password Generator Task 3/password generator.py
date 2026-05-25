import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())

        characters = ""

        if var_lower.get():
            characters += string.ascii_lowercase

        if var_upper.get():
            characters += string.ascii_uppercase

        if var_numbers.get():
            characters += string.digits

        if var_symbols.get():
            characters += string.punctuation

        if characters == "":
            messagebox.showwarning(
                "Warning",
                "Select at least one option"
            )
            return

        password = ""

        for i in range(length):
            password += random.choice(characters)

        result_label.config(
            text="Generated Password:\n" + password
        )

    except:
        messagebox.showerror(
            "Error",
            "Enter valid password length"
        )

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")

title = tk.Label(
    root,
    text="Password Generator",
    font=("Arial",16,"bold")
)
title.pack(pady=10)

tk.Label(
    root,
    text="Enter Password Length"
).pack()

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

var_lower = tk.IntVar()
var_upper = tk.IntVar()
var_numbers = tk.IntVar()
var_symbols = tk.IntVar()

tk.Checkbutton(
    root,
    text="Lowercase (a-z)",
    variable=var_lower
).pack()

tk.Checkbutton(
    root,
    text="Uppercase (A-Z)",
    variable=var_upper
).pack()

tk.Checkbutton(
    root,
    text="Numbers (0-9)",
    variable=var_numbers
).pack()

tk.Checkbutton(
    root,
    text="Symbols (!@#$)",
    variable=var_symbols
).pack()

tk.Button(
    root,
    text="Generate Password",
    command=generate_password
).pack(pady=15)

result_label = tk.Label(
    root,
    text="Generated Password:",
    wraplength=350
)
result_label.pack()

root.mainloop()