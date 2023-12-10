# https://www.pythontutorial.net/tkinter/tkinter-panedwindow/
"""
Tkinter PanedWindow
Summary: In this tutorial, you'll learn how to use the Tkinter PanedWindow widget to divide the space of a frame or a
window.

Introduction to the Tkinter PanedWindow widget
The PanedWindow widget divieds the space of a frame(https://www.pythontutorial.net/tkinter/tkinter-frame/) or a
window(https://www.pythontutorial.net/tkinter/tkinter-window/). A PanedWindow is like a Frame that acts as a container
for holding child widgets.
Typically, a PanedWindow contains a vertical or horizontal stack of child widgets:
A PanedWindow uses a bar to separate the child widgets. This bar is called a sash.
A sash can have a handle which is a small squre that you can drag it with a mouse.
A pane is an area occupided by one child widgget.
To create a PanedWindow widget, you use the following syntax:
    ttk.PanedWindow(container, **options)

A notable option of a PanedWindow widget is the orient option.
if you set the orient to tk.HORIZONTAL, it'll stack child widgets side by side. If orient is tk.VERTICAL, i'll stack
child widgets top to bottom. The orient option defaults to tk.VERTICAL.

Tkinter PanedWindow widget example
The following example illustrates how to use the PanedWindow widget to separate two
Listbox(https://www.pythontutorial.net/tkinter/tkinter-listbox/) widgets:
"""
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('PanedWindow Demo')
        self.geometry("300x200")

        # change style to classic (Windows only)
        # to show the sash and handle
        style = ttk.Style()
        style.theme_use('classic')

        # paned window
        pw = ttk.Panedwindow(orient=tk.HORIZONTAL)

        # left listbox
        left_list = tk.Listbox(self)
        left_list.pack(side=tk.LEFT)
        pw.add(left_list)

        # Right listbox
        right_list = tk.Listbox(self)
        right_list.pack(side=tk.LEFT)
        pw.add(right_list)

        # place the panedwindow on the root window
        pw.pack(fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()

"""
If you run the program on Windows, you're likely will not see the sash and handle displaying. To made it visible, you
can set the default theme to classic

Summary
    + Use the Tkinter PanedWindow widget to divide the space of a window or a frame.
"""