# https://www.pythontutorial.net/tkinter/tkinter-askokcancel/
"""
Tkinter askokcancel
Summary: in this tutorial, you'll learn how to use the Tkinter askokcancel() function to show a confirmation dialog.

Introduction to the Tkinter askokcancel() function
The askokcancel() function shows a confirmation dialog that has two buttons: ok and cancel.
    answer=askokcancel(title, message, **options)

if you click the ok button, the function returns True. However, if you click the cancel button, the function returns
false.

Tkinter askokcancel() example
The following program shows a Delete All button. If you click the button, the program will show a confirmation dialog
that has two buttons: ok and Cancel.

If you click the ok button, the program will show a message box indicating that all the data has been deleted
successfully:

The program:
"""
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel, showinfo, WARNING


def confirm():
    answer = askokcancel(
        title='Confirmation',
        message='Deleting will delete all the data.',
        icon=WARNING
    )

    if answer:
        showinfo(
            title='Deletion Status',
            message='The data is deleted successfully'
        )


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter Ok/Cancel Dialog')
        self.geometry('300x150')

        delete_button = ttk.Button(
            self,
            text='Delete All',
            command=confirm)

        delete_button.pack(expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()

"""
Summary
    + Use the Tkinter askokcancel() function to display a confirmation dialog with two buttons OK and Cancel.
    + The askokcancel() function returns True if you click the OK button and False if you click the Cancel button
"""
