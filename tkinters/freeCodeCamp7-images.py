from tkinter import *
from PIL import ImageTk, Image

root = Tk()

# creating a Label
root.title('Learn TK')
root.iconbitmap('C:/Users/MOTTIER LUCIE/Documents/GitHub/tkinter/logo.ico')

my_img1 = ImageTk.PhotoImage(Image.open(
    'C:/Users/MOTTIER LUCIE/Documents/GitHub/tkinter/dragon.png'))
my_img2 = ImageTk.PhotoImage(Image.open(
    'C:/Users/MOTTIER LUCIE/Documents/GitHub/tkinter/images01.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open(
    'C:/Users/MOTTIER LUCIE/Documents/GitHub/tkinter/images02.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open(
    'C:/Users/MOTTIER LUCIE/Documents/GitHub/tkinter/images03.png'))
my_img5 = ImageTk.PhotoImage(Image.open(
    'C:/Users/MOTTIER LUCIE/Documents/GitHub/tkinter/images04.png'))

images_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

status = Label(root, text="Image 1 of " +
               str(len(images_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=images_list[image_number-1])
    button_forward = Button(
        root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image " + str(image_number) + " of " +
                   str(len(images_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=images_list[image_number-1])
    button_forward = Button(
        root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    # Update Status Bar
    status = Label(root, text="Image " + str(image_number) + " of " +
                   str(len(images_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
