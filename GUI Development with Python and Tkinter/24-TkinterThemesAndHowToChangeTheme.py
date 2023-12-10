import tkinter as tk
from tkinter import ttk, font
from roots import set_dpi_awareness

set_dpi_awareness()


def greet(*args):
    print(f"Hello, {user_name.get()}")


root = tk.Tk()
root.resizable(False, False)
root.title("Greeter")

style = ttk.Style(root)
print(style.theme_names())
print(style.theme_use("clam"))

main = ttk.Frame(root, padding=(40, 20))
main.grid()

user_name = tk.StringVar()

name_label = ttk.Label(main, text="Name:")
name_label.grid(column=0, row=0, padx=(0, 10))
name_entry = ttk.Entry(main, width=15, textvariable=user_name)
name_entry.grid(column=1, row=0, padx=0)
name_entry.focus()

greet_button = ttk.Button(main, text="Greet", command=greet)
greet_button.grid(column=2, row=0, stick="EW", padx=10)

root.mainloop()