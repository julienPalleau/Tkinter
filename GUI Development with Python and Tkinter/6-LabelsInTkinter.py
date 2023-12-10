import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from roots import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

greeting = tk.StringVar()

image = Image.open("160.jpg").resize((500, 300))
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, textvariable=greeting, image=photo, padding=5, compound="right")
label.pack()

greeting.set("Hello, John!")

root.mainloop()