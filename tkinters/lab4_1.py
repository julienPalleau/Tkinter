# -----------------------------------------------
# X:\backup\IT stuff\Cours de programmation\Python\[Linkedin Learning] L'essentiel de Python 3\05 - Construire une interface graphique sous Tkinter
# INDISPENSABLE D'ALLER VOIR https://docs.python.org/3/library/tkinter.html
# voir aussi http://tkinter.fdex.eu/doc

from tkinter import *
##########################################################################################################################
# Video 1 - Inserer des widgets sous Tkinter
##########################################################################################################################

# ----------------------------------------------- Exemple 1.1 ----------------------------------------------------------
# # Creation d'un container avec les onglets Ouvrir, Fermer et Reduire
# fenetre = Tk()
# label = Label(fenetre, text="Vive la programmation sous Python 3")
# label.pack()
# fenetre.mainloop()


##########################################################################################################################
# Video 2 - Installer des widgets pour les textures
##########################################################################################################################

# ----------------------------------------------- Exemple 2.1 ----------------------------------------------------------
# fenetre = Tk()

# Label = Label(fenetre, text="Vive la programmation sous Python 3")
# label.pack()
# TitreCadre = LabelFrame(fenetre, text="Le titre du cadre")
# TitreCadre.pack(fill="both", expand="yes")
#
# fenetre.mainloop()

# ----------------------------------------------- Exemple 2.2 ----------------------------------------------------------
# fenetre = Tk()

# Label = Label(fenetre, text="Vive la programmation sous Python 3")
# label.pack()

# # # Widget label
# # # bg = background
# # label = Label(fenetre, text="Un autre label", bg="red")
# # label.pack()
# #
# # # Widget label
# # label = Label(fenetre, text="Le bouton ci-dessous permet de fermer la fenetre.", background="yellow")
# # label.pack()
# #
# # # Widget label couleur avec le code hexadecimal
# # # Trouvez votre couleur sur http://www.code-couleur.com/
# # label = Label(fenetre, text="Le bouton ci-dessous permet de fermer la fenetre.", background='#40E0D0')
# # label.pack()

# # Widget Bouton
# # Bouton est le container... commande associee... on modifie la couleur de
# bouton = Button(fenetre, text="Fermer cette fenetre", fg="white", bg='#001FFF', command=fenetre.quit)
# bouton.pack()
#
# fenetre.mainloop()

# ----------------------------------------------- Exemple 2.3 ----------------------------------------------------------
# fenetre = Tk()
# fenetre.title("Titre de la fenetre")
# fenetre.geometry("500x500")
# fenetre.iconbitmap("Book.ico") # L'emplacement est au meme endroit que le fichier source.
#
# label = Label(fenetre, text="Vive la programmation sous Python 3")
# label.pack()

# # Widget Bouton
# # Bouton est dans le container... commande associee quit
# bouton1 = Button(fenetre, text="style de type FLAT", fg="red", relief=FLAT, command=fenetre.quit).pack()
# bouton2 = Button(fenetre, text="style de type RAISED", fg="orange", relief=RAISED, command=fenetre.quit).pack()
# bouton3 = Button(fenetre, text="style de type SUNKEN", bg="green", relief=SUNKEN, command=fenetre.quit).pack()
# bouton4 = Button(fenetre, text="style de type GROOVE", relief=GROOVE, command=fenetre.quit).pack()
# bouton5 = Button(fenetre, text="style de type RIDGE", relief=RIDGE, command=fenetre.quit).pack()

# fenetre.mainloop()

##########################################################################################################################
# Video 3 - Installer d'autre widgets
##########################################################################################################################

# ----------------------------------------------- Exemple 3.1 ----------------------------------------------------------
# fenetre = Tk()
# fenetre.title("Vive la programmation sous Python 3 !")
# fenetre.geometry("700x1000")
# fenetre.iconbitmap("Book.ico")

# label = Label(fenetre, text="On va mettre de tout dans cette fenetre!")
# label.pack()

