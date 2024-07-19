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

root.mainloop()