# ----------------------------------------------------------------------------------------------------------------------#
# --------------------------------- Part 1 Introduction to TKinter-----------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------------------#
# https://www.youtube.com/watch?v=YXPyB4XeYLA

#############################################
# Tkinter
# Create the thing and put it on the screen
############################################
# -------------------------------------
# 1- 5 - Sublime text install and setup
# -------------------------------------

# # ---------------
# # 6 - Hello World
# # ---------------
# from tkinter import *
# root = Tk()
# root.title("Hello World!")
# root.geometry("400x400")
#
# root.mainloop()


# ---------
# 7 - Label
# ---------
from tkinter import *

# Root widget, always start by this.
root = Tk()

root.title("Hello World!")
root.geometry("400x400")

# Creating a Label Widget
my_label = Label(root, text="Hello World!")
# Showing it ontop the screen
my_label.pack()

my_label2 = Label(root, text="Second thing!!")
my_label2.pack()

# Create an event loop
root.mainloop()


# # -----------------
# # 8 - Label Options
# # -----------------
# from tkinter import *
# root = Tk()
# root.title("Hello World!")
# root.geometry("1200x400")
#
# my_label = Label(root, text="Background color, Foreground color, font type and size!", fg="white", bg="black", font=("Helvetica", 32))
# my_label.pack()
#
# my_label2 = Label(root, text="Relief option: sunken!!", relief="sunken")
# my_label2.pack()
#
# my_label3 = Label(root, text="Relief option: raised!!", relief="raised")
# my_label3.pack()
#
# my_label4 = Label(root, text="Relief option: groove!!", relief="groove")
# my_label4.pack()
#
# my_label5 = Label(root, text="Relief option: ridge!!", relief="ridge")
# my_label5.pack()
#
# my_label6 = Label(root, text="State option: disabled!!", state="disabled")
# my_label6.pack()
#
# my_label7 = Label(root, text="Background color, Foreground color, font type, size, pady, height, width", fg="white", bg="black", font=("Helvetica", 20), height=100, width=100)
# my_label7.pack(pady=50)
#
#
# root.mainloop()


# # ------------------
# # 9 - Pack Vs. Grid
# # -----------------
# from tkinter import *
# root = Tk()
# root.title("Hello World!")
# root.geometry("400x400")
#
# my_label = Label(root, text="Grid row=0, column=0")
# my_label.grid(row=0, column=0, pady=20)
#
# my_label2 = Label(root, text="Grid row=1, column=0")
# my_label2.grid(row=1, column=0, pady=20)
#
# my_label3 = Label(root, text="Grid row=0, column=1")
# my_label3.grid(row=0, column=1, padx=20)
#
# my_label4 = Label(root, text="Grid row=1, column=1")
# my_label4.grid(row=1, column=1, padx=20)
#
# root.mainloop()


# # -----------------
# # 10 - Grid Option
# # ----------------
# from tkinter import *
# root = Tk()
# root.title("Hello World!")
# root.geometry("500x400")
#
# # Create labels
# my_label = Label(root, text="Hello World!", fg="white", bg="black", font=("Helvetica", 32))
# my_label.grid(row=0, column=0)
#
# # In the lines below the label2 will be centered on label1, default behaviour
# my_label2 = Label(root, text="Column 0")
# my_label2.grid(row=1, column=0)
#
# # In the lines below the label2 will be centered on label1, default behaviour
# my_label3 = Label(root, text="Centered under Hello World!!")
# my_label3.grid(row=2, column=0)
#
# # Now let's assume we don't want label3 to be centered on label1. We use E,W,N,S to define where goes our text
# my_label4 = Label(root, text="We use sticky on West side")
# my_label4.grid(row=3, column=0, sticky=W)
#
# # Now let's assume we don't want label4 to be sticky W. But we want to be sticky E
# my_label5 = Label(root, text="We use sticky on East side")
# my_label5.grid(row=4, column=0, sticky=E, pady=(0, 20))  # it doesn't go on the extreme right of the main root as we positioned it in column 0. We could position it on column 1.
#                                         # pady=(0, 20) means 20 pixel away below and 0 pixel away above
#
# # Now let's have a look to columnspan
# my_label6 = Label(root, text="Column Span", fg="white", bg="black", font=("Helvetica", 32))
# my_label6.grid(row=5, column=0, columnspan=2)
#
# my_label7 = Label(root, text="column 0")
# my_label7.grid(row=6, column=0, pady=(0, 20))
#
# my_label8 = Label(root, text="column 1")
# my_label8.grid(row=6, column=1, pady=(0, 20))
#
# # Now let's have a look to rowspan
# my_label9 = Label(root, text="row 7")
# my_label9.grid(row=7, column=0)
#
# my_label10 = Label(root, text="row 8")
# my_label10.grid(row=8, column=0)
#
# my_label11 = Label(root, text=" row Span ", fg="white", bg="black", font=("Helvetica", 32))
# my_label11.grid(row=7, column=1, rowspan=2, pady=(0,5))
#
# my_label12 = Label(root, text="row 9")
# my_label12.grid(row=10, column=0)
#
# my_label13 = Label(root, text="Single row", fg="white", bg="black", font=("Helvetica", 32))
# my_label13.grid(row=10, column=1)
#
# root.mainloop()


