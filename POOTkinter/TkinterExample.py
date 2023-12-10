# https://www.pythontutorial.net/tkinter/tkinter-example/
"""
Tkinter Example

The same program but with a better architecture is available under "Developping a Full Tkinter-Oriented Apllication"

Summary: in this tutorial, you'll learn how to build a Tkinter temperature converter application.

Introduction to the Temperature Converter application
The following show the Temperature Converter application that you're going to build. The application converts a
temperature from Fahrenheit to Celsius:

Basically, the application has a label(https://www.pythontutorial.net/tkinter/tkinter-label/), an
entry(https://www.pythontutorial.net/tkinter/tkinter-entry/) and a
button(https://www.pythontutorial.net/tkinter/tkinter-button/). When you enter a temperature in Fahrenheit and click the
Convert button, it'll convert the value in the textbox from Fahrenheit to Celsius.

If you enter a value that cannot be converted to a number, the program will show an error.
To build this application, you follow these steps.

First, import the tkinter module, ttk submodule, and the showerror function from tkinter.messagebox:
    import tkinter as tk
    from tkinter import ttk
    from tkinter.messagebox import showerror

Second, create the root window and set its configurations:

    class App(tk.Tk)
    self.title('Temperature Converter')
    self.geometry(300x70')
    self.resizable(False, False)

Third, define a function that converts a temperature from Fahrenheit to Celsius:
    def fahrenheit_to_celsisus(f):
    Convert fahrenheit to celsius
    return (f - 32) * 5/9

Fourth, create a frame(https://www.pythontutorial.net/tkinter/tkinter-frame/) that holds form fields:
    frame = ttk.Frame(self)

Fith, define an option that will be used by all the form fields:
    option = {'padx': 5, 'pady': 5}

Sixth, define the label, entry, and button. The label will show the result once you click the Convert button:
    # temperature label
    temperature_label = ttk.Label(frame, text='Fahrenheit')
    temperature.Label.grid(column=0, row=0, sticky='W', **options)

    # temperature entry
    temperature_entry = ttk.Entry(frame, textvariable=temperature)
    temperature_entry.grid(column=1, row=0, **options)
    temperature_entry.focus()

    # convert button
    convert_button = ttk.Button(frame, text='Convert')
    convert_button.grid(column=2, row=0, sticky='W', **options)
    convert_button.configure(command=convert_button_clicked)

    # reslut label
    result_label = ttk.Label(frame)
    result_label.grid(row=1, columnspan=3, **options)

Finally, place the frame on the root window and run the mainloop() method:
    frame.grid(padx=10, pady=10)
    root.mainloop()

Put it all together.
"""
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror


def fahrenheit_to_celsius(f):
    """ Convert fahrenheit to celsius
    """
    return (f - 32) * 5 / 9


def convert_button_clicked(temperature, result_label):
    """ Handle convert button click event
    """
    try:
        f = float(temperature.get())
        c = fahrenheit_to_celsius(f)
        result = f'{f} Fahrenheit = {c:.2f} Celsius'
        result_label.config(text=result)
    except ValueError as error:
        showerror(title='Error', message=error)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Temperature Converter')
        self.geometry("300x70")
        self.resizable(False, False)

        # frame
        frame = ttk.Frame(self)

        # field options
        options = {'padx': 5, 'pady': 5}

        # temperature label
        temperature_label = ttk.Label(frame, text='Fahrenheit')
        temperature_label.grid(column=0, row=0, sticky='W', **options)

        # temperature entry
        temperature = tk.StringVar()
        temperature_entry = ttk.Entry(frame, textvariable=temperature)
        temperature_entry.grid(column=1, row=0, **options)
        temperature_entry.focus()

        # result label
        result_label = ttk.Label(frame)
        result_label.grid(row=1, columnspan=3, **options)

        conver_button = ttk.Button(frame, text='Convert')
        conver_button.grid(column=2, row=0, sticky='W', **options)
        conver_button.configure(command=lambda: convert_button_clicked(temperature, result_label))

        # add padding to the forame and show it
        frame.grid(padx=10, pady=10)


# start the app
if __name__ == "__main__":
    app = App()
    app.mainloop()
