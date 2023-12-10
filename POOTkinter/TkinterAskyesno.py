# https://www.pythontutorial.net/tkinter/tkinter-askyesno/
"""
Tkinter askyesno

Summary: in this tutorial, you'll learn how to use the Tkinter askyesno() function to show a dialog that asks for user
confirmation.

Introduction to the Tkinter askyesno() function
Sometimes, you need to ask for suer confirmation. For example, if users click the quit button, you want to ask whether
they really want to close the application. Or they just accidentally do so:

To show a dialog that asks for user confirmation, you use the askyesno() function.
Sometimes, you need to ask for user configrmation. For example, if users click the quit button, you want to ask whether
they really want to close the application. Or they just accidentally do so:

To show a dialog that asks for user confirmation, you use the askyesno() function.

The dialog will have a title, a message, and two buttons (yes and no).

When you click the yes button, the function returns True. However, if you click the no button, it return False.

The following shows the syntax of the askyesno() function:
    answer = askyesno(title, message, **options)

Note that the answer is a Boolean value, either True or False.

Tkinter also has another function called askquestion(), which is similar to the askyesno() function except that it
returns a string with a value of 'yes' or 'no':
    answer= askquestion(title, message, **options)

Tkinter askyesno() function example
The following program illustrates how to use the Tkinter askyesno() function:

When you click the Quit button, it'll show a confirmation dialog:

If you click the yes button, the application will be closed. Otherwise, it'll stay.
"""
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter Yes/No Dialog')
        self.geometry('300x150')

        # click event handler
        def confirm():
            answer = askyesno(title='confirmation',
                              message='Are you sure that you want to quit?')
            if answer:
                self.destroy()

        ttk.Button(
            self,
            text='Ask Yes/No',
            command=confirm).pack(expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()

"""
Summary
    + Use the Tkinter askyesno() function to show a dialog that asks for user confirmation.
    + The askyesno() function returns True if you click the yes button, otherwise, it returns False.
    + The askquestion() function returns a string with a value of 'yes' or 'no' instead.
"""