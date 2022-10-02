from tkinter import *
top=Tk()
top.geometry("200x200")
mb=Menubutton(top,text="click")
mb.place(x=50,y=30)
mb.menu=Menu(mb)
mb["menu"]=mb.menu
first=IntVar()
sec=IntVar()
mb.menu.add_checkbutton(label="first",variable=first)
mb.menu.add_checkbutton(label="second",variable=sec)

    

top.mainloop()
