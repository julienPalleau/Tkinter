# # In This section we'll see frame and how you can use it to overpass grid limitation
# # Indeed in grid system column width is define by the element you put in for exemple
# row0 = ** will be 2 caracteres width
# row1 = ********** will be 10 caracteres width, so dependint what you want to achieve you might have to mix grid and
# frame system. Below you'll find an example:

# # Frames
import tkinter
from tkinter import BOTH

# Define root
root = tkinter.Tk()
root.title('Frame Basics')
root.iconbitmap('thinking.ico')
root.geometry('500x850')

# # Example of why to use frames
# name_label = tkinter.Label(root, text='Enter your name')
# name_label.pack()
# name_button = tkinter.Button(root, text='Submit your name')
# name_button.grid(row=0, column=1)

# # Define frames
pack_frame = tkinter.Frame(root, bg='blue')
grid_frame_1 = tkinter.Frame(root, bg='white')
grid_frame_2 = tkinter.LabelFrame(root, text='Grid system rules!', borderwidth=5, bg='red')

# # Pack frames onto root
pack_frame.pack(fill=BOTH, expand=True)
grid_frame_1.pack(fill='x', expand=True)
grid_frame_2.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Pack frame
tkinter.Label(pack_frame, text='text').pack()
tkinter.Label(pack_frame, text='text').pack()
tkinter.Label(pack_frame, text='text').pack()

# Grud 1 layout
tkinter.Label(grid_frame_1, text='text').grid(row=0, column=0)
tkinter.Label(grid_frame_1, text='text').grid(row=1, column=1)
tkinter.Label(grid_frame_1, text='text').grid(row=2, column=2)
# tkinter.Label(grid_frame_1, text='aaaaaaaaaaaaaaaaaaaaaaaa').grid(row=3, column=0)

# Grid 2 layout
tkinter.Label(grid_frame_2, text='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').grid(row=0, column=0)


#run root root's main loop
root.mainloop()