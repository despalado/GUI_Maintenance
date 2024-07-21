from tkinter import *
from tkinter import ttk

# Function to open Workorder window
def WindowWorkorder():
    GUI2 = Toplevel()
    GUI2.title('Workorder')
    GUI2.geometry('500x500')
    #F1 = WorkOrder(GUI2, insert_caseorder, update_table)  # insert_caseorder and update_table from db_maintenance.py
    #F1.pack()
    GUI2.mainloop()

# Create the main window and frame
root = Tk()
root.title("Customer Service Management System")
root.geometry("600x400")  # Adjust the window size as needed

T1 = Frame(root)
T1.pack(fill=BOTH, expand=True)

# Create the icon menu button for Workorder using Label
FBM1 = Frame(T1)
FBM1.place(x=50, y=50)
icon_bm1 = PhotoImage(file='list-box.png')  # Adjust the file path as needed
BM1 = Label(FBM1, text='Workorder', image=icon_bm1, compound='top', bg=T1.cget("background"))
BM1.pack(ipadx=50, ipady=20)

# Bind the click event to the label to act like a button
#BM1.bind("<Button-1>", lambda e: WindowWorkorder())

root.mainloop()