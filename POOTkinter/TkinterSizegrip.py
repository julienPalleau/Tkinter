# https://www.pythontutorial.net/tkinter/tkinter-sizegrip/
"""
Tkinter Sizegrip
Summary: in this tutorial, you'll learn how to use the Tkinter Sizegrip widget that allows you to resize the entire
appication window.

Introduction to the Tkinter Sizegrip widget
The Sizegrip widget typically locates in the bottom right corner of the window. It allows you to resize the enter
application window:
To create a Sizegrip widget, you use the following syntax:
    ttk.Sizegrip(parent, **option)

To make sure Sizegrip widget works properly, you need to make the root window resizable.
If you use the grid geometry manager, you need to configure column and row sizes.

Tkinter Sizegrip widget example
The following program displays a Sizegrip at the bottom right of the root window:
"""
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sizegrip demo")
        self.geometry("300x200")
        self.resizable(True, True)

        # grid layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # create the sizegrip
        sg = ttk.Sizegrip(self)
        sg.grid(row=1, sticky=tk.SE)


if __name__ == "__main__":
    app = App()
    app.mainloop()

"""
How it works.
First, make sure the root window resizable:
    self.resizable(True, True)
    
Second, configure the grid layout:
    self.columnconfigure(0, weight=1)
    self.rowconfigure(0, weight=1)
    
Third, create a Sizegrip widget:
    sg = ttk.Sizegrip(root)
    sg.grid(row=1, sticky=tk.SE)
    
Summary
+ Use the Tkinter Sizegrip widget to allow users to resize the entire window application.
"""