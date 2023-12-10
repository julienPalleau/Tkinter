# import tkinter as tk
#
# # Tkninter Hello, World!
# root = tk.Tk()
#
# # # place a label on the root root
# # message = tk.Label(root, text="Hello, World!")
# # message.pack()
#
# # keep the root displaying
# root.mainloop()

# #                   ---
# # Displaying a label
# # Now, it's time to place a component on the root. In Tkinter, components are called widgets.
# # The following adds a label widget to the root root:
# import tkinter as tk
#
# root = tk.Tk()
#
# # place a label on the root root
# message = tk.Label(root, text="Hello, World!")
# message.pack()
#
# # keep the root displaying
# root.mainloop()

# # -----------------------------------------------
# # Tkinter root
#
# import tkinter as tk
#
# root = tk.Tk()
# # To print a title in your root:
# root.title("Tkinter root Demo")
# root.geometry('600x400+50+50')
# #
# # # To get the root's title
# # title = root.title()
# # print(title)
#
# root.mainloop()

# -----------------------------------------------
# # Changing root size and location
# import tkinter as tk
#
# root = tk.Tk()
# root.title('Tkinter root Demo')
# root.geometry('600x400+50+50')  # 600x400 taille de la fenetre. A 50 du bord guauche A 50 du haut, les axes x et y ont pour origine le coin superieur gauche.
#
# root.mainloop()

# #                   ---
# # # sometimes, you may want to center the root on the screen. The following program illustrates how to do it.
# import tkinter as tk
#
# root = tk.Tk()
# root.title("Tkinter root - Center")
#
# root_width = 300
# root_height = 200
#
# # get the scree dimension
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
#
# # find the center point
# center_x = int(screen_width / 2 - root_width / 2)
# center_y = int(screen_height / 2 - root_height / 2)
#
# # set the position of the root to the center of the screen
# root.geometry(f"{root_width}x{root_height}+{center_x}+{center_y}")
#
# # to get the current gemoetry of a root, you can use the geometry()
# print(root.geometry())
# print(screen_width)
# print(screen_height)
# root.mainloop()

#                   ---
# Resizing behavior
# import tkinter as tk
#
# root = tk.Tk()
# root.title("Tkinter root Demo")
# root.geometry('600x400+50+50')
# root.resizable(False, False)
# root.resizable(True, True)
# root.minsize(300, 300)
# root.maxsize(1200, 600)
#
# root.mainloop()

# #                  ---
# # Transparency
# import tkinter as tk
#
# root = tk.Tk()
# root.title('Tkinter root Demo')
# root.geometry('600x400+50+50')
# root.resizable(False, False)
# root.attributes('-alpha', 0.5)
#
# root.mainloop()

#                   ---
# root stacking order
# The root stack order refers to the order of roots placed on the screen from bottom to top. The closer root is
# on the the top of the stack and it overlaps the one lower.
#
# To ensure that a root is always at the to of the stacking order, you can uste the -topmost attribute like this:
# import tkinter as tk
#
# root = tk.Tk()
# root.title('Tkinter root Demo')
# root.geometry('300x200+50+50')
# root.resizable(0, 0)
# root.attributes('-topmost', 1)
# root.mainloop()

# #                   ---
# Changing the default icon
# import tkinter as tk
#
# root = tk.Tk()
# root.title('Tkinter root Demo')
# root.geometry('300x200+50+50')
# root.resizable(False, False)
# root.iconbitmap('./pythontutorial.ico')
# root.mainloop()

# #                   ---
# # Ttk Widgets
# # Tkinter has two generation of widgets:
# #   + The old classic Tk widgets. Tkinter introduced them in 1991.
# #   + The newer themed ttk widgets added in 2007 with Tk 8.5. The newer Tk themed widgets replace many (but not all) classic widgets.
# #     Note that tkk stansds for Tk themed.
# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
#
# tk.Label(root, text='Classic Label').pack()
# ttk.Label(root, text='Themed Label').pack()
#
# root.mainloop()

#                   ---
# # 3 Ways to set Options for a Tk Themed Widget
# #   + At widget creation, usking keyword arguments
# #   + After widget creation, using a dictionary index.
# #   + And use the config() method with keyword attributes.
#
# # 1 - Using keyword arguments when creating the widget
# # The following illustrates how to use the keyword arguments to set the text option for a label:
# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
# ttk.Label(root, text='Hi, there').pack()
#
# root.mainloop()

# # 2 - Using a dictionary index after widget creation
# # The following program shows the same label. However, it uses a dictionary index to set the text option for the Label widget:
# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
#
# label = ttk.Label(root)
# label['text'] = 'Hi, there'
# label.pack()
# root.mainloop()

# # 3 - Using the config() method with keyword attributes
# # The following program illustrates how to use the config() method to set the text option for the label:
# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
#
# label = ttk.Label(root)
# label.config(text='Hi, there')
# label.pack()
# root.mainloop()

# # -----------------------------------------------
# # Tkinter StringVar
# # Tkinter StringVar example
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinter StrinVar')
        self.geometry("300x80")

        self.name_var = tk.StringVar()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.create_widgets()

    def create_widgets(self):
        padding = {'padx': 5, 'pady': 5}
        # label
        ttk.Label(self, text='Name:').grid(column=0, row=0, **padding)

        # Entry
        name_entry = ttk.Entry(self, textvariable=self.name_var)
        name_entry.grid(column=1, row=0, **padding)
        name_entry.focus()

        # Button
        submit_button = ttk.Button(self, text='Submit', command=self.submit)
        submit_button.grid(column=2, row=0, **padding)

        # Output label
        self.output_label = ttk.Label(self)
        self.output_label.grid(column=0, row=1, columnspan=3, **padding)

    def submit(self):
        self.output_label.config(text=self.name_var.get())


if __name__ == "__main__":
    app = App()
    app.mainloop()


#                   ---
# Tkinter StringVar - Tracing text changes example

    contents = StringVar() # setup the wrapper
    myentry = Entry(master, textvariable = contents)
    myentry.pack()
    display.set("Default")
    mylabel.text = contents.get()

