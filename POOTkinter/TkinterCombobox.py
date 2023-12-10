# https://www.pythontutorial.net/tkinter/tkinter-combobox/
"""
Tkinter Combobox
Summary: In this tutorial, you'll learn to create a Tkinter combobox widget that allows users to select one value from
a set of values.

Introduction to the Tkinter Combobox widget
A combobox is a combination of an Entry and a Listbox widget. A combobox widget allows you to select one value in a set
of values. In addition, it allows you to enter a custom value.

Create a combobox
To create a combobox widget, you'll use the ttk.Combobox() constructor. The following example creates a combobox widget
and links it to a string variable:
    current_var = tk.StringVar()
    combobox = ttk.combobox(container, textvariable=current_var)

The container is the window or frame on which you want to place the combobox widget.
The textvariable argument links a variable current_var to the current value of the combobox.
To get the currently selected value, you can use the current_var variable:
    current_value = current_var.get()

Alternatively, you can use the get() method of the combobox object:
current_value = combobox.get()
To set the current value, you use the current_var variable or the set() method of the combobox object:
current_value.set(new_value)
    comobobx.set(new_valuel)

Define value list
The combobox has the values property that you can assign a list of values to it like this:
    combobox['values'] = ('value1', 'value2', 'value3')

Byt default, you can enter a custom value in the combobox, if you don't want this, you can set the state option to
'readonly':
combobox['stat'] = 'readonly'
To re-enable editing the combobox, you use the 'normal' state like this:
    combobox['state'] = 'normal'

Bind events
When a select value changes, the combobox widget generates a '<<ComboboxSelected>>' virtual event. To handle the event,
you can use the bind() like this:
    combobox.bind('<<ComboboxSelected>>', callback)

In this example, the callback function will execute when the selected value of the combobox changes.

Set the current value
To set the current value, you use the set() method:
    combobox.set(self, value)
Also you can use the current() method:
    current(self, newindex=None)

The newindex specifies the index of values from the list that you want to select as the current value.
If you don't specify the newindex, the current() method will return the index of the current value in the list of values
or -1 if the current value doesn't appear in the list.

Python Tkinter combobox example
The following progruam illustrates how to create a combobox widget:
"""
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # config the root window
        self.geometry("300x200")
        self.resizable(False, False)
        self.title('Combobox Widget')

        # label
        label = ttk.Label(text="Please select a month:")
        label.pack(fill=tk.X, padx=5, pady=5)

        # create a combobox
        selected_month = tk.StringVar()
        month_cb = ttk.Combobox(self, textvariable=selected_month)

        # get first 3 letters of every month name
        month_cb['values'] = [month_name[m][0:3] for m in range(1, 13)]

        # prevent typing a value
        month_cb['state'] = 'readonly'

        # place the widget
        month_cb.pack(fill=tk.X, padx=5, pady=5)

        # bind the selected value changes
        def month_chanded(event):
            """ handle the month changed event """
            showinfo(
                title='Result',
                message=f'You selected {selected_month.get()}!'
            )

        month_cb.bind('<<ComboboxSelected>>', month_chanded)


if __name__ == "__main__":
    app = App()
    app.mainloop()
