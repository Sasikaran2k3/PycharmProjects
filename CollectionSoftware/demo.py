import tkinter as tk

def button_clicked(event):
    if event.num == 1:  # Left mouse button
        print("Left button clicked!")
    elif event.num == 3:  # Right mouse button
        print("Right button clicked!")

root = tk.Tk()

button = tk.Button(root, text="Click Me")
button.pack()

button.bind("<Button-1> <Button-3>", button_clicked)  # Bind both left and right button click events

root.mainloop()
