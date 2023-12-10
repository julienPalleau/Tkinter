import tkinter as tk

root = tk.Tk()

# Adds a title to the root
root.title("My Awesome App!")

# Size the root when first appears, measured in pixels
root.geometry("400x400")

# LABELS
prompt = tk.Label(text="This is CS50. \nWelcome to my awesome app!", font=("Times New Roman", 20))
prompt.grid()

# ENTRY FIELD
entry_field = tk.Entry()
entry_field.grid()

# BUTTONS
button1 = tk.Button(text="Click me!", bg="red")
button1.grid()

# TEXT FIELDS
text_field = tk.Text(master=root, height=10, width=30)
text_field.grid()

# Makes the frame appear on screen. Akin to calling a function
root.mainloop()