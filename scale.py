from tkinter import *
def select():
    sel=str(v.get())
    label.config(text=sel)
top=Tk()
top.geometry("300x300")
v=DoubleVar()
scale=Scale(top,variable=v,from_=1,to_=100,orient=VERTICAL)

scale.pack(anchor=E)
bt=Button(top,text="value",command=select)
bt.pack()
label=Label(top)
label.pack()
top.mainloop()