# # -------------
# # 11 - Buttons
# # -------------
# from tkinter import *
# root = Tk()
# root.title("Hellow World!")
# root.geometry("400x400")
#
# # Create clicked function
# def clicked():
#     my_label2 = Label(root, text="You clicked the button!")
#     my_label2.pack()
#
# # Create labels
# my_label = Label(root, text="Hello World!", fg="white", bg="black", font=("Helvetica", 32))
# my_label.pack()
#
# # Create Buttons
# my_button = Button(root, text="Click Me!", command=clicked)
# my_button.pack(pady=20)
#
#
# root.mainloop()


# # ----------------------------------
# # 12 - Input Boxes or Entry Widget
# # ---------------------------------
# from tkinter import *
# root = Tk()
# root.title("Hellow World!")
# root.geometry("400x400")
#
# # Create clicked function
# def clicked():
#     input = e.get()
#
#     my_label2 = Label(root, text="Hi " + input)
#     my_label2.pack()
#
#     my_label3 = Label(root, text="Hello " + e.get())
#     my_label3.pack()
#
# # Create labels
# my_label = Label(root, text="Enter your Name:")
# my_label.pack()
#
# # Create Entry Widgets Input Box
# e = Entry(root, font=("Helvetica", 18))
# e.pack(pady=20)
#
# # Create Buttons
# my_button = Button(root, text="Click Me!", command=clicked)
# my_button.pack(pady=20)



# root.mainloop()


# # ------------
# # 13 - Icons
# # ------------
# from tkinter import *
#
# root = Tk()
# root.title("Hellow World!")
# root.geometry("400x400")
# root.iconbitmap(r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Tkinter\Codemy\logo_NISNOOBS.ico")
#
# root.mainloop()

# # -------------
# # 14 - Images
# # -------------
# from tkinter import *
# from PIL import ImageTk, Image
#
# root = Tk()
# root.title("Hellow World!")
# root.geometry("400x400")
# root.iconbitmap(r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Tkinter\Codemy\logo_NISNOOBS.ico")
#
#
# # Create clicked function
# def clicked():
#     input = e.get()
#     my_label2 = Label(root, text="Hello " + input)
#     my_label2.pack()
#
# # Add Images
# my_image = ImageTk.PhotoImage(Image.open("a209b.jpg"))
# image_label = Label(image=my_image)
# image_label.pack()
#
# # Create labels
# my_label = Label(root, text="Enter Your Name:")
# my_label.pack()
#
# # Create Entry Widget Input Box
# e = Entry(root, font=("Helvetica", 18))
# e.pack(pady=20)
#
# # Create Buttons
# my_button = Button(root, text="Click Me!", command=clicked)
# my_button.pack(pady=20)
#
# root.mainloop()


