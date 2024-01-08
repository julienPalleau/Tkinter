# https://www.youtube.com/watch?v=0tM-l_ZsxjU
# https://ttkbootstrap.readthedocs.io/en/latest/gettingstarted/tutorial/
# import sys
# print(sys.version)

# import tkinter as tk
# import ttkbootstrap as ttk
# from ttkbootstrap.constants import *
#
# root = tk.Tk()
#
# b1 = ttk.Button(root, text="Button 1", bootstyle=SUCCESS)
# b1.pack(side=LEFT, padx=5, pady=10)
#
# b2 = ttk.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE))
# b2.pack(side=LEFT, padx=5, pady=10)
#
# root.mainloop()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Labels and Buttons
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# # https://www.youtube.com/watch?v=0tM-l_ZsxjU&t=547s
# from tkinter import *
# from ttkbootstrap.constants import *
# import ttkbootstrap as tb
#
# root = tb.Window(themename="superhero")
# # root = Tk()
# root.title("TTK Bootstrap!")
# root.iconbitmap()
# root.geometry('500x350')
#
# # Create a Function for the Button
# counter = 0
#
#
# def changer():
#     global counter
#     counter += 1
#     if counter % 2 == 0:
#         my_label.config(text="Hello World!")
#     else:
#         my_label.config(text="Goodbye World!")
#
#
# # Create a Function for the Button
#
# # Colors:
# # Default, primary, secondary, success, info, warning, danger, light, dark
#
# # Create a Label
# my_label = tb.Label(text="Hello World!", font=("Helvetica", 28), bootstyle="danger")
# my_label.pack(pady=50)
#
# # Create a Button
# my_button = tb.Button(text="Click Me!", bootstyle="success, outline", command=changer)
# my_button.pack(pady=20)
#
# root.mainloop()


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Labels and Buttons
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# # https://www.youtube.com/watch?v=0tM-l_ZsxjU&t=1199s
#
# from tkinter import *
# import ttkbootstrap as tb
#
# root = tb.Window(themename="superhero")
#
# # root = Tk()
# root.title("TTK Bootstrap!")
# root.iconbitmap()
# root.geometry('500x350')
#
#
# def checker():
#     if var1.get() == 1:
#         my_label.config(text="Checked1!")
#         print(f"test var1: {var1.get()}")
#     elif var1.get() == 0:
#         my_label.config(text="UnChecked1!")
#         print(f"test var1: {var1.get()}")
#     elif var2.get() == 1:
#         my_label.config(text="Checked2!")
#         print(f"test var2: {var2.get()}")
#     elif var2.get() == 0:
#         my_label.config(text="UnChecked2!")
#         print(f"test var2: {var2.get()}")
#     elif var3.get() == 1:
#         my_label.config(text="Checked!")
#     elif var3.get() == 0:
#         my_label.config(text="UnChecked!")
#     elif var4.get() == 1:
#         my_label.config(text="Checked!")
#     elif var4.get() == 0:
#         my_label.config(text="UnChecked!")
#     elif var5.get() == 1:
#         my_label.config(text="Checked!")
#     else:
#         my_label.config(text="UnChecked!")
#
#
# # Label
# my_label = Label(text="Click the checkbutton below", font=("Helvetica", 18))
# my_label.pack(pady=(40, 10))
#
# # CheckButton
# var1 = IntVar()
# print("var1")
# my_check = tb.Checkbutton(bootstyle="primary",
#                           text="Check Me Out!",
#                           variable=var1,
#                           onvalue=1,
#                           offvalue=0,
#                           command=checker)
# my_check.pack(pady=10)
#
# # ToolButton
# var2 = IntVar()
# print("var2")
# my_check2 = tb.Checkbutton(bootstyle="danger, toolbutton",
#                            text="ToolButton!!",
#                            variable=var2,
#                            onvalue=1,
#                            offvalue=0,
#                            command=checker)
# my_check2.pack(pady=10)
#
# # Outlines Toolbutton
# var3 = IntVar()
# my_check3 = tb.Checkbutton(bootstyle="danger, toolbutton, outline",
#                            text="Outlined ToolButton!!",
#                            variable=var3,
#                            onvalue=1,
#                            offvalue=0,
#                            command=checker)
# my_check3.pack(pady=10)
#
# # Round Toggle Button
# var4 = IntVar()
# my_check4 = tb.Checkbutton(bootstyle="success, round-toggle",
#                            text="Round Toggle!!",
#                            variable=var4,
#                            onvalue=1,
#                            offvalue=0,
#                            command=checker)
# my_check4.pack(pady=10)
#
# # Square Toggle Button
# var5 = IntVar()
# my_check5 = tb.Checkbutton(bootstyle="warning, square-toggle",
#                            text="Square Toggle!!",
#                            variable=var5,
#                            onvalue=1,
#                            offvalue=0,
#                            command=checker)
# my_check5.pack(pady=10)
#
# root.mainloop()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Resizing Buttons
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# # https://www.youtube.com/watch?v=0tM-l_ZsxjU&t=1790s
# from tkinter import *
# import ttkbootstrap as tb
#
# root = tb.Window(themename="superhero")
#
# root.title("TTK Bootstrap!")
# root.iconbitmap()
# root.geometry('500x350')
#
# # Style
# my_style = tb.Style()
# my_style.configure('success.Outline.TButton', font=("Helvetica", 18))
#
#
# my_button = tb.Button(text="Hello World!",
#                       bootstyle="success",
#                       style="success.Outline.Tbutton",
#                       width=20)
# my_button.pack(pady=40)
#
# root.mainloop()


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Combo Boxes
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# https://www.youtube.com/watch?v=0tM-l_ZsxjU&t=2146s
from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

root.title("TTK Bootstrap!")
root.iconbitmap()
root.geometry('500x350')


# Create Binding function
def click_bind(e):
    my_label.config(text=f"You Clicked On {my_combo.get()}!")


# Create button click function
def clicker():
    my_label.config(text=f"You Clicked On {my_combo.get()}!")


# Create Label
my_label = tb.Label(root, text="Hello World!", font=("Helvetica", 18))
my_label.pack(pady=30)

# Create Dropdown options
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Create Combobox
my_combo = tb.Combobox(root, bootstyle="success", values=days)
my_combo.pack(pady=20)

# Set Combo Default
my_combo.current(0)

# Create a button
my_button = tb.Button(root, text="Click Me!", command=clicker, bootstyle="danger")
my_button.pack(pady=20)

# Bind the combobox
my_combo.bind("<<ComboboxSelected>>", click_bind)

root.mainloop()