import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    ERROR = 'Error.TLabel'
    SUCCESS = 'Success.TLabel'

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
        self.style.configure('Success.TLable', foreground='green')

        self.create_widgets()


    def create_widgets(self):
        """ create a widget
        """

        padding = {'padx': 5, 'pady': 5, 'sticky': tk.W}
        # message
        self.message_label = ttk.Label(self)
        self.message_label.grid(column=0, row=0, columnspan=3, **padding)

        # password
        ttk.Label(self, text='New Password:').grid(column=0, row=1, **padding)

        password_entry = ttk.Entry(
            self, textvariable=self.password_var, show='*')
        password_entry.grid(column=1, row=1, **padding)
        password_entry.focus()

        # confirm password
        ttk.Label(self, text='Confirm Password').grid(column=0, row=2, **padding)

        confirm_password = ttk.Entry(
            self, textvariable=self.confirm_password_var, show='*')
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
        """ Validate the password
        """
        password = self.password_var.get()
        confirm_password = self.confirm_password_var.get()

        if confirm_password == password:
            self.set_message(
                "Success: The new password looks good!", self.SUCCESS)
            return

        if password.startswith(confirm_password):
            self.set_message('Warning: Keep entering the password')

        self.set_message("Error: Passwords don't match!", self.SUCCESS)


if __name__ == "__main__":
    app = App()
    app.mainloop()

# # -----------------------------------------------
# # Tkinter Command Binding

# # Introduction to Tkinter command binding
# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
#
#
# def select(option):
#     print(option)
#
#
# ttk.Button(root, text='Rock', command=lambda: select('Rock')).pack()
# ttk.Button(root, text='Paper', command=lambda: select('Paper')).pack()
# ttk.Button(root, text='Scissors', command=lambda: select('Scissors')).pack()
#
# root.mainloop()

# # -----------------------------------------------
# # Tkinter event Binding

# # Tkinter event binding examples

# import tkinter as tk
# from tkinter import ttk
#
#
# def return_pressed(event):
#     print('Return key pressed.')
#
#
# def log(event):
#     print(event)
#
#
# root = tk.Tk()
#
# btn = ttk.Button(root, text='Save')
# btn.bind('<Return>', return_pressed)
# btn.bind('<Return>', log, add='+')
#
# btn.focus()
# btn.pack(expand=True)
#
# root.mainloop()

# # -----------------------------------------------
# # Tkinter Label

# # Introduction to Tkinter Label widget

# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Label Widget Demo')
#
# # show the label here
#
# root.mainloop()

# #                   ---
# # Displaying a regular label
# import tkinter as tk
# from tkinter.ttk import Label
#
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Label Widget Demo')
#
# # Show a Label
# label = Label(root, text='This is a label')
# label.pack(ipadx=10, ipady=10)
#
# root.mainloop()

# #                   ---
# # Setting a specific font for the Label
# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Label Widget Demo')
#
# # Label with a specific font
# label = ttk.Label(
#     root,
#     text='A Label with the Helvetica font',
#     font=('Helvetica', 14))
#
# label.pack(ipadx=10, ipady=10)
#
# root.mainloop()

#                   ---
# # Displaying an image
# import tkinter as tk
# from tkinter import ttk
#
# #  create the root root
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Label Widget Image')
#
# # display an image label
# photo = tk.PhotoImage(file='./assets/python.png')
# image_label = ttk.Label(
#     root,
#     image=photo,
#     padding=5,
# )
# image_label.pack()
#
# root.mainloop()

# #                   ---
# # Display both text and image on a label:
# import tkinter as tk
# from tkinter import ttk
#
# #  create the root root
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Label Widget Image')
#
# # display an image label
# photo = tk.PhotoImage(file='./assets/python.png')
# image_label = ttk.Label(
#     root,
#     image=photo,
#     padding=5,
#     text='Python',
#     compound='top'  # display the image above the text
# )
# image_label.pack()
#
# root.mainloop()

# # -----------------------------------------------
# # Tkinter Button
# # Tkinter button example
#
# import tkinter as tk
# from tkinter import ttk
#
# # root root
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Button Demo')
#
# # exit button
# exit_button = ttk.Button(
#     root,
#     text='Exit',
#     command=lambda: root.quit()
# )
#
# exit_button.pack(
#     ipadx=5,
#     ipady=5,
#     expand=True
# )
#
# root.mainloop()

#                   ---
# Tkinter image button example
# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo
#
#
# # root root
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Image Button Demo')
#
#
# # download button
# def download_clicked():
#     showinfo(
#         title='Information',
#         message='Download button clicked!'
#     )
#
#
# download_icon = tk.PhotoImage(file='./assets/download.png')
# download_button = ttk.Button(
#     root,
#     image=download_icon,
#     command=download_clicked
# )
#
# download_button.pack(
#     ipadx=5,
#     ipady=5,
#     expand=True
# )
#
#
# root.mainloop()

# # -----------------------------------------------
# # Displaying an image button
#
# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo
#
#
# # root root
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Image Button Demo')
#
#
# # download button handler
# def download_clicked():
#     showinfo(
#         title='Information',
#         message='Download button clicked!'
#     )
#
#
# download_icon = tk.PhotoImage(file='./assets/download.png')
#
# download_button = ttk.Button(
#     root,
#     image=download_icon,
#     text='Download',
#     compound=tk.LEFT,
#     command=download_clicked
# )
#
# download_button.pack(
#     ipadx=5,
#     ipady=5,
#     expand=True
# )
#
#
# root.mainloop()
#
# # -----------------------------------------------
# # Tkinter Entry
# # Showing a Tkinter password entry
#
# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo
#
# # root root
# root = tk.Tk()
# root.geometry("300x150")
# root.resizable(False, False)
# root.title('Sign In')
#
# # store email address and password
# email = tk.StringVar()
# password = tk.StringVar()
#
#
# def login_clicked():
#     """ callback when the login button clicked
#     """
#     msg = f'You entered email: {email.get()} and password: {password.get()}'
#     showinfo(
#         title='Information',
#         message=msg
#     )
#
#
# # Sign in frame
# signin = ttk.Frame(root)
# signin.pack(padx=10, pady=10, fill='x', expand=True)
#
# # email
# email_label = ttk.Label(signin, text="Email Address:")
# email_label.pack(fill='x', expand=True)
#
# email_entry = ttk.Entry(signin, textvariable=email)
# email_entry.pack(fill='x', expand=True)
# email_entry.focus()
#
# # password
# password_label = ttk.Label(signin, text="Password:")
# password_label.pack(fill='x', expand=True)
#
# password_entry = ttk.Entry(signin, textvariable=password, show="*")
# password_entry.pack(fill='x', expand=True)
#
# # login button
# login_button = ttk.Button(signin, text="Login", command=login_clicked)
# login_button.pack(fill='x', expand=True, pady=10)
#
# root.mainloop()

