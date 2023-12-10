import random
import tkinter as tk

root = tk.Tk()
root.title("Greetings ____")
root.geometry("400x400")


# FUNCTIONS
def phrase_generator():
    phrases = ["Hello ", "What's up ", "Aloha ", "Hafa Adai "]
    name = str(entry1.get())
    return phrases[random.randint(0, 3)] + name


def phrase_display():
    greeting = phrase_generator()

    # This creates the text field
    greeting_display = tk.Text(master=root, height=10, width=30)
    greeting_display.grid(column=0, row=3)

    greeting_display.insert(tk.END, greeting)


# LABEL
label1 = tk.Label(text="Welcome to my app")
label1.grid(column=0, row=0)

label2 = tk.Label(text="What is your name? ")
label2.grid(column=0, row=1)

# ENTRIES
entry1 = tk.Entry()
entry1.grid(column=1, row=1)

# BUTTOM
button1 = tk.Button(text="Click me!", command=phrase_display)
button1.grid(column=0, row=2)

root.mainloop()
