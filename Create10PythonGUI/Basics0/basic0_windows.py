# OG - Udemy.Create.10.Python.GUIs.with.Tkinter
# https://www.iconarchives.com/tag/ico-files

# Windos Basics
import tkinter

# Define window
root = tkinter.Tk()
root.title('Window Basics')
root.iconbitmap('thinking.ico')
root.geometry('250x700')  # width x height
root.resizable(0, 1)  # 0 don't allow for resizing width, 1 allow resizing height
root.config(bg='blue')

# Second window
top = tkinter.Toplevel()
top.title('Second window')
top.config(bg='#123456')
top.geometry('200x200+500+50')  # we provide the window size 200x200 and the window location 500(x) and 50(height)

# Run root window's mainloop
root.mainloop()
