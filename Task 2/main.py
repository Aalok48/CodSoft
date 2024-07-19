from tkinter import *

root = Tk()
root.geometry("400x425")
root.resizable(False,False)
root.title("Calculator project")
root.iconbitmap("D:\CodSoft\Task 2\photos\download.ico") 

def click(event):
    text=event.widget.cget("text")
    if text=="=":
        if scvalue.get().isdigit():
          value = int(scvalue.get())
        else:
            value=eval(screen.get())
        scvalue.set(value)
        screen.update()
        

    elif text=="c":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvariable=scvalue,font="comicsans 25",relief='groove')
screen.pack(ipadx=10,pady=15)

#frame for buttons 9 8 7
f1=Frame(root)
for i in range(7,10):
    b=Button(f1,text="{}".format(i),padx=10,pady=8)
    b.pack(side=LEFT,padx=10)
    b.bind("<Button-1>",click)
f1.pack(pady=15)


#frame for buttons 6 5 4
f2=Frame(root)
for i in range(4,7):
    b=Button(f2,text="{}".format(i),padx=10,pady=8)
    b.pack(side=LEFT,padx=10)
    b.bind("<Button-1>",click)
f2.pack(pady=15)

#frame for buttons 3 2 1
f3=Frame(root)
for i in range(1,4):
    b=Button(f3,text="{}".format(i),padx=10,pady=8)
    b.pack(side=LEFT,padx=10)
    b.bind("<Button-1>",click)
f3.pack(pady=15)

#frame for c = and 0
f4=Frame(root)
l1=['c','=','0']
for i in range(len(l1)):
    b = Button(f4, text=l1[i],padx=10,pady=8)
    b.pack(side=LEFT,padx=10)
    b.bind("<Button-1>", click)
f4.pack(pady=15) 

#function for mathematical operatio + - /
f5=Frame(root)
l2=['+','-','/']
for i in range(len(l2)):
    b=Button(f5,text=l2[i],padx=10,pady=8)
    b.pack(side=LEFT,padx=10)
    b.bind("<Button-1>",click)
f5.pack(pady=15)

root.mainloop()