# https://www.pythontutorial.net/tkinter/tkinter-listbox/
"""
Tkinter Listbox
Summary: in this tutorial, you'll learn how to use the Tkinter Listbox widget to display a list of items.

Introduction to the Tkinter Listbox
A Listbox widget displays a list of single-line text items. A Listbox allows you to browse through the items and select
one or multiple items at once.
To create a listbox, you use the tk.Listbox class like this:
    listbox = tk.Listbox(container, listvariable, height)

In this syntax:
    + The container is the parent component of the listbox.
    + listvariable links to a StringVar object. More explanation on this later.
    + The height is the number of items that the listbox will display without scrolling

Managing list items
To populate items to a Listbox, you first create a StingVar object that is initialized with a list of items. And then
you assigh this StrinVar object to the listvariable option as follow:
    list_items = StringVar(value=items)
    listbox = tk.Listbox(
        container,
        height,
        listvariable=list_items
    )

To add, remove, or rearrange items in the Listbox, you just need to modify the list_items variable.

Selecting list items
The selectmode option determines whether you can select a single item or multiple items at a time.
    + 'browse' - allows a single selection.
    +   'extended' - allows multiple selection.
By default, the selectmode is 'browse'. The curselection() method returns a list of currently selected indices.

Binding the selected event
To execute a function when the selected itms changes, you bind that function to the
<<listboxSelect>> event:
    listbox.bind('<<ListboxSelect>>', callback)

Tkinter Listbox widget example
The following program displays a Listbox that contains a list of programming languages.
When you select one or more item, the program displays the selected ones on a message box:
"""
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


# create the root window
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("200x100")
        self.resizable(False, False)
        self.title('Listbox')

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # create a list box
        langs = ('Java', 'C#', 'C', 'C++', 'Python',
                 'Go', 'JavaScript', 'Java', 'PHP',
                 'Swift')

        langs_var = tk.StringVar(value=langs)

        listbox = tk.Listbox(
            self,
            listvariable=langs_var,
            height=6,
            selectmode="multiple"
        )

        listbox.grid(
            column=0,
            row=0,
            sticky='nwes'
        )

        # handle event
        def items_selected(event):
            """ handle item selected event
            """
            # get selected indices
            selected_indices = listbox.curselection()
            # get selected items
            selected_langs = ",".join([listbox.get(i) for i in selected_indices])
            msg = f'You selected: {selected_langs}'

            showinfo(
                title='Information',
                message=msg
            )

        listbox.bind('<<ListboxSelect>>', items_selected)


if __name__ == "__main__":
    app = App()
    app.mainloop()

"""
How it works.
First, create a Stringvar that holds a list of programming languages:
    langs = ('Java', 'C#', 'C', 'C++', 'Python',
                     'Go', 'JavaScript', 'Java', 'PHP',
                     'Swift')
    langs_var = tk.StringVar(value=langs)
    
Second, create a new Listbox widget and assign the StringVar object to the listvariable:
    listbox = tk.Listobx(
                self,
                listvariable=lang_var,
                height=6,
                selectmode='extended')
                
The height shows six programming languages without scrolling. The selectmode='extended' allows multiple selections.

Third, define a function that will be invoked when one or more items are selected. The items_selected() function shows
a list of currently selected list items:
        def items_selected(event):
            # get selected indices
            selected_indices = listbox.curselection()
            # get selected items
            selected_langs = ",".join([listbox.get(i) for i in selected_indices])
            msg = f'You selected: {selected_langs}'

Adding a scrollbar to the listbox
The following program illustrates how to add a scrollbar to a listobx:
"""
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


# create the root window
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("200x100")
        self.resizable(False, False)
        self.title('Listbox')

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # create a lit box
        langs = ('Java', 'C#', 'C', 'C++', 'Python',
                 'Go', 'JavaScript', 'PHP', 'Swift')

        langs_var = tk.StringVar(value=langs)

        listbox = tk.Listbox(
            self,
            listvariable=langs_var,
            height=6,
            selectmode='multiple'
        )

        listbox.grid(
            column=0,
            row=0,
            sticky='nwes'
        )

        # link a scrollbar to a list
        scrollbar = ttk.Scrollbar(
            self,
            orient='vertical',
            command=listbox.yview()
        )

        listbox['yscrollcommand'] = scrollbar.set

        scrollbar.grid(
            column=1,
            row=0,
            sticky='ns'
        )

        # handle event

        def items_selected(event):
            """ event: handle item selected evet
            """
            # get selected indices
            selected_indices = listbox.curselection()
            # get selected items
            selected_langs = ",".join([listbox.get(i) for i in selected_indices])
            msg = f'You selected: {selected_langs}'

            showinfo(
                title='Information',
                message=msg
            )

        listbox.bind('<<ListboxSelect>>', items_selected)


if __name__ == "__main__":
    app = App()
    app.mainloop()

"""
For more information on how to link a scrollbar to a scrollable widget, check out the 
scrollbar widget tutorial (https://www.pythontutorial.net/tkinter/tkinter-scrollbar/)

Summary
    + Use the tk.Listbox(container, height, listvariable) to create a Listbox widget; a listvariable should be a
      tk.StringVar(value=items).
    + Set the selectmode to 'extended' to allow multiple selection; otherwise, use 'browse'.
    + Bind a callback function to the '<>' event to execute the function when one or more list items are selected.
"""