from tkinter  import *
top=Tk()
top.geometry("500x500")

    
l=Label(top,text="list")
listbox=Listbox(top,background="Pink",foreground="red",highlightcolor="blue")
def deletei():
    listbox.delete(ANCHOR)
def geti():
   i=input() 
   listbox.get(ANCHOR)
b=Button(text="delete",command=deletei).place(x=200,y=350)
b=Button(text="get",command=geti).place(x=200,y=400)
listbox.insert(1,"name")
listbox.insert(2,"roll")
listbox.insert(3,"section")
l.pack()
listbox.place(x=200,y=200)
top.mainloop()
