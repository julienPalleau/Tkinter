import tkinter as tk
from tkinter import ttk
import tkinter.font as font

root = tk.Tk()
style = ttk.Style(root)

# What family are available in the OS
print(font.families())

# Helvetica, Courier, Times are supported by all OS. The other family name are not necessary.
warningLabelFont = font.Font(family="Helvetica", size=14, weight="bold")

# To change the font
# warningLabelFont = font.nametofont("TkDefaultFont") # will change the fonts across everything (button and label are
# both large.
warningLabelFont = font.nametofont("TkDefaultFont").copy() # here you get a copy of defautl font, so only the label is
# in size 15 and bold while the button use the default font.
warningLabelFont.configure(size=15)

name = ttk.Label(root, text="Hello world!", font=warningLabelFont)
entry = ttk.Entry(root, width=15)
button = ttk.Button(root, text="Press me.")
name.pack()
entry.pack()
button.pack()

root.mainloop()