# # -----------------------------
# # 15 - Pack Forget and Destroy
# # ----------------------------
# from tkinter import *
#
# root = Tk()
# root.title("Hellow World!")
# root.geometry("400x400")
# root.iconbitmap(r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Tkinter\Codemy\logo_NISNOOBS.ico")
#
#
# # Create clicked function
# def clicked():
#     global my_label2
#     input = e.get()
#     my_label2 = Label(root, text="Hello " + input)
#     my_label2.pack()
#
#
# def hide():
#     my_label2.pack_forget()
#     # my_label2.destory() # as it destroy it the button show won't work because once it is destroyed you can't show it any more
#
#
# def show():
#     my_label2.pack()
#
#
# # Create labels
# my_label = Label(root, text="Enter Your Name:")
# my_label.pack()
#
# # Create Entry Widget Input Box
# e = Entry(root, font=("Helvetica", 18))
# e.pack(pady=20)
#
# # Create Buttons
# my_button = Button(root, text="Click Me!", command=clicked)
# my_button.pack(pady=20)
#
# hide_button = Button(root, text="Hide", command=hide)
# hide_button.pack(pady=20)
#
# show_button = Button(root, text="Show", command=show)
# show_button.pack(pady=20)
#
# root.mainloop()


# # ---------------------------
# # 16 & 17 Menu Part1 & Part2
# # --------------------------
# from tkinter import *
#
# root = Tk()
# root.title("Hellow World!")
# root.geometry("400x400")
# root.iconbitmap(r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Tkinter\Codemy\logo_NISNOOBS.ico")
#
#
# # Define our fake command
# def fake_command():
#     my_label = Label(root, text="you clicked a menu item!")
#     my_label.pack()
#
#
# # Define a Menu
# my_menu = Menu(root)
# root.config(menu=my_menu)
#
# # Create Menu Items
# file_menu = Menu(my_menu)
# my_menu.add_cascade(label="File", menu=file_menu)
# file_menu.add_command(label="New", command=fake_command)
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)
#
# # Create another subenu Edit
# edit_menu = Menu(my_menu)
# my_menu.add_cascade(label="Edit", menu=edit_menu)
# edit_menu.add_command(label="Cut", command=fake_command)
# edit_menu.add_command(label="Copy", command=fake_command)
# edit_menu.add_command(label="Paste", command=fake_command)
#
# root.mainloop()


# # ------------
# # 18 - Frames
# # ------------
# from tkinter import *
#
# root = Tk()
# root.title("Hellow World!")
# root.geometry("400x400")
# root.iconbitmap(r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Tkinter\Codemy\logo_NISNOOBS.ico")
#
#
# # Define our fake command
# def fake_command(lemenu):
#     my_label = Label(root, text=f"you clicked {lemenu}")
#     my_label.grid(row=2, column=0)
#
#
# def hide():
#     my_frame.grid_forget()
#
#
# def show():
#     my_frame.grid(row=1, columnspan=2, padx=20, pady=20)
#
#
# # Define a Menu
# my_menu = Menu(root)
# root.config(menu=my_menu)
#
# # Create Menu Items
# file_menu = Menu(my_menu)
# my_menu.add_cascade(label="File", menu=file_menu)
# file_menu.add_command(label="New", command=fake_command)
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)
#
# # Create another subenu Edit
# edit_menu = Menu(my_menu)
# my_menu.add_cascade(label="Edit", menu=edit_menu)
# edit_menu.add_command(label="Cut", command=lambda: fake_command("Cut"))
# edit_menu.add_command(label="Copy", command=lambda: fake_command("Copy"))
# edit_menu.add_command(label="Paste", command=lambda: fake_command("Paste"))
#
# show_button = Button(root, text="Show", command=show)
# hide_button = Button(root, text="Hide", command=hide)
#
# show_button.grid(row=0, column=0)
# hide_button.grid(row=0, column=1)
#
# my_frame = Frame(root, width=200, height=200, bd=5, bg="blue", relief="sunken")
# my_frame.grid(row=1, columnspan=2, padx=20, pady=20)
#
# frame_label = Label(my_frame, text="Hello World!", font=("Helvetica", 20))
# frame_label.pack(padx=20, pady=20)
#
# root.mainloop()


