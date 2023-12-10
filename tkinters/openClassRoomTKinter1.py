""" Premier exemple avec Tkinter.

On cree une fenetre simple qui souhaite la bienvenue a l'utilisateur

"""

# On importe Tkinter
from tkinter import *

# On cree une fenetre, racine de notre interface
fenetre = Tk()

# On cree un label (ligne de texte) souhaitant la bienvenue
# Note : le premier parametre passe au constructeur de label est notre
# interface racine

champ_label = Label(fenetre, text="Salut les Zeros !")

# On affiche le label dans la fenetre
champ_label.pack()

# les boutons, ex: bouton quitter
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack()

# une ligne de saisie
var_texte = StringVar()
ligne_texte = Entry(fenetre, textvariable=var_texte, width=30)
ligne_texte.pack()

# les cases a cocher
var_case = IntVar()
case = Checkbutton(
    fenetre, text="Ne plus poser cette question", variable=var_case)
case.pack()

# Les boutons radio
var_choix = StringVar()

choix_rouge = Radiobutton(fenetre, text="Rouge",
                          variable=var_choix, value="rouge")
choix_vert = Radiobutton(fenetre, text="Vert",
                         variable=var_choix, value="vert")
choix_bleu = Radiobutton(fenetre, text="Bleu",
                         variable=var_choix, value="bleu")

choix_rouge.pack()
choix_vert.pack()
choix_bleu.pack()

# liste deroulantes
liste = Listbox(fenetre)
liste.pack()

liste.insert(END, "Julien")
liste.insert(END, "Lucie")
liste.insert(END, "Tom")
liste.insert(END, "Eliott")

# frame
cadre = Frame(fenetre, width=768, height=576, borderwidth=1)
cadre.pack(fill=BOTH)

message = Label(cadre, text="Notre fenetre")
message.pack(side="top", fill=X)

# On demarre la boucle tkinter qui s'interompt quand on ferme la fenetre
fenetre.mainloop()
