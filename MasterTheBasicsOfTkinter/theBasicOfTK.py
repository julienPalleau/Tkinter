import tkinter
from tkinter import Button, Checkbutton, Entry, Label, messagebox, Menu, OptionMenu, Radiobutton, StringVar
import sqlite3
from PIL import Image, ImageTk

root = tkinter.Tk()
root.geometry("600x900")
root.title("Registration Form")


def abt():
    tkinter.messagebox.showinfo("Welcome to authors", "This is demo for menu fields")


def database():
    name1 = fn.get()
    last1 = ln.get()
    date = dob.get()
    country = var.get()
    prog = var_c2
    gender = radio_var.get()
    conn = sqlite3.connect("Form.db")
    with conn:
        cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Student (Name TEXT, Last TEXT, DOB TEXT, country TEXT, Programming TEXT, Gender TEXT)')
    cursor.execute('INSERT INTO Student(Name, Last, DOB, country, Programming, Gender) VALUES(?,?,?,?,?,?)', (name1, last1, date, country, prog, gender))
    conn.commit()


def printt():
    first = fn.get()
    second = ln.get()
    dob1 = dob.get()
    var1 = var.get()
    var3 = var_c1
    var3 = var_c2
    var4 = radio_var.get()
    print(f"Your Fullname is {first}" + " " + f"{second}")
    print(f"Your date of birth is {dob1}")
    print(f"Your Country is {var1}")
    print(f"Your prog language is {var3}")
    print(f"Your Gender is {var4}")
    tkinter.messagebox.showinfo("Welcome", "User is successfully signed up !!")


def second_win():
    window = tkinter.Tk()
    window.title("Welcome to second window")
    window.geometry('250x200')
    label_02 = Label(window, text='Registration Complete', relief="solid", font=('arial', 12, 'bold'))
    label_02.place(x=30, y=70)
    but_01=Button(window, text='demo', width=12, bg='brown', fg='white', command=abt)
    but_01.place(x=80, y=110)

image = Image.open('team.png')
photo=ImageTk.PhotoImage(image)

lab=Label(image=photo)
lab.grid(row=0, column=0)

menu = Menu(root)
root.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="File", menu=subm1)
subm1.add_command(label="Exit", command=root.destroy)

subm2 = Menu(menu)
menu.add_cascade(label="Option", menu=subm2)
subm2.add_command(label="About", command=abt)

fn = StringVar()
ln = StringVar()
dob = StringVar()
var = StringVar()
var_c1 = "Java"
var_c2 = "Python"
radio_var = StringVar()


label_0 = Label(root, text="Registration Form", relief='solid', width=20, font=("arial",19,"bold"))
label_0.grid(row=1, column=0, pady=10)

label_1 = Label(root, text="FirstName :", width=20, font=("arial", 10, "bold"))
label_1.place(x=155, y=500)
entry_1 = Entry(root, textvar=fn)
entry_1.place(x=300, y=500)

label_2 = Label(root, text="LastName :", width=20, font=("arial", 10, "bold"))
label_2.place(x=155, y=550)
entry_2 = Entry(root, textvar=ln)
entry_2.place(x=300, y=550)

label3 = Label(root, text="DOB :", width=20, font=("arial", 10, "bold"))
label3.place(x=137, y=600)
entry_3 = Entry(root, textvar=dob)
entry_3.place(x=300, y=600)

label4 = Label(root, text="Country :", width=20, font=("arial", 10, "bold"))
label4.place(x=149, y=650)

list1=['France', 'Allemagne', 'Italie', 'Espagne', 'Belgique', 'Slovenie']
droplist=OptionMenu(root, var, *list1)
var.set("Select country")
droplist.config(width=15)
droplist.place(x=298, y=650)

label5 = Label(root, text="Prog Lang :", width=20, font=("arial", 10, "bold"))
label5.place(x=156, y=700)

c1 = Checkbutton(root, text="Java", variable=var_c1)
c1.place(x=298, y=700)
c2 = Checkbutton(root, text="Python", variable=var_c2)
c2.place(x=358, y=700)

label6 = Label(root, text="Gender :", width=20, font=("arial", 10, "bold"))
label6.place(x=148, y=750)


radio_var.set('Female')


r1 = Radiobutton(root, text='Male', variable=radio_var, value="Male")
r2 = Radiobutton(root, text='Female', variable=radio_var, value="Female")
r1.place(x=298, y=750)
r2.place(x=358, y=750)


btn_signup = Button(root, text="Signup", width=12, bg='brown', fg='white', command=database)
btn_signup.place(x=210, y=800)
root.bind("<Return>", database)

btn_quit = Button(root, text="Quit", width=12, bg='brown', fg='white', command=root.destroy)
btn_quit.place(x=310, y=800)

btn_login = Button(root, text="login", width=12, bg='brown', fg='white',command=second_win)
btn_login.place(x=260, y=850)

root.mainloop()
