from tkinter import *
from random import randint

win = Tk()

def new_rand():
    passentry.delete(0,END)
    passlenght = int(myentry.get())
    mypas = ''
    for i in range(passlenght):
        mypas += chr(randint(33,126))

    passentry.insert(0,mypas)

def reset():
    myentry.delete(0,END)
    passentry.delete(0,END)

Label(win,text="PASSWORD GENERATOR....",font=("helvetica",30),fg=("blue")).pack()

lf = LabelFrame(win,text="Lenght of password",font=("helvetica",20))
lf.pack(pady=20)

myentry = Entry(lf,font=("helvetica",24))
myentry.pack(pady=20,padx=20)

lab = LabelFrame(win,text="Password",font=("helvetica",20))
lab.pack(pady=20)

passentry = Entry(lab, text='',font=("helvetica", 24), bg="systembuttonface",border=0)
passentry.pack(pady=20,padx=20)

myframe = Frame(win)
myframe.pack(pady=20)

grbutton = Button(myframe,text="Generate password",font=("helvetica",20),bg="#00ff00", command=new_rand)
grbutton.pack(pady=20)

rsbutton = Button(myframe,text="Reset",font=("helvetica",20),bg="red",command=reset)
rsbutton.pack(pady=10)

win.mainloop()