# # Case à cocher
# caseAcocher1 = Checkbutton(fenetre, text="case N1").pack()
# caseAcocher2 = Checkbutton(fenetre, text="case N2").pack()
# caseAcocher3 = Checkbutton(fenetre, text="case N3") # Si on appelle pas la methode pack
# caseACocher3.pack() # Il faut le faire ici.
#
# # entree
# value = StringVar()
# value.set("texte par defaut")
# entree = Entry(fenetre, textvariable=value, width=30)
# entree.pack()
#
# # liste
# liste = Listbox(fenetre)
# liste.insert(1, "Ligne 1") # La methode .pack() n'est prise en charge.
# liste.insert(2, "Ligne 2") # L'index ne correpond pas à la position dans la liste.
# liste.insert(3, "Ligne 3")
# liste.insert(4, "Ligne 4")
# liste.insert(5, "Ligne 5")
# liste.pack()
#
# label2 = Label(fenetre,text=liste.size(),fg="red")
# label2.pack()
#
# valeur = DoubleVar()
# # Par defaut, l'echelle est de 0 à 100.
# scale1 = Scale(fenetre, variable=valeur,orient='horizontal', from_=0, to=50, resolution=1, tickinterval=5, length=350,
#                label='Scale horizontal de 0 à 50')
# scale1.pack()
#
# scale2 = Scale(fenetre, variable=valeur,orient='vertical', from_=200, to=-200, resolution=5, tickinterval=50,
#                length=400, label='Scale vertical de 200 à -200')
# scale2.pack()
#
# # La variable 'valeur' est commune aux 2 echelles... Il y aura donc influence.
# # https://www.tutorialspoint.com/python/tk_spinbox.htm
# # SpinBox
# spinbox1 = Spinbox(fenetre, from_=-50, to=50, textvariable=valeur)
# spinbox1.pack()
#
# label3 = Label(fenetre,text=valeur,fg="red")
# label3.pack()
#
# fenetre.mainloop()

#####################################################################################################################
# Video 4 - Mettre en page une fenetre graphique
#####################################################################################################################

# ----------------------------------------------- Exemple 4.1 ----------------------------------------------------------
# fenetre = Tk()
# fenetre.title("Vive la programmation sous Python 3 !")
# fenetre.geometry("400x200")
# fenetre.iconbitmap("Book.ico") # L'emplacement est au meme endroit que le fichier source
# fenetre['bg'] = 'grey' # Definition de la couleur de fond de la fenetre principale
#
# cadre1 = Frame(fenetre)
# cadre1.pack(side=BOTTOM)                        # Toujours en bas et au centre
# #Label(cadre1, text="Cadre 1").pack()           # Ajuste a l'ecriture du contenu
# #Label(cadre1, text="Cadre 1").pack(pady=20)    # On impose une hauteur de 20 px
# Label(cadre1, text="Cadre1").pack(padx=10, pady=40) # On impose une hauteur de 40 px et une marge de 10 px

# ----------------------------------------------- Exemple 4.2 ----------------------------------------------------------
# fenetre = Tk()
# fenetre.title("Vive la programmation sous python 3")
# fenetre.geometry("400x200")
# fenetre.iconbitmap("Book.ico") # L'emplacement est au meme endroit que le fichier source
# fenetre['bg'] = 'orange' # Definition de la couleur de fond de la fenetre principale
#
# cadre2 = Frame(fenetre)
# #cadre2.pack(side=LEFT)                 # Toujours à gauche et au centre
# #cadre2.pack(side=RIGHT)                # Toujours à droite et au centre
# cadre2.pack(side=TOP)                   # Toujours à droite en haut et au centre
# Label(cadre2, text="Cadre 2").pack()    # Ajuste à l'ecriture du contenu
# fenetre.mainloop()

# ----------------------------------------------- Exemple 4.3 ----------------------------------------------------------
# fenetre = Tk()
# fenetre.title("Vive la programmation en python 3")
# fenetre.geometry("400x200")
# fenetre.iconbitmap("Book.ico") # L'emplacement est au meme endroit que le fichier source
# fenetre['bg'] = 'navy' # Definition de la couleur de fond de la fenetre principale
#
# cadre2 = Frame(fenetre)
# cadre2.pack(side=LEFT)                      # Toujours à gauche et au centre
#
# Label1 = Label(cadre2, text="Cadre 1 à gauche", fg="grey").pack(side=LEFT) # Les cadres sont places les uns à la suite des autres
# Label2 = Label(cadre2, text="Cadre2 à guauche", fg="grey").pack(side=LEFT) # dans un meme cadre
# Label3 = Label(cadre2, text="Cadre 3 en bas", fg="grey").pack(side=BOTTOM)
# Label4 = Label(cadre2, text="Cadre 4 à droite", fg="grey").pack(side=RIGHT)
# Label5 = Label(cadre2, text="Cadre 5 en haut", fg="grey").pack(side=TOP)
# fenetre.mainloop()


