from tkinter import *


class root(Tk):
    def __init__(self):
        super(root, self).__init__()

        self.title("Tkinter Label")
        self.minsize(500, 400)
        self.wm_iconbitmap("icone.ico")

        self.create_layout()

    def create_layout(self):
        Label(self, text="Pack Layout Example").grid(column=0, row=0)

root = root()
root.mainloop()