# # -----------------------------------------------
# # Tkinter Pack
# # Tkinter pack geometry manager example
#
# import tkinter as tk
#
# root = tk.Tk()
# root.title('Pack Demo')
# root.geometry("300x200")
#
# # box1
# box1 = tk.Label(
#     root,
#     text="Box 1",
#     bg="green",
#     fg="white"
# )
#
# box1.pack(
#     ipadx=10,
#     ipady=10
# )
#
# # box2
# box2 = tk.Label(
#     root,
#     text="Box 2",
#     bg="red",
#     fg="white"
# )
#
# box2.pack(
#     ipadx=10,
#     ipady=10
# )
# root.mainloop()

# #                   ---
# # Using the fill option
# import tkinter as tk
#
# root = tk.Tk()
# root.title('Pack Demo')
# root.geometry("300x200")
#
# # box1
# box1 = tk.Label(
#     root,
#     text="Box 1",
#     bg="green",
#     fg="white"
# )
#
# box1.pack(
#     ipadx=10,
#     ipady=10,
#     fill='y'
# )
#
# # box2
# box2 = tk.Label(
#     root,
#     text="Box 2",
#     bg="red",
#     fg="white"
# )
#
# box2.pack(
#     ipadx=10,
#     ipady=10
# )
#
# root.mainloop()

# #                   ---
# # Using the expand option
#
# import tkinter as tk
#
# root = tk.Tk()
# root.title('Pack Demo')
# root.geometry("300x200")
#
# # box1
# box1 = tk.Label(
#     root,
#     text="Box 1",
#     bg="green",
#     fg="white"
# )
#
# box1.pack(
#     ipadx=10,
#     ipady=10,
#     expand=True,
#     fill='both'
# )
#
# # box2
# box2 = tk.Label(
#     root,
#     text="Box 2",
#     bg="red",
#     fg="white"
# )
#
# box2.pack(
#     ipadx=10,
#     ipady=10,
#     expand=True
# )
#
# root.mainloop()

# #                   ---
# # Using the side option
# import tkinter as tk
# root = tk.Tk()
# root.title('Pack Demo')
# root.geometry("300x200")
#
# # box 1
# box1 = tk.Label(
#     root,
#     text="Box 1",
#     bg="green",
#     fg="white"
# )
#
# box1.pack(
#     ipadx=10,
#     ipady=10,
#     expand=True,
#     fill='both',
#     side='left'
# )
#
# box2 = tk.Label(
#     root,
#     text="Box 2",
#     bg="red",
#     fg="white"
# )
#
# box2.pack(
#     ipadx=10,
#     ipady=10,
#     expand=True,
#     fill='both'
# )
#
# root.mainloop()

#                   ---
# to make their space even again
# import tkinter as tk
# root = tk.Tk()
# root.title('Pack Demo')
# root.geometry("300x200")
#
# # box 1
# box1 = tk.Label(
#     root,
#     text="Box 1",
#     bg="green",
#     fg="white"
# )
#
# box1.pack(
#     ipadx=10,
#     ipady=10,
#     expand=True,
#     fill='both',
#     side='left'
# )
#
# box2 = tk.Label(
#     root,
#     text="Box 2",
#     bg="red",
#     fg="white"
# )
#
# box2.pack(
#     ipadx=10,
#     ipady=10,
#     expand=True,
#     fill='both',
#     side='left'
# )
#
# root.mainloop()

# #                   ---
# # When to use the pack geometry manager
# import tkinter as tk
# from tkinter import ttk
#
# root=tk.Tk()
# root.title('Pack Demo')
# root.geometry("300x200")
#
# # place widget top down
# label1 = tk.Label(
#     root,
#     text='Box 1',
#     bg="red",
#     fg="white",
# )
#
# label1.pack(
#     ipadx=10,
#     ipady=10,
#     fill='x'
# )
#
# label2 = tk.Label(
#     root,
#     text='Box 2',
#     bg="green",
#     fg="white",
# )
# label2.pack(
#     ipadx=10,
#     ipady=10,
#     fill='x'
# )
#
# label3 = tk.Label(
#     root,
#     text='Box 3',
#     bg="blue",
#     fg="white"
# )
#
# label3.pack(
#     ipadx=10,
#     ipady=10,
#     fill='x'
# )
#
# # place widgets side by side
#
# label4 = tk.Label(
#     root,
#     text='Left',
#     bg="cyan",
#     fg="black"
# )
#
# label4.pack(
#     ipadx=10,
#     ipady=10,
#     expand=True,
#     fill='both',
#     side='left'
# )
#
# label5 = tk.Label(
#     root,
#     text='Center',
#     bg="magenta",
#     fg="black"
# )
#
# label5.pack(
#     ipadx=10,
#     ipady=10,
#     expand=True,
#     fill='both',
#     side='left'
# )
#
# label6 = tk.Label(
#     root,
#     text='Right',
#     bg="yellow",
#     fg="black"
# )
#
# label6.pack(
#     ipadx=10,
#     ipady=10,
#     expand=True,
#     fill='both',
#     side='left'
# )
# root.mainloop()

# # -----------------------------------------------
# # Tkinter Grid
# # Tkinter grid geometry manager example
#
# import tkinter as tk
# from tkinter import ttk
#
# # root root
# root = tk.Tk()
# root.geometry("240x100")
# root.title('Login')
# root.resizable(0, 0)
#
# # Configure the grid
# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=3)
#
# # username
# username_label = ttk.Label(root, text="Username :")
# username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
#
# username_entry = ttk.Entry(root)
# username_entry.grid(column=1, row=0, sticky=tk.E, padx =5, pady=5)
#
# # password
# password_label = ttk.Label(root, text="Password :")
# password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
#
# password_entry = ttk.Entry(root, show="*")
# password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
#
# # login button
# login_button = ttk.Button(root, text="Login")
# login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
#
# root.mainloop()


# #                   ---
# # The following shows the same program as above. However, it uses object-oriented programming instead:
#
# import tkinter as tk
# from tkinter import ttk
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#
#         self.geometry("240x100")
#         self.title('Login')
#         self.resizable(0, 0)
#
#         # configure the grid
#         self.columnconfigure(0, weight=1)
#         self.columnconfigure(1, weight=3)
#
#         self.create_widgets()
#
#     def create_widgets(self):
#         # username
#         username_label = ttk.Label(self, text="Username:")
#         username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
#
#         username_entry = ttk.Entry(self, text="Username")
#         username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
#
#         # password
#         password_label = ttk.Label(self, text="Password:")
#         password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
#
#         password_entry = ttk.Entry(self, show="*")
#         password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
#
#         # Login button
#         login_button = ttk.Button(self, text="Login")
#         login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

