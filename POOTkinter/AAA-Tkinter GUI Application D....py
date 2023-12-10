#####################################
# 1 - Getting Started with Tkinter  #
#####################################


# W:\Perso\backup\IT stuff\Cours de programmation\Python\GUI\TKINTER\AAA-Tkinter GUI Application D....pdf
# Exemple 1
# Getting Ready
# We will take the following programs as an example:

# from tkinter import *
# root = Tk()
# btn = Button(root, text='Click me!')
# btn.config(command=lambda: print('Hello, Tkinter!'))
# btn.pack(padx=120, pady=30)
# root.title("My Tkinter app")
#
# root.mainloop()


# Exemple 2
# Working with buttons
"""Button widges represent a clickable item of your GUI applications. They typically use a text or an image indicating
the action that will be performed when clicked. Tkinter allows you to easily configure this functionality with some
 options of the Button widget class standard."""

# import tkinter as tk
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.btn = tk.Button(self, text="Click me!", command=self.say_hello)
#         self.btn.pack(padx=120, pady=30)
#
#     def say_hello(self):
#         print("Hello, Tkinter!")
#
#
# if __name__ == "__main__":
#     app = App()
#     app.title("My Tkinter app")
#     app.mainloop()


# # Exemple 3
# import tkinter as tk
#
# RELIEFS = [tk.SUNKEN, tk.RAISED, tk.GROOVE, tk.RIDGE, tk.FLAT]
#
#
# class ButtonsApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.img = tk.PhotoImage(file="python.gif")
#         self.btn = tk.Button(self, text="Button with image",
#                              image=self.img, compound=tk.LEFT,
#                              command=self.disable_btn)
#         self.btns = [self.create_btn(r) for r in RELIEFS]
#         self.btn.pack()
#         for btn in self.btns:
#             btn.pack(padx=10, pady=10, side=tk.LEFT)
#
#     def create_btn(self, relief):
#         return tk.Button(self, text=relief, relief=relief)
#
#     def disable_btn(self):
#         self.btn.config(state=tk.DISABLED)
#
#
# if __name__ == "__main__":
#     app = ButtonsApp()
#     app.mainloop()


# Exemple 4
# Creating text entries
# import App as App
# from PIL.ImageWin import Window
import csv
from typing import List, Any

"""The Entry widget represents a text input displayed in a single line. Along with the Label and Button classes, it is
one of the most commonly used Tkinter classes."""

# import tkinter as tk
#
#
# class LoginApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#
#         self.username_lbl = tk.Label(self, text="Username:")
#         self.username_lbl.grid(row=0, column=0)
#         self.password_lbl = tk.Label(self, text="Password:")
#         self.password_lbl.grid(row=1, column=0)
#
#         self.username_ent = tk.Entry(self)
#         self.password_ent = tk.Entry(self, show="*")
#         self.login_btn = tk.Button(self, text="Log in", command=self.print_login)
#         self.clear_btn = tk.Button(self, text="Clear", command=self.clear_form)
#
#         self.username_ent.grid(row=0, column=1)
#         self.password_ent.grid(row=1, column=1)
#         self.login_btn.grid(row=2, columnspan=2, sticky='ew')
#         self.clear_btn.grid(row=3, columnspan=2, sticky='ew')
#
#     def print_login(self):
#         print("Username: {}".format(self.username_ent.get()))
#         print("Password: {}".format(self.password_ent.get()))
#
#     def clear_form(self):
#         self.username_ent.delete(0, tk.END)
#         self.username_ent.insert(0, "default value")
#         self.password_ent.delete(0, tk.END)
#
#
# if __name__ == "__main__":
#     app = LoginApp()
#     app.title("Login boxe")
#     app.mainloop()


# # Exemple 5
# Tracing a text change
"""Tk variables allow your applications to get notified when an input changes its value. There are four variables
classes in Tkinter.BooleanVar, DoubleVar, IntVar, and StringVar. Each one wras the value of the corresponding Python
type, which should match the type of the input widget attached to the variable.
This feature is particularly useful if you want to automatically update certain parts of your application based on the 
current state of some imput widgets."""

# import tkinter as tk
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.var = tk.StringVar()
#         self.var.trace("w", self.show_message)
#         self.entry = tk.Entry(self, textvariable=self.var)
#         self.btn = tk.Button(self, text="Clear", command=lambda: self.var.set(""))
#         self.label = tk.Label(self)
#         self.entry.pack()
#         self.btn.pack()
#         self.label.pack()
#
#     def show_message(self, *args):
#         value = self.var.get()
#         text = "Hello, {}!".format(value) if value else ""
#         self.label.config(text=text)
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()


# Exemple 6
# Validate a text entry
"""Typically, text inputs represent fields that follow certain validation rules, such as having a maximum length or
matching a specific format. Some applications allow typing any kind of content into these fields and trigger the
validation when the whole form is submitted.
Under some circumstances, we want to prevent users from typing invalid content into a text field. We will tak a look at
how to implement this behavior using the validation options of the Entry widget."""

# import re
# import tkinter as tk
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.pattern = re.compile("^\w{0,10}$")
#         self.label = tk.Label(self, text="Enter your username")
#         vcmd = (self.register(self.validate_username), "%i", "%P")
#         self.entry = tk.Entry(self, validate="key",
#                               validatecommand=vcmd,
#                               invalidcommand=self.print_error)
#         self.label.pack()
#         self.entry.pack(anchor=tk.W, padx=10, pady=10)
#
#     def validate_username(self, index, username):
#         print("Modification at index " + index)
#         return self.pattern.match(username) is not None
#
#     def print_error(self):
#         print("Invalid username character")
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()


# Exemple 7
# Selecting numerical values
""" Previous recipes cover how to work with text inputs; we may want to enforce some inputes to contain only numerical
values. This is the use case for the Spinbox and Scale classes - both witdgets allow users to select a numerical value
from a range or a list of valid options, but trere are several differences in the way they are displayed and
# configured"""
# import tkinter as tk
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.spinbox = tk.Spinbox(self, from_=0, to=5)
#         self.scale = tk.Scale(self, from_=0, to=5, orient=tk.HORIZONTAL, resolution=0.2)  # default resolution is 1
#         self.btn = tk.Button(self, text="Print values", command=self.print_values)
#         self.spinbox.pack()
#         self.scale.pack()
#         self.btn.pack()
#
#     def print_values(self):
#         print(f"Spinbox: {self.spinbox.get()}")
#         print(f"Scale: {self.scale.get()}")
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()


