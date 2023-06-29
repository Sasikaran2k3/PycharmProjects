from tkinter import *

def button_clicked(event):
    if event.num == 1:  # Left mouse button
        print("Left button clicked!")
    elif event.num == 3:  # Right mouse button
        print("Right button clicked!")

root = Tk()
root.geometry("500x500")

scroll_frame = Frame(root)
scroll_frame.pack(fill=BOTH,expand=1)

canva = Canvas(scroll_frame)
canva.pack(fill=BOTH, expand=1)

scroll = Scrollbar(scroll_frame,orient=VERTICAL,command=canva.yview)
scroll.pack(side=RIGHT, fill=Y)

canva.config(yscrollcommand=scroll.set)
canva.bind("<Configure>", lambda e: canva.config(scrollregion=canva.bbox("all")))

out = Frame(Canvas)

root.mainloop()