# # -----------------------------------------------
# # Tkinter Place
# # Tkinter place geometry manager example
#
# import tkinter as tk
#
# root = tk.Tk()
# root.title('Tkinter place Geometry Manager')
#
# # label 1
# label1 = tk.Label(
#     root,
#     text="Absolute placement",
#     bg='red',
#     fg='white'
# )
#
# label1.place(x=20, y=10)
#
# # label 2
# label2 = tk.Label(
#     root,
#     text="Relative placement",
#     bg="blue",
#     fg="white"
# )
#
# label2.place(relx=0.8, rely=0.2, relwidth=0.5, anchor='ne')
#
# root.mainloop()

# # -----------------------------------------------
# # Tkinter Frame
# # Tkinter Frame example
# import tkinter as tk
# from tkinter import ttk
#
#
# def create_input_frame(container):
#     frame = ttk.Frame(container)
#
#     # grid layout for the input frame
#     frame.columnconfigure(0, weight=1)
#     frame.columnconfigure(0, weight=3)
#
#     # Find what
#     ttk.Label(frame, text='Find what:').grid(column=0, row=0, sticky=tk.W)
#     keyword = ttk.Entry(frame, width=30)
#     keyword.focus()
#     keyword.grid(column=1, row=0, sticky=tk.W)
#
#     # Replace with:
#     ttk.Label(frame, text='Replace with:').grid(column=0, row=1, sticky=tk.W)
#     replacement = ttk.Entry(frame, width=30)
#     replacement.grid(column=1, row=1, sticky=tk.W)
#
#     # Match Case checkbox
#     match_case = tk.StringVar()
#     match_case_check = ttk.Checkbutton(
#         frame,
#         text='Match case',
#         variable=match_case,
#         command=lambda: print(match_case.get()))
#     match_case_check.grid(column=0, row=2, sticky=tk.W)
#
#     # Wrap Around checkbox
#     wrap_around = tk.StringVar()
#     wrap_around_check = ttk.Checkbutton(
#         frame,
#         variable=wrap_around,
#         text='Wrap around',
#         command=lambda: print(wrap_around.get()))
#     wrap_around_check.grid(column=0, row=3, sticky=tk.W)
#
#     for widget in frame.winfo_children():
#         widget.grid(padx=0, pady=5)
#
#     return frame
#
#
# def create_button_frame(container):
#     frame = ttk.Frame(container)
#
#     frame.columnconfigure(0, weight=1)
#
#     ttk.Button(frame, text='Find Next').grid(column=0, row=0)
#     ttk.Button(frame, text='Replace').grid(column=0, row=1)
#     ttk.Button(frame, text='Replace All').grid(column=0, row=2)
#     ttk.Button(frame, text='Cancel').grid(column=0, row=3)
#
#     for widget in frame.winfo_children():
#         widget.grid(padx=0, pady=3)
#
#     return frame
#
#
# def create_main_root():
#
#     # root root
#     root = tk.Tk()
#     root.title('Replace')
#     root.geometry('400x150')
#     root.resizable(0, 0)
#     # roots only (remove the minimize/maximise button)
#     root.attributes('-toolroot', True)
#
#     # layout on the root root
#     root.columnconfigure(0, weight=4)
#     root.rowconfigure(1, weight=1)
#
#     input_frame = create_input_frame(root)
#     input_frame.grid(column=0, row=0)
#
#     button_frame = create_button_frame(root)
#     button_frame.grid(column=1, row=0)
#
#     root.mainloop()
#
#
# if __name__ == "__main__":
#     create_main_root()

# # -----------------------------------------------
# # Tkinter Text
# # Introduction to Tkinter Text widget
# from tkinter import Tk, Text
#
# root = Tk()
# root.resizable(False, False)
# root.title("Text Widget Example")
#
# text = Text(root, height=8)
# text.pack()
# root.mainloop()

# #                   ---
# # The following shows the same program as above. However, it uses object-oriented programming instead:
# from tkinter import Tk, Text
#
# root = Tk()
# root.resizable(False, False)
# root.title("Text Widget Example")
#
# text = Text(root, height=8)
# text.pack()
#
# text.insert('1.0', 'This is a Text widget demo')
#
# root.mainloop()
#
# # -----------------------------------------------
# # Tkinter Scrollbar
# # Tkinter scrollbar widget example
# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
# root.resizable(False, False)
# root.title("Scrollbar Widget Example")
#
# # apply the grid layout
# root.grid_columnconfigure(0, weight=1)
# root.grid_rowconfigure(0, weight=1)
#
# # create the text widget
# text = tk.Text(root, height=10)
# text.grid(row=0, column=0, sticky='ew')
#
# # create a scrollbar widget ans set its command to the text widget
# scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
# scrollbar.grid(row=0, column=1, sticky='ns')
#
# # communicate back to the scrollbar
# text['yscrollcommand'] = scrollbar.set
#
# root.mainloop()

# # -----------------------------------------------
# # Tkinter ScrollText
# # Tkinter scrollText widget example
#
# import tkinter as tk
# from tkinter.scrolledtext import ScrolledText
#
# root = tk.Tk()
# root.title("ScrolledText Widget")
#
# st = ScrolledText(root, width=50, height=10)
# st.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#
# root.mainloop()

# #                   ---
# # The sane program as above but written using the object-oriented programming approach:
# import tkinter as tk
# from tkinter.scrolledtext import ScrolledText
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("ScrolledText Widget")
#         st = ScrolledText(self, width=50, height=10)
#         st.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

# # -----------------------------------------------
# # Tkinter Separator
# # Introduction to the Tkinter Separator widget
# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Separator Widget Demo')
#
# ttk.Label(root, text="First Label").pack()
#
# separator = ttk.Separator(root, orient='horizontal')
# separator.pack(fill='x')
# ttk.Label(root, text='Second Label').pack()
#
# root.mainloop()

# #                   ---
# # Tkinter checkbox example
# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo
#
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Checkbox Demo')
#
# agreement = tk.StringVar()
#
#
# def agreement_changed():
#     tk.messagebox.showinfo(title='Result', message=agreement.get())
#
#
# ttk.Checkbutton(root,
#                 text='I agree',
#                 command=agreement_changed,
#                 variable=agreement,
#                 onvalue='agree',
#                 offvalue='disagree').pack()
#
# root.mainloop()

