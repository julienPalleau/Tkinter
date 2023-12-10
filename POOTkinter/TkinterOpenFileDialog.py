# https://www.pythontutorial.net/tkinter/tkinter-open-file-dialog/
"""
Tkinter Open File Dialog
Summary: in this tutorial, you'll learn how to show an open file dialog in Tkinter applications.

Introduction to the Tkinter Open File Dialog functions
when developping a Tkinter application that deals with the file system, you need to provide a dialog that allows file
selections.

To do that, you can use the tkinter.filedialog module. The following steps show how to display an open file dialog:
First, import the tkinter.filedalog module:
    from tkinter import filedialog as fd

Second, call the fd.askopenfilename() function to show a dialog that allows a single file selection:
    filename = fd.askopenfilename()

The askopenfilename() function returns the file name that you selected.
The askopenfilename() also suspends other useful options including the initial directory displayed by the dialog or
filtering files by their extensions.
The following program displays a button:

if you click the button, i'll open a file dialog:

After you select a file, the program will show the full path of the selected file:

The program:
"""
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter Open File Dialog')
        self.resizable(False, False)
        self.geometry('300x150')

        open_button = ttk.Button(
            self,
            text='Open a File',
            command=select_file
        )

        open_button.pack(expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()

"""
Selecting multiple files
The askopenfilenames() function displays a file dialog for multiple file selections. It returns the selected file names
as a tuple. For example:
"""
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


def select_files():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open Files',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected Files',
        message=filenames
    )


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter File Dialog')
        self.resizable(False, False)
        self.geometry('300x150')

        # open button
        open_button = ttk.Button(
            self,
            text='Open Files',
            command=select_files
        )

        open_button.pack(expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()

"""
Opening files directly
After getting the selected file names, you can open them using the open() method.
To make it more convenient, the tkinter.filediag module also provides some functions that allow you to select one or 
more files and return the file objects directly.
The askopenfile() function diplays a file dialog and returns a file object of the selected file:
    f = fd.askopenfile()
And the askopenfiles() function shows a file dialog and return file object of the selected files:
    f = fd.askopenfiles()
The following program illustrates how to use the askopenfile() function:
it'll allow you to open a text file and display the file content on a Text widget:
"""
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd


def open_text_file(text):
    # file type
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    # show the open file dialog
    f = fd.askopenfile(filetypes=filetypes)
    # read the text file and show its content on the Text
    text.insert('1.0', f.readlines())


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Display a Text File')
        self.resizable(False, False)
        self.geometry("550x250")

        # Text editor
        text = tk.Text(self, height=12)
        text.grid(column=0, row=0, sticky='nsew')

        # open file button
        open_button = ttk.Button(
            self,
            text='Open a File',
            command=lambda: open_text_file(text)
        )

        open_button.grid(column=0, row=1, sticky='w', padx=10, pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()

"""
Summary
    + Use the askopenfilename() function to display an open file dialog that allows users to select one file.
    + Use the askopenfilename() function to display an open file dialog that allows users to select multiple files.
    + Use the askpenfile() or askopenfiles() function to display an open file dialog that allows users to select one
      or multiple files and receive a file or multiple file objects
"""