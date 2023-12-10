# https://www.pythontutorial.net/tkinter/tkinter-messagebox/
"""
Tkinter Messagebox
Summary: in this tutorial, you'll learn how to show various message boxes using the tkinter.messagebox module.

Introduction to tkinter.messagebox module
When developing a Tkinter application, you often want to notify users about the events that occured.

For example, when users clic the save button(https://www.pythontutorial.net/tkinter/tkinter-button/), you want to notify
them that the record has been saved successfully.

If an error occured, for example, the database server is not reachable, you can notify users of the error.

When the update has been completed but the record already exists, you may want to show a warning.

To cover all of these scenarios, you can use various functions from the tkinter.messagebox module:
    + showinfo() - notify that an operation completed successfully.
    + showerror() - notify that an operation hasn't completed due to an error.
    + showarning() - notify that an operation completed but something didn't behave as expected.

All of these functions accept tow arguments:
    whowinfo(title, message)
    showerror(title, message)
    showwarning(title, message)

    + The title is dsplayed on the title bar of the dialog.
    + The message is shown on the dialog.

To span the message multiple lines, you can add the new line character '\n'.

Tkinter messagebox examples
The following program consists of three buttons. When you click a button, the corresponding message box will display.
"""
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo


# create the root window
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MessageBox')
        self.resizable(False, False)
        self.geometry('300x150')

        options = {'fill': 'both', 'padx': 10, 'pady': 10, 'ipadx': 5}

        ttk.Button(
            self,
            text='Show an error message',
            command=lambda: showerror(
                title='Error',
                message='This is an error message')
        ).pack(**options)

        ttk.Button(
            self,
            text='Show an information message',
            command=lambda: showinfo(
                title='Information',
                message='This is an information message.')
        ).pack(**options)

        ttk.Button(
            self,
            text='Show a warning message',
            command=lambda: showwarning(
                title='Warning',
                message='This is a warning message.')
        ).pack(**options)


if __name__ == "__main__":
    app = App()
    app.mainloop()

"""
Summary
    + Use showinfo(), showerror(), showwarning() functions form the tkinter.messagebox module to show an information,
      error, and warning message.
"""