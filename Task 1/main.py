from tkinter import *
from openpyxl import Workbook, load_workbook

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
    # this clears the existing widgets and buttons from the main page
    for widget in root.winfo_children():
        widget.destroy()

    root.geometry('700x300')

    # welcome frame for the add list
    create_welcome_frame = Frame(root, width=375, height=75)
    create_welcome_frame.pack(pady=35)

    # text lable for the add list
    create_welcome_text = Label(create_welcome_frame, text='Add your to-do items', font=35)
    create_welcome_text.place(x=85,y=35)

    # frame where all the text options and save button
    create_menu_frame = Frame(root, width=375, height=275)
    create_menu_frame.pack(pady=0)

    # area for the set_to_do
    set_to_do = Label(create_menu_frame, width=30, height=10, font=10, text='Set-To-Do')
    set_to_do.pack()

    # main text area for the add list
    entry1 = Text(create_menu_frame, width=25, height=5, borderwidth=2, font=10)
    entry1.pack()

    # relatively smaller text area for the category
    category = Entry(create_menu_frame, width=10, font=10, borderwidth=2)
    category.pack(pady=15)

    # function is called when the save button is clicked
    def save_items():
        to_do_entry = entry1.get('1.0', END)
        to_do_category = category.get()

        try:
        # Try to load the existing workbook
            wb = load_workbook('to_do_list.xlsx')
            sheet = wb.active
        except FileNotFoundError:
        # If the file doesn't exist, create a new workbook
            wb = Workbook()
            sheet = wb.active
            sheet.title = "To-Do List"
            sheet['A1'] = 'Task'
            sheet['B1'] = 'Category'
            sheet['C1'] = 'is_todo'

    # Get the last row number
        last_row = sheet.max_row

    # Write data to the next available row
        sheet.cell(row=last_row + 1, column=1).value = to_do_entry
        sheet.cell(row=last_row + 1, column=2).value = to_do_category
        sheet.cell(row=last_row + 1, column=3).value = True

        wb.save('to_do_list.xlsx')
        

    save_button = Button(create_menu_frame, text='Save', command=save_items, width=15, relief=GROOVE)
    save_button.pack()
    

# this is update function
def update():
    print('Update button clicked')

# this is track function
def track():
    print('Track button clicked')

# three button namingly create, update and track button are made
# this is create button
button1 = Button(options_frame, text='Create', width=15, borderwidth=1, command=create, font=1)
button1.place(x=105, y=45)

# this is update button
button2 = Button(options_frame, text='Update', width=15, borderwidth=1, command=update, font=1)
button2.place(x=105, y=115)

# this is track button
button3 = Button(options_frame, text='Track', width=15, borderwidth=1, command=track, font=1)
button3.place(x=105, y=185)

root.mainloop()