# ----------------------------------------------- Exemple 4.4 ----------------------------------------------------------
# # Associer un cadre pour chaque element
# # Creer un container avec les onglets Ouvrir, Fermer, et Reduire
# fenetre = Tk()
# fenetre.title("Vive la programmation en python 3")
# fenetre.geometry("400x200")
# fenetre.iconbitmap("Book.ico") # L'emplacement est au meme endroit que le fichier source
# fenetre['bg'] = 'green' # Definition de la couleur de fond de la fenetre principale
#
# # cadre1
# cadre1 = Frame(fenetre, borderwidth=2, relief=RAISED)
# cadre1.pack(side=TOP, padx=20, pady=10) # pady est sans effet car side
#
# # cadre2
# cadre2 = Frame(fenetre, borderwidth=2, relief=SUNKEN)
# cadre2.pack(side=LEFT, padx=10, pady=10)
#
# # cadre3
# cadre3 = Frame(fenetre, bg="white", borderwidth=2, relief=GROOVE)
# cadre3.pack(side=RIGHT, padx=5, pady=5)
#
# # cadre4
# cadre4 = Frame(fenetre, bg="white", borderwidth=2, relief=GROOVE)
# cadre4.pack(side=BOTTOM, padx=5, pady=5)
#
# # Ajouter des composants
# Bouton = Button(cadre1, text="Le bouton 1 ici").pack(padx=10, pady=10)
# Label1 = Label(cadre2, text="Cadre 1").pack(padx=10, pady=10)
# Bouton2 = Button(cadre3, text="Le bouton 2 ici").pack(padx=10, pady=10)
# Label2 = Label(cadre4, text="Cadre 2").pack(padx=10, pady=10)
#
# fenetre.mainloop()

# ----------------------------------------------- Exemple 4.5 ----------------------------------------------------------
# # Associer un cadre dans un cadre
#
# # Creer un container avec les onglets Ouvrir, Fermer et Reduire
# fenetre = Tk()
# fenetre.title("Vive la programmmation sous Python 3 !")
# fenetre.geometry("400x200")
# fenetre.iconbitmap("Book.ico") # L'emplacement est au meme endroit que le fichier source.
# fenetre['bg'] = 'yellow'
#
# # Grand cadre
# cadreGrand = Frame(fenetre, borderwidth = 2, relief = RAISED)
# cadreGrand.pack(side=TOP, padx = 20, pady = 10)
#
# # Cadre 2
# cadre2 = Frame(cadreGrand, borderwidth = 2, relief = SUNKEN)
# cadre2.pack(side = LEFT, padx = 20, pady = 10)
#
# # Cadre 3
# cadre3 = Frame(cadreGrand, borderwidth = 2, relief = GROOVE)
# cadre3.pack(side=BOTTOM, padx = 10, pady = 10)
#
# Bouton = Button(cadre2, text = "Le bouton 1 ici").pack(padx = 10, pady = 10)
# Bouton = Button(cadre2, text = "Le bouton 2 ici").pack(padx = 10, pady = 10)
# Bouton = Button(cadre3, text = "Le bouton 3 ici").pack(padx = 10, pady = 10)
# fenetre.mainloop()

#####################################################################################################################
# Video 5 - Ajouter des alertes sous formes de boites de message
# Programme principal
#####################################################################################################################

# ----------------------------------------------- Exemple 5.1 ----------------------------------------------------------

