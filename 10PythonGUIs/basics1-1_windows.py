# root Basics
import tkinter

# # Define root
root = tkinter.Tk()
root.title('root Basics!')
root.iconbitmap('thinking.ico')
root.geometry('250x700')
root.resizable(0, 0)
root.config(bg='blue')

# Second root
top = tkinter.Toplevel()
top.title('Second root')
top.config(bg="#123456")
top.geometry('200x200+500+50')

# # Run root root's main loop
root.mainloop()