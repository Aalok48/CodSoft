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
button_frame.place(x=35, y=95)

root.mainloop()