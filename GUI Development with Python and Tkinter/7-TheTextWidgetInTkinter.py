import tkinter as tk
from tkinter import ttk
from roots import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

text = tk.Text(root, height=8)
text.pack()


def Add():
    text_content1 = text.get("1.0", "end")
    print(text_content1)


button1 = tk.Button(root, text='Add', command=Add)
button1.pack()

text.insert("1.0", "Please enter a comment...")  # the 1 refers to the line number
# the 0 refers to the character number
# We go to the first line and 0 character
text["state"] = "normal"  # normal or disabled depending if you want the user to write inside the text field

text_content2 = text.get("1.0", "end")  # First line charcter 0 till the end
print(text_content2)

root.mainloop()