# # --------------------------------------------------
# #       Zone des 'imports de modules
# # --------------------------------------------------
# from tkinter import *
# from tkinter.messagebox import *
#
# # --------------------------------------------------
# #   Zone de declaration des variables globales
# # --------------------------------------------------
#
#
# # --------------------------------------------------
# #   Zone de declaration des modules ou des fonctions
# # --------------------------------------------------
# def messageYesNo():
#     if askyesno("Boite de message formatee OUI/NON", "Voulez-vous me donner 10 000 euros ?"):
#         showwarning('Logo ATTENTION', "Merci, c'est cool!")
#     else:
#         showinfo("Logo INFO", "Tant pis... j'aurais essaye.")
#         showerror("Logo ERREUR", "Ce n'est pas grave, je finirai par les avoir !")
#
#
# def messageCancel():
#     if askokcancel("Boite de message formatee OK/ANNULER", "Voulez-vous me donner 10 000 euros ?"):
#         showinfo("LOGO info", "D'accord... Pas de probleme")
#     else:
#         showwarning("LOGO attention", "Vous avez tout annule... c'est à dire pas grand chose.")
#
#
# def messageRetryCancel():
#     if askretrycancel("Boite de message formatee RESSAYER/ANNULER", "Voulez-vous me donner 10 000 euros ?"):
#         showinfo("LOGO info", "C'est bien de reessayer mais il faut le faire !")
#     else:
#         showwarning("LOGO attention", "Vous annulez... vous ne voulez vraiment pas !")
#
# # label de cadre
# fenetre = Tk()
# fenetre.title("Vive la programmation sous python 3 !")
# fenetre.geometry("500x200")
# fenetre.iconbitmap("Book.ico")  # L'emplacement est au meme endroit que le fichier source.
# fenetre['bg'] = 'yellow'
#
# # Grand cadre
# cadreGrand = Frame(fenetre, borderwidth = 2, relief = RAISED, bg = "red")
# cadreGrand.pack(side=TOP, padx=20, pady=40)
#
# # cadre 2
# cadre2 = Frame(cadreGrand, borderwidth = 2, relief = SUNKEN)
# cadre2.pack(side=LEFT, padx=20, pady=10)
#
# #cadre 3
# cadre3 = Frame(cadreGrand, borderwidth = 2, relief = SUNKEN)
# cadre3.pack(side=RIGHT, padx=10, pady=10)
#
# # Les icones pour les messageBox sont les memes que l'icone de la fenetre principale
# Bouton = Button(cadre2, text="Le bouton Annuler ici", command=messageCancel, cursor="circle").pack(padx=10, pady=10)
# Bouton = Button(cadre3, text="Le bouton Oui/Non ici", command=messageYesNo, cursor="cross").pack(padx=10, pady=10)
# Bouton = Button(cadre3, text="Le bouton Essayer/Annuler ici", command=messageRetryCancel, cursor="pirate").pack(padx=10, pady=10)
#
# fenetre.mainloop()

#####################################################################################################################
# Video 6 - Gerer l'interactivite avec des widgets
#####################################################################################################################

# ----------------------------------------------- Exemple 6.1 ----------------------------------------------------------
# from tkinter.messagebox import *
# import webbrowser
#
#
# def messageNouveauProjet():
#     showinfo("Logo INFO", "Vous venez de creer un nouveau projet.")
#
#
# def messageOuvrir():
#     showinfo("Logo INFO", "Vous venez d'ouvrir un fichier")
#
#
# def messageCopier():
#     showinfo("Logo INFO", "Vous venez de copier la selection.")
#
#
# def messageColler():
#     showinfo("Logo INFO", "Vous venez de coller la selection.")
#
#
# def nouvelleFenetre():
#     nouvelleFenetre = Toplevel(fenetre)
#     label1 = Label(nouvelleFenetre, text="1 - Vous devez declarer chacun des sous-menus.", padx=50, pady=10)
#     label2 = Label(nouvelleFenetre, text="2 - Vous devez entrer chaque item du sous menu", padx=50, pady=10)
#     label1.pack()
#     label2.pack()
#
#
# def lien_html():
#     webbrowser.open('http://www.python.org')
#
#
# def choix():
#     choix = "Vous avez fait le choix N" + str(varGr.get())
#     label.config(text=choix)


# ---------------------------------------
#       PROGRAMME
# ---------------------------------------

# # INDISPENSABLE D'ALLER VOIR https://docs.python.org/3/library/tkinter.html`
# # Voir https://www.tutorialspoint.com/python/
# fenetre = Tk()
# fenetre.title("Vive la programmation sous python 3 !")
# fenetre.geometry("400x200")
# fenetre.iconbitmap("Book.ico") # L'emplacement est au meme endroit que le fichier source.
#
# barreDeMenu = Menu(fenetre)
#
# # #----------------------------- Menu 1 -----------------------------
#
# itemMenu1 = Menu(barreDeMenu, tearoff=0)
# # Si tearoff=0, le menu n'a plus d'elements graphique de <<detachement>>,
# # et les choix sont ajoutes à partir de la position 0.
#
# itemMenu1.add_command(label="Nouveau projet", command=messageNouveauProjet)
# itemMenu1.add_command(label="Ouvrir", command=messageOuvrir)
# itemMenu1.add_separator()
# itemMenu1.add_command(label="Quitter", command=fenetre.destroy)
# barreDeMenu.add_cascade(label="Fichier", menu=itemMenu1)
#
# # #----------------------------- Menu 2 -----------------------------
#
# itemMenu2 = Menu(barreDeMenu, tearoff=1)
# itemMenu2.add_command(label="Copier", command=messageCopier)
# itemMenu2.add_command(label="Coller", command=messageColler)
# barreDeMenu.add_cascade(label="Editer", menu=itemMenu2)
#
# # #----------------------------- Menu 3 -----------------------------
#
# itemMenu3 = Menu(barreDeMenu, tearoff=0)
# itemMenu3.add_command(label="Aller voir sur la documentation", command=nouvelleFenetre)
# itemMenu3.add_command(label="Vers le site...", command=lien_html)
# barreDeMenu.add_cascade(label="Aide",menu=itemMenu3)
#
# fenetre.config(menu=barreDeMenu)
# fenetre.mainloop()

