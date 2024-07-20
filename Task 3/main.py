from tkinter import *

root = Tk()
root.geometry("450x550")
root.title("Password Generator")
root.resizable(False, False)
root.iconbitmap("D:\CodSoft\Task 3\Photos\icon.ico")

img = PhotoImage(file=r"D:\CodSoft\Task 3\Photos\img3.gif")
label1 = Label(root, width=300, height=300, image=img, bd=0)
label1.place(x=75, y=0, anchor="nw")

Label(root, text="Enter length of password:", font="comics 12").place(x=20, y=325)
entry1 = Entry(root, width=20, font="comics 12", borderwidth=2, border=3)
entry1.place(x=210, y=325)

def generate():
    pass

Button(root, text="Generate", font="comics 12", command=generate).place(x=180, y=400)

root.mainloop()