# ----------------------
# 19 - Frames and Menus
# ----------------------
# from tkinter import *
#
# root = Tk()
# root.title("Hellow World!")
# root.geometry("400x400")
# root.iconbitmap(r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Tkinter\Codemy\logo_NISNOOBS.ico")
#
#
# # Define our fake command
# def fake_command():
#     pass
#
#
# def new():
#     file_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
#
#
# def cut():
#     edit_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
#
#
# # Define a Menu
# my_menu = Menu(root)
# root.config(menu=my_menu)
#
# # Create Menu Items
# file_menu = Menu(my_menu)
# my_menu.add_cascade(label="File", menu=file_menu)
# file_menu.add_command(label="New", command=new)
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)
#
# # Create another subenu Edit
# edit_menu = Menu(my_menu)
# my_menu.add_cascade(label="Edit", menu=edit_menu)
# edit_menu.add_command(label="Cut", command=cut)
# edit_menu.add_command(label="Copy", command=fake_command)
# edit_menu.add_command(label="Paste", command=fake_command)
#
#
# # File Menu Frame
# file_frame = Frame(root, width=200, height=200, bd=5, bg="blue", relief="sunken")
# # file_frame.grid(row=1, columnspan=2, padx=20, pady=20)
#
# file_label = Label(file_frame, text="File Frame", font=("Helvetica", 20))
# file_label.pack(padx=20, pady=20)
#
# # Edit Menu Frame
# edit_frame = Frame(root, width=200, height=200, bd=5, bg="blue", relief="sunken")
# # file_frame.grid(row=1, columnspan=2, padx=20, pady=20)
#
# edit_label = Label(edit_frame, text="Cut Frame", font=("Helvetica", 20))
# edit_label.pack(padx=20, pady=20)
#
#
# root.mainloop()


# ------------------------------------
# 20 - Hiding and Showing Menu Frames
# ------------------------------------
# from tkinter import *
#
# root = Tk()
# root.title("Hellow World!")
# root.geometry("400x400")
# root.iconbitmap(r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Tkinter\Codemy\logo_NISNOOBS.ico")
#
#
# # Define our fake command
# def fake_command():
#     pass
#
#
# def new():
#     hide_menu_frames()
#     file_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
#
#
# def cut():
#     hide_menu_frames()
#     edit_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
#
#
# def hide_menu_frames():
#     edit_frame.grid_forget()
#     file_frame.grid_forget()
#
#
#
# # Define a Menu
# my_menu = Menu(root)
# root.config(menu=my_menu)
#
# # Create Menu Items
# file_menu = Menu(my_menu)
# my_menu.add_cascade(label="File", menu=file_menu)
# file_menu.add_command(label="New", command=new)
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)
#
# # Create another subenu Edit
# edit_menu = Menu(my_menu)
# my_menu.add_cascade(label="Edit", menu=edit_menu)
# edit_menu.add_command(label="Cut", command=cut)
# edit_menu.add_command(label="Copy", command=fake_command)
# edit_menu.add_command(label="Paste", command=fake_command)
#
#
# # File Menu Frame
# file_frame = Frame(root, width=200, height=200, bd=5, bg="blue", relief="sunken")
# # file_frame.grid(row=1, columnspan=2, padx=20, pady=20)
#
# file_label = Label(file_frame, text="File Frame", font=("Helvetica", 20))
# file_label.pack(padx=20, pady=20)
#
# # Edit Menu Frame
# edit_frame = Frame(root, width=200, height=200, bd=5, bg="blue", relief="sunken")
# # file_frame.grid(row=1, columnspan=2, padx=20, pady=20)
#
# edit_frame_label = Label(edit_frame, text="Cut Frame", font=("Helvetica", 20))
# edit_frame_label.pack(padx=20, pady=20)
#
#
# root.mainloop()