# Exemple 8
# Creating selections with radio buttons
"""With the Radiobutton, you can let user select among several options. This patter works well for a relatively small
number of mutally exclusive choices."""
# import tkinter as tk
#
# COLORS = [("Red", "red"), ("Green", "green"), ("Blue", "blue")]
#
#
# class ChoiceApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.var = tk.StringVar()
#         self.var.set("red")
#         self.buttons = [self.create_radio(c) for c in COLORS]
#         for button in self.buttons:
#             button.pack(anchor=tk.W, padx=10, pady=5)
#
#     def create_radio(self, option):
#         text, value = option
#         return tk.Radiobutton(self, text=text, value=value, command=self.print_option, variable=self.var)
#
#     def print_option(self):
#         print(self.var.get())
#
#
# if __name__ == "__main__":
#     app = ChoiceApp()
#     app.mainloop()

# Exemple 9
# Implementing switches with checkboxes
"""Choices between two alternatives are typycally implemented with checkboxes and lists of options where each choice
is independent from the rest. As we will see in the next example, these concepts can be implemented using the 
Checkbutton widget"""
# import tkinter as tk

# Variante 1
# class SwitchApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.var = tk.IntVar()
#         self.cb = tk.Checkbutton(self, text="Activate?",
#                                  variable=self.var,
#                                  command=self.print_value)
#         self.cb.pack()
#
#     def print_value(self):
#         print(self.var.get())
#
#
# if __name__ == "__main__":
#     app = SwitchApp()
#     app.mainloop()

# Variante 1
# class SwitchApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.var = tk.StringVar()
#         self.var.set("OFF")
#         self.cb = tk.Checkbutton(self, text="Activate?",
#                                  onvalue="ON", offvalue="OFF",
#                                  variable=self.var,
#                                  command=self.print_value)
#         self.cb.pack()
#
#     def print_value(self):
#         print(self.var.get())
#
#
# if __name__ == "__main__":
#     app = SwitchApp()
#     app.mainloop()

# Exemple 10
# Displaying a list of items
"""The Listbox widget contains text items that can be selected by the user with the mouse or keyboard. This selection
can be individual or multiple, depending on the widget configuration."""
# import tkinter as tk
#
# DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
# MODES = [tk.SINGLE, tk.BROWSE, tk.MULTIPLE, tk.EXTENDED]
#
#
# class ListApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.frame = tk.Frame(self)
#         self.scroll = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
#         self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
#
#         self.list = tk.Listbox(self)
#         self.list = tk.Listbox(self.frame, yscrollcommand=self.scroll.set)
#         self.list.insert(0, *DAYS)
#         self.print_btn = tk.Button(self, text="Print selection",
#                                    command=self.print_selection)
#         self.btns = [self.create_btn(m) for m in MODES]
#         self.scroll.config(command=self.list.yview)
#         self.frame.pack()
#         self.list.pack()
#
#         self.print_btn.pack(side=tk.BOTTOM, fill=tk.BOTH)
#         for btn in self.btns:
#             btn.pack(side=tk.LEFT)
#
#     def create_btn(self, mode):
#         cmd = lambda: self.list.config(selectmode=mode)
#         return tk.Button(self, command=cmd,
#                          text=mode.capitalize())
#
#     def print_selection(self):
#         selection = self.list.curselection()
#         print([self.list.get(i) for i in selection])
#
#
# if __name__ == "__main__":
#     app = ListApp()
#     app.mainloop()

# Exemple 11
# Handling mouse and keyboard events
"""Being able to react events is one of the most basic but important topics in GUI application develpment since it
determines how users can interact with the program.
Pressing keys of the keyboard and clicking with the mouse are some common type of events, which are automatically handled
in some Tkinter classes. For instance, this behavior is already implemented on the command option of the Button widget
class, which invokes the specified callback function.
Some events can get triggered without user interaction, such as changing the input focus programmatically from one widget
to another."""

# import tkinter as tk
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         frame = tk.Frame(self, bg="green", height=100, width=100)
#         frame.bind("<Button-1>", self.print_event)
#         frame.bind("<Double-Button-1>", self.print_event)
#         frame.bind("<ButtonRelease-1>", self.print_event)
#         frame.bind("<Button-2>", self.print_event)
#         frame.bind("<Button-3>", self.print_event)
#         frame.bind("<B1-Motion>", self.print_event)
#         frame.bind("<Enter>", self.print_event)
#         frame.bind("<Leave>", self.print_event)
#         frame.pack(padx=50, pady=50)
#
#     def print_event(self, event):
#         position = "(x={}, y={})".format(event.x, event.y)
#         print(event.type, "event", position)
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

"""The following example contains an Entry widtet with a couple of bindings; one for the event that gets triggered when
the entry gets the focus, and another for all the key press events:"""
# import tkinter as tk
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         entry = tk.Entry(self)
#         entry.bind("<FocusIn>", self.print_type)
#         entry.bind("<Key>", self.print_key)
#         entry.pack(padx=20, pady=20)
#
#     def print_type(self, event):
#         print(event.type)
#
#     def print_key(self, event):
#         args = event.keysym, event.keycode, event.char
#         print("Symbol: {}, Code: {}, Char: {}".format(*args))
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

# Exemple 12
# Setting the main window's icon, title, and size
# """The Tk instance differs from normal widgets in the way that it is configured, so we will explore some basic methods
# that allow us to customize how it is displayed."""
# import tkinter as tk
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("My Tkinter App")
#         self.iconbitmap("python.ico")
#         self.geometry("400x200+10+10")  # make the application 400x200 at position 10,10
#         # self.state("zoomed") # make the application fullscreen
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()


