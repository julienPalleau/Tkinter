# https://www.pythontutorial.net/tkinter/tkinter-text/
"""
Tkinter Text
Summary: In this tutorial, you'll learn how to use the Tkinter Text widget to add a text editor to your application.

Introduction to Tkinteter Text widget
The Text widget allows you to display and edit multi-line textarea with various styles. Besides the plain text, the text
widget supports embedded images and links.
To create a text widget, you use the following syntax:
text = tk.Text(master, conf={}, **kw)
In this syntax:
    + The master is the parent component of the text widget.
    + The conf is a dictionary that specifies the widget's configuration.
    + The kw is one or more keyword argument used to configure the Text wdiget.

-----------------------------------------------------------------------------------------
Note that the Text is only available in the Tkinter module, not the tkinter.ttk module. -
-----------------------------------------------------------------------------------------

-----------------------------------------------------------------------------------------------
The following example creates a Text widget with eight rows and places it on the root window: -
-----------------------------------------------------------------------------------------------
"""
# import tkinter as tk
# from tkinter import Tk, Text
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#
#         self.resizable(False, False)
#         self.title("Text Widget Example")
#
#         text = Text(self, height=8)
#         text.pack()
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

"""
In this example, the height argument specifies the number of rows of the Text widget.
Inserting initial content
To insert contents into the text area, you use the insert() method. For example:
"""
import tkinter as tk
from tkinter import Tk, Text


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.resizable(False, False)
        self.title("Text Widget Example")

        text = Text(self, height=8)
        text.pack()
        text.insert("1.0", "This text has been inserted in line 1, column 0")


if __name__ == "__main__":
    app = App()
    app.mainloop()

"""
The first argument of the insert() method is the position where you want to insert the text.
The position has the following format:
'line.column'

In the above example, '1.0' means line 1, character 0, which is the first character of the first line on the text area.

Retrieving the text value
To retrive the contents of a text widget, you use its get() method. For example:
text_content = text.get('1.0', 'end')

The get() method accepts two arguments. The first argument is the position, and the second is the end position.
To retrieve only part of the text, you can specify different start and end positions.

Disabling the Text widget
To prevent users from chaning the content of a Text widget, you can disable it by setting the state option to 'disable'
like this:
text['state'] = 'disabled'
To re-enable editing, you can change the state option back to normal:
text['state'] = 'normal'

Summary
+   Use Tkinter Text widget to create multi-line text area
"""