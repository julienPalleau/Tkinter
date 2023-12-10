# https://www.pythontutorial.net/tkinter/tkinter-hello-world/
"""
Tkinter Hello, World!
Summary: in this tutorial, you'll learn step by step how to developp the Tkinter "Hello, World!" program.

Creating a window
The following program shows how to display a window(https://www.pythontutorial.net/tkinter/tkinter-window/) or the
screen.
"""
import tkinter as tk


def placeALabel(self):
    message = tk.Label(self, text="Hello World!")
    message.grid(column=0, row=0, padx=20, pady=20, sticky=tk.NSEW)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('First window')
        self.geometry('300x150')
        placeALabel(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
