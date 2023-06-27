from tkinter import *

def move(e):
    print("s")

root = Tk()

frame = Frame()

l = Entry(frame)
e = Entry(frame).pack()
#l.bind("<KeyRelease>",move)
l.pack()
for i in frame.winfo_children():
    i.bind("<KeyRelease>",move)
frame.pack()
root.mainloop()