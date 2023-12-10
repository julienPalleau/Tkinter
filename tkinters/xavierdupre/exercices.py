# http://www.xavierdupre.fr/app/teachpyx/helpsphinx/c_gui/tkinter.html
#################
# Zone de Texte #
#################

# import tkinter
# root = tkinter.Tk()
# zone_texte1 = tkinter.Label(text = "premier texte")
# zone_texte2 = tkinter.Label(text = "second texte")
# zone_texte1.config(text = "premier texte avec un texte normale", state = tkinter.NORMAL)
# zone_texte2.config(text = "second texte avec une texte grisee", state = tkinter.DISABLED)
# zone_texte1.pack()
# zone_texte2.pack()
# root.mainloop()

#-----------------------------------------------------------------------------------------------------------------------
##########
# Bouton #
##########

# from tkinter import *
# root = Tk()
#
# bouton1 = Button(text = "Preceden")
# bouton2 = Button(text = "Suivant")
# bouton3 = Button()
#
# # pour changer de texte
# bouton1.config(text = "Precedent")
# # pour changer un bouton d'etat
# bouton2.config(text = "Bouton grise", state = DISABLED)
# # pour inserer une image dans un bouton
# im = PhotoImage(file="bbette2.gif")
# bouton3.config(image=im)
#
# bouton1.pack()
# bouton2.pack()
# bouton3.pack()
#
# root.mainloop()

#-----------------------------------------------------------------------------------------------------------------------
##################
# Zone de saisie #
##################
from time import sleep
from tkinter import *
root = Tk()

saisie = Entry()


def effacer():
    # Pour supprimer le contenu de la zone de saisie, il faut utiliser la méthode delete. Cette méthode supprime le
    # texte entre deux positions.
    # Supprime le texte entre les positions pos1, pos2
    saisie.delete(0, len(saisie.get()))


bouton1 = Button(root, text = "Effacer", command=effacer)
bouton2 = Button(root, text = "Quitter", command=root.destroy)

# Pour modifier le contenu de la zone de saisie, il faut utiliser la méthode insert qui insere un texte à une position
# donnée.
# Le premier paramètre est la position
# où insérer le texte,
# second paramètre: le texte
saisie.insert(0, "Hello Julien")
# Pour obtenire le contenu de la zone de saisie, il faut utiliser la méthode get:
contenu = saisie.get()


saisie.pack()
bouton1.pack(side="left")
bouton2.pack(side="right")
print(contenu)

root.mainloop()

