from tkinter import *
from tkinter.ttk import *
master=Tk()
master.geometry("400x250")
l1=Label(master,text="height")
l2=Label(master,text="width")
l1.grid(row=0,column=0,sticky=W,pady=1)
l2.grid(row=1,column=0,sticky=W,pady=1)
e1=Entry(master)
e2=Entry(master)

e1.grid(row=0,column=1,sticky=W,pady=1)
e2.grid(row=1,column=1,sticky=W,pady=1)
b1=Button(master,text="click1")
b1.grid(row=2,column=0,sticky=E)
b2=Button(master,text="click2")
b2.grid(row=2,column=1,sticky=E)


