from tkinter import *

root1 = Tk()
root2 = Tk()
root3 = Tk()


def myClick():
    myLabel = Label(root3, text="Look! I clicked a Button!")
    myLabel.pack()


myButton1 = Button(root1, text="Click me!", state=DISABLED)
myButton1.pack()

myButton2 = Button(root2, text="Click me!", padx=50)
myButton2.pack()

myButton3 = Button(root3, text="Click me!",
                   command=myClick, bg='blue', fg='red')
myButton3.pack()

root1.mainloop()
root2.mainloop()
root3.mainloop()
