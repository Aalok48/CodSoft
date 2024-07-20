from tkinter import *
from tkinter import messagebox as tmsg
import random

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

def generate_password(length):
    # Define a list of characters that can be used in the password
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+"

    # Generate a random sequence of characters from the list with the desired length
    password = ""
    for i in range(length):
        password += random.choice(chars)

    return password

def generate():
    length = entry1.get()
    if not length:
        tmsg.showerror("Error", "Please enter some numeric value")
    elif length.isalpha():
        tmsg.showerror("Error", "Please enter a digit")
    elif not (8 <= int(length) <= 18):
        tmsg.showerror("Error", "Password length must be between 8 and 18 characters")
    else:
        x = generate_password(int(length))
        root1 = Tk()
        root1.geometry("150x150")
        root1.title("Password")
        label2 = Label(root1, text=x, font="comics 12")
        label2.place(x=10, y=5)

        def ok():
            root1.destroy()
            Button(root1, text="OK", command=ok).place(x=60, y=55)
            root1.mainloop()

Button(root, text="Generate", font="comics 12", command=generate).place(x=180, y=400)

root.mainloop()