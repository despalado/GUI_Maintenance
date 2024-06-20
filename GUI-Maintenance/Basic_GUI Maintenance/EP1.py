from tkinter import *
from tkinter import messagebox

import csv
from datetime import datetime

def writecsv(recod_list):
    with open('data.csv', 'a', newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(recod_list)

GUI = Tk()

GUI.title('Customer Service Management System')
GUI.geometry('500x500+50+50')
####FONT#####
FONT1 = ('Angsana New',20)
FONT2 = ('Angsana New',15)

#############
L = Label(GUI,text='Service Record',font=FONT1)
L.pack()

#-------------
L = Label(GUI,text='Customer Name',font=FONT2)
L.place(x=30,y=50)
v_custname = StringVar()
E1 = Entry(GUI,textvariable=v_custname,font=FONT2)
E1.place(x=150,y=50)

#-------------
L = Label(GUI,text='Site Name',font=FONT2)
L.place(x=30,y=100)
v_sitename = StringVar()
E2= Entry(GUI,textvariable=v_sitename,font=FONT2)
E2.place(x=150,y=100)
#-------------
L = Label(GUI,text='System/Model',font=FONT2)
L.place(x=30,y=150)
v_system = StringVar()
E3 = Entry(GUI,textvariable=v_system,font=FONT2)
E3.place(x=150,y=150)
#-------------
L = Label(GUI,text='Description',font=FONT2)
L.place(x=30,y=200)
v_description = StringVar()
E4 = Entry(GUI,textvariable=v_description,font=FONT2)
E4.place(x=150,y=200)
#-------------
L = Label(GUI,text='Serial/Model',font=FONT2)
L.place(x=30,y=250)
v_serial = StringVar()
E5 = Entry(GUI,textvariable=v_serial,font=FONT2)
E5.place(x=150,y=250)
#-------------
L = Label(GUI,text='Contact Number',font=FONT2)
L.place(x=30,y=300)
v_phonenumber = StringVar()
E6 = Entry(GUI,textvariable=v_phonenumber,font=FONT2)
E6.place(x=150,y=300)

def Save():
    contactname = v_custname.get() #.get() คือ ให้แสดงผลออกมา จาก v_contactname หรือ stringvar
    sitename = v_sitename.get()
    system = v_system.get()
    description = v_description.get()
    serial = v_serial.get()
    phonenumber = v_phonenumber.get()

    text ='Customer Name:' + contactname + '\n'
    text += 'Site Name:' + sitename + '\n'
    text += 'System/Model:' + system + '\n'
    text += 'Description:' + description + '\n'
    text += 'Serial:' + serial + '\n'
    text += 'Contact Number:' + phonenumber + '\n'
    
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    datalist = [dt,contactname,sitename,system,description,serial,phonenumber]
    writecsv(datalist)
    # messagebox.showinfo('Save Succesful',text)
    messagebox.showinfo('Save Succesful',text)
    

B = Button(GUI,text='Save',font=FONT2, command=Save)
B.place(x=200,y=350)

# L.pack()
# L.grid(row=1,column=1)
# L.place(x=20,y=100)
GUI.mainloop()
