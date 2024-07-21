from tkinter import *
from tkinter import messagebox as tmsg

root = Tk()
root.geometry("400x450")
root.resizable(False, False)
root.title("Contact Management System")
root.iconbitmap("D:\CodSoft\Task 5\Photos\contact.ico")

# frame for the "Welcome to contact management" text
main_frame = Frame(root, width=370, height=100, bg="red")
main_frame.place(x=45, y=30)
# label for the text "Welcome to contact management"
l1 = Label(main_frame, text="Welcome to Contact Management", font='comics 15')
l1.pack(anchor="center")

# frame for all the buttons
button_frame = Frame(root, width=350, height=300)
button_frame.place(x=55, y=105)

def add():
    pass

def delete():
    pass

def edit():
    pass

def view():
    pass

def search():
    pass

# creating first button named add a contact
b1 = Button(button_frame, text="1. Add a contact", command=add, borderwidth=0, font="15")
b1.pack(fill=X)

# creating second button named delete a contact
b2 = Button(button_frame, text="     2. Delete a Contact", command=delete, borderwidth=0, font=15)
b2.pack(fill=X, pady=5)

# creating third button named edit a contact
b3 = Button(button_frame, text="3. Edit a contact", command=edit, borderwidth=0, font=15)
b3.pack(pady=2)

# creating forth button named see all contacts
b4 = Button(button_frame, text="     4. View all contacts", borderwidth=0, command=view, font=15)
b4.pack(pady=5)

# creating fifth button named search contacts
b5 = Button(button_frame, text="     5. Search a contact", command=search, borderwidth=0, font="15")
b5.pack(pady=5)

root.mainloop()