# https://www.pythontutorial.net/tkinter/tkinter-validation/
"""
Tkinter Validation
Summary: in this tutorial, you 'll learn how to use the Tkinter validation to validate user inputs.

Introduction to the Tkinter validation
Tkinter validation relies on the three options that you can use for any input widget such as
Entry(https://www.pythontutorial.net/tkinter/tkinter-entry/) widget:
    + validate: speicifies which type of event will trigger the validation.
    + validatecommand: check if a data is valid
    + invalidcommand: executes when the data is invalid. In other words, i'll execute if the validatecommand returns
      false

Validate
The validate command can be one of the following string values:
------------------------------------------------
focus    | validate whenever the widget gets or loses focus
focusin  | validate whenever the widget gets focus.
focusout | validate whenever the widget loses focus.
key      | validate whenever any keystroke changes the widget's contents.
all      | validate in all the above situations focusing, focusout, and key
none     | Turn the validation off. This is the default. Please note that the string 'none' is not the None value in
Python

Validatecommand
The validatecommand is a tuple that contains:
    + A reference to a Tcl/Tk function
    + Zero or more substitution codes specify the information that triggers the event you want to pass into the function

To get a reference to a Tcl/Tk function, you pass a callable to the widget.register() method. It returns a string that
you can use with the validatecommand.

The following table shows the substitution codes that  you can use with the tuple:
----------------------------------------------------------------------------------
%d      Action code: 0 for an attempted deletion, 1 for an attempted insertion, or -1 if the callback was called for
        focus in, focus out, or a chage to the textvariable.

%i      When the user attempts to insert or delete text, this argument will be the index of the beginning of the
        insertion or deletion. If the callback was due to focus in, focus out, or a chage to the textvariable, the
        argumnent will be -1.

%P      The value that the next will have if the change is allowed.

%s      The text in the entry before the change.

%S      If the call was due to an insertion or deletion, this argument will the text being inserted or deleted.

%v      The current value of the widget's validate option.

%V      The reason for this callback: one of 'focusin', 'focusout', 'key', or 'forced' if the textvariable was changed.

%W      The name of the widget.

The following example constructs a validatecommand that use the self.validate() method and %P substitution code:
vcmd = (self.register(self.validate), '%P')

invalidcommand
Like the validatecommand, the invalidcommand also requires the use of the widget.register() method and substitute code.
The following example returns a tuple that you can pass into the invalidcommand option:
ivcmd = (self.register(self.on_invalid),)

Tkinter validation example
We'll create a form that contains an email input. If you enter an invalid email address, it'll show an error message and
change the text color of the email input to red. And we'll trigger the validation event when the focus is moving out the
entry.
Here's teh completer program:
"""
import tkinter as tk
from tkinter import ttk
import re


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter Validation Demo')

        self.create_widgets()

    def create_widgets(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=1)

        # label
        ttk.Label(text='Email:').grid(row=0, column=0, padx=5, pady=5)

        # email entry
        vcmd = (self.register(self.validate), '%P')
        ivcmd = (self.register(self.on_invalid),)

        self.email_entry = ttk.Entry(self, width=50)
        self.email_entry.config(validate='focusout', validatecommand=vcmd, invalidcommand=ivcmd)
        self.email_entry.grid(row=0, column=1, columnspan=2, padx=5)

        self.label_error = ttk.Label(self, foreground='black')
        self.label_error.grid(row=1, column=1, sticky=tk.W, padx=5)

        # button
        self.send_button = ttk.Button(text='Send').grid(row=0, column=4, padx=5)

    def show_message(self, error='', color='black'):
        print(error, color)
        self.label_error['text'] = error
        self.email_entry['foreground'] = color

    def validate(self, value):
        """
        Validate the email entry
        :param value:
        :return:
        """
        print("validate1")
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value) is None:
            print("validate2")
            return False

        self.show_message('validate', 'green')
        print("validate3")
        return True

    def on_invalid(self):
        """
        Show the error message if the data is not valid
        :return:
        """
        self.show_message('Please enter a valid email', 'red')
        print("on_invalid")


if __name__ == "__main__":
    app = App()
    app.mainloop()
