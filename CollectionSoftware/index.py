from tkinter import *

from openpyxl import load_workbook

root = Tk()
root.geometry("1080x720")

l = ['sasi','karan','jeya','sivakumar']


def get_list(e):
    out = []
    leng = len(str(data.get()))
    for i in l:
        if(data.get().startswith(i[:leng])):
            out.append(i)
    list.delete(0,END)
    for i in out:
        list.insert(END,i)
    list.select_set(0)


def enter(e):
    list.focus_set()


def show_accounts(e):
    out = []
    for i in list.curselection():
        store_name = list.get(i)
        wb = load_workbook(store_name+".xlsx")
        pointer = wb.active
        output_frame = Frame(root)
        for row,i in enumerate(pointer["B"]):
            e = Entry(output_frame,relief=GROOVE)
            e.grid(row=row+1, column=0)
            e.insert(END,i.value)
            e.focus_set()
            output_frame.pack()


Label(root,text = "WELCOME TO COLLECTION SOFTWARE").pack(side=TOP,pady=20)

input_frame = Frame(root)
Label(input_frame,text= "Store Name : ").grid(row=0,column=0)
data = StringVar()
text = Entry(input_frame,width=90,bd=15,textvariable=data)
text.bind("<KeyRelease>",get_list)
text.bind("<Return>", enter)
text.grid(row=0,column=1)
input_frame.pack(pady=30)


scroll = Scrollbar(root)
list = Listbox(root, height=10,yscrollcommand=scroll.set,font=("Calibri", 15))
list.pack(fill='x',pady=20)
list.bind("<Return>", show_accounts)


lab = Label(root,text="")
lab.pack()

root.mainloop()