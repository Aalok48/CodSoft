from tkinter import *

root = Tk()                                                     # creating the root for tkinter
root.geometry("375x500")                                        # defining the geometry for the tkinter window
root.resizable(False, False)                                    # making the tkinter window not resizable
root.title("To-Do List")                                        # title for the tkinter
root.iconbitmap("D:\CodSoft\Task 1\photos\download1.ico")       # specifying the icon for the tkinter

# welcome frame for the welcome text
welcome_label_frame = Frame(root, width=375, height=60)
welcome_label_frame.pack(pady=35)

# lable for the welcome frame 
welcome_label = Label(welcome_label_frame, text="Welcome to TO-DO List", font=35)
welcome_label.pack()

# main frame that contains the create, update and track options
options_frame = Frame(root, width=375, height=275)
options_frame.place(x=0, y=125)

# function part
# this is create funtion
def create():
    print("Create button clicked")

# this is update function
def update():
    print('Update button clicked')

# this is track function
def track():
    print('Track button clicked')

# three button namingly create, update and track button are made
# this is create button
button1 = Button(options_frame, text='Create', width=15, borderwidth=1, command=create)
button1.place(x=135, y=45)

# this is update button
button2 = Button(options_frame, text='Update', width=15, borderwidth=1, command=update)
button2.place(x=135, y=95)

# this is track button
button3 = Button(options_frame, text='Track', width=15, borderwidth=1, command=track)
button3.place(x=135, y=145)

root.mainloop()