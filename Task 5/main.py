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
    root2 = Tk()
    root2.geometry("350x300")
    root2.resizable(False, False)
    root2.iconbitmap("D:\CodSoft\Task 5\Photos\contact.ico")
    root2.title("Add contact")

    # code for name label and name entry
    name = Label(root2, text="Name:", font="comics 12")
    name.place(x=35, y=50)
    name_entry = Entry(root2, width=25, relief="groove", borderwidth=5, border=5)
    name_entry.place(x=105, y=50, )

    # code for contact label and contact entry
    contact = Label(root2, text="Contact:", font="comics 12")
    contact.place(x=35, y=90)
    contact_entry = Entry(root2, width=25, relief="groove", borderwidth=5, border=5)
    contact_entry.place(x=105, y=90)

    # code for address label and address entry
    address = Label(root2, text="Address:", font="comics 12")
    address.place(x=35, y=130)
    address_entry = Entry(root2, width=25, relief="groove", border=5, borderwidth=5)
    address_entry.place(x=105, y=130)

    # code for gmail label and gmail entry
    gmail = Label(root2, text="G-mail:", font="comics 12")
    gmail.place(x=35, y=170)
    gmail_entry = Entry(root2, width=25, relief="groove", border=5, borderwidth=5)
    gmail_entry.place(x=105, y=170)

    # code for finish button
    # first stored the value entered in entry box in their respective variables and stored them in a nested dictionary
    # if the user clicks on 'yes' in messagebox then the dictionary is changed to string and then stored in the file
    def finish():
        name_text = name_entry.get()
        contact_text = contact_entry.get()
        address_text = address_entry.get()
        gmail_text = gmail_entry.get()
        data_dict = {name_text: {"contact": contact_text, "address": address_text, "gmail": gmail_text}}
        answer = tmsg.askquestion("Ready to save", "Save changes")
        if answer == 'yes':
            with open("data.txt", "a") as file:
                dict_str = str(data_dict)
                file.write(dict_str)
                file.write('\n')
                file.close()
        root2.destroy()

    # button for the finish block
    Button(root2, text="Finish", width=10, borderwidth=0, font="comics 10", command=finish).place(x=125, y=230)

    root2.mainloop()

def delete():
    root_delete = Tk()
    root_delete.title("Delete a contact")
    root_delete.geometry("200x100")
    label4 = Label(root_delete, text="Enter name: ")
    label4.place(x=10, y=20)
    del_entry = Entry(root_delete, width=15, relief="sunken")
    del_entry.place(x=85, y=20)

    # the delete function asks for the name of the contact to be deleted and stores it in the del_entry_value variable
    # the file where the data is stored is opened in read mode and the data is stored in content variable
    # a new list is created and the content variable is iterated and checked for the contact to be deleted
    # the contact that is not matched with contact to be deleted is saved to list and stored to the file
    def delete_contact():
        del_entry_value = del_entry.get()
        with open("data.txt", "r") as file:
            content = file.readlines()

        new_content = []
        for line in content:
            if del_entry_value not in line:
                new_content.append(line)

        with open("data.txt", "w") as file:
            file.writelines(new_content)
            file.close()

        root_delete.destroy()

    button_del = Button(root_delete, text="Delete", width=10, relief="groove", command=delete_contact)
    button_del.place(x=65, y=55)

    root_delete.mainloop()

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