from tkinter import*

#initialization 
win = Tk()

#input
Label(win,text="Equation -> ").grid(row=0,column=0)
a = Entry(win,width=5)
a.grid(row=0,column=12)
Label(win,text="x^2 +").grid(row=0,column=18)
b = Entry(win,width=5)
b.grid(row=0,column=24)
Label(win,text="x +").grid(row=0,column=30)
c = Entry(win,width=5)
c.grid(row=0,column=34)
Label(win,text=" = 0").grid(row=0,column=40)

#output
output =Entry(win,width=40,)
output.grid(row=2)
output1 =Entry(win,width=40,)
output1.grid(row=3)

def cal():
    output.delete(0,END)
    output1.delete(0,END)
    # #calculation
    x1=(a.get())
    x2=(b.get())
    x3=(c.get()) 
    eq = [int(x1),int(x2),int(x3)]
    D = pow(eq[1],2) - (4*eq[0]*eq[2])
    if(D>0):
        x1 = (-eq[1] + pow(D,0.5))/(2*eq[0])
        x2 = (-eq[1] - pow(D,0.5))/(2*eq[0])
        output.insert(0, ("x1 =" + str(x1) + "\n"))
        output1.insert(0, ("x2 =" + str(x2) + "\n"))
    elif(D==0):
        x = -eq[1]/(2*eq[0])
        output.insert(0,"only one value")
        output1.insert(0, ("x ="+str(x)))
    elif(D<0):
        al = -eq[1]
        bi = -D
        output.insert(0,("x1 = " + str(al) + " + i(" + str(bi) + "^(1/2))"))
        output1.insert(0,("x1 = " + str(al) + " - i(" + str(bi) + "^(1/2))"))

   

Button(win,text="calculate",command=cal).grid(row=1)

win.mainloop()