##################################
# 2 - Window Layout              #
##################################
# import tkinter as tk
#
#
# class ListFrame(tk.Frame):
#     def __init__(self, master, items=[]):
#         super().__init__(master)
#         self.list = tk.Listbox(self)
#         self.scroll = tk.Scrollbar(self, orient=tk.VERTICAL,
#                                    command=self.list.yview)
#         self.list.config(yscrollcommand=self.scroll.set)
#         self.list.insert(0, *items)
#         self.list.pack(side=tk.LEFT)
#         self.scroll.pack(side=tk.LEFT, fill=tk.Y)
#
#     def pop_selection(self):
#         index = self.list.curselection()
#         if index:
#             value = self.list.get(index)
#             self.list.delete(index)
#             return value
#
#     def insert_item(self, item):
#         self.list.insert(tk.END, item)
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         months = ["January", "Frebruary", "March", "April", "May", "June", "July", "August", "September", "October",
#                   "November", "December"]
#         self.frame_a = ListFrame(self, months)
#         self.frame_b = ListFrame(self)
#         self.btn_right = tk.Button(self, text=">", command=self.move_right)
#         self.btn_left = tk.Button(self, text="<", command=self.move_left)
#         self.frame_a.pack(side=tk.LEFT, padx=10, pady=10)
#         self.frame_b.pack(side=tk.RIGHT, padx=10, pady=10)
#         self.btn_right.pack(expand=True, ipadx=5)
#         self.btn_left.pack(expand=True, ipadx=5)
#
#     def move_right(self):
#         self.move(self.frame_a, self.frame_b)
#
#     def move_left(self):
#         self.move(self.frame_b, self.frame_a)
#
#     def move(self, frame_from, frame_to):
#         value = frame_from.pop_selection()
#         if value:
#             frame_to.insert_item(value)
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

# Exemple 12
# Using the Pack geometry manager
"""In previous recipes, we have seen that creating a widget does not automatically display it on the scrren. We have
called the pack() method on each widget to do so, which means that we used the Pack geometry manager.
This one of the three available geometry managers in Tkinter, and it is well suited for simple layouts, such as when
you want to place all the widgets on top of each other or side by side."""
# import tkinter as tk
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         label_a = tk.Label(self, text="Label A", bg="yellow")
#         label_b = tk.Label(self, text="Lable B", bg="orange")
#         label_c = tk.Label(self, text="Lable C", bg="red")
#         label_d = tk.Label(self, text="Label D", bg="green")
#         label_e = tk.Label(self, text="Label E", bg="blue")
#
#         opts = {'ipadx': 10, 'ipady': 10, 'fill': tk.BOTH}
#         label_a.pack(side=tk.TOP, **opts)
#         label_b.pack(side=tk.TOP, **opts)
#         label_c.pack(side=tk.LEFT, **opts)
#         label_d.pack(side=tk.LEFT, **opts)
#         label_e.pack(side=tk.LEFT, **opts)
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

# Exemple 13
# Using the Grid geometry manager
"""The Grid geometry manager is considered the more versatile of the three geometry managers. It directly reassembles
the grid concept that is commonly used in user interface design a two-dimensional table difvided into rows and columns,
 where each cell represents the space available for a widget."""
# import tkinter as tk
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         label_a = tk.Label(self, text="Label A", bg="yellow")
#         label_b = tk.Label(self, text="Label B", bg="orange")
#         label_c = tk.Label(self, text="Label C", bg="red")
#         label_d = tk.Label(self, text="Label D", bg="green")
#         label_e = tk.Label(self, text="Label E", bg="blue")
#
#         opts = {'ipadx': 10, 'ipady': 10, 'sticky': 'nswe'}
#         label_a.grid(row=0, column=0, **opts)
#         label_b.grid(row=1, column=0, **opts)
#         label_c.grid(row=0, column=1, rowspan=2, **opts)
#         label_d.grid(row=0, column=2, rowspan=2, **opts)
#         label_e.grid(row=2, column=0, columnspan=3, **opts)
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

# Exemple 14
# Using the Place Geometry manager
"""The Place geometry manager allows you to set the position and size of a widget in absolute terms, or in relative terms
to another one.
Of the three geometry managers, it is the least commonly used one. On the other hand, it can fit some complex scenarios
where you want to freely position a widget or overlap a previously placed one."""
# import tkinter as tk
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         label_a = tk.Label(self, text="Label A", bg="yellow")
#         label_b = tk.Label(self, text="Label B", bg="orange")
#         label_c = tk.Label(self, text="Label C", bg="red")
#         label_d = tk.Label(self, text="Label D", bg="green")
#         label_e = tk.Label(self, text="Label E", bg="blue")
#
#         label_a.place(relwidth=0.25, relheight=0.25)
#         label_b.place(x=100, anchor=tk.N, width=100, height=50)
#         label_c.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.5, relheight=0.5)
#         label_d.place(in_=label_c, anchor=tk.NW, x=48, y=48, relwidth=0.5, relheight=0.5)
#         label_e.place(x=200, y=200, anchor=tk.SE, relwidth=0.25, relheight=0.25)
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()


# Exemple 15
# Grouping inputs with the LabelFrame widget
"""The LabelFrame class can be used to group multiple input widgets, indicating the logical entity with a label they
represent. It is typically used in forms and is very similar to the Frame widget."""
# import tkinter as tk
#
#
# def print_info(value):
#     print(value)
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         group_1 = tk.LabelFrame(self, padx=15, pady=10,
#                                 text="Personal Information")
#         group_1.pack(padx=10, pady=5)
#
#         tk.Label(group_1, text="First name").grid(row=0)
#         tk.Label(group_1, text="Last name").grid(row=1)
#         self.first_name = tk.Entry(group_1)
#         self.first_name.grid(row=0, column=1, sticky=tk.W)
#         self.last_name = tk.Entry(group_1)
#         self.last_name.grid(row=1, column=1, sticky=tk.W)
#
#         group_2 = tk.LabelFrame(self, padx=15, pady=10,
#                                 text="Address")
#         group_2.pack(padx=10, pady=5)
#
#         tk.Label(group_2, text="Street").grid(row=0)
#         tk.Label(group_2, text="City").grid(row=1)
#         tk.Label(group_2, text="ZIP Code").grid(row=2)
#         self.street_name = tk.Entry(group_2)
#         self.street_name.grid(row=0, column=1, sticky=tk.W)
#         self.city_name = tk.Entry(group_2)
#         self.city_name.grid(row=1, column=1, sticky=tk.W)
#         self.ZipCode = tk.Entry(group_2, width=8)
#         self.ZipCode.grid(row=2, column=1, stick=tk.W)
#
#         self.btn_submit = tk.Button(self, text="Print info", command=self.print_info)
#         self.btn_submit.pack(padx=10, pady=10, side=tk.RIGHT)
#
#     def print_info(self):
#         print("{}".format(self.first_name.get()))
#         print("{}".format(self.last_name.get()))
#         print("")
#         print("{}".format(self.street_name.get()))
#         print("{}".format(self.city_name.get()))
#         print("{}".format(self.ZipCode.get()))
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

# Dynamically laying out widgets
"""The Grid geometry manager is easy to use both in simple and advanced layouts, and it is also a powerful mechinism
to combine with a list of widgets.
We will take a look at how we can reduce the number of lines and calle the geometry manager methodes with just a few
lines, thanks to list comprehension and the zip and enumerate built-in functions."""

# Getting Ready
"""The application we will build contains four Entry widgets, each one with its corresponding label that indicates the 
meaning of the input. We will also add a button to print all the entries' value.
Instead of creating and assigning each widget to a separate attribute, we will work with lists of widgets. Since we will
track the index while iterating over these lists, we can easily invoke the grid() method with the appropriate column
option."""

# How to do it
"""We will aggregate the lists of labels and entries with the zip function. The button will be created and displayed 
individually, as it does not share any option with the rest of the widgets:"""
# import tkinter as tk
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         fields = ["First name", "Last name", "Phone", "Email"]
#         labels = [tk.Label(self, text=f) for f in fields]
#         entries = [tk.Entry(self) for _ in fields]
#         self.widgets = list(zip(labels, entries))
#         self.submit = tk.Button(self, text="Print info", command=self.print_info)
#
#         for i, (label, entry) in enumerate(self.widgets):
#             label.grid(row=i, column=0, padx=10, sticky=tk.W)
#             entry.grid(row=i, column=1, padx=10, pady=5)
#         self.submit.grid(row=len(fields), column=1, sticky=tk.E,
#                          padx=10, pady=10)
#
#     def print_info(self):
#         for label, entry in self.widgets:
#             print("{} = {}".format(label.cget("text"), entry.get()))
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

# Exemple 16
# Creating horizontal and vertical scrollbars
"""In Tkinter, geometry managers take all the necessary space to fit all the widget in their parent container. However, 
if the container has a fixed size or exceeds the screen's size, there will be a region that will not be visible to users.

Scroll bar widget are not automatically added in Tkinter, so you must create and lay them out as any other type of
widget. Another consideration is that only a few widget classes have the configuration options that make it possible to
connect them to a scrollbar.

To work around this, you will learn to take advantage of the flexibility of the Canvas widget to make any container
scrollable.
"""

# Getting ready
"""To demonstrate the combination of the Canvas and Scrollbar classes to create a resizable and scrollable frame, we
will build an application that dynamically changes its size by loading an image.

When the Load image button is clicked, it removes itself and loads an image into the Canvas that is larger than the 
scrollable region for this eexample, we used a predefined image, but you can modify this program to select any other GIF 
image with a file dialog

This enables the horizontal and vertical scrollbars, which automatically adjust themselves if the main window is 
resized"""

# How to do it
"""When we will dive into the functionality of the Canvas widget in a separate chapter, this application will 
introduce its standard scroll interface and the create_window() method. Note that this script requires the file
python.gif to be placed in the same directory"""
# import tkinter as tk
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.scroll_x = tk.Scrollbar(self, orient=tk.HORIZONTAL)
#         self.scroll_y = tk.Scrollbar(self, orient=tk.VERTICAL)
#         self.canvas = tk.Canvas(self, width=300, height=100,
#                                 xscrollcommand=self.scroll_x.set,
#                                 yscrollcommand=self.scroll_y.set)
#         self.scroll_x.config(command=self.canvas.xview)
#         self.scroll_y.config(command=self.canvas.yview)
#
#         self.frame = tk.Frame(self.canvas)
#         self.btn = tk.Button(self.frame, text="Load image", command=self.load_image)
#         self.btn.pack()
#         self.canvas.create_window((0, 0), window=self.frame,
#                                   anchor=tk.NW)
#         self.canvas.grid(row=0, column=0, sticky="nswe")
#         self.scroll_x.grid(row=1, column=0, sticky="we")
#         self.scroll_y.grid(row=0, column=1, sticky="ns")
#
#         self.rowconfigure(0, weight=1)
#         self.columnconfigure(0, weight=1)
#         self.bind("<Configure>", self.resize)
#         self.update_idletasks()
#         self.minsize(self.winfo_width(), self.winfo_height())
#
#     def resize(self, event):
#         region = self.canvas.bbox(tk.ALL)
#         self.canvas.configure(scrollregion=region)
#
#     def load_image(self):
#         self.btn.destroy()
#         self.image = tk.PhotoImage(file="python.gif")
#         tk.Label(self.frame, image=self.image).pack()
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

###########################
# 3 - Customizing Widgets #
###########################
"""In this chapter, we will cover the following recipes:
    * Working with colors
    * Setting widget fonts
    * Using the options database
    * Changing the cursor icon
    * Introducing the Text widget
    * Adding tags to the Text widget
"""
# Introduction
"""By default Tkinter widets will display with a native look and feel. While this standard appearance could be enough
for quick prototyping, we might want to customize some widget attributes, such as font, color, and background.

This customization does not affect only the widets itself, vut also its inner items. We will dive into the Text widget,
which along with the Canvas widget is one of the most versatile Tkinter classes. The Text widget represents a multiline
text area with formatted content, with several methods that make it possible to format characters or lines and add
event-specific event bindings."""

# Exemple 17
# Working with colors
"""In previous recipes, we have set the colors of a widget using color names, such as white, blue, or yellow. These 
value are passed as string to the foreground and bacground options, which modify the widget's text and background 
colors.

Color names are internally mapped to RGB value (an additive model that respresent a color by it combination of red, 
green, and blue intensities), and this translation is based on a tables that is platform-dependent. Therefore, if you
want to consitently display the same color in different platforms, you can pass the RGB value to widget options."""

# from functools import partial
# import tkinter as tk
# from tkinter.colorchooser import askcolor
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Colors demo")
#         text = "The quick brown for jumps over the lazy dog"
#         self.label = tk.Label(self, text=text)
#         self.fg_btn = tk.Button(self, text="Set foreground color",
#                                 command=partial(self.set_color, "fg"))
#         self.bg_btn = tk.Button(self, text="Set Background color",
#                                 command=partial(self.set_color, "bg"))
#         self.label.pack(padx=20, pady=20)
#         self.fg_btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#         self.bg_btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#
#     def set_color(self, option):
#         color = askcolor()[1]
#         print("Chosen color:", color)
#         self.label.config(**{option: color})
#         print({**{option: color}})
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()


# Exemple 18
# Setting widget fonts
"""In Tkinter, it is possible to customize the font used in widgets that display text to the users, such as buttons, 
labels and entries. By default, the font is system-specific, but you can change it using the font option."""

# import tkinter as tk
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Font Demo")
#         text = "The quick brown fox jumps over the lazy dog"
#         self.label = tk.Label(self, text=text)
#
#         self.family = tk.StringVar()
#         self.family.trace("w", self.set_font)
#         families = ("Times", "Courier", "Helvetica")
#         self.option = tk.OptionMenu(self, self.family, *families)
#
#         self.size = tk.StringVar()
#         self.size.trace("w", self.set_font)
#         self.spinbox = tk.Spinbox(self, from_=8, to=18, textvariable=self.size)
#
#         self.family.set(families[0])
#         self.size.set("10")
#         self.label.pack(padx=20, pady=20)
#         self.option.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#         self.spinbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#
#     def set_font(self, *args):
#         family = self.family.get()
#         size = self.size.get()
#         self.label.config(font=(family, size))
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()


# Exemple 19
# Using the options database
"""Tkinter defines a concept called option database, a mechanism used to customize the appearance of the application
without having to specify it for each widget. It allows you to decouple some widget options from the individual widget
configuration, providing standardize defaults based on the widget hierarchy."""
# import tkinter as tk
# import tkinter.messagebox as mb
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("option demo")
#         self.option_add("*font", "helvetica 10")
#         self.option_add("*header.font", "helvetica 18 bold")
#         self.option_add("*subtitle.font", "helvetica 14 italic")
#         self.option_add("*Button.foreground", "blue")
#         self.option_add("*Button.background", "white")
#         self.option_add("*Button.activeBackground", "gray")
#         self.option_add("*Button.activeForeground", "black")
#
#         self.create_label(name="header", text="This is the header")
#         self.create_label(name="subtitle", text="This is the subtitle")
#         self.create_label(text="This is a paragraph")
#         self.create_label(text="This is another paragraph")
#         self.create_button_1(text="See more")
#         self.create_button_2(text="Quit")
#
#     def create_label(self, **options):
#         tk.Label(self, **options).pack(padx=20, pady=5, anchor=tk.E)
#
#     def create_button_1(self, **options):
#         tk.Button(self, **options, command=self.info_button).pack(padx=5, pady=5, side=tk.LEFT, anchor=tk.W)
#
#     def create_button_2(self, **options):
#         tk.Button(self, **options, command=self.quit).pack(padx=5, pady=5, side=tk.RIGHT, anchor=tk.E)
#
#     def info_button(self):
#         text = "This is a graphical user interface's demo"
#         mb.showinfo('Information', message=text)
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

# Exemple 20
# Changing the cursor icon
"""Tkinter allows you to customize the cursor icon while hovering over a widget. This behavior is sometimes enabled by
default, like the Entry widget that displays an-I-beam pointer."""
# import tkinter as tk
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Cursors demo")
#         self.resizable(0, 0)
#         self.label = tk.Label(self, text='Click the button to start')
#         self.btn_launch = tk.Button(self, text="Start!",
#                                     command=self.perform_action)
#         self.btn_help = tk.Button(self, text="Help",
#                                   cursor="question_arrow")
#         btn_opts = {"side": tk.LEFT, "expand": True, "fill": tk.X, "ipadx": 30, "padx": 20, "pady": 5}
#         self.label.pack(pady=10)
#         self.btn_launch.pack(**btn_opts)
#         self.btn_help.pack(**btn_opts)
#
#     def perform_action(self):
#         self.config(cursor="watch")
#         self.btn_launch.config(state=tk.DISABLED)
#         self.btn_help.config(state=tk.DISABLED)
#         self.label.config(text="Working...")
#         self.after(3000, self.end_action)
#
#     def end_action(self):
#         self.config(cursor="arrow")
#         self.btn_launch.config(state=tk.NORMAL)
#         self.btn_help.config(state=tk.NORMAL)
#         self.label.config(text="Done!")
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()


# Exemple 21
# Introducing the text widget
"""The Text widget offers an advanced functionality compared with other widget classes. It displays multiple lines of
editable text that can be indexed by lines and columns. Additionally, you can refer to ranges of text using tags,
which may define a customized appearance and behavior."""
# import tkinter as tk
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Text Demo")
#         self.resizable(0, 0)
#         self.text = tk.Text(self, width=50, height=10)
#         self.btn_clear = tk.Button(self, text="Clear text",
#                                    command=self.clear_text)
#         self.btn_insert = tk.Button(self, text="Insert text",
#                                     command=self.insert_text)
#         self.btn_print = tk.Button(self, text="Print selection",
#                                    command=self.print_selection)
#         self.text.pack()
#         self.btn_clear.pack(side=tk.LEFT, expand=True, pady=10)
#         self.btn_insert.pack(side=tk.LEFT, expand=True, pady=10)
#         self.btn_print.pack(side=tk.LEFT, expand=True, pady=10)
#
#     def clear_text(self):
#         self.text.delete("1.0", tk.END)
#
#     def insert_text(self):
#         self.text.insert(tk.INSERT, "Hello, world")
#
#     def print_selection(self):
#         selection = self.text.tag_ranges(tk.SEL)
#         if selection:
#             content = self.text.get(*selection)
#             print(content)
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()


# Exemple 22
# Adding tags to the Text widget
"""In this recipe, you will learn how to configure the behavior of a tagged range of characters within a Text widget.
All the concepts are the same as those that apply to regular widgets, such as event sequences or configuration options,
which have already been covered in previous recipes. The main difference is that  we need to work with the text indices 
to identify the tagged content, instead of using object references."""
# import tkinter as tk
# import webbrowser
# from urllib.parse import urlparse
#
#
# def validate_hperlink(url):
#     return urlparse(url).netloc
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Text tags demo")
#         self.text = tk.Text(self, width=50, height=10)
#         self.btn_link = tk.Button(self, text="Add hyperling",
#                                   command=self.add_hyperlink)
#         self.text.tag_config("link", foreground="blue", underline=1)
#         self.text.tag_bind("link", "<Button-1>", self.open_link)
#         self.text.tag_bind("link", "<Enter>", lambda _: self.text.config(cursor="hand2"))
#         self.text.tag_bind("link", "<Leave>", lambda e: self.text.config(cursor=""))
#
#         self.text.pack()
#         self.btn_link.pack(expand=True)
#
#     def add_hyperlink(self):
#         selection = self.text.tag_ranges(tk.SEL)
#         if selection:
#             self.text.tag_add("link", *selection)
#
#     def open_link(self, event):
#         position = "@{}, {} + 1c".format(event.x, event.y)
#         index = self.text.index(position)
#         prevrange = self.text.tag_prevrange("link", index)
#         url = self.text.get(*prevrange)
#         webbrowser.open(url)
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()


#########################
# 4 - Dialogs and Menus #
#########################
"""In this chapter, we will cover the following recpes:
+ Showing alert dialogs
+ Asking for user confimation
+ Choosing files and directories
+ Saving data into a file
+ Creating a menu bar
+ Using variables in menus
+ Displaying context menus
+ Opening a secondary window
+ Passing variables between windows
+ Handling window deletion
"""

# Introduction
"""Almost every nontrivial GUI application is composed of multiple views. In browsers, this is achiveved by navigating
from one HTML page to another, and in desktop applications, it is represented by multiple windows and dialogs that users 
can interact with.

So far, we have learned how to create only a root window, which is associated with the Tcl interpreter. However, Tkinter
allows us to create multiple top-level windows under the same application, and it also includeds specicfic modules with
built-in dialogs.
Another way to structure how to navigate in your application in using menus, which are usually displayed under the litle
bar in desktop applications. In Tkinter, these menus are represented by a widget class; we will dive later into its
methods and how to integrate it with the rest of our application.
"""

# Exemple 23
# Showing alert dialogs
"""A common use case for dialogs is notifying users of events that occured in our application, such as that a record has
been saved, or that it failed to open a file. We will now take a look at some of the basic functions included in Tkinter
to display informational dialogs."""

# import tkinter as tk
# import tkinter.messagebox as mb
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         btn_info = tk.Button(self, text="Show Info",
#                              command=self.show_info)
#         btn_warn = tk.Button(self, text="Show Warning",
#                              command=self.show_warning)
#         btn_error = tk.Button(self, text="Show Error",
#                               command=self.show_error)
#         opts = {'padx': 40, 'pady': 5, 'expand': True, 'fill': tk.BOTH}
#         btn_info.pack(**opts)
#         btn_warn.pack(**opts)
#         btn_error.pack(**opts)
#
#     def show_info(self):
#         msg = "Your user preference have been saved"
#         mb.showinfo("Information", msg)
#
#     def show_warning(self):
#         msg = "Temporary files have not been correctly removed"
#         mb.showwarning("Warning", msg)
#
#     def show_error(self):
#         msg = "The application has encountered an unknown error"
#         mb.showerror("Error", msg)
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

# Exemple 24
# Asking for user confirmation
"""Other types of ialogs included in Tkinter are those used to ask for user confirmation, such as the ones shown when
we want to save a file and are about to override an existing one with the soame name.

These dialogs differ from the preceding one because the values returned byt the functions will depend on the confirmation
button clicked by the user. This way, we can interact with the program to indicate whether to continue or cancel the
action.
"""
# import tkinter as tk
# import tkinter.messagebox as mb
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.create_button(mb.askyesno, "Ask Yes/No",
#                            "Return True or False")
#         self.create_button(mb.askquestion, "Ask a question",
#                            "Returns 'Yes' or 'No'")
#         self.create_button(mb.askretrycancel, "Ask Retry/Cancle",
#                            "Returns True or False")
#         self.create_button(mb.askyesnocancel, "Ask Yes/No/Cancel",
#                            "Returns True, False or None")
#
#     def create_button(self, dialog, title, message):
#         command = lambda: print(dialog(title, message))
#         btn = tk.Button(self, text=title, command=command)
#         btn.pack(padx=40, pady=5, expand=True, fill=tk.BOTH)
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

# Exemple 25
# Choosing files and directories
"""File dialogs allow users to select one or multiple files from the filesystem. In Tkinter, these functions are
declared in the tkinter.filedialog module, wich also includes dialogs for choosing directories. It also lets you 
customize the behavior of a new dialog, such as filtering the files by their extension or choosing the initial displayed
by the dialog.
"""
# import tkinter as tk
# import tkinter.filedialog as fd
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         btn_file = tk.Button(self, text="Choose file",
#                              command=self.choose_file)
#         btn_dir = tk.Button(self, text="Choose directory",
#                             command=self.choose_directory)
#         btn_file.pack(padx=60, pady=10)
#         btn_dir.pack(padx=60, pady=10)
#
#     def choose_file(self):
#         filetypes = (("Plain text files", "*.txt"),
#                      ("images", "*.jpg *.gif *.png"),
#                      ("All files", "*"))
#         filename = fd.askopenfilename(title="Open file", initialdir="/", filetypes=filetypes)
#         if filename:
#             print(filename)
#
#     def choose_directory(self):
#         directory = fd.askdirectory(title="Open directory", initialdir="/")
#         if directory:
#             print(directory)
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()


# Exemple 26
# Saving data into a file
"""Apart from selecting existing files and directories, it is also possible to create a new file using Tkinter dialogs.
They can used to persist data generated by our application, letting users choose the name and locaton of the new file.
"""

# import tkinter as tk
# import tkinter.filedialog as fd
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.text = tk.Text(self, height=10, width=50)
#         self.btn_save = tk.Button(self, text="Save",
#                                   command=self.save_file)
#         self.text.pack()
#         self.btn_save.pack(pady=10, ipadx=5)

# # asksaveasfile returns a file object instead of a string, named asksavefile.
# # def save_file(self):
#     contents = self.text.get(1.0, tk.END)
#     new_file = fd.asksaveasfile(title="Save file",
#                                     defaultextension=".txt",
#                                     filetypes=(("Text files", "*.txt"),))
#
#     print(new_file)
#     if new_file:
#         new_file.write(contents)
#         new_file.close()

# # asksaveasfilename returns the path of the selected file. You can use this function if you want to modify the path
# # or perform any validation before opening the file for writing.
# def save_file(self):
#     contents = self.text.get(1.0, tk.END)
#     new_file = fd.asksaveasfilename(title="Save file",
#                                     defaultextension=".txt",
#                                     filetypes=(("Text files", "*.txt"),))
#     print(new_file)
#
#     with open(new_file, 'w') as f:
#         f.write(contents)
#         f.close()


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

# Exemple 27
# Creating a menu bar
"""Complex GUIs typically use menu bars to organize the actions and navigations that are available in our application.
This pattern is also used to group operations that are closely related, such as the File menu included in most text 
editors.

Tkinter natively supports these menus, which are displayed with the look and feel of the target destkop environment.
Therefore, you do not have to simulate them with frames or labels, because you would lose the cross-platform features
that have already been built into Tkinter.
"""

# import tkinter as tk
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         menu = tk.Menu(self)
#         file_menu = tk.Menu(menu, tearoff=0)
#
#         file_menu.add_command(label="New file")
#         file_menu.add_command(label="Open")
#         file_menu.add_separator()
#         file_menu.add_command(label="Save")
#         file_menu.add_command(label="Save as...")
#
#         menu.add_cascade(label="File", menu=file_menu)
#         menu.add_command(label="About")
#         menu.add_command(label="Quit", command=self.destroy)
#         self.config(menu=menu)
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

# Exemple 28
# Using varialbles in menus
"""Apart from calling commands and nesting submenus, it is also possible to connect Tkinter variables to menu entries
"""
# import tkinter as tk
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.checked = tk.BooleanVar()
#         self.checked.trace('w', self.mark_checked)
#         self.radio = tk.StringVar()
#         self.radio.set("1")
#         self.radio.trace("w", self.mark_radio)
#         menu = tk.Menu(self)
#         submenu = tk.Menu(menu, tearoff=0)
#         submenu.add_checkbutton(label="Checkbutton", onvalue=True,
#                                 offvalue=False, variable=self.checked)
#         submenu.add_separator()
#         submenu.add_radiobutton(label="Radio 1", value="1",
#                                 variable=self.radio)
#         submenu.add_radiobutton(label="Radio 2", value="2",
#                                 variable=self.radio)
#         submenu.add_radiobutton(label="Radio 3", value="3",
#                                 variable=self.radio)
#
#         menu.add_cascade(label="Options", menu=submenu)
#         menu.add_command(label="Quit", command=self.destroy)
#         self.config(menu=menu)
#
#     def mark_checked(self, *args):
#         print(self.checked.get())
#
#     def mark_radio(self, *args):
#         print(self.radio.get())
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

# Exemple 29
# Displaying context menus
"""Tkinter menus do not necessarily have to be located on the menu bar, but they can actually be freely placed at any
coordinate. These types of menus are called context menus, and they are usually displayed when users right-click on an 
itm.

Context menus are widely used in GUI applications; for instance, file browsers display them to offer the available 
operations over the selected file, so its intuitive for users to know how to interact with them.
"""
# import tkinter as tk
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.menu = tk.Menu(self, tearoff=0,
#                             postcommand=self.enable_selection)
#         self.menu.add_command(label="Cut", command=self.cut_text)
#         self.menu.add_command(label="Copy", command=self.copy_text)
#         self.menu.add_command(label="Paste", command=self.paste_text)
#         self.menu.add_command(label="Delete", command=self.delete_text)
#
#         self.text = tk.Text(self, height=10, width=50)
#         self.text.bind("<Button-3>", self.show_popup)
#         self.text.pack()
#
#     def show_popup(self, event):
#         self.menu.post(event.x_root, event.y_root)
#
#     def cut_text(self):
#         self.copy_text()
#         self.delete_text()
#
#     def copy_text(self):
#         selection = self.text.tag_ranges(tk.SEL)
#         if selection:
#             self.clipboard_clear()
#             self.clipboard_append(self.text.get(*selection))
#
#     def paste_text(self):
#         try:
#             self.text.insert(tk.INSERT, self.clipboard_get())
#         except tk.TclError:
#             pass
#
#     def delete_text(self):
#         selection = self.text.tag_ranges(tk.SEL)
#         if selection:
#             self.text.delete(*selection)
#
#     def enable_selection(self):
#         state_selection = tk.ACTIVE if self.text.tag_ranges(tk.SEL) else tk.DISABLED
#         state_clipboard = tk.ACTIVE
#         try:
#             self.clipboard_get()
#         except tk.TclError:
#             state_clipboard = tk.DISABLED
#
#         self.menu.entryconfig(0, state=state_selection) # Cut
#         self.menu.entryconfig(1, state=state_selection) # Copy
#         self.menu.entryconfig(2, state=state_clipboard) # Paste
#         self.menu.entryconfig(3, state=state_selection) # Delete
#
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()


# Exemple 30
# Opening a secondary window
"""The root Tk instance represents the main window of our GUI - when it is destroyed, the application quits and the
event mainloop finishes.

However, there is another Tkinter class to create additional top-level windows in our application, called Toplevel. You
can use this class to display any kind of window, from custom dialog to wizard forms.
"""
# import tkinter as tk
#
#
# class Window(tk.Toplevel):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.label = tk.Label(self, text="This is another window")
#         self.button = tk.Button(self, text="Close", command=self.destroy)
#         self.label.pack(padx=20, pady=20)
#         self.button.pack(pady=5, ipadx=2, ipady=2)
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.btn = tk.Button(self, text="Open new window",
#                              command=self.open_window)
#         self.btn.pack(padx=50, pady=20)
#
#     def open_window(self):
#         window = Window(self)
#         window.grab_set()
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()


# Exemple 31
# Handling window deletion
"""Under some circunstances, you might want to perform an action before the user closes a top-level window, 
for instance, to prevent you losing unsaved work.Tkinter allows you to intercept this type of event to conditionally
destroy the window.
"""
# import tkinter as tk
# import tkinter.messagebox as mb
#
#
# class Window(tk.Toplevel):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.protocol("WM_DELETE_WINDOW", self.confirm_delete)
#
#         self.label = tk.Label(self, text="This is another window")
#         self.button = tk.Button(self, text="Close",
#                                 command=self.destroy)
#         self.label.pack(padx=20, pady=20)
#         self.button.pack(pady=5, ipadx=2, ipady=2)
#
#     def confirm_delete(self):
#         message = "Are you sure you want to close this window?"
#         if mb.askyesno(message=message, parent=self):
#             self.destroy()
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.btn = tk.Button(self, text="Open new window",
#                              command=self.open_window)
#         self.btn.pack(padx=50, pady=20)
#
#     def open_window(self):
#         window = Window(self)
#         window.grab_set()
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

# Exemple 32
# Passing variables between windows
"""Two different windows may need to share information during program exection. While this data might be saved to disk
and read from the window that consumes it, in some circumstances it is more straightforward to handle it in memory and 
simply pass the information as variables.
"""
# import tkinter as tk
# from collections import namedtuple
#
# User = namedtuple("User", ["username", "password", "user_type"])
#
#
# class UserForm(tk.Toplevel):
#     def __init__(self, parent, user_type):
#         super().__init__(parent)
#
#         self.username = tk.StringVar()
#         self.password = tk.StringVar()
#         self.user_type = user_type
#
#         label = tk.Label(self, text="Create a new " + user_type.lower())
#         entry_name = tk.Entry(self, textvariable=self.username)
#         entry_pass = tk.Entry(self, textvariable=self.password)
#
#         btn = tk.Button(self, text="Submit", command=self.destroy)
#
#         label.grid(row=0, columnspan=2)
#         tk.Label(self, text="Username:").grid(row=1, column=0)
#         tk.Label(self, text="Password:").grid(row=2, column=0)
#         entry_name.grid(row=1, column=1)
#         entry_pass.grid(row=2, column=1)
#         btn.grid(row=3, columnspan=2)
#
#     def open(self):
#         self.grab_set()
#         self.wait_window()
#         username = self.username.get()
#         password = self.password.get()
#         return User(username, password, self.user_type)
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         user_types = ("Administrator", "Supervisor", "Regular user")
#         self.user_type = tk.StringVar()
#         self.user_type.set(user_types[0])
#
#         label = tk.Label(self, text="Please, select the type of user")
#         radios = [tk.Radiobutton(self, text=t, value=t, \
#                                  variable=self.user_type) for t in user_types]
#         btn = tk.Button(self, text="Create user", command=self.open_window)
#         label.pack(padx=10, pady=10)
#         for radio in radios:
#             radio.pack(padx=10, anchor=tk.W)
#         btn.pack(pady=10)
#
#     def open_window(self):
#         window = UserForm(self, self.user_type.get())
#         user = window.open()
#         print(user)
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()


###########################################
# 5 - Object-Oriented Programming and MVC #
###########################################
"""In this chatper, we will cover the following recipes:
    + Structuring our data wih a class
    + Composing widgets to display information
    + Reading records from a CSV file
    + Persisting data into a SQLite database
    + Refactoring using the MVC pattern
"""

# Introduction
"""So far, all our applications held data in memory as local variables or attributes. However, we also want to be able 
to persist information so that it is not lost when the program is closed.

In this chapter, we will discuss how to represent and display this data using object-oriented programming(OOP) 
principles and applying the Model-View-Controller(MVC) pattern. In short, this pattern proposes three components into
which we can divide our GUI: a model that holds the application data, a view that displays this data, and a controller 
that handles user events and connects the view with the model.

These concpts are related to how we manipulate and persist information, and in turn help us to imporve the organization
of our programs. Most of these recipes are not specific to Tkinter, and you can apply the same principles to other GUI
libraires."""

# Structuring our data with a class
"""We will take the example of a contact list application to illustrate how to model our data using Python classes. Even
though the user interface may offer lots of different functionalities, we will need to define what attributes represent
our domain model-in our case, each individual contact."""
import tkinter as tk
import tkinter.messagebox as mb
import re
from collections import namedtuple
import pandas as pd

import attr


# def required(value, message):
#     if not value:
#         raise ValueError(message)
#     return value


def matches(value, regex, message):
    if value and not regex.match(value):
        raise ValueError(message)
    return value


class Contact(object):
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    phone_regex = re.compile(r"\([0-9]{3}\)\s[0-9]{7}")

    def __init__(self, last_name, first_name, email, phone):
        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.phone = phone

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = required(value, "Last name is required")

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, value):
        self._email = matches(value, self.email_regex, "Invalid email format")


Contact.first_name = "John"  # Stores "John in contact._first_name
print(f"debug Contact.first_name: {Contact.first_name}")  # Reads "John" from contact._first_name
Contact.last_name = ""  # ValueError raised byt the required function

Contact = namedtuple("Contact", ["last_name", "first_name", "email", "phone"])

# Composing widgets to display information
"""It is difficult to build large applications if all the code is contained in a single class. By splitting the GUI code
 specific classes, we can modularize the structure of our program and create widgets with well-defined purposes."""


def required(message):
    def func(self, attr, val):
        if not val:
            raise ValueError(message)

    return func


def match(pattern, message):
    regex = re.compile(pattern)

    def func(self, attr, val):
        if val and not regex.match(val):
            raise ValueError(message)
        return func


@attr.s
class Contact(object):
    # last_name = attr.ib(validator=required("Last name is required"))
    # first_name = attr.ib(validator=required("First name is required"))
    # email = attr.ib(validator=match(r"[^@]+@[^@]+\.[^@]+", "Invalid email format"))
    # phone = attr.ib(validator=match(r"\([0-9]{3}\)\s[0-9]{7}", "Invalid phone format"))
    last_name = "Palleau"
    first_name = "Julien"
    email = "jpalleau@gmail.com"
    phone = "0493421980"


class ContactList(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)

        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insert(self, contact, index=tk.END):
        text = "{}, {}".format(contact.last_name, contact.first_name)
        self.lb.insert(index, text)

    def delete(self, index):
        self.lb.delete(index, index)

    def update(self, contact, index):
        self.delete(index)
        self.insert(contact, index)

    def bind_double_click(self, callback):
        print(f"DEBUG bind_double_click 1")
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)
        print(f"DEBUG bind_double_click 2")


"""To display and allow us to edit the detais of a contact, we will also create a specific form.
We will take the LableFrame widget as a base class, with a Lable and an Entry for field:"""


class ContactForm(tk.LabelFrame):
    fields = ("Last name", "First name", "Email", "Phone")

    def __init__(self, master, **kwargs):
        super().__init__(master, text="Contact", padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.create_field, enumerate(self.fields)))
        self.frame.pack()

    def create_field(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry

    @staticmethod
    def load_details(self, contact):
        print(f"debug load_details1 {contact}")
        # values = (contact.last_name, contact.first_name,
        #           contact.email, contact.phone)
        # for entry, value in zip(self.entries, values):
        #     print(f"debug load_details2 {value}")
        #     entry.delete(0, tk.END)
        #     entry.insert(0, value)

    def get_details(self):
        print(f"debug get_details")
        values = [e.get() for e in self.entries]
        try:
            return Contact(*values)
        except ValueError as e:
            mb.showerror("Validation error", str(e), parent=self)

    def clear(self):
        for entry in self.entries:
            entry.delete(0, tk.END)


# def load_contacts():
#     with open('contacts1.csv', encoding='utf-8', newline="") as f:
#         result = []
#         for r in csv.reader(f, delimiter=";"):
#             result += r
#         return [Contact(result) for r in csv.reader(f)]


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CSV Contact list")
        self.list = ContactList(self, height=12)
        self.form = ContactForm(self)
        self.contacts = self.load_contacts()

        for contact in self.contacts:
            self.list.insert(contact)

        print(f"debug contact {self.list}")
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(side=tk.LEFT, padx=10, pady=10)
        self.list.bind_double_click(self.show_contact)
        print(f"debug appel de show_contact")

    def load_contacts(self):
        with open('contacts1.csv', encoding='utf-8', newline="") as f:
            result = []
            for r in csv.reader(f, delimiter=";"):
                result += r
            return [Contact(*r) for r in csv.reader(f)]

    def show_contact(self, index):
        print(f"show_contact 1 {index}")
        contact = self.contacts[index]
        self.form.load_details(contact)
        print(f"show_contact 2")


if __name__ == "__main__":
    app = App()
    app.mainloop()
