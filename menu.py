from tkinter import *
from tkinter import messagebox
top=Tk()
menubar=Menu(top)
def fun():
    messagebox.showinfo("message","hello friends")

file=Menu(menubar,tearoff=0)
file.add_command(label="new")
file.add_separator()
menubar.add_cascade(label="file",menu=file)
edit=Menu(menubar,tearoff=0)
edit.add_command(label="new")
edit.add_command(label="new1",command=fun)


edit.add_separator()
menubar.add_cascade(label="edit",menu=edit)

top.config(menu=menubar)
top.mainloop()


