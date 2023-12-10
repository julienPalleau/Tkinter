import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)

style.theme_use("clam")

style.map("CustomButton.TButton",
          foreground=[("pressed", "red"), ("active", "blue")],  # we change the foreground color when we press the button
          background=[("pressed", "!disabled", "black"), ("active", "black")],  # we change the background color ...
          font=[("pressed", ("TkDefaultFont", 15))]  # We change the font size ...
          # to get the background working it is necessary to change the them as roots theme (by default)
          # doesn't allow you to change background.
          )

name = ttk.Label(root, text="Hello, world!")
entry = ttk.Entry(root, width=15)
button = ttk.Button(root, text="Press me.", style="CustomButton.TButton")
name.pack()
entry.pack()
button.pack()

root.mainloop()
