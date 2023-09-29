import os
from tkinter import *
from tkinter import ttk
from random import *
import csv
import pandas


def open_csv(e):
    n = int(entry.get())
    print(n)
    f1 = open("Sample_reasons.txt", "r").readlines()
    f = open("list_of_reasons.csv", "w", newline="")
    writer = csv.writer(f)
    l = []
    for i in range(n):
        l.append(choice(f1).strip())
        writer.writerow([choice(f1).strip()])
    f.close()
    df = pandas.DataFrame(l)
    print(df)
    df.to_clipboard(index=False)
    Label(root,text="Successfully Created the reasons",font=("Calibri", 15)).pack(pady=10)
    flag = os.O_RDWR | os.O_CREAT
    os.open("list_of_reasons.csv",flag,0o666)

root = Tk()
root.title = "Absent Reason Teller"
root.geometry("500x500")
Label(root,text="Welcome to Absentees Reason Teller",font=("Calibri", 15)).pack(side=TOP)
frame = Frame(root)
Label(frame,text="Enter the number of Absentees : ",font=("Calibri", 15)).grid(row=2,column=0)
entry = Entry(frame, width=50)
entry.bind("<Return>",lambda e: but.focus_set())
entry.grid(row=2, column=1,pady=90)
but = Button(root, text="Submit")
but.bind("<Return>", open_csv)
but.bind("<Button-1>", open_csv)
frame.pack()
but.pack()


root.mainloop()