# ----------------------------------------------- Exemple 6.2 ----------------------------------------------------------

# # Bouton radio
#
# fenetre = Tk()
# fenetre.title("Vive la programmation sous Python 3 !")
# fenetre.geometry("400x300")
# fenetre.iconbitmap("Book.ico") # L'emplacement est au meme endroit que le fichier source.
#
# label1 = Label(fenetre, text = "Bloc de boutons radio", padx=20, pady=20)
# label1.pack()
#
# valeurs = [1,2,3]
# etiquette = ['Choix N1', 'Choix N2', 'Choix N3']
# varGr = StringVar()
# varGr.set(valeurs[0]) # par defaut c'est le choix n 1
# for i in range(3):
#     # boutonRadio = Radiobutton(fenetre, variable = varGr, text = etiquette[i], value = valeurs[i], indicatoron = 0)
#     boutonRadio = Radiobutton(fenetre, variable = varGr, text = etiquette[i], value = valeurs[i], command = choix)
#     boutonRadio.pack(expand=1) # expand=1 permet d'afficher sur toute la longueur de la fenetre
#
# bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.destroy, anchor=CENTER)
# bouton_quitter.pack(pady=20)
#
# label = Label(fenetre, pady=20)
# label.pack()
#
# # On demarre la boucle Tkinter qui s'interrompt quand on ferme la fenetre.
# fenetre.mainloop()

# ----------------------------------------------- Exemple 6.3 ----------------------------------------------------------

# # Les grilles
# fenetre = Tk()
# fenetre.title("Vive la programmation sous Python 3 !")
# fenetre.geometry("420x310")
# fenetre.iconbitmap("Book.ico") # L'emplacement est au meme endroit que le fichier source.
#
# for ligne in range(5):
#     for colonne in range(5):
#         Label(fenetre, text='L%s-C%s' % (ligne, colonne), borderwidth=5, relief=GROOVE, padx=20, pady=15,)\
#             .grid(row=ligne, column=colonne)
#
# # Button(fenetre, text='L1-C1', borderwidth=1).grid(row=1, column=1)
# # Button(fenetre, text='L1-C2', borderwidth=1).grid(row=1, column=2)
# # Button(fenetre, text='L2-C3', borderwidth=1).grid(row=2, column=3)
# # Button(fenetre, text='L2-C4', borderwidth=1).grid(row=2, column=4)
# # Button(fenetre, text='L1-C5', borderwidth=1).grid(row=3, column=3)
#
# fenetre.mainloop()

#####################################################################################################################
# Video 7 - Utiliser les canvas
#####################################################################################################################
# fenetre = Tk()
# fenetre.title("Tire au pistolet")
# fenetre.geometry("400x400")
# fenetre.iconbitmap("Book.ico")  # L'emplacement est au meme endroit que le fichier source.
#
# # ----------------------------------------------- Exemple 7.1 ----------------------------------------------------------
#
# # Lignes - rectangle - cercle - ovales
#
# # Creation de la fenetre ou va se situer le dessin
#
# mon_canvas = Canvas(fenetre, width=400, height=200)
# mon_canvas.pack()
#
# # lignes
# ligne1 = mon_canvas.create_line(0, 0, 200, 100, 20, 50)  # x0, y0, x1, y1, x2, y2 par defaut: noir et plein
# ligne2 = mon_canvas.create_line(0, 100, 200, 0, fill="red",
#                                 dash=(10, 1))  # couleur rouge - pointilles de 10 px pleins, vide
#
# # rectangle
# mon_canvas.create_rectangle(50, 25, 150, 75, fill="blue")
#
# # Ovale
# cercle = mon_canvas.create_oval(20, 20, 90, 90, width=5, outline="green")
# oval = mon_canvas.create_oval(120, 130, 190, 180, width=10, fill="red")
#
# # mon_canvas.delete(ligne1)
# # mon_canvas.delete(ALL)
# fenetre.mainloop()

