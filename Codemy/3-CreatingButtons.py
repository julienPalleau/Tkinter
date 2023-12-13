from tkinter import *

root = Tk()

##########
# Button #
##########
myButton = Button(root, text="Click Me!")
myButton.pack()

#################
# Button State #
#################
myButton = Button(root, text="Click Me!", state=DISABLED)
myButton.pack()


############################################################
# Button padding it makes the button wider                 #
# you can pad along the x axe and y axe using padx or pady #
############################################################
myButton = Button(root, text="Click Me - 1!", padx=50, pady=50)
myButton.pack()


############################################################
# Add a function linked to our button we've created above #
###########################################################
def myClick():
    myLabel = Label(root, text="Look! I clikced a Button!!")
    myLabel.pack()


myButton = Button(root, text="Click Me - 2!", command=myClick, fg="blue", bg="red")
myButton.pack()

root.mainloop()
