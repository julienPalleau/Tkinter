# https://www.pythontutorial.net/tkinter/tkinter-notebook/
"""
Tkinter Notebook
Summary: in this tutorial, you'll learn how to use the Tkinter Notebook widget to create tabs.

Introduction to the Tkinter Notebook widget
The Notebook widget allows you to seclt pages of contents by clicking on tabs:

When you click one of these tabs, the Notebook widget will display a child pane associated with the selected tab.
Typically, a child pane is a Frame widget.

To create a Notebook widget, you use the ttk.Notebook class as follows:
    notebook = ttk.Notebook(container, **options)

In this syntax, the contanier is the parent of the notebook. Typically, it's root window.

The notebook has some useful options. For example, you use height and width options to specify the height and with in
pixels allocated to the widget.

Also, you can add some space around the outside of the widget by using the padding option.

Notebook methods
The ttk.Notebook class provides you with many handy methods that allow you to manage tabs effectively.

The following describes the most commonly used ones:

add(child, **kwargs)

The add() method adds a child widget to a window. The **kwargs argument is one or more options. Here are the important
ones:
    + The child is a widget to add to the notebook.
    + The text option specifies the label that appears on the tab.
    + The image option specifies the image to be displayed on the tab.
    + If you use bot text and image options, you need to use the compound option. The compound option describels the
      position of the image relative to the text. It can be tk.TOP, tk.BOTTOM, tk.LEFT, tk.RIGHT, tk.CENTER. For
      example, tk.LEFT would place the image to the left of the text.
    + The underline iption that takes wero or positive integer. It specifies the character at a position of the text on
      the tab to be underlined.

hide(tabld)
The hide() method temporarily removes the tab identified by the tabId from the Notebook.
Tabs has a zero-based index. It means that the first tab start at zero.

To show the tab, you need to call the add() method again. There's no corresponging show() method.

forget(child)
The foreget() permanently removes the specified child widget from the notebook.

Tkinter Notebook widget example
The following program shows how to create a notebooks with two bars:
"""
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("400x300")
        self.title('Notebook Demo')

        # create a notebook
        notebook = ttk.Notebook(self)
        notebook.pack(pady=10, expand=True)

        # create frames
        frame1 = ttk.Frame(notebook, width=400, height=280)
        frame2 = ttk.Frame(notebook, width=400, height=280)

        frame1.pack(fill='both', expand=True)
        frame2.pack(fill='both', expand=True)

        # add frames to notebook
        notebook.add(frame1, text='General Information')
        notebook.add(frame2, text='Profile')


if __name__ == "__main__":
    app = App()
    app.mainloop()

"""
How it works.
First, create a notebook widget whose parent is the root window:
    notebook = ttk.Notebook(root)
    notebook.pack(pady=10, expand=True)

Second, create two frames whose parent is the notebook:
    frame1 = ttk.Frame(notebook, width=400, height=280)
    frame2 = ttk.Frame(notebook, width=400, height=280)

    frame1.pack(fill='both', expand=True)
    frame2.pack(fill='both', expand=True)

Third, add these frames to the notebook by using the add() method:
    notebook.add(frame1, text='General Information')
    notebook.add(frame2, text='Profile')
    
Summary
    + Use the ttk.Notebook class to create a notebook widget.
    + Use the add() method to add a tab to the notebook.
    + Use the hide() method to temporarily remove a tab from the notebook. To remove a tab permanently, use the forget()
      method.
"""