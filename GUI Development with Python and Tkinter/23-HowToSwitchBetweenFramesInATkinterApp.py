import tkinter as tk
from tkinter import ttk, font
from roots import set_dpi_awareness

set_dpi_awareness()


class DistanceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Distance Converter")
        self.frames = dict()

        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky="EW")

        # # frame = FeetToMetres(container)
        # feet_to_metres = FeetToMetres(container, self)
        # feet_to_metres.grid(column=0, row=0, sticky="NSEW")
        #
        # # frame = MetresToFeet(container)
        # metres_to_feet = MetresToFeet(container, self)
        # metres_to_feet.grid(column=0, row=0, sticky="NSEW")
        #
        # self.frames[FeetToMetres] = feet_to_metres
        # self.frames[MetresToFeet] = metres_to_feet

        # the above commented section of code is replaced by the for loop below. Shorter and nicer

        for FrameClass in (MetresToFeet, FeetToMetres):
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.grid(column=0, row=0, sticky="NSEW")

        self.show_frame(MetresToFeet)

    def show_frame(self, container):
        frame = self.frames[container]
        self.bind("<Return>", frame.calculate)
        self.bind("<KP_Enter>", frame.calculate)
        frame.tkraise()


class MetresToFeet(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        self.metres_value = tk.StringVar(value="Metre shown here.")
        self.feet_value = tk.StringVar()

        metres_label = ttk.Label(self, text="Metres:")
        metres_input = ttk.Entry(self, width=15, textvariable=self.metres_value, font=("Segoe UI", 8))
        feet_label = ttk.Label(self, text="Feet:")
        feet_display = ttk.Label(self, textvariable=self.feet_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)
        switch_page_button = ttk.Button(
            self,
            text="Switch to feet conversion",
            command=lambda: controller.show_frame(FeetToMetres)
        )

        metres_label.grid(column=0, row=0, stick="W")
        metres_input.grid(column=1, row=0, stick="EW")
        metres_input.focus()

        feet_label.grid(column=0, row=1, stick="W")
        feet_display.grid(column=1, row=1, stick="EW")

        calc_button.grid(column=0, row=2, columnspan=2, stick="EW")
        switch_page_button.grid(column=0, row=3, columnspan=2, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

    def calculate(self, *args):
        try:
            metres = float(self.metres_value.get())
            feet = metres * 3.28084
            self.feet_value.set(f"{feet:.3f}")
        except ValueError:
            print("saisir un entier")


class FeetToMetres(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        self.metres_value = tk.StringVar()
        self.feet_value = tk.StringVar(value="Feet shown here.")

        feet_label = ttk.Label(self, text="Feet:")
        feet_input = ttk.Entry(self, width=15, textvariable=self.feet_value, font=("Segoe UI", 8))
        metres_label = ttk.Label(self, text="Metres:")
        metres_display = ttk.Label(self, textvariable=self.metres_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)
        switch_page_button = ttk.Button(
            self,
            text="Switch to metres conversion",
            command=lambda: controller.show_frame(MetresToFeet)
        )

        feet_label.grid(column=0, row=0, stick="W")
        feet_input.grid(column=1, row=0, stick="EW")
        feet_input.focus()

        metres_label.grid(column=0, row=1, stick="W")
        metres_display.grid(column=1, row=1, stick="EW")

        calc_button.grid(column=0, row=2, columnspan=2, stick="EW")
        switch_page_button.grid(column=0, row=3, columnspan=2, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

    def calculate(self, *args):
        try:
            feet = float(self.feet_value.get())
            metres = feet / 3.28084
            self.metres_value.set(f"{metres:.3f}")
        except ValueError:
            print("saisir un entier")


root = DistanceConverter()

font.nametofont("TkDefaultFont").configure(size=15)

root.columnconfigure(0, weight=1)
root.mainloop()
