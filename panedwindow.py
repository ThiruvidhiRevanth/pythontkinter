from tkinter import *
def add():
  a=int(e1.get())
  b=int(e2.get())
  leftdata=str(a+b)
  left.insert(1,leftdata)
w1=PanedWindow()
w1.pack(fill=BOTH,expand=Y)
left=Entry(w1,border=5)
w2=PanedWindow(w1,orient=VERTICAL)
w1.add(w2)
e1=Entry(w2)
e2=Entry(w2)
w2.add(e1)
w2.add(e2)
bt=Button(w2,text="add",command=add)
w2.add(bt)
mainloop()

