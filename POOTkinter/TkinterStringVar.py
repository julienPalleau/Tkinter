# https://www.pythontutorial.net/tkinter/tkinter-stringvar/
"""
Tkinter StringVar
Summary
In this tutorial, you'll learn about the Tkinter StringVar object and how to use it to manipulate values of widgets.

Introduction to the Tkinter StringVar
The Tkinter StringVar helps you manage the value of a widget such as a Label or Entry more effectively.
To create a new StringVar object, you use the StringVar constructor like this:
string_var = tk.StringVar(container, value, name)
The StringVar constructor accepts three optional arguments:
    + container is a widget that the StringVar object associated with. If you skip the container, it defaults to the
    root window.
    + value is the initial value that defaults to an empty string ''.
    + name is a Tcl name that defaults to PY_VARnum e.g. PY_VAR1, PY_VAR2, etc...

After creating the StringVar object, you can assign it to the textvariable of a widget that accepts a StringVar object.
For example, the following assigns the string_var to textvariable of the Entry widget:
name_entry = ttk.Entry(root, textvariable=stringvar)

To get the current value of the Entry widget, you can use the get() method of the StringVar object:
name_var.get()

To invoke a callback whenever the value of an StringVar object changes, you use the trace() method of the StringVar
object:
string_var.trace('w', callback)
The 'w' mode will automatically invoke the callback whenever the value of the string_var changes.
The StringVar also provides you with two other modes 'r' and 'u':
    + 'r' (read) - invoke the callback whenever the variable is read.
    + 'u' (unset) - invoke the callback whenever the variable is deleted.

Tkinter StringVar example
The following example illustrates how to use the StringVar object for an Entry widget:
# """
# import tkinter as tk
# from tkinter import ttk
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title('Tkinter StringVar')
#         self.geometry("300x80")
#
#         self.name_var = tk.StringVar(self, 'hello')
#
#         self.columnconfigure(0, weight=1)
#         self.columnconfigure(1, weight=1)
#
#         self.create_widgets()
#
#     def create_widgets(self):
#         padding = {'padx': 5, 'pady': 5}
#         # label
#         ttk.Label(self, text='Name').grid(column=0, row=0, **padding)
#
#         # Entry
#         name_entry = ttk.Entry(self, textvariable=self.name_var)
#         name_entry.grid(column=1, row=0, **padding)
#         name_entry.focus()
#
#         # Button
#         submit_button = ttk.Button(self, text='Submit', command=self.submit)
#         submit_button.grid(column=2, row=0, **padding)
#
#         # Output label
#         self.output_label = ttk.Label(self)
#         self.output_label.grid(column=0, row=1, columnspan=3, **padding)
#
#     def submit(self):
#         self.output_label.config(text=self.name_var.get())
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

"""
How it works.
First, create a new StringVar object in the __init__() method of the App class:
self.name_var = tk.StringVar()

Second, assign the StringVar object to the textvariable option of the Entry widget in the create_widgets() method:
name_entry = ttk.Entry(self, textvariable=self.name_var)

Third, set the text of the output_label widget to the value of the name_var object the button is clicked.
self.output_label.config(text=self.name_var.get())

Tkinter StringVar - Tracing text changes example
The following example illustrates how to use the StringVar object to trace text changes.
The root window has two Entry widgets: password and confirm password. If you enter the confirm password that is
different from the password. it'll show an error message. Otherwise, it'll show a success message:
"""
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    ERROR = 'Error.TLabel'
    SUCCESS = 'Success.TLabel'
    WARNING = 'Warning.TLabel'

    def __init__(self):
        super().__init__()
        self.title('Change Password')
        self.geometry("300x130")

        self.password_var = tk.StringVar()
        self.confirm_password_var = tk.StringVar()

        self.confirm_password_var.trace('w', self.validate)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # set style
        self.style = ttk.Style(self)
        self.style.configure('Error.TLabel', foreground='red')
        self.style.configure('Success.TLabel', foreground='green')
        self.style.configure('Warning.TLabel', foreground='orange')

        self.create_widgets()

    def create_widgets(self):
        """ create a widget
        """
        padding = {'padx': 5, 'pady': 5, 'sticky': tk.W}

        # message
        self.message_label = ttk.Label(self)
        self.message_label.grid(column=0, row=0, columnspan=3, **padding)

        # password
        ttk.Label(self, text='New Password').grid(column=0, row=1, **padding)

        password_entry = ttk.Entry(self, textvariable=self.password_var, show='*')
        password_entry.grid(column=1, row=1, **padding)
        password_entry.focus()

        # Confirm password
        ttk.Label(self, text='Confirm Password:').grid(column=0, row=2, **padding)

        confirm_password = ttk.Entry(self, textvariable=self.confirm_password_var, show='*')
        confirm_password.grid(column=1, row=2, **padding)
        confirm_password.focus()

        # Change button
        submit_button = ttk.Button(self, text='Change')
        submit_button.grid(column=0, row=3, **padding)

    def set_message(self, message, type=None):
        """ set the error or success message
        """
        self.message_label['text'] = message
        if type:
            self.message_label['style'] = type

    def validate(self, *args):
        """ validate the password
        """
        password = self.password_var.get()
        confirm_password = self.confirm_password_var.get()

        if confirm_password == password:
            self.set_message(
                "Success: The new password looks good!", self.SUCCESS
            )
            return

        if password.startswith(confirm_password):
            self.set_message('Warning: Keep entering the password', self.WARNING)
            return

        self.set_message("Error: Passwords don't match!", self.ERROR)


if __name__ == "__main__":
    app = App()
    app.mainloop()
