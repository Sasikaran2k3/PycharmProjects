from tkinter import *

from openpyxl import load_workbook

root = Tk()
root.geometry("1080x720")

l = ['sasi','karan','jeya','sivakumar']


def get_list(e):
    out = []
    leng = len(str(data.get()))
    if data.get() != "":
        for i in l:
            if(data.get().startswith(i[:leng])):
                out.append(i)
        list.delete(0,END)
    else:
        out = l[:]
        list.delete(0, END)
    for i in out:
        list.insert(END,i)

    global store_name
    store_name=list.select_set(0)


def enter(e):
    list.focus_set()


def show_accounts(ev):
    out = []
    global store_name
    for i in list.curselection():
        store_name = list.get(i)
        wb = load_workbook(store_name+".xlsx")
        pointer = wb.active
        for i in output_frame.winfo_children():
            i.destroy()
        for row,i in enumerate(pointer["B"]):
            e = Entry(output_frame,relief=GROOVE)
            e.grid(row=row+1, column=0)
            e.bind("<Down>", movement_down)
            e.bind("<Up>", movement_up)
            e.bind("<Return>", movement_down)
            e.insert(END,i.value)
            e.focus_set()
            output_frame.pack()
            if row+1 == len(pointer["B"]):
                e.bind("<Return>", jump_to_save)


def movement_down(e):
    total_row =output_frame.grid_size()[1]
    info = output_frame.focus_get().grid_info()
    current_row = info["row"]+1
    if total_row-1 >= current_row:
        output_frame.grid_slaves(current_row)[0].focus_set()

def movement_up(e):
    info = output_frame.focus_get().grid_info()
    current_row = info["row"]-1
    if 1 <= current_row:
        output_frame.grid_slaves(current_row)[0].focus_set()

def jump_to_save(e):
    buttons_of_operation.grid_slaves(row=0,column=1)[0].focus_set()

def save_to_main(e):
    print(store_name)
    wb = load_workbook(str(store_name) + ".xlsx")
    pointer = wb.active
    total_row = output_frame.grid_size()[1]
    new = []
    for i in range(1,total_row):
        value = output_frame.grid_slaves(i)[0].get()
        pointer['C%d' % i].value = value
    wb.save((store_name)+".xlsx")



def view_store():
    pass

Label(root, text="WELCOME TO COLLECTION SOFTWARE").pack(side=TOP,pady=20)

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
list.bind("<Double-Button-1>", show_accounts)
store_name = ""

output_frame = Frame(root)
output_frame.pack()

buttons_of_operation = Frame(root)
view = Button(buttons_of_operation, text="View", command=view_store).grid(row=0,column=0)
save_but = Button(buttons_of_operation, text="Save Changes")
save_but.bind("<Return>", save_to_main)
save_but.bind("<Button-1>", save_to_main)
save_but.grid(row=0,column=1)
buttons_of_operation.pack()


lab = Label(root,text="")
lab.pack()

root.mainloop()