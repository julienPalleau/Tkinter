# Images
import tkinter
from PIL import ImageTk, Image

# Define root
root = tkinter.Tk()
root.title('Image Basics')
root.iconbitmap('thinking.ico')
root.geometry('700x450')


# Define function
# If you try to display an image inside a function like we are doing here. You have to keep a reference to the image
# by storing it in a global variable
def make_image():
    """print an image"""
    # Using Pil for jpg
    global cat_image

    cat_image = ImageTk.PhotoImage(Image.open('cat.jpg'))
    cat_label = tkinter.Label(root, image=cat_image)
    cat_label.pack()


# Loading an image is a multi-step process in tkinter
# First you need to create the image
# Then you have to put the image on a label or a button (widget)
# Then you put that widget onto the screen
# Basics...works for png
my_image = tkinter.PhotoImage(file='shield.png')  # image creation
my_label = tkinter.Label(root, image=my_image)  # Put that image onto a label. Remember label can be used to put not
# only text onto the screen but images too.
my_label.pack()

my_button = tkinter.Button(root, image=my_image)
my_button.pack()

# Not for jpeg if you want to use anything else than png you need to import PIL library (pipenv install Pillow)
# cat_image = tkinter.PhotoImage('file=cat.jpg')
# cat_label = tkinter.Label(root, image=cat_image)
# cat_label.pack()

make_image()

# Run root root's main loop
root.mainloop()
