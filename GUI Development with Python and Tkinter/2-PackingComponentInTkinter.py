import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

rectangle_1 = tk.Label(root, text="Rectangle 1", bg="blue", fg="white")
rectangle_1.pack(side="left", ipadx=10, ipady=10, fill="both", expand=True)

rectangle_2 = tk.Label(root, text="Rectangle 2", bg="white", fg="blue")
rectangle_2.pack(side="left", ipadx=10, ipady=10, fill="both", expand=True)

rectangle_3 = tk.Label(root, text="Rectangle 3", bg="red", fg="white")
rectangle_3.pack(side="left", ipadx=10, ipady=10, fill="both", expand=True)

root.mainloop()