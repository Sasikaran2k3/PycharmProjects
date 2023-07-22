import datetime
import os.path
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox

import openpyxl
from openpyxl import load_workbook
def pop_ask(e):
    global mycanva
    global scroll
    mycanva.delete(ALL)
    scroll.destroy()
    mycanva = Canvas(outside)
    mycanva.pack(side=LEFT)
    scroll = ttk.Scrollbar(outside, orient=VERTICAL, command=mycanva.yview)
    scroll.pack(side=RIGHT, fill=Y)
    mycanva.bind("<Configure>", lambda e: mycanva.config(scrollregion=mycanva.bbox(ALL)))
    output_frame = Frame(mycanva, highlightbackground="black", highlightthickness=2)
    output_frame.pack()
    mycanva.config(yscrollcommand=scroll.set)
    mycanva.create_window((0, 0), window=output_frame, anchor=NW)
    for i in range(100):
        Label(output_frame, text="SASI").grid(row=i, column=i % 2)
root = Tk()
outside = Frame(root)
mycanva = Canvas(outside)
scroll = ttk.Scrollbar(outside, orient=VERTICAL, command=mycanva.yview)
scroll.pack(side=RIGHT, fill=Y)
mycanva.pack(side=LEFT)
button = Button(text="press")
button.bind("<Button-1>", pop_ask)
button.pack()
outside.pack()
root.mainloop()