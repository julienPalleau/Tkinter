# Import bibliotheque
import tkinter as tk

# Creation de l'objet fenetre
fen = tk.Tk()

# Titre de la fenetre
fen.title("NSINoobs - Exemples tkinter")

# Raille de la fenetre
fen.geometry("300x400")

# Icone de fenetre
fen.iconbitmap(f"C:\\Users\\MOTTIER LUCIE\\Documents\\GitHub\\Tkinter\\CedricGERLAND\\images\\logo_NINOOBS.ico")

# Configuration du fond (couleur ou autre)
fen.config(background='#CCCCCC')

# Rendre possible (ou non) le redimensionnement de la fenetre
fen.resizable(width=True, height=True)

# Ajout d'un titre
label_titre = tk.Label(fen,
                       text="Etude des prenoms en France",
                       height=1,
                       relief=tk.SUNKEN,
                       fg='white',
                       font=("Calibri", 10),
                       bg="#550000")
# Ajout du texte a la fenetre - Ligne n1
label_titre.grid(row=0, columnspan=2, padx=10, pady=15)

# Ajout d'un canevas
can = tk.Canvas(fen,
                width=250,
                height=100,
                bg="ivory")
# Ajout du canevas a la fenetre - Ligne n2
can.grid(row=1, columnspan=2, padx=20, pady=25)

# Ajout d'un bouton quitter
boutonQ = tk.Button(fen,
                    text="Quitter",
                    command=fen.destroy)
# Ajout du bouton Quitter a la fenetre
boutonQ.grid(row=2, column=0, pady=20)

# Ajout du bouton Aide
button = tk.Button(fen,
                   text='Aide',
                   bg='#dee5dc',
                   bd=4)
# Positionnement du bouton Aide
button.grid(row=2, column=1, pady=20)

# Ajout d'un bouton Reinitialiser
buttonReinitialiser = tk.Button(fen,
                                text='Reinitialiser')
# Positionnement du bouton Reinitialiser
buttonReinitialiser.grid(row=4, column=0, pady=20)

# Ajout d'un bouton Sauvegarder
buttonSauvegarder = tk.Button(fen,
                              text='Sauvegarder')
# Positionnement du bouton Sauvegarder
buttonSauvegarder.grid(row=4, column=1, pady=20)

# Ajout d'un bouton Effectuer la recherche
buttonRecherche = tk.Button(fen,
                            text='Effectuer la recherche')
# Positionnement du bouton Effectuer la recherche
buttonRecherche.grid(row=5, columnspan=2, pady=20)

# Recuperation et ajout de l'image
image = tk.PhotoImage(file=f"C:\\Users\\MOTTIER LUCIE\\Documents\\GitHub\\Tkinter\\CedricGERLAND\\images\\python.gif").zoom(1)

# Boucle d'affichage
fen.mainloop()