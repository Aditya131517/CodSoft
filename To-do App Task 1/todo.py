import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)

# Refresh list display
def refresh_list():
    task_list.delete(0, tk.END)

    for task in tasks:
        text = task["name"]

        if task["completed"]:
            text = "✔ " + text

        task_list.insert(tk.END, text)

# Add task
def add_task():
    task = entry.get().strip()

    if task:
        tasks.append({
            "name": task,
            "completed": False
        })

        save_tasks()
        refresh_list()
        entry.delete(0, tk.END)

    else:
        messagebox.showwarning(
            "Warning",
            "Task cannot be empty!"
        )

# Delete task
def delete_task():
    try:
        index = task_list.curselection()[0]

        tasks.pop(index)

        save_tasks()
        refresh_list()

    except:
        messagebox.showwarning(
            "Warning",
            "Select a task first!"
        )

# Mark complete
def complete_task():
    try:
        index = task_list.curselection()[0]

        tasks[index]["completed"] = not tasks[index]["completed"]

        save_tasks()
        refresh_list()

    except:
        messagebox.showwarning(
            "Warning",
            "Select a task first!"
        )

# Update task
def update_task():
    try:
        index = task_list.curselection()[0]

        new_text = entry.get().strip()

        if new_text:
            tasks[index]["name"] = new_text

            save_tasks()
            refresh_list()

            entry.delete(0, tk.END)

        else:
            messagebox.showwarning(
                "Warning",
                "Enter new task text!"
            )

    except:
        messagebox.showwarning(
            "Warning",
            "Select a task!"
        )

# Main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("450x500")

tasks = load_tasks()

title = tk.Label(
    root,
    text="To-Do List",
    font=("Arial", 18, "bold")
)

title.pack(pady=10)

entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 12)
)

entry.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

btn_add = tk.Button(
    frame,
    text="Add",
    width=10,
    command=add_task
)

btn_add.grid(row=0,column=0,padx=5)

btn_update = tk.Button(
    frame,
    text="Update",
    width=10,
    command=update_task
)

btn_update.grid(row=0,column=1,padx=5)

btn_complete = tk.Button(
    frame,
    text="Complete",
    width=10,
    command=complete_task
)

btn_complete.grid(row=0,column=2,padx=5)

btn_delete = tk.Button(
    frame,
    text="Delete",
    width=10,
    command=delete_task
)

btn_delete.grid(row=0,column=3,padx=5)

task_list = tk.Listbox(
    root,
    width=50,
    height=18,
    font=("Arial",11)
)

task_list.pack(pady=20)

refresh_list()

root.mainloop()