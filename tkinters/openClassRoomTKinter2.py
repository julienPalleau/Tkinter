from tkinter import *


class Interface(Frame):
    """ Notre fenetre principale.
    Tous les widgets sont stockes comme attributs de cette fenetre."""

    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)
        self.nb_clic = 0

        # Creation de nos widgets
        self.message = Label(
            self, text="Vous n'avez pas clique sur le bouton.")
        self.message.pack()

        self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
        self.bouton_quitter.pack(side="left")

        self.bouton_cliquer = Button(self, text="Cliquez ici", fg="red",
                                     command=self.cliquer)
        self.bouton_cliquer.pack(side="right")

    def cliquer(self):
        """Il y a eu un clic sur le bouton
        On change la valeur du label message."""

        self.nb_clic += 1
        self.message["text"] = "Vous avez clique {} fois.".format(
            self.nb_clic)


fenetre = Tk()
interface = Interface(fenetre)

interface.mainloop()
interface.destroy()
