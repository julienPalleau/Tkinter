# https://www.pythontutorial.net/tkinter/tkinter-askretrycancel/
"""
Tkinter askretrycancel
Summary: in this tutorial, you'll learn how to use the Tkinter askretrycancel() function to show a Retry/Cancel
confirmation dialog.

Introduction to the Tkinter askretrycancel() function
Sometimes, the application performs a tasks but fails to do so because of an error.

For example, you may want to connect to a database server. However, the database server is currently not reacheable. It
may be offline for a short period of time.

In this case, you can display a confirmation dialog that allow users to reconnect to the database or just keep the
application as is.

To display the Retry/Cancel dialog, you can use the askretrycancel() functions:
    answer = askretrycancel(title, message, **options)

The askretrycancel() function returns True if the Retry button is clicked. If the Cancel button is clicked, it returns
False.

Tkinter askretrycancel() function example
The following program shows a button that simulates a bad database connection:

If you click the button, it'll show a Retry/Cancel dialog saying that the database server is not reachable. It'll also
request you to reconnect to the database server:

If you click the Retry button, it'll show a dialog indicating that the program is attempting to reconnect to the
database server.

Program:
"""
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askretrycancel, showinfo


def confirm():
    answer = askretrycancel(
        title='Connection Issue',
        message='The database server is unreachable. Do you want to retry?'
    )
    if answer:
        showinfo(
            title='Information',
            message='Attempt to connect to the database again.'
        )


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter OK/Retry Dialog')
        self.geometry('300x150')

        ttk.Button(
            self,
            text='Connect to the Database Server',
            command=confirm).pack(expand=True
                                  )


if __name__ == "__main__":
    app = App()
    app.mainloop()

"""
Summary
    + Use the askretrycancel() function to display a Retry/Cancel dialog to confirm users to carry an operation again.
    + The askretrycancel() function returns True if the Retry button is clicked. If the Cancel button is clicked, it 
      returns False.
"""