from tkinter import *
top=Tk()
top.geometry("500x500")
r1=Radiobutton(top,text="c++",value=1)
r1.place(x=50,y=70)

r2=Radiobutton(top,text="java",value=2)
r2.place(x=50,y=100)

r3=Radiobutton(top,text="python",value=3)
r3.place(x=50,y=130)
top.mainloop()


