# https://www.pythontutorial.net/tkinter/tkinter-menubutton/
"""
Tkinter Menubutton
Summary: in this tutorial, you'll learn how to use the Tkinter Menubutton widget.

Introduction to the Menubutton widget
A Menubutton widget is a combination of a Button and a Menu widget.
When you click the Menubutton, it shows a menu with choices. For example:
To create a Menubutton widget, you follow these steps:

First, create a Menubutton widget:
    menu_button = ttk.Menubutton(container, **options)

Second, create a new instance of the Menu class:
    menu = tk.Menu(menu_button, tearoff=False)

Third, add one or more menu items to the menu instance. And you can add Checkbutton or Radiobutton widgets to the menu.
Finally, assign the Menu to the MenuButton instance:
    menu_button["menu"] = menu

Tkinter Menubutton widget example
The following program illustrates how to use Menubutton widget. When you click the Menubuton, it'll display a menu that
constists of three choices:red, green, and blue.

The background color of the main window will change based on the selected menu item of the Menubutton:
"""
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("300x250")
        self.title('Menubutton Demo')

        # Menubutton variable
        self.selected_color = tk.StringVar()
        self.selected_color.trace('w', self.menu_item_selected)

        # create the menu button
        self.create_menu_button()

    def menu_item_selected(self, *args):
        """ handle menu selected event """
        self.config(bg=self.selected_color.get())

    def create_menu_button(self):
        """ create a menu button """
        # menu variable
        colors = ('Red', 'Green', 'Blue')

        # create the Menubutton
        menu_button = ttk.Menubutton(
            self,
            text='Select a color'
        )

        # create a new menu instance
        menu = tk.Menu(menu_button, tearoff=0)

        for color in colors:
            menu.add_radiobutton(
                label=color,
                value=color,
                variable=self.selected_color)

        # associate menu with the Menubtton
        menu_button["menu"] = menu
        menu_button.pack(expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()
