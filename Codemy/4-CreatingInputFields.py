from tkinter import *

root = Tk()

#############
# input box #
#############
e = Entry(root, width=50, bg="blue", fg="white", borderwidth=5)
e.pack()


def myClick():
    myLabel = Label(root, text=f"Hello {e.get()}")
    myLabel.pack()


myButton = Button(root, text="Enter Your Stock Quote", command=myClick)
myButton.pack()

root.mainloop()
