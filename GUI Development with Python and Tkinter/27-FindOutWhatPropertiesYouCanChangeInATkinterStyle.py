import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)

name = ttk.Label(root, text="Hello, world!")
name.pack()

print(style.layout("TLabel"))

print(style.element_options("Label.border"))
print(style.element_options("Label.padding"))
print(style.element_options("Label.label"))

print(style.lookup("TLablel", "font"))  # retrieve value of style properties
print(style.lookup("TLablel", "foreground"))  # retrieve value of style properties
print(style.lookup("TLablel", "compound"))  # no value returned because it is not set

style.theme_use("clam")  # we are setting a theme and look at the setting again

print(style.layout("TLabel"))

print(style.element_options("Label.border"))
print(style.element_options("Label.padding"))
print(style.element_options("Label.label"))

print(style.lookup("TLablel", "font"))  # retrieve value of style properties
print(style.lookup("TLablel", "foreground"))  # retrieve value of style properties
print(style.lookup("TLablel", "compound"))  # no value returned because it is not set

# Let's create a border with the clam them (you can't do it with roots style)
style.configure("TLabel", bordercolor="#f00")
style.configure("TLabel", borderwidth=20)  # in clam theme borderwidth can't exceed 2 pixels
style.configure("TLabel", relief="solid")

root.mainloop()