# # -----------------------------------------------
# # Tkinter radio button
# # Tkinter radio button example
# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo
#
# # root widget
# root = tk.Tk()
# root.geometry('300x220')
# root.resizable(False, False)
# root.title('Radio Button Demo')
#
#
# def show_selected_size():
#     showinfo(
#         title='Result',
#         message=selected_size.get()
#     )
#
#
# selected_size = tk.StringVar()
# sizes = (('Small', 'S'),
#          ('Medium', 'M'),
#          ('Large', 'L'),
#          ('Extra Large', 'XL'),
#          ('Extra Extra Large', 'XXL'))
#
# # Label
# label = ttk.Label(text="What's your t-shirt size?")
# label.pack(fill='x', padx=5, pady=5)
#
# # Radio buttons
# for size in sizes:
#     r = ttk.Radiobutton(
#         root,
#         text=size[0],
#         value=size[1],
#         variable=selected_size
#     )
#     r.pack(fill='x', padx=5, pady=5)
#
# # buttons
# button = ttk.Button(
#     root,
#     text="Get Selected Size",
#     command=show_selected_size)
#
# button.pack(fill='x', padx=5, pady=5)
#
# root.mainloop()

# -----------------------------------------------
# Tkinter Combobox
# Tkinter combobox example

# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo
#
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Combobox Widget')
#
#
# def month_changed(event):
#     msg = f'You selected {month_cb.get()}!'
#     showinfo(title='Result', message=msg)
#
#
# # month of year
# months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
#
# label = ttk.Label(text="Please select a month:")
# label.pack(fill='x', padx=5, pady=5)
#
# # create a combobox
# selected_month = tk.StringVar()
#
# month_cb = ttk.Combobox(root, textvariable=selected_month)
# month_cb['values'] = months
# month_cb['state'] = 'readonly'  # normal
# month_cb.pack(fill='x', padx=5, pady=5)
#
# month_cb.bind('<<ComboboxSelected>>', month_changed)
#
# root.mainloop()

# # -----------------------------------------------
# # Tkinter Listbox
# # Tkinter Listbox widget example
#
# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo
#
# # create the root root
#
# root = tk.Tk()
# root.geometry('200x100')
# root.resizable(False, False)
# root.title('Listbox')
#
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
#
# # create a list box
# langs = ('Java', 'C#', 'C', 'C++', 'Python', 'Go', 'JavaScript', 'PHP', 'Swift')
#
# langs_var = tk.StringVar(value=langs)
#
# listbox = tk.Listbox(
#     root,
#     listvariable=langs_var,
#     height=6,
#     selectmode='extended'
# )
#
# listbox.grid(
#     column=0,
#     row=0,
#     sticky='nwes'
# )
#
#
# # handle event
# def items_selected(event):
#     """ handle item selected event
#     """
#
#     # get selected incices
#     selected_indices = listbox.curselection()
#     # get selected items
#     selected_langs = ",".join([listbox.get(i) for i in selected_indices])
#     msg = f'You selected: {selected_langs}'
#
#     showinfo(
#         title='Information',
#         message=msg
#     )
#
#
# listbox.bind('<<ListboxSelect>>', items_selected)
#
# root.mainloop()

# #                   ---
# # Adding a scrollbar to the listbox
#
# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo
#
# # create the root root
# root = tk.Tk()
# root.geometry('200x100')
# root.resizable(False, False)
# root.title('Listbox')
#
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
#
# # create a list box
# langs = ('Java', 'C#', 'C', 'C++', 'Python', 'Go', 'JavaScript', 'PHP', 'Swift')
#
# langs_var = tk.StringVar(value=langs)
#
# listbox = tk.Listbox(
#     root,
#     listvariable=langs_var,
#     height=6,
#     selectmode='extended'
# )
#
# listbox.grid(
#     column=0,
#     row=0,
#     sticky='nwes'
# )
#
# # link a scrollbar to a list
# scrollbar = ttk.Scrollbar(
#     root,
#     orient='vertical',
#     command=listbox.yview
# )
#
# listbox['yscrollcommand'] = scrollbar.set
#
# scrollbar.grid(
#     column=1,
#     row=0,
#     sticky='ns'
# )
#
#
# # handle event
# def items_selected(event):
#     """ handle item selected event
#     """
#     # get selected indices
#     selected_indices = listbox.curselection()
#     # get selected items
#     selected_langs = ",".join([listbox.get(i) for i in selected_indices])
#     msg = f"You selected: {selected_langs}"
#
#     showinfo(
#         title='Information',
#         message=msg
#     )
#
#
# listbox.bind('<<ListboxSelect>>', items_selected)
#
# root.mainloop()

# # -----------------------------------------------
# # Tkinter Panedroot
# # Tkinter Panedroot widget example
# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
# root.title=('Pannedroot Demo')
# root.geometry('300x200')
#
# # Change style to classic (root only)
# # to show the sash and handle
# style = ttk.Style()
# style.theme_use('classic')
#
# # paned root
# pw = ttk.Panedroot(orient=tk.HORIZONTAL)
#
# # Left listbox
# left_list = tk.Listbox(root)
# left_list.pack(side=tk.LEFT)
# pw.add(left_list)
#
# # Rignt listbox
# right_list = tk.Listbox(root)
# right_list.pack(side=tk.LEFT)
# pw.add(right_list)
#
# # place the panedroot on the root root
# pw.pack(fill=tk.BOTH, expand=True)
#
# root.mainloop()

# # -----------------------------------------------
# # Tkinter Slider
# # Tkinter slidr example
#
# import tkinter as tk
# from tkinter import ttk
#
# # root root
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Slider Demo')
#
# root.columnconfigure(0, weight=1)
# root.rowconfigure(1, weight=3)
#
# # slider current value
# current_value = tk.DoubleVar()
#
#
# def get_current_value():
#     return '{: .2f}'.format(current_value.get())
#
#
# def slider_changed(event):
#     value_label.configure(text=get_current_value())
#
#
# # label for the slider
# slider_label = ttk.Label(
#     root,
#     text='Slider:'
# )
#
# slider_label.grid(
#     column=0,
#     row=0,
#     sticky='w'
# )
#
#
# # slider
# slider = ttk.Scale(
#     root,
#     from_=0,
#     to=100,
#     orient='horizontal',
#     command=slider_changed,
#     variable=current_value
# )
#
# slider.grid(
#     column=1,
#     row=0,
#     sticky='we'
# )
#
# # current value label
# current_value_label = ttk.Label(
#     root,
#     text='Current Value:'
# )
#
# current_value_label.grid(
#     row=1,
#     columnspan=2,
#     sticky='n',
#     ipadx=10,
#     ipady=10
# )
#
# # value label
# value_label = ttk.Label(
#     root,
#     text=get_current_value()
# )
#
# value_label.grid(
#     row=2,
#     columnspan=2,
#     sticky='n'
# )
#
# root.mainloop()

