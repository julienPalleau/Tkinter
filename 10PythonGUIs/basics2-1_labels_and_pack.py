# Labels and pack
import tkinter

# Define root
root = tkinter.Tk()
root.title("Label Basics!")
root.iconbitmap('thinking.ico')
root.geometry('400x400')
root.resizable(0,0)
root.config(bg='blue')

# Create widgets
name_label_1 = tkinter.Label(root, text='Hello, my name is Julien.')
name_label_1.pack()

name_label_2 = tkinter.Label(root, text='Hello, my name is John.', font=('Arial', 18, 'bold'))
name_label_2.pack()

#name_label_3 = tkinter.Label(root)
# name_label_3.config(text='Hell, my name is Paul.')
# name_label_3.config(font=('Cambria, 10'))
# name_label_3.config(bg='red')

# # so the 3 lines, above can be written on only one line as follow
name_label_3 = tkinter.Label(root, text='Hello, my name is Paul.', font=('Cambria', 10), bg='red')
name_label_3.pack(padx=10, pady=50)

# # Let's see pad, ipad(internal pad), Anchor, fill
name_label_4 = tkinter.Label(root, text="Hello, my name is Sue", bg="#000000", fg="green")
name_label_4.pack(pady=(0, 10), ipadx=50, ipady=10, anchor='w')  # it gives 0 padding on the top and 10 padding on the bottom

name_label_5 = tkinter.Label(root, text='Hello, my name is Pat', bg='#ffffff', fg='#123456')
# name_label_5.pack(fill='x')
# name_label_5.pack(fill='y', expand=True)
# # If you want to expand in x and y then you can replace the two lines above by
name_label_5.pack(fill='both', expand=True, padx=10, pady=10)

# Run the root root's main loop
root.mainloop()