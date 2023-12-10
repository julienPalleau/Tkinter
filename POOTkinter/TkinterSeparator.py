# https://www.pythontutorial.net/tkinter/tkinter-separator/
"""
Tkinter Separator
Summary: In this tutorial, you'll learn how to use the Tkinter Separator widget to display a thin horizontal or vertical
rule between groups of widgets.

Introduction to the Tkinter Separator widget
A separator widget places a thin horizontal or vertical rule between groups of widgets.

To create a separator widget, you use the ttk.Separator constructor like this:
sep = ttk.Separator(container, orient='horizontal')

The orient option can either 'horizontal' or 'vertical'.

The following example illustrates how to use a separator widget to separate two
labels(https://www.pythontutorial.net/tkinter/tkinter-label/):
"""
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x200')
        self.resizable(True, True)
        self.title('Separator Widget Demo')

        ttk.Label(self, text="First Label").pack()

        separator = ttk.Separator(self, orient='horizontal')
        separator.pack(fill='x')
        ttk.Label(self, text='Second Label').pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()

"""
Notice that the size of a separor is 1 px. Therefore, you need to set the fill or sticky property to adjust its size.
Summary
    + Use a separator widget to place a thin horizontal or vertical rule between groups of widgets.
    + Remember to set the fill or sticky property to adjust the size of the separator.
"""