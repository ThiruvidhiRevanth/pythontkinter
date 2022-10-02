from tkinter import*
top1=Tk()
top1.geometry("200x200")
def open1():
 top=Toplevel(top1)
 top.mainloop()
def or1():
    or1=Toplevel(top1)
    or1.mainloop()
btn=Button(top1,text="open",command=open1)
btn.pack(anchor=CENTER)
bt=Button(top1,text="or",command=or1)
bt.place(x=30,y=50)
top1.mainloop()
