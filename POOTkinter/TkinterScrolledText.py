# https://www.pythontutorial.net/tkinter/tkinter-scrolledtext/
"""
Tkinter ScrolledText
Summary: In this tutorial, you'll learn how to use the Tkinter ScrolledText widget that constis of a Text widget and
vertical Scrollbar widget.

Introduction to the Tkinteter ScrolledText widget
So far, you've learned how to create a Text(https://www.pythontutorial.net/tkinter/tkinter-text/) and how to link a
vertical Scrollbar(https://www.pythontutorial.net/tkinter/tkinter-scrollbar/) to the text widget.

To make it more venient, Tkinter provides you the ScrolledText widget which does the same things as a text widget linked
to a vertical scroll bar.

To use the ScrolledText widget, you need to import the ScrolledText class from tkinter.scrolledtext module.

Technically, the ScrolledText class inherits from the Text class.

The ScrolledText widget uses a frame(https://www.pythontutorial.net/tkinter/tkinter-frame/) widget inserted between the
container and the Text widget to hold the Scrollbar widget.

Therefore, the ScrolledText has the same properties and methods as the Text widget. In addition, the geometry manager
methods including pack(https://www.pythontutorial.net/tkinter/tkinter-pack/),
grid(https://www.pythontutorial.net/tkinter/tkinter-grid/), and
place(https://www.pythontutorial.net/tkinter/tkinter-place/) are restricted to the Frame.

Tkinter ScrolledText widget example
The following program illustrates how to create a ScrolledText widget:
"""
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("ScrolledText Widget")

        st = ScrolledText(self, width=50, height=10)
        st.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()

"""
How it works.
    + First, import the tkinter module and the ScrolledText class from the tkinter.scrolledtext module.
    + Second, create the root window and set its title to 'scrolledText Widget'.
    + Third, create a new ScrolledText widget and display it on the root window.
    + Finally, start the main loop.
"""