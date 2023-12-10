# https://www.pythontutorial.net/tkinter/tkinter-radio-button/
"""
Tkinter Radio Button
Summary: in this tutorial, you'll learn how to use the Tkinter radio button widget to allow users to select between
one of a number of mutually exclusive choices.

Introduction to Tkinter radio buttons
Radio buttons allow you to select between one of a number of mutually exclusive choices.
Typically, you use radio buttons together in a set. The're a good option if you have a few choices that you want users
to select.

To create radio buttons, you use the Radiobutton widget. The following shows how to create rado buttons using the
ttk.Radiobutton constructor:
selected = tk.StringVar()
r1 = ttk.Radiobutton(container, text='Option 1', value='Value 1', variable=selected)
r2 = ttk.Radiobutton(container, text='Option 2', value='Value 2', variable=selected)
r3 = ttk.Radiobutton(container, text='Option 3', value='Value 3', variable=selected)

Each radio button has a different value. However, radio buttons in the same group share the same variable.
The container is the parent widget which you place the radio button on.
The text argument specicifies the text appears on the radio button.
The value argument specifies the value that the radio button will hold.
the variable must be a tk.StringVar().

Tkinter radio button example
The following program illustrates how to use radio buttons. It returns the selected size once you click the GetSelected
Size button.
"""
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


# root window
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("300x220")
        self.resizable(False, False)
        self.title('Radio Button Demo')

        def show_selected_size():
            showinfo(
                title='Result',
                message=selected_size.get()
            )

        selected_size = tk.StringVar()
        sizes = (('Small', 'S'),
                 ('Medium', 'M'),
                 ('Large', 'L'),
                 ('Extra Large', 'XL'),
                 ('Extra Extra Large', 'XXL'))

        # Label
        label = ttk.Label(text="What's your t-shirt size?")
        label.pack(fill='x', padx=5, pady=5)

        # radio buttons
        for size in sizes:
            r = ttk.Radiobutton(
                self,
                text=size[0],
                value=size[1],
                variable=selected_size
            )
            r.pack(fill='x', padx=5, pady=5)

        # button
        button = ttk.Button(
            self,
            text="Get Selected Size",
            command=show_selected_size
        )

        button.pack(fill='x', padx=5, pady=5)


if __name__ == "__main__":
    app = App()
    app.mainloop()

"""
Summary
    + Use ttk.Radiobutton(text, variable) to create a radio button, the variable should be a tk.StringVar()
    + A set of radio button share the same variable.
"""