# ---------------------- Button -----------------------------------------------------------------------------------------
# from tkinter import *
# fenetre = Tk()
# button = Button(fenetre, text='Cliquez sur moi', width=25, command=fenetre.destroy)
# button.pack()
# fenetre.mainloop()

# ---------------------- Canvas ----------------------------------------------------------------------------------------
# from tkinter import *
# fenetre = Tk()
# C = Canvas(fenetre, bg="sky blue", height=250, width=300)
# coord = 10, 50, 240, 210
# arc = C.create_arc(coord, start=0, extent=150, fill="red")
# C.pack()
# fenetre.mainloop()

# ---------------------- CheckButton -----------------------------------------------------------------------------------
# from tkinter import *
#
# fenetre = Tk()
# v1 = IntVar()
# Checkbutton(fenetre, text='Python', width=25, variable=v1).grid(row=0, sticky=S)
# v2 = IntVar()
# Checkbutton(fenetre, text='Programmation web', width=25, variable=v2).grid(row=1, sticky=S)
# v3 = IntVar()
# Checkbutton(fenetre, text='HTML5 et CSS3', width=25, variable=v3).grid(row=2, sticky=S)
# v4 = IntVar()
# Checkbutton(fenetre, text='Javascript', width=25, variable=v4).grid(row=3, sticky=S)
# v5 = IntVar()
# Checkbutton(fenetre, text='Bootstrap4', width=25, variable=v5).grid(row=4, sticky=S)
#
# fenetre.mainloop()

# ---------------------- Entry -----------------------------------------------------------------------------------------
from tkinter import *


def affiche():
    print(e1.get())
    print(e2.get())


fenetre = Tk()
fenetre.geometry("300x200")
Label(fenetre, text='Saisir votre prenom').grid(row=0)
Label(fenetre, text='Saisir votre nom').grid(row=1)
e1 = Entry(fenetre)
e2 = Entry(fenetre)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
button = Button(fenetre, text='Validez', width = 10, command=affiche).grid(row=2, column=1)


mainloop()