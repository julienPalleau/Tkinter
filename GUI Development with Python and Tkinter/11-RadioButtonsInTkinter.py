import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from roots import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

storage_variable = tk.StringVar()


def viewSelected():
    choice = storage_variable.get()
    if choice == "First option":
        output = "Science"
    elif choice == "Second option":
        output = "Commerce"
    elif choice == "Third option":
        output = "Art"
    else:
        output = "Invalid selection"

    return messagebox.showinfo('PythonGuides', f'You Seleceted {output}.')


option_one = ttk.Radiobutton(
    root,
    text="Science",
    variable=storage_variable,
    value="First option",
    command=viewSelected
)

option_two = ttk.Radiobutton(
    root,
    text="Commerce",
    variable=storage_variable,
    value="Second option",
    command=viewSelected
)

option_three = ttk.Radiobutton(
    root,
    text="Arts",
    variable=storage_variable,
    value="Third option",
    command=viewSelected
)

option_one.pack()
option_two.pack()
option_three.pack()

root.mainloop()