# # -----------------------------------------------
# # Tkinter spinbox
# # A simple Tkinter Spinbox widget example
# import tkinter as tk
# from tkinter import ttk
#
# # root root
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Spinbox Demo')
#
# # Spinbox
# current_value = tk.StringVar(value=0)
# spin_box = ttk.Spinbox(
#     root,
#     from_=0,
#     to=30,
#     textvariable=current_value,
#     wrap=True
# )
#
# spin_box.pack()
#
# root.mainloop()

# #                   ---
#
# import tkinter as tk
# from tkinter import ttk
#
# # root root
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Spinbox Demo')
#
# # spinbox
# current_value = tk.StringVar()
# spin_box = ttk.Spinbox(
#     root,
#     from_=0,
#     to=50,
#     values=(0, 10, 20, 30, 40, 50),
#     textvariable=current_value,
#     wrap=True
# )
#
# spin_box.pack()
#
# root.mainloop()

# # -----------------------------------------------
# # Tkinter Sizegrip
# # Tkinter Sizegrip widget example
#
# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(True, True) # remind that you need to have a resizable root to use Sizegrip!
# root.title('Sizegrep Demo')
#
# # grid layout
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
#
# # Create the sizegrip
# sg = ttk.Sizegrip(root)
# sg.grid(row=1, sticky=tk.SE)
#
# root.mainloop()

# # -----------------------------------------------
# # Tkinter LabelFrame
# # Tkinter LabelFrame widget example
# import tkinter as tk
# from tkinter import ttk
#
# # root root
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('LabelFrame Demo')
#
# # label frame
# lf = ttk.LabelFrame(
#     root,
#     text='Alignment'
# )
#
# lf.grid(column=0, row=0, padx=20, pady=20)
#
# alignment = tk.StringVar()
#
# # left radio button
# left_radio = ttk.Radiobutton(
#     lf,
#     text='Left',
#     value='left',
#     variable=alignment
# )
# left_radio.grid(column=0, row=0, ipadx=10, ipady=10)
#
# # center radio button
# center_radio = ttk.Radiobutton(
#     lf,
#     text='Center',
#     value='center',
#     variable=alignment
# )
# center_radio.grid(column=1, row=0, ipadx=10, ipady=10)
#
# # right alignment radiobutton
# right_radio = ttk.Radiobutton(
#     lf,
#     text='Right',
#     value='right',
#     variable=alignment
# )
# right_radio.grid(column=2, row=0, ipadx=10, ipady=10)
#
# root.mainloop()

# # -----------------------------------------------
# # Tkinter Progressbar
# # Tkinter Progressbar example
# # 1 - Tkinter Progressbar in the indeterminate mode example
# import tkinter as tk
# from tkinter import ttk
#
# # root root
# root = tk.Tk()
# root.geometry('300x120')
# root.title('Progressbar Demo')
#
# root.grid()
#
# # progressbar
# pb = ttk.Progressbar(
#     root,
#     orient='horizontal',
#     mode='indeterminate',
#     length=280
# )
#
# # place the progressbar
# pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
#
# # start button
# start_button = ttk.Button(
#     root,
#     text='Start',
#     command=pb.start
# )
# start_button.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)
#
# # stop button
# stop_button = ttk.Button(
#     root,
#     text='Stop',
#     command=pb.stop
# )
# stop_button.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)
#
# root.mainloop()

# #                   ---
# # 1 - Tkinter Progressbar in the determinate mode example
# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo
#
# # root root
# root = tk.Tk()
# root.geometry('300x120')
# root.title('Progressbar Demo')
#
#
# def update_progress_label():
#     return f"Current Progress: {pb['value']}%"
#
#
# def progress():
#     if pb['value'] < 100:
#         pb['value'] += 20
#         value_label['text'] = update_progress_label()
#     else:
#         showinfo(message='The progress completed!')
#
#
# def stop():
#     pb.stop
#     value_label['text'] = update_progress_label()
#
#
# # prgressbar
# pb = ttk.Progressbar(
#     root,
#     orient='horizontal',
#     mode='determinate',
#     length=280
# )
#
# # place the progressbar
# pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
#
# # label
# value_label = ttk.Label(root, text=update_progress_label())
# value_label.grid(column=0, row=1, columnspan=2)
#
# # start/stop button
# start_button = ttk.Button(
#     root,
#     text='Progress',
#     command=progress
# )
# start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)
#
# stop_button = ttk.Button(
#     root,
#     text='Stop',
#     command=stop
# )
# stop_button.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)
#
# root.mainloop()

# # -----------------------------------------------
# # Tkinter Notebook
# # Tkinter Notebook widget example
# import tkinter as tk
# from tkinter import ttk
#
# # root root
# root = tk.Tk()
# root.geometry('400x300')
# root.title('Notebook Demo')
#
# # create a notebook
# notebook = ttk.Notebook(root)
# notebook.pack(pady=10, expand=True)
#
# # create frames
# frame1 = ttk.Frame(notebook, width=400, height=280)
# frame2 = ttk.Frame(notebook, width=400, height=280)
#
# frame1.pack(fill='both', expand=True)
# frame2.pack(fill='both', expand=True)
#
# # add frames to notebook
# notebook.add(frame1, text='General Information')
# notebook.add(frame2, text='Profile')
#
# root.mainloop()

# -----------------------------------------------
# Tkinter Treeview
# Using Tkinter Treeview to display tabular data
# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo
#
# root = tk.Tk()
# root.title('Treeview demo')
# root.geometry('620x200')
#
# # Columns
# columns = ('#1', '#2', '#3')
# tree = ttk.Treeview(root, columns=columns, show='headings')
#
# # define headings
# tree.heading('#1', text='First Name')
# tree.heading('#2', text='Last Name')
# tree.heading('#3', text='Email')
#
# # generate sample data
# contacts = []
# for n in range(1, 100):
#     contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))
#
# # adding data to the treeview
# for contact in contacts:
#     tree.insert('', tk.END, values=contact)
#
#
# # bind the select event
# def item_selected(event):
#     for selected_item in tree.selection():
#         # dictionary
#         item = tree.item(selected_item)
#         # list
#         record = item['values']
#         showinfo(title='Information', message=','.join(record))
#
#
# tree.bind('<<TreeviewSelect>>', item_selected)
#
# tree.grid(row=0, column=0, sticky='nsew')
#
# # add a scrollbar
# scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
# tree.configure(yscroll=scrollbar.set)
# scrollbar.grid(row=0, column=1, sticky='ns')
#
# # run the app
# root.mainloop()