#####################################################################################################################
# Video 8 - Creer un jeu de tir
#####################################################################################################################
# # Cannevas
# # Parce qu'un canevas peut etre plus large que sa fenetre de visualisation et qu'il peut etre equipe de barres de
# # defilement / deplacement, il y a deux systemes de coordonnees pour chaque canevas:
# #
# # Les coordonnees d'un point dans la fenetre de vue, elles sont relatives au bord superieur gauche de cette fenetre
# # Les coordonnees d'un point dans le canevas lui-meme.
# import random
# import pygame
#
#
# pygame.mixer.init()
# son = pygame.mixer.Sound("tk_coup_fusil.wav")
# # reglage volume
# son.set_volume(1)
#
# def playSon():
#     son.play()
#
# def trouDeLaBalle():
#     """ Dessine un cercle de centre (x, y) et de rayon r """
#     x = random.randint(0, Largeur)
#     y = random.randint(0, Hauteur)
#     r = 10
#
#     # On dessine un cecle dans la zone graphique.
#     trou = Canevas.create_oval(x - r, y - r, x + r, y + r, outline='black', fill='red')
#     playSon()
#     print("Creation du cercle (item", trou, ")")
#     # Affichage de tous les items de Canevas
#     print(Canevas.find_all())
#
#
# def retour():
#     """ Efface le dernier cercle """
#     if len(Canevas.find_all()) > 1:
#         item = Canevas.find_all()[-1]
#         # On efface le cercle.
#         Canevas.delete(item)
#
#         print("Suppression du cercle (item", item, ")")
#         # Affichage de tous les items de Canevas
#         print(Canevas.find_all())
#
#
# def toutEffacer():
#     """ Efface tous les cercles """
#     while len(Canevas.find_all()) > 1:
#         retour()
#
#
# fenetre = Tk()
# fenetre.title("Tire au pistolet")
# fenetre.geometry("400x400")
# fenetre.iconbitmap("balle_icone.ico")
#
# # -------------------------------- JEU ----------------------------------------------------------------------------------
# # Image de fond
# # La fonction PhotoImage de tkinter prend que les formats GIF et PRM /PGM
# # il faut convertir l'image au bon format (en utilisant par exemple un locigicel
# photo = PhotoImage(file="cible-pistolet.png")
#
# # Creation d'un widget Canvas (zone graphique)
# Largeur = 350
# Hauteur = 350
# Canevas = Canvas(fenetre, width=Largeur, height=Hauteur)
# item = Canevas.create_image(5, 5, anchor=NW, image=photo)
# print("Image de fond(item", item, ")")
# Canevas.pack()
#
# # Creation d'un widget Button
# BoutonGo = Button(fenetre, text='Tirer', command=trouDeLaBalle)
# BoutonGo.pack(side=LEFT, padx=10, pady=10)
#
# # Creation d'un widget Button
# BoutonEffacer = Button(fenetre, text='Effacer le dernier tir', command=retour)
# BoutonEffacer.pack(side=LEFT, padx=10, pady=10)
#
# # Creation d'un widget Button
# BoutonEffacerTout = Button(fenetre, text='Effacer', command=toutEffacer)
# BoutonEffacerTout.pack(side=LEFT, padx=10, pady=10)
#
# # Creation d'un widget Button (bouton Quitter)
# BoutonQuitter = Button(fenetre, text='Quitter', command=fenetre.destroy)
# BoutonQuitter.pack(side=LEFT, padx=10, pady=10)
#
# fenetre.mainloop()

#####################################################################################################################
# Video 9 - Decouvrir la bibliotheque Turtle
#####################################################################################################################

# from turtle import *
#
# # ----------------------------------------------- Exemple 9.1 ----------------------------------------------------------
# Turtle

# reset()
# variable = 0
# while variable < 12:
#     variable += 1
#     forward(150)
#     left(150)
#

# ----------------------------------------------- Exemple 9.2 ----------------------------------------------------------
# reset()
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

# ----------------------------------------------- Exemple 9.3 ----------------------------------------------------------
# reset()
# color('red', 'green')
# begin_fill()
#
# for i in range(5):
#     forward(200)
#     right(144)
# end_fill()
# done()

# #####################################################################################################################
# # Video 10 - Aborder un programme de jeu
# #####################################################################################################################
# # ----------------------------------------------- Exemple 10.1 ---------------------------------------------------------
# from random import randint  # entier aleatoire
# from tkinter import *
#
# # -----------------------------------------
# # Zone de declaration des varables globales
# # -----------------------------------------
# ton_score = 0
# mon_score = 0
#
#
# # ------------------------------------------------
# # Zone de declaration des modules ou des fonctions
# # ------------------------------------------------
#
#
# def augmenter_scores(mon_coup, ton_coup):
#     global mon_score, ton_score
#     if mon_coup == 1 and ton_coup == 2:
#         ton_score += 1
#     elif mon_coup == 2 and ton_coup == 1:
#         mon_score += 1
#     elif mon_coup == 1 and ton_coup == 3:
#         mon_score += 1
#     elif mon_coup == 3 and ton_coup == 1:
#         ton_score += 1
#     elif mon_coup == 3 and ton_coup == 2:
#         mon_score += 1
#     elif mon_coup == 2 and ton_coup == 3:
#         ton_score += 1
#
#
# def jouer(ton_coup):
#     global mon_score, ton_score, score1, score2
#     mon_coup = randint(1, 3)
#     if mon_coup == 1:
#         lab3.configure(image=pierre)
#     elif mon_coup == 2:
#         lab3.configure(image=feuille)
#     else:
#         lab3.configure(image=ciseaux)
#     augmenter_scores(mon_coup, ton_coup)
#     score1.configure(text=str(ton_score))
#     score2.configure(text=str(mon_score))
#
#
# def jouer_pierre():
#     jouer(1)
#     lab1.configure(image=pierre)
#
#
# def jouer_feuille():
#     jouer(2)
#     lab1.configure(image=feuille)
#
#
# def jouer_ciseaux():
#     jouer(3)
#     lab1.configure(image=ciseaux)
#
#
# def reinit():
#     global mon_score, ton_score, score1, score2, lab1, lab3
#     ton_score = 0
#     mon_score = 0
#     score1.configure(text=str(ton_score))
#     score2.configure(text=str(mon_score))
#     lab1.configure(image=rien)
#     lab3.configure(image=rien)
#
#
# # On peut declarer et ecrire lses fonctions (ou modules) avant, pendant ou apres le programme principal.
#
# # -----------------------------------------------
# #           PROGRAMME
# # -----------------------------------------------
#
# # Fenetre Graphique
# fenetre = Tk()
# fenetre.title("Pierre, Feuille, Ciseaux")
#
# # Images
# pierre = PhotoImage(file='pierre.gif')
# feuille = PhotoImage(file='feuille.gif')
# ciseaux = PhotoImage(file='ciseaux.gif')
#
# rien = PhotoImage(file='nulle.gif')
# versus = PhotoImage(file='fight.gif')
#
# # Label
# texte1 = Label(fenetre, text="Humain :", font=("Arial", 20, "bold"))
# texte1.grid(row=0, column=0)
#
# texte2 = Label(fenetre, text="Machine :", font=("Arial", 20, "bold"))
# texte2.grid(row=0, column=2)
#
# texte3 = Label(fenetre, text="Pour jouer, cliquez sur une des icones ci-dessous.", font=("Arial", 20, "bold"))
# texte3.grid(row=3, columnspan=3, pady=5)
#
# score1 = Label(fenetre, text="0", font=("Arial", 20, "bold"))
# score1.grid(row=1, column=0)
#
# score2 = Label(fenetre, text="0", font=("Arial", 20, "bold"))
# score2.grid(row=1, column=2)
#
# lab1 = Label(fenetre, image=rien)
# lab1.grid(row=2, column=0)
#
# lab2 = Label(fenetre, image=versus)
# lab2.grid(row=2, column=1)
#
# lab3 = Label(fenetre, image=rien)
# lab3.grid(row=2, column=2)
#
# # Boutons
# bouton1 = Button(fenetre, command=jouer_pierre)
# bouton1.configure(image=pierre)
# bouton1.grid(row=4, column=0)
#
# bouton2 = Button(fenetre, command=jouer_feuille)
# bouton2.configure(image=feuille)
# bouton2.grid(row=4, column=1)
#
# bouton3 = Button(fenetre, command=jouer_ciseaux)
# bouton3.configure(image=ciseaux)
# bouton3.grid(row=4, column=2)
#
# bouton4 = Button(fenetre, text='Recommencer', command=reinit, font=("Arial", 20, "bold"))
# bouton4.grid(row=5, column=0, pady=10, sticky=E)
#
# bouton5 = Button(fenetre, text='Quitter', command=fenetre.destroy, font=("Arial", 20, "bold"))
# bouton5.grid(row=5, column=2, pady=10, sticky=W)
#
# fenetre.mainloop()

