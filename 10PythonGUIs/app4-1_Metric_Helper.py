# Metric Helper
# Icon from http://www.inconsmind.com
# https://coolors.co/ to generate colors and get hex code.

from decimal import *
import tkinter
from os import truncate
from tkinter import ttk
from tkinter import END

root = tkinter.Tk()
root.title("Metric Helper")
root.iconbitmap("ruler.ico")
root.geometry("480x200")
root.resizable(1, 0)
root.config(bg='#ADE8F4')


# Fonctions
def convert():
    final_metric.delete(0, END)
    dico_unite = {'femto': 10**-15,
                  'pico': 10**-12,
                  'nano': 10**-9,
                  'micro': 10**-6,
                  'milli': 10**-3,
                  'centi': 10 ** -2,
                  'deci': 10 ** -1,
                  'base value': 1,
                  'deca': 10 ** 1,
                  'hecto': 10 ** 2,
                  'kilo': 10 ** 3,
                  'mega': 10 ** 4,
                  'giga': 10 ** 5,
                  'tera': 10 ** 6,
                  'peta': 10 ** 7}

    precision = (dico_unite.get(Combo2.get())) / dico_unite.get(Combo1.get())
    # precision = int(math.log10(precision))
    precision = len(initial_metric.get())
    print(f"Debug precision : {precision}")
    if precision > 0:
        getcontext().prec = precision
    else:
        pass

    print(f"{initial_metric.get()}")
    print(f"{Combo1.get()} {dico_unite.get(Combo1.get(), 'unknow unity')}")
    print(f"{Combo2.get()} {dico_unite.get(Combo2.get(), 'unknow unity')}")
    print(f"Debug boite2: {float(initial_metric.get())} {float(dico_unite.get(Combo1.get()))} {float(dico_unite.get(Combo2.get()))} {float(initial_metric.get()) * float(dico_unite.get(Combo1.get())) * float(dico_unite.get(Combo2.get()))}")

    if dico_unite.get(Combo1.get()) > dico_unite.get(Combo2.get()):
        print("debug")
        final_metric.insert(0,
                            f"{float(initial_metric.get()) * float(dico_unite.get(Combo1.get())) * float(dico_unite.get(Combo2.get()))}")
    elif dico_unite.get(Combo1.get()) == dico_unite.get(Combo2.get()):
        final_metric.insert(0, f"{Decimal(float(initial_metric.get()))}")
    else:
        final_metric.insert(0,
                            f"{Decimal(float(initial_metric.get()) * float(dico_unite.get(Combo1.get()))) * (1 / Decimal(float(dico_unite.get(Combo2.get()))))}")


# Definition de l'interface

initial_metric = tkinter.Entry(root, width=30)
initial_metric.grid(row=0, column=0, padx=15, pady=(20, 20), sticky="W")
initial_metric.insert(END, 'Enter your quantity')

egalite_label = tkinter.Label(root, text='=')
egalite_label.grid(row=0, column=1, padx=15, pady=(20, 20))

final_metric = tkinter.Entry(root, width=30)
final_metric.grid(row=0, column=2, padx=15, pady=(20, 20), sticky="E")

convert_button = tkinter.Button(root, text='Convert', width=30, bg='#00B4D8', activebackground='#0077B6',
                                command=convert)
convert_button.grid(row=2, columnspan=3, padx=15, pady=10)

vlist = ['femto', 'pico', 'nano', 'micro', 'milli', 'centi', 'deci', 'base value', 'deca', 'hecto', 'kilo', 'mega', 'giga', 'tera', 'peta']
Combo1 = ttk.Combobox(root, values=vlist, width=27)
Combo1.set("base value")
Combo1.grid(row=3, column=0, padx=15, pady=(20, 20), sticky="W")

to_label = tkinter.Label(root, text='to')
to_label.grid(row=3, column=1, padx=15, pady=(20, 20))

Combo2 = ttk.Combobox(root, values=vlist, width=27)
Combo2.set("base value")
Combo2.grid(row=3, column=2, padx=15, pady=(20, 20), sticky="E")

# Run root root's main loop
root.mainloop()
