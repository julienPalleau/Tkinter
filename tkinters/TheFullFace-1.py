from tkinter import *
import webbrowser


def open_web_channel():
    webbrowser.open_new("http://youtube.com/gravenilvectuto")


# creer une premiere fenetre
root = Tk()

# personnaliser cette fenetre
root.title("My Application")
root.geometry("720x480")
root.minsize(480, 360)
root.iconbitmap(
    "C:\\Users\\MOTTIER LUCIE\\Documents\\GitHub\\tkinter\\logo.ico")
root.config(background='#41B77F')

# creer la frame
frame = Frame(root, bg='#41B77F')

# ajouter un premier texte
label_title = Label(
    frame, text="Bienvenue sur l'application", font=("Helvetica", 40), bg='#41B77F', fg='white')
label_title.pack(expand=YES)

# ajouter un second texte
label_subtitle = Label(
    frame, text="Hey salut à tous c'est moi", font=("Helvetica", 25), bg='#41B77F', fg='white')
label_subtitle.pack(expand=YES)

# ajouter le text
frame.pack(expand=YES)

# construction d'un bouton
qb = Button(frame, text='Tuto web TKinter', font=("Helvetica", 25),
            bg='white', fg='#41B77F', command=open_web_channel)

# ajouter le bouton
qb.pack(pady=50, fill=X)

# afficher
root.mainloop()
