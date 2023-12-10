import string
from random import randint, choice
from tkinter import *


def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = "".join(choice(all_chars)
                       for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# creer la fenetre
root = Tk()
root.title("Generateur de mot de passe")
root.geometry("720x480")
root.iconbitmap(
    "C:\\Users\\MOTTIER LUCIE\\Documents\\GitHub\\tkinter\\logo.ico")
root.config(background='#4065A4')

# creer la frame principale
frame = Frame(root, bg='#4065A4')

# creation d'image
width = 300
height = 300
image = PhotoImage(
    file="C:\\Users\\MOTTIER LUCIE\\Documents\\GitHub\\tkinter\\key.png").subsample(3)
canvas = Canvas(frame, width=width, height=height,
                bg='#4065A4', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

# creer une sous boite
right_frame = Frame(frame, bg='#4065A4')

# creer un titre
label_title = Label(right_frame, text="Mot de passe", font=(
    "Helvetica", 20), bg='#4065A4', fg='white')
label_title.pack()

# creer un champs/entree/input
password_entry = Entry(right_frame, font=(
    "Helvetica", 20), bg='#4065A4', fg='white')
password_entry.pack()

# creer un bouton
generate_password_button = Button(right_frame, text="Generer", font=(
    "Helvetica", 20), bg='#4065A4', fg='white', command=generate_password)
generate_password_button.pack(fill=X)

# on place la sous boite a droite de la frame principal
right_frame.grid(row=0, column=1, sticky=W)

# afficher la frame
frame.pack(expand=YES)

# creation d'une barre de menu
menu_bar = Menu(root)
# creer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=root.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# configurer notre fenetre pour ajouter cette menu bar
root.config(menu=menu_bar)

# afficher la fenetre
root.mainloop()
