# Only one youtube video: https://www.youtube.com/watch?v=RkaekNkIKNY at this time

from tkinter import *


class Window:
    n = 0

    def __init__(self, root, title, geometry, message):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)  # input, sizexsizey
        Label(self.root, bg='red', text=message).pack()
        button1 = Button(self.root, bg='white', text="Increment", command=self.increment)
        button1.pack()
        self.root.mainloop()
        pass

    def increment(self):
        self.n += 1
        print(self.n)
        return None

    pass


def main():
    root = Tk()
    window11 = Window(root, "Class base windows", '400x500', "Hello user, this is an object window")
    return None


main()