# ----------------
# 21 - Status Bar
# ---------------
# from tkinter import *
#
# root = Tk()
# root.title("Hellow World!")
# # root.geometry("400x400")
# root.iconbitmap(r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Tkinter\Codemy\logo_NISNOOBS.ico")
#
#
# # Define our fake command
# def fake_command():
#     pass
#
#
# def new():
#     hide_menu_frames()
#     current_status.set("File Status")
#     file_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
#
#
# def cut():
#     hide_menu_frames()
#     current_status.set("Cut Status")
#     edit_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
#
#
# def hide_menu_frames():
#     edit_frame.grid_forget()
#     file_frame.grid_forget()
#
#
# # Define a Menu
# my_menu = Menu(root)
# root.config(menu=my_menu)
#
# # Create Menu Items
# file_menu = Menu(my_menu)
# my_menu.add_cascade(label="File", menu=file_menu)
# file_menu.add_command(label="New", command=new)
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)
#
# # Create another subenu Edit
# edit_menu = Menu(my_menu)
# my_menu.add_cascade(label="Edit", menu=edit_menu)
# edit_menu.add_command(label="Cut", command=cut)
# edit_menu.add_command(label="Copy", command=fake_command)
# edit_menu.add_command(label="Paste", command=fake_command)
#
# # File Menu Frame
# file_frame = Frame(root, width=200, height=200, bd=5, bg="blue", relief="sunken")
# # file_frame.grid(row=1, columnspan=2, padx=20, pady=20)
#
# file_label = Label(file_frame, text="File Frame", font=("Helvetica", 20))
# file_label.pack(padx=20, pady=20)
#
# # Edit Menu Frame
# edit_frame = Frame(root, width=200, height=200, bd=5, bg="blue", relief="sunken")
# # file_frame.grid(row=1, columnspan=2, padx=20, pady=20)
#
# edit_frame_label = Label(edit_frame, text="Cut Frame", font=("Helvetica", 20))
# edit_frame_label.pack(padx=20, pady=20)
#
# current_status = StringVar()
# current_status.set("Waiting")
#
# my_status = Label(root, textvariable=current_status, bd=2, relief="sunken", width=56, anchor=E)
# my_status.grid(row=1, column=0)
#
# root.mainloop()


# -------------------
# 22 - Radio Buttons
# -------------------
# from tkinter import *
#
# root = Tk()
# root.title("Hellow World!")
# root.geometry("400x400")
# root.iconbitmap(r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Tkinter\Codemy\logo_NISNOOBS.ico")
#
#
# # Create radio button function
# def radio():
#     if v.get() == "one":
#         my_label = Label(root, text="You Clicked Radio Button One!")
#     else:
#         my_label = Label(root, text="You Clicked Radio Button Two!")
#
#     my_label.pack(pady=10)
#
#
# v = StringVar()
# v.set("one")  # define which value is set by default
#
# Radiobutton(root, text="One", variable=v, value="one").pack()
# Radiobutton(root, text="Two", variable=v, value="two").pack()
#
# my_button = Button(root, text="Click Met", command=radio)
# my_button.pack(pady=20)
#
# root.mainloop()

# -----------------
# 23 - Check Boxes
# -----------------
# from tkinter import *
#
# root = Tk()
# root.title("Hellow World!")
# root.geometry("400x400")
# root.iconbitmap(r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Tkinter\Codemy\logo_NISNOOBS.ico")
#
#
# # Create toppings function
# def toppings():
#     if v.get() == "pepperoni":
#         my_label = Label(root, text="You ordered pepperoni")
#     else:
#         my_label = Label(root, text="You don't want pepperoni")
#
#     # my_label = Label(root, text=v.get())
#     my_label.pack(pady=10)
#
#
# # Check Boxes
# v = StringVar()
# my_check = Checkbutton(root, text="Pepperoni", variable=v, onvalue="pepperoni", offvalue="no_pepperoni")
# my_check.deselect()
# my_check.pack()
#
# Button(root, text="Select Toppings", command=toppings).pack(pady=10)
#
# root.mainloop()

