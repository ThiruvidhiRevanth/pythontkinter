from tkinter import *
top=Tk()
red=Button(top,text="click",fg="RED")
red.pack(side=BOTTOM,fill=X,expand=TRUE)
blue=Button(top,text="blue")
blue.pack( fill=BOTH,expand=TRUE,side=TOP)
green=Button(top)
green.pack(side=TOP,fill=NONE,expand=FALSE)

top.mainloop
