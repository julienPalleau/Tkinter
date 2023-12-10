import tkinter as tk
import tkinter.font as font
from tkinter import ttk
from roots import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.title("Distance Converter")

font.nametofont("TkDefaultFont").configure(size=15)

metres_value = tk.StringVar()
feet_value = tk.StringVar(value="Feet shown here.")


def calculate_feet(*args):
    try:
        metres = float(metres_value.get())
        feet = metres * 3.28084
        feet_value.set(f"{feet:.3f}")
    except ValueError:
        print("saisir un entier")


root.columnconfigure(0, weight=1)

main = ttk.Frame(root, padding=(30, 15))
main.grid()

metres_label = ttk.Label(main, text="Metres:")
metres_input = ttk.Entry(main, width=10, textvariable=metres_value, font=("Segoe UI", 15))
feet_label = ttk.Label(main, text="Feet:")
feet_display = ttk.Label(main, textvariable=feet_value)
calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)

metres_label.grid(column=0, row=0, stick="W")
metres_input.grid(column=1, row=0, stick="EW")
metres_input.focus()

feet_label.grid(column=0, row=1, stick="W")
feet_display.grid(column=1, row=1, stick="EW")

calc_button.grid(column=0, row=2, columnspan=2, stick="EW")

for child in main.winfo_children():
    child.grid_configure(padx=15, pady=15)

root.bind("<Return>", calculate_feet)
root.bind("<KP_Enter>", calculate_feet)

root.mainloop()