# ----------------------------
# 24, 25 - Pop Up Message Box
# ----------------------------
# from tkinter import *
# from tkinter import messagebox
#
# root = Tk()
# root.title("Hellow World!")
# root.geometry("400x600")
# root.iconbitmap(r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Tkinter\Codemy\logo_NISNOOBS.ico")
#
# # Popub Boxes
# # showinfo, showwarning, showerror, askquestion, askokcancel, askyesnon
#
#
# # Create Popup function with showinfo
# response = ""
#
#
# def popup_showinfo():
#     response = messagebox.showinfo("Popup Title", "Look at my Popup ShowInfo message!!")
#     Label(root, text=response).pack(pady=10)
#
#
# def warning_showinfo():
#     response = messagebox.showwarning("Waring Title", "Look at my Warning ShowInfo message!!")
#     Label(root, text=response).pack(pady=10)
#
#
# def error_showinfo():
#     response = messagebox.showerror("Error Title", "Look at my Error ShowInfo message!!")
#     Label(root, text=response).pack(pady=10)
#
#
# # Create Popup function with askquestion
# def popup_askquestion():
#     response = messagebox.askquestion("Popup Title", "Look at my Popup AskQuestion message!!")
#     Label(root, text=response).pack(pady=10)
#
#
# def popup_askokcancel():
#     response = messagebox.askokcancel("AskOkCancel Title", "Look at my AskOkCancel message !!")
#     Label(root, text=response).pack(pady=10)
#
#
# def popup_askyesno():
#     response = messagebox.askyesno("AskYesNo Title", "Look at my AskYesNo message!!")
#     Label(root, text=response).pack(pady=20)
#
#
# if response == 1:
#     Label(root, text="you clicked Yes!").pack(pady=10)
# else:
#     Label(root, text="you clicked No!").pack(pady=10)
#
# Label(root, text="showinfo message box").pack()
#
# pop_button1 = Button(root, text="Click to Pop Up!", command=popup_showinfo)
# pop_button1.pack(pady=20)
#
# pop_button2 = Button(root, text="Click to Warning!", command=warning_showinfo)
# pop_button2.pack(pady=20)
#
# pop_button3 = Button(root, text="Click to Error!", command=error_showinfo)
# pop_button3.pack(pady=20)
#
# Label(root, text="askquestion message box").pack()
#
# pop_button4 = Button(root, text="Click to askquestion!", command=popup_askquestion)
# pop_button4.pack(pady=20)
#
# pop_button5 = Button(root, text="Click to askokcancel!", command=popup_askokcancel)
# pop_button5.pack(pady=20)
#
# pop_button6 = Button(root, text="Click to askyesnon!", command=popup_askyesno)
# pop_button6.pack(pady=20)
#
# Label(root, text="message box answer").pack()
# root.mainloop()


# -----------------
# 26 - Combo Boxes
# -----------------
# from tkinter import *
# from tkinter import ttk
#
# root = Tk()
# root.title("Hellow World!")
# root.geometry("400x600")
# root.iconbitmap(r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Tkinter\Codemy\logo_NISNOOBS.ico")
#
#
# # Create Select function
# def select():
#     if my_combo.get() == "Monday":
#         Label(root, text="You Clicked Monday!").pack(pady=10)
#     else:
#         Label(root, text="You Clicked on " + my_combo.get() + "!").pack(pady=10)
#
#
# # Combo Boxes
# options = [
#     "Monday",
#     "Tuesday",
#     "Wednesday",
#     "Thursday",
#     "Friday",
#     "Saturday",
#     "Sunday",
# ]
#
# my_combo = ttk.Combobox(root, value=options)
# my_combo.current(0)  # pass the index number
# my_combo.pack(pady=10)
#
# Button(root, text="Select", command=select).pack()
#
# root.mainloop()


# -----------------
# 27 - New roots
# -----------------
# from tkinter import *
#
# root = Tk()
# root.title("Hellow World!")
# root.geometry("400x600")
# root.iconbitmap(r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Tkinter\Codemy\logo_NISNOOBS.ico")
#
# # Create second root function
# def open_root():
#     new = Toplevel()
#     new.title("Second root")
#     new.geometry("300x200")
#     new.iconbitmap(r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Tkinter\Codemy\logo_NISNOOBS.ico")
#
#     Label(new, text="Look at my fancy second root!").pack(pady=20)
#
#     new.mainloop()
#
# # Create New roots
# my_button = Button(root, text="Open 2nd root", command=open_root)
# my_button.pack()
#
# root.mainloop()


# -------------------------------
# 28 - New roots Hide And Kill
# -------------------------------
# from tkinter import *
#
# root = Tk()
# root.title("Hellow World!")
# root.geometry("400x600")
# root.iconbitmap(r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Tkinter\Codemy\logo_NISNOOBS.ico")
#
# # Create second root function
# def open_root():
#     new = Toplevel()
#     new.title("Second root")
#     new.geometry("300x200")
#     new.iconbitmap(r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Tkinter\Codemy\logo_NISNOOBS.ico")
#
#     Label(new, text="Look at my fancy second root!").pack(pady=20)
#
#     destroy_button = Button(new, text="Quit", command=new.destroy)
#     destroy_button.pack()
#
#     # Minimize Original root
#     # hide_button = Button(new, text="Hide Main root", command=root.iconify)
#     # show_button = Button(new, text="Show Main root", command=root.deiconify)
#
#     # Withdraw Original root
#     hide_button = Button(new, text="Hide Main root", command=root.withdraw)
#     show_button = Button(new, text="Show Main root", command=root.deiconify)
#
#     kill_original = Button(new, text="Quit Original", command=root.destroy).pack()
#
#     hide_button.pack()
#     show_button.pack()
#
#     new.mainloop()
#
# # Create New roots
# my_button = Button(root, text="Open 2nd root", command=open_root)
# my_button.pack()
#
# root.mainloop()


# ---------------------------
# 29 - Images in New roots
# ---------------------------
# from tkinter import *
# from PIL import ImageTk, Image
#
# root = Tk()
# root.title("Hellow World!")
# root.geometry("400x400")
# root.iconbitmap(r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Tkinter\Codemy\logo_NISNOOBS.ico")
#
#
# # Create second root function
# def open_root():
#     new = Toplevel()
#     new.title("Second root")
#     new.geometry("400x400")
#     new.iconbitmap(r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Tkinter\Codemy\logo_NISNOOBS.ico")
#
#     Label(new, text="Look at my fancy second root!").pack(pady=20)
#
#     my_img = ImageTk.PhotoImage(Image.open("a209b.jpg"))
#     img_label = Label(new, image=my_img)
#     img_label.pack(pady=5)
#
#     destroy_button = Button(new, text="Quit", command=new.destroy)
#     destroy_button.pack()
#
#     # Minimize Original root
#     # hide_button = Button(new, text="Hide Main root", command=root.iconify)
#     # show_button = Button(new, text="Show Main root", command=root.deiconify)
#
#     # Withdraw Original root
#     hide_button = Button(new, text="Hide Main root", command=root.withdraw)
#     show_button = Button(new, text="Show Main root", command=root.deiconify)
#
#     Button(new, text="Quit Original", command=root.destroy).pack()
#
#     hide_button.pack()
#     show_button.pack()
#
#     new.mainloop()  # It is really important to think about adding the mainloop to the new root otherwise the image won't be displayed.
#
#
# # Create New roots
# my_button = Button(root, text="Open 2nd root", command=open_root)
# my_button.pack()
#
# root.mainloop()


# ---------------------------
# 30 - Openn File Dialog Box
# ---------------------------
# from tkinter import *
# from PIL import ImageTk, Image
# from tkinter import filedialog
# root = Tk()
# root.title("Hellow World!")
# root.geometry("400x400")
# root.iconbitmap(r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Tkinter\Codemy\logo_NISNOOBS.ico")
#
# #Open File Dialog Box
# root.filename = filedialog.askopenfilename(initialdir='f:', title="Open an image File", filetypes=(("All Files", "*.*"), ("PNG File", "*.png")))
#
# root.mainloop()

# --------------------------------------
# 31 - Openn Dialog Box Image To Screen
# --------------------------------------
# from tkinter import *
# from PIL import ImageTk, Image
# from tkinter import filedialog
#
# root = Tk()
# root.title("Hellow World!")
# root.geometry("400x400")
# root.iconbitmap(r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Tkinter\Codemy\logo_NISNOOBS.ico")
#
# # Create open dialog box function
# def open_image():
#     # Open File Dialog Box
#     root.filename = filedialog.askopenfilename(initialdir=r'F:', title='Open An Image File',
#                                                filetypes=(("JPG File", "*.jpg"), ("All Files", "*.*")))
#     # my_label = Label(root, text=root.filename).pack(pady=10)
#     global my_img
#     # Open image and place on screen
#     my_img = ImageTk.PhotoImage(Image.open(root.filename))
#     img_label = Label(root, image=my_img)
#     img_label.pack(pady=10)
#
# # Open Dialog Box
# my_button = Button(root, text="Open Image", command=open_image).pack(pady=10)
#
#
# root.mainloop()