#####################################################################################################################
# Video 11 - Jouer avec le temps et animer simplement.mp4
#####################################################################################################################

# -----------------------------------------------
#           Zone des 'imports' de modules
# -----------------------------------------------

import time
from tkinter import *
import random
import math

# ---------------------------------------------------------------------
#           Zone de declaration des variables globales
# ---------------------------------------------------------------------

LARGEUR = 500  # Largeur de la fenetre d'evolution de la balle
HAUTEUR = 300  # Hauteur de la fenetre d'evolution de la balle
RAYON = 20  # Rayon de la balle

# Position initiale au milieu
X = LARGEUR / 2
Y = HAUTEUR / 2
coef_vitesse = 5

# Direction initiale aleatoire
vitesse = random.uniform(1.8, 2) * coef_vitesse
angle = random.uniform(0, 2 * math.pi)
DX = vitesse * math.cos(angle)
DY = vitesse * math.sin(angle)


# ---------------------------------------------------------------------
#           Zone de declaration des modules ou des fonctions
# ---------------------------------------------------------------------

def cycle_1s():
    # On arrive ici toutes les 100 ms.
    heure.set(time.strftime('Nous sommes le: %A-%d-%B-%Y-%Hh-%Mmin-%Ss'))
    fenetre.after(1000, cycle_1s)  # Rafraichissement de la fenetre toute les 1000 ms


def deplacement():
    """ Deplacement de la balle """
    global X, Y, DX, DY, RAYON, LARGEUR, HAUTEUR

    # rebond à droite
    if X + RAYON + DX > LARGEUR:
        X = 2 * (LARGEUR - RAYON) - X
        DX = -DX

    # rebond à gauche
    if X - RAYON + DX < 0:
        X = 2 * RAYON - X
        DX = -DX

    # rebond en bas
    if Y + RAYON + DY > HAUTEUR:
        Y = 2 * (HAUTEUR - RAYON) - Y
        DY = -DY

    # rebond en haut
    if Y - RAYON + DY < 0:
        Y = 2 * RAYON - Y
        DY = -DY

    X = X + DX
    Y = Y + DY

    # Affichage
    Canevas.coords(Balle, X - RAYON, Y - RAYON, X + RAYON, Y + RAYON)
    fenetre.after(50, deplacement)


# ---------------------------------------------------------------------
#           PROGRAMME
# ---------------------------------------------------------------------

# # ----------------------------------------------- Exemple 11.1 ---------------------------------------------------------
# # fenetre graphique
# fenetre = Tk()
# fenetre.title("Donne-moi l'heure !")
# fenetre.geometry("700x200")
# fenetre.iconbitmap("Book.ico")  # L'emplacement est au meme endroit que le fichier source.
# fenetre['bg'] = ''  # blanc par defaut
#
# # Creation des widgets label
# Label(fenetre, text="Voici l'heure courante de mon 'Operating System'", font=("Arial", 20, "bold")).pack(padx=10,
#                                                                                                          pady=10)
# heure = StringVar()
# Label(fenetre, textvariable=heure, font=("Arial", 14, "bold",), bg="grey").pack(padx=10, pady=10)
#
# cycle_1s()
#
# fenetre.mainloop()

# ----------------------------------------------- Exemple 11.2 ---------------------------------------------------------
# Creation de la fenetre principale
fenetre = Tk()
fenetre.title("Animation Balle")

# Creation d'un objet graphique
Canevas = Canvas(fenetre, height=HAUTEUR, width=LARGEUR, bg='grey')
Canevas.pack(padx=5, pady=5)

# Creation d'un objet graphique
Balle = Canevas.create_oval(X - RAYON, Y - RAYON, X + RAYON, Y + RAYON, width=1, fill='green')

deplacement()

fenetre.mainloop()
