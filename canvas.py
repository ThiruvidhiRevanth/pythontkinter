from tkinter import*
top=Tk()
top.geometry("500x500")
c=Canvas(top,bg="pink")
arc=c.create_arc((15,100,150,200),start=0,extent=150,fill="white")
circle =c.create_oval((20,10,60,150),fill="white")

c.pack()
top.mainloop()
