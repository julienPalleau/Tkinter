# https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter

import tkinter as tk


def test():
    name = entry.get()
    print(name)
    entry.delete(0, tk.END)
    greeting.configure(text=name)
    # text_box.get("1.0", tk.END)
    text_box.delete("1.0", "1.4")
    print(text_box.get("1.0"))
    text_box.delete("1.0", tk.END)
    text_box.insert("2.0", "\nHello Julien !")
    text_box.insert(tk.END, "\nPut me at the end!")


root = tk.Tk()
text_box = tk.Text()
text_box.pack()

greeting = tk.Label(text="Hello, Tkinter",
                    fg="white", # Set the text color to white
                    bg="black", # Set backgrround color to black
                    width=20,
                    height=10
)

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=test
)

label = tk.Label(text="Name")
entry = tk.Entry(
    fg="black",
    bg = "white",
    width = 50
)

greeting.pack()
button.pack()
label.pack()
entry.pack()
root.mainloop()

