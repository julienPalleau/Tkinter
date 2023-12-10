import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)

name = ttk.Label(root, text="Hello, world!", style="TLabel")
# or
name = ttk.Label(root, text="Hello, world!")
ttk.Label(root, text="Hello, world!")
#entry = ttk.Entry(root, width=15)
#entry["style"] = "CustomEntryStyle"  # Either the style is included in ttk.Label like above (commented line)
                                    # or we define the style on a sparated line like here
name.pack()

style.configure("TLabel", font=("Segoe UI", 20))

root.mainloop()
