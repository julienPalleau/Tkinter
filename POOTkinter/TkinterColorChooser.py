# https://www.pythontutorial.net/tkinter/tkinter-color-chooser/
"""
Tkinter Color Chooser
Summary: in this tutorial, you'll learn how to display a color chooser dialog using the askcolor() function from the
tkinter.colorchooser module.

Introduction to the Tkinter color chooser dialog
To display a nativoe color chooser dialog, you use the tkinter.colorchooser module.

First, import the askcolor() function from the tkinter.colorchooser module:
    from tkinter.colorchooser import askcorlor

Second, call the askcolor() function to display the color chooser dialog:
    askcolor(color=None, **options)

If you select a color, the askcolor() function returns a tuple that contains tw values that represent the selected
color:
    + The first value is the RGB representation.
    + The second value is a hexadecimal representation.

For example:
    (255.99609375, 0.0, 255.99609375), '#ff00ff')

If you don't select any color form the color chooser dialog. The background of the root window will change to the
selected color.
"""
import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor


def change_color(self):
    colors = askcolor(title="Tkinter Color Chooser")
    self.configure(bg=colors[1])


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter Color Chooser')
        self.geometry("300x150")

        ttk.Button(
            self,
            text='Select a Color',
            command=lambda: change_color(self)).pack(expand=True)


if __name__ == '__main__':
    app = App()
    app.mainloop()

"""
How it works.
First, import tkinter and colochooser:
    import tkinter as tk
    from tkinter import ttk
    from tkinter.colorchooser import askcolor

Second, create the root window:
    class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter Color Chooser')
        self.geometry("300x150")
        
Third, define a function that will be executed when the 'Select a Color' Button is clicked:
    def change_color(self):
        colors = askcolor(title="Tkinter Color Chooser")
        self.configure(bg=colors[1])
        
Fourth, create a button and assign the change_color() function to its command option:
    ttk.Button(
            self,
            text='Select a Color',
            command=lambda: change_color(self)).pack(expand=True)
            
Finally, run the mainloop() method of the root window:
    if __name__ == '__main__':
        app = App()
        app.mainloop()
        
Summary
    + Use the askcolor() function form tkinter.colorchooser module to display a color chooser dialog.
    + The askcolor() function returns a tuple of the selected color or None.
"""