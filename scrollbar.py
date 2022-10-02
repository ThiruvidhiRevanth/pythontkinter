from tkinter import *
top=Tk()
top.geometry("500x500")
sb=Scrollbar(top)
sb.pack(side=RIGHT,fill=Y)
mylist=Listbox(top,yscrollommand=sb.set)
for line in range(30):
    mylist.insert(END,str(line))
mylist.pack(side=LEFT)
sb.config(command=mylist.yview)

top.mainloop()
