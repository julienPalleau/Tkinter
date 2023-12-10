# http://thinkingtkinter.sourceforge.net/languages/france/penser_en_tkinter.html
# # programation procedural
# from tkinter import * ### (1)
#
# root = Tk()
#
# myContainer1 = Frame(root)  ### (1)
# myContainer1.pack()         ### (2)
#
# button1 = Button(myContainer1)
#
# button1 = Button(root,
#                  text="Bonjour, Monde !",
#                  background="green")
#
# button1.pack()
#
# root.mainloop()


# Meme programme que ci-dessus, mais en OOP
# import tkinter as tk
# from tkinter import *
#
# from main import Window
#
#
# class MyApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.myContainer1 = Frame()
#         self.myContainer1.pack()
#
#         self.button1 = Button(self.myContainer1,
#                               text='OK',
#                               background="green")
#         self.button1.pack(side=LEFT)
#         self.button1.bind("<Button-1>", self.button1Click)
#
#         self.button2 = Button(self.myContainer1,
#                               text='Cancel',
#                               background="red")
#         self.button2.pack(side=RIGHT)
#         self.button2.bind("<Button-1>", self.button2Click)
#
#     def button1Click(self, event):
#         if self.button1["background"] == "green":
#             self.button1["background"] = "yellow"
#         else:
#             self.button1["background"] = "green"
#
#     def button2Click(self, event):
#         self.destroy()
#
#
# if __name__ == "__main__":
#     myapp = MyApp()
#     myapp.mainloop()


# https://www.youtube.com/watch?v=xuXYKhdoTsw&list=PL1FgJUcJJ03tVAsiuEuQrl9w2weP16NYw&index=1
from tkinter import *


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("Tkinter OOP Window")
        self.minsize(500, 400)
        self.wm_iconbitmap("python.ico")


if __name__ == "__main__":
    win = Window()
    win.mainloop()