# -----------------------
# 32 - Grid Forget Part 1
# -----------------------
# from tkinter import *
#
# root = Tk()
# root.title("Hellow World!")
# root.geometry("400x400")
# root.iconbitmap(r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Tkinter\Codemy\logo_NISNOOBS.ico")
#
# # Submit Function
# def submit():
#     global hello_label
#     hello_label = Label(root, text="Hello " + e.get())
#     hello_label.grid(row=3, column=0)
#
# # Clear Function
# def clear():
#     hello_label.grid_forget()
#
# # Forget
# my_label = Label(root, text="Enter Your Name:").grid(row=0, column=0)
#
# e = Entry(root)
# e.grid(row=1, column=0, padx=20, pady=(10, 10))
#
# my_button = Button(root, text="Submit", command=submit).grid(row=2, column=0)
#
# clear_button = Button(root, text="Clear", command=clear).grid(row=2, column=1)
#
#
# root.mainloop()


# -----------------------
# 33- Grid Forget Part 2
# -----------------------
# from tkinter import *
#
# root = Tk()
# root.title("Hellow World!")
# root.geometry("400x400")
# root.iconbitmap(r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Tkinter\Codemy\logo_NISNOOBS.ico")
#
# hello_label = Label(root)
#
# # Submit Function
# def submit():
#     global hello_label
#     clear()
#     hello_label = Label(root, text="Hello " + e.get())
#     hello_label.grid(row=3, column=0)
#
# # Clear Function
# def clear():
#     hello_label.grid_forget()
#
# # Forget
# my_label = Label(root, text="Enter Your Name:").grid(row=0, column=0)
#
# e = Entry(root)
# e.grid(row=1, column=0, padx=20, pady=(10, 10))
#
# my_button = Button(root, text="Submit", command=submit).grid(row=2, column=0)
#
# clear_button = Button(root, text="Clear", command=clear).grid(row=2, column=1)
#
#
# root.mainloop()

# -------------------------
# 34- Color Chooser Part 1
# -------------------------
# from tkinter import *
# from tkinter import colorchooser
#
# root = Tk()
# root.title("Hellow World!")
# root.geometry("400x400")
# root.iconbitmap(r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Tkinter\Codemy\logo_NISNOOBS.ico")
#
#
# def color():
#     my_color = colorchooser.askcolor()[0] # [0] is rgb code, [1] is hexa code
#     my_label = Label(root, text=my_color).pack()
#
#
# my_button = Button(root, text="Pick A Color", command=color).pack()
# root.mainloop()


# -------------------------
# 35- Color Chooser Part 2
# -------------------------
# from tkinter import *
# from tkinter import colorchooser
#
# root = Tk()
# root.title("Hellow World!")
# root.geometry("400x400")
# root.iconbitmap(r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Tkinter\Codemy\logo_NISNOOBS.ico")
#
#
# def color():
#     my_color = colorchooser.askcolor()[1]  # [0] is rgb code, [1] is hexa code
#     Label(root, text=my_color).pack()
#     Label(root, text="You Picked A Color!!", font=("Helvetica", 32), bg=my_color).pack()
#
#
# my_button = Button(root, text="Pick A Color", command=color).pack()
# root.mainloop()


# -------------------
# 36- Standalone exe
# -------------------
# 1 -   Install pyinstaller: pipenv install pysinstaller or pip depending on what you are using
# 2 -   Cd followed by the location where your Python script is stored.
#       Now you are currently in the directory where your python file is. The following command will help to create an exe
#       file from your .py file. Replace pythonScriptName with the name of your python file name.
# 3 -   pyinstaller --onefile pythonScriptName.py
# 4 -   Your executable should now get created at the location that you specified.
