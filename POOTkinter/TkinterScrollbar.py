# https://www.pythontutorial.net/tkinter/tkinter-scrollbar/
"""
Tkinter Scrollbar
Summary: in this tutoiral, you'll learn about the Tkinter Scrollbar widget and how to link it to a scrollable widget.

Introduction to the Tkinter scrollbar widget
A scrollbar allows you to view all parts of another widget whose content is typically larger than available space.
Tkinter scrollbar widget is not a part of any other widgets such as
Text(https://www.pythontutorial.net/tkinter/tkinter-text/) and
Listbox(https://www.pythontutorial.net/tkinter/tkinter-listbox/). Instead, a scrollbar an independant widget.
To use the scrollbar widget, you need to:
    + Frist, create a scrollbar widget.
    + Second, link the scrollbar with a scrollable widget.

The following shows how to create a scrollbar widget using the ttk.Scrollbar constructor:
scrollbar == ttk.Scrollbar(
    container,
    orient='vertical',
    command=widget.yview
)

In this syntax:
    + The container is the window(https://www.pythontutorial.net/tkinter/tkinter-window/) or
    frame (https://www.pythontutorial.net/tkinter/tkinter-frame/) on which the scrollbar locates.
    + The orient argument specifies whether the scrollbar needs to scroll horizontally or vertically.
    + The command argument allows the scrollbar widget to communicate with the scrollable widget.

The scrollable widget also needs to communicate back to the scrollbar about the percentage of the entire content area
that is currently visible.

Every scrollable widget has a yscrollcommand and/or xscrollcommand options. And you can assign the scrollbar.set method
to it:
widget['yscrollcommand'] = scrollbar.set

Tkinter scrollbar widget example
The Text widgets are one of several types of scrollable widgets. The following program illustrates a simple user
interface that consists of Text and Scrollbar widgets:
"""
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.resizable(False, False)
        self.title("Scrollbar Widget Example")

        # apply the grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # create the text widget
        text = tk.Text(self, height=10)
        text.grid(row=0, column=0, sticky='ew')

        # create a scrollbar widget and set its command to the text widget
        scrollbar = ttk.Scrollbar(self, orient='vertical', command=text.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')

        # communicate back to the scrollbar
        text['yscrollcommand'] = scrollbar.set


if __name__ == "__main__":
    app = App()
    app.mainloop()

"""
Summary
    + Create a scrollbar with ttk.Scrollbar(orient, command)
    + The orient can be 'vertical' or 'horizontal'
    + The command can be yview or xview property of the scrollable widget that links to the scrollbar.
    + Set the yscrollcommand property of the scrollable widget so it links to the scrollbar.
"""