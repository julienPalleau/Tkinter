# https://www.youtube.com/watch?v=nCD3rHKYEI0
from tkinter import *
import numpy as np
import numpy_financial as npf


class LoanCalculator:

    def __init__(self):
        window = Tk()
        window.title("LoanCalculator")

        Label(window, text="Loan Amount:").grid(row=1, column=1, sticky=W)
        Label(window, text="Interest Rate:").grid(row=2, column=1, sticky=W)
        Label(window, text="Term (years):").grid(row=3, column=1, sticky=W)
        Label(window, text=None).grid(row=4, column=1, sticky=W)

        # outputs
        Label(window, text="Payment").grid(row=5, column=1, sticky=W)
        Label(window, text="Total Payments:").grid(row=6, column=1, sticky=W)

        # Variable to store inputs
        self.pv = StringVar()
        self.interest_rate = StringVar()
        self.term = StringVar()

        # Variable for outputs
        self.pmt = StringVar()
        self.total = StringVar()

        # text boxes to hold inputs and outputs
        Entry(window, textvariable=self.pv, justify=RIGHT).grid(row=1, column=2, padx=(0,5))
        Entry(window, textvariable=self.interest_rate, justify=RIGHT).grid(row=2, column=2)
        Entry(window, textvariable=self.term, justify=RIGHT).grid(row=3, column=2)
        Label(window, textvariable=self.pmt, font="Helvetica 12 bold", justify=RIGHT).grid(row=5, column=2, sticky=E)
        Label(window, textvariable=self.total, font="Helvetica 12 bold", justify=RIGHT).grid(row=6,column=2, sticky=E)

        Button(window, text="Calculate Payment", command=self.calcPayment).grid(row=7, column=2, padx=(60,5), pady=5)

        window.mainloop()

    def calcPayment(self):
        pv = float(self.pv.get())
        rate = float(self.interest_rate.get())
        term = int(self.term.get())
        pmt = (rate / 100)*term
        total = pmt * 12
        self.pmt.set("Euros" + format(pmt, "8,.2f"))
        self.total.set("Euros" + format(total, "8,.2f"))


LoanCalculator()
