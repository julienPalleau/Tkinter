import tkinter as tk
from tkinter import ttk
from roots import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

programming_languages = ("C", "Go", "JavaScript", "Perl", "Python", "Rust")

langs = tk.StringVar(value=programming_languages)
langs_select = tk.Listbox(root, listvariable=langs, height=6)  # Listbox is part of tkinter is not a themable tkinter
# widget so we have to use tk and not ttk

# To activate multiple lines choice the two lines below are equivalent
# langs_select = tk.Listbox(root, listvariable=langs, height=6, selectmode="extended")
langs_select["selectmode"] = "extended"  # allow the user to select multiple line. # "browse" is the counterpart
langs_select.pack()


def handle_selection_change(event):
    selected_indices = langs_select.curselection()
    for i in selected_indices:
        print(langs_select.get(i))


langs_select.bind("<<ListboxSelect>>", handle_selection_change)

root.mainloop()