# #                   ---
# # Using Tkinter Treeview to display hierarchical data
#
# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import  showinfo
#
# # create root root
# root = tk.Tk()
# root.geometry('400x200')
# root.title('Treeview Demo - Hierachical Data')
#
# # configure the grid layout
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
#
# # create a treeview
# tree = ttk.Treeview(root)
# tree.heading('#0', text='Departments', anchor='w')
#
# # adding data
# tree.insert('', tk.END, text='Administration', iid=0, open=False)
# tree.insert('', tk.END, text='Logistics', iid=1, open=False)
# tree.insert('', tk.END, text='Sales', iid=2, open=False)
# tree.insert('', tk.END, text='Finance', iid=3, open=False)
# tree.insert('', tk.END, text='IT', iid=4, open=False)
#
# # adding children of first node
# tree.insert('', tk.END, text='John Doe', iid=5, open=False)
# tree.insert('', tk.END, text='Jane Doe', iid=6, open=False)
# tree.move(5, 0, 0)
# tree.move(6, 0, 1)
#
# # place the Treeview widget ont the root root
# tree.grid(row=0, column=0, sticky='nsew')
#
# # run the app
# root.mainloop()

# -----------------------------------------------
# Tkinter OOP
# Another example of an object-oriented root in Tkinter
# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#
#         # configure the root root
#         self.title('My Awesome App')
#         self.geometry('300x50')
#
#         # label
#         self.label = ttk.Label(self, text='Hello, Tkinter!')
#         self.label.pack()
#
#         # button
#         self.button = ttk.Button(self, text='Click Me')
#         self.button['command'] = self.button_clicked
#         self.button.pack()
#
#     def button_clicked(self):
#         showinfo(title='Information',
#                  message='Hello, Tkinter!')
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

# # -----------------------------------------------
# # Tkinter OOP
# # Another example of an object-oriented Frames
# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo
#
#
# class MainFrame(ttk.Frame):
#     def __init__(self, container):
#         super().__init__(container)
#
#         options = {'padx': 5, 'pady': 5}
#
#         # Label
#         self.label = ttk.Label(self, text='Hello, Tkinter!')
#         self.label.pack(**options)
#
#         # button
#         self.button = ttk.Button(self, text='Click Me')
#         self.button['command'] = self.button_clicked
#         self.button.pack(**options)
#
#         # Show the frame on the container
#         self.pack(**options)
#
#     def button_clicked(self):
#         showinfo(title='Information',
#                  message='Hello, Tkinter!')
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         # configure the root root
#         self.title('My Awesome App')
#         self.geometry('300x100')
#
#
# if __name__ == "__main__":
#     app = App()
#     frame = MainFrame(app)
#     app.mainloop()

# # -----------------------------------------------
# # Tkinter OOP
# # More Object-oriented Frame example
# import tkinter as tk
# from tkinter import ttk
#
#
# class InputFrame(ttk.Frame):
#     def __init__(self, container):
#         super().__init__(container)
#         # setup the grid layout manager
#         self.rowconfigure(0, weight=1)
#         self.columnconfigure(0, weight=3)
#
#         self.__create_widgets()
#
#     def __create_widgets(self):
#         # Find what
#         ttk.Label(self, text='Find what:').grid(column=0, row=0, sticky=tk.W)
#         keyword = ttk.Entry(self, width=30)
#         keyword.focus()
#         keyword.grid(column=1, row=0, sticky=tk.W)
#
#         # Replace with:
#         ttk.Label(self, text='Replace with:').grid(
#             column=0, row=1, sticky=tk.W)
#         replacement = ttk.Entry(self, width=30)
#         replacement.grid(column=1, row=1, sticky=tk.W)
#
#         # Match Case checkbox
#         match_case = tk.StringVar()
#         match_case_check = ttk.Checkbutton(
#             self,
#             text='Match case',
#             variable=match_case,
#             command=lambda: print(match_case.get()))
#         match_case_check.grid(column=0, row=2, sticky=tk.W)
#
#         # Wrap Around checkbox
#         wrap_around = tk.StringVar()
#         wrap_around_check = ttk.Checkbutton(
#             self,
#             text="Wrap around",
#             variable=wrap_around,
#             command=lambda: print(wrap_around.get()))
#         wrap_around_check.grid(column=0, row=3, sticky=tk.W)
#
#         for widget in self.winfo_children():
#             widget.grid(padx=0, pady=5)
#
#
# class ButtonFrame(ttk.Frame):
#     def __init__(self, container):
#         super().__init__(container)
#         # setup the grid layout manager
#         self.columnconfigure(0, weight=1)
#
#         self.__create_widgets()
#
#     def __create_widgets(self):
#         ttk.Button(self, text='Find Next').grid(column=0, row=0)
#         ttk.Button(self, text='Replace').grid(column=0, row=1)
#         ttk.Button(self, text='Replace All').grid(column=0, row=2)
#         ttk.Button(self, text='Cancel').grid(column=0, row=3)
#
#         for widget in self.winfo_children():
#             widget.grid(padx=0, pady=3)
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title('Replace')
#         self.geometry('400x150')
#         self.resizable(0, 0)
#
#         # roots only (remove the minimize/maximize button)
#         self.attributes('-toolroot', True)
#
#         # layout on the root root
#         self.columnconfigure(0, weight=4)
#         self.columnconfigure(1, weight=1)
#
#         self.__create_widgets()
#
#     def __create_widgets(self):
#         # create the input frame
#         input_frame = InputFrame(self)
#         input_frame.grid(column=0, row=0)
#
#         # create the button frame
#         button_frame = ButtonFrame(self)
#         button_frame.grid(column=1, row=0)
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

# # -----------------------------------------------
# # Tkinter OOP
# # Developping Tkinter Object-Oriented App
# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showerror
#
#
# class TemperatrureConverter:
#     @staticmethod
#     def fahrenheit_to_celsius(f):
#         return (f - 32) * 5 / 9
#
#
# class ConverterFrame(ttk.Frame):
#     def __init__(self, container):
#         super().__init__(container)
#         # field options
#         options = {'padx': 5, 'pady': 5}
#
#         # temperature label
#         self.temperature_label = ttk.Label(self, text='Fahrenheit')
#         self.temperature_label.grid(column=0, row=0, sticky=tk.W, **options)
#
#         # temperature entry
#         self.temperature = tk.StringVar()
#         self.temperature_entry = ttk.Entry(self, textvariable=self.temperature)
#         self.temperature_entry.grid(column=1, row=0, **options)
#         self.temperature_entry.focus()
#
#         self.convert_button = ttk.Button(self, text='Convert')
#         self.convert_button['command'] = self.convert
#         self.convert_button.grid(column=2, row=0, sticky=tk.W, **options)
#
#         # result label
#         self.result_label = ttk.Label(self)
#         self.result_label.grid(columnspan=3, row=1, **options)
#
#         # add padding to the frame and show it
#         self.grid(padx=10, pady=10, sticky=tk.NSEW)
#
#     def convert(self):
#         """ Handle button click event
#         """
#         try:
#             f = float(self.temperature.get())
#             c = TemperatrureConverter.fahrenheit_to_celsius(f)
#             result = f'{f} Fahrenheit = {c:.2f} Celsius'
#             self.result_label.config(text=result)
#         except ValueError as error:
#             showerror(title='Error', message=error)
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#
#         self.title('Temperature Converter')
#         self.geometry('300x70')
#         self.resizable(False, False)
#
#
# if __name__ == "__main__":
#     app = App()
#     ConverterFrame(app)
#     app.mainloop()

# # -----------------------------------------------
# # Tkinter OOP
# # Developping Tkinter Object-Oriented App
# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showerror
#
#
# class TemperatureConverter:
#     @staticmethod
#     def fahrenheit_to_celsius(f, format=True):
#         result = (f - 32) * 5/9
#         if format:
#             return f'{f} Fhrenheit = {result:.2f} Celsisus'
#         return result
#
#     @staticmethod
#     def celsius_to_fahrenheit(c, format=True):
#         result = c * 9/5 + 32
#         if format:
#             return f'{c} Celsius = {result:.2f} Fahrenheit'
#         return result
#
#
# class ConverterFrame(ttk.Frame):
#     def __init__(self, container, unit_from, converter):
#         super().__init__(container)
#
#         self.unit_from = unit_from
#         self.converter = converter
#
#         # field options
#         options = {'padx': 5, 'pady': 0}
#
#         # temperature label
#         self.temperature_label = ttk.Label(self, text=self.unit_from)
#         self.temperature_label.grid(column=0, row=0, sticky='w', **options)
#
#         # temperature entry
#         self.temperature = tk.StringVar()
#         self.temperature_entry = ttk.Entry(self, textvariable=self.temperature)
#         self.temperature_entry.grid(column=1, row=0, sticky='w', **options)
#         self.temperature_entry.focus()
#
#         # button
#         self.convert_button = ttk.Button(self, text='Convert')
#         self.convert_button.grid(column=2, row=0, sticky='w', **options)
#         self.convert_button.configure(command=self.convert)
#
#         # result label
#         self.result_label = ttk.Label(self)
#         self.result_label.grid(columnspan=3, row=1, **options)
#
#         # add padding to the frame and show it
#         self.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")
#
#     def convert(self, event=None):
#         """ Handle button click event
#         """
#         try:
#             input_value = float(self.temperature.get())
#             result = self.converter(input_value)
#             self.result_label.config(text=result)
#         except ValueError as error:
#             showerror(title='Error', message=error)
#
#     def reset(self):
#         self.temperature_entry.delete(0, "end")
#         self.result_label.text = ''
#
#
# class ControlFrame(ttk.LabelFrame):
#     def __init__(self, container):
#
#         super().__init__(container)
#         self['text'] = 'Option'
#
#         # radio buttons
#         self.selected_value = tk.IntVar()
#
#         ttk.Radiobutton(
#             self,
#             text='F to C',
#             value=0,
#             variable=self.selected_value,
#             command=self.change_frame).grid(column=0, row=0, padx=5, pady=5)
#
#         ttk.Radiobutton(
#             self,
#             text='C to F',
#             value=1,
#             variable=self.selected_value,
#             command=self.change_frame).grid(column=1, row=0, padx=5, pady=5)
#
#         self.grid(column=0, row=1, padx=5, pady=5, sticky='ew')
#
#         # initialize frames
#         self.frames= {}
#         self.frames[0] = ConverterFrame(
#             container,
#             'Fahrenheit',
#             TemperatureConverter.fahrenheit_to_celsius)
#         self.frames[1] = ConverterFrame(
#             container,
#             'Celsius',
#             TemperatureConverter.celsius_to_fahrenheit)
#
#         self.change_frame()
#
#     def change_frame(self):
#         frame = self.frames[self.selected_value.get()]
#         frame.reset()
#         frame.tkraise()
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#
#         self.title('Temperature Converter')
#         self.geometry('300x120')
#         self.resizable(False, False)
#
#
# if __name__ == "__main__":
#     app = App()
#     ControlFrame(app)
#     app.mainloop()

# -----------------------------------------------
# Tkinter Themes
# Introduction to Tkinter ttk themes

import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # root root
        self.title('Theme Demo')
        self.geometry('400x300')
        self.style = ttk.Style(self)

        # label
        label = ttk.Label(
            self,
            text='Name')
        label.grid(column=0, row=0, padx=10, pady=10, sticky='w')
        # entry
        textbox = ttk.Entry(self)
        textbox.grid(column=1, row=0, padx=10, pady=10, sticky='w')
        # button
        btn = ttk.Button(self, text='Show')
        btn.grid(column=2, row=0, padx=10, pady=10, sticky='w')

        # radio button
        self.selected_theme = tk.StringVar()
        theme_frame = ttk.LabelFrame(self, text='Themes')
        theme_frame.grid(padx=10, pady=10, ipadx=20, ipady=20, sticky='w')

        for theme_name in self.style.theme_names():
            rb = ttk.Radiobutton(
                theme_frame,
                text=theme_name,
                value=theme_name,
                variable=self.selected_theme,
                command=self.change_theme)
            rb.pack(expand=True, fill='both')

    def change_theme(self):
        self.style.theme_use(self.selected_theme.get())

if __name__=="__main__":
    app = App()
    app.mainloop()