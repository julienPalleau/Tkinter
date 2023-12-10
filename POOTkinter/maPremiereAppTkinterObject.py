# https://python.sdv.univ-paris-diderot.fr/20_tkinter/
import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Ma Premiere App :-)")
        self.geometry("200x50+10+10")
        self.creer_widgets()

    def creer_widgets(self):
        self.label = tk.Label(self, text="J'adore Python !")
        self.bouton = tk.Button(self, text="Quitter", command=self.quit)
        self.label.pack()
        self.bouton.pack()


if __name__ == "__main__":
    app = Application()
    app.mainloop()