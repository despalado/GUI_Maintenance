from tkinter import *
from tkinter import messagebox
from datetime import datetime
from tkinter import ttk

import csv
# database #
from db_maintenance import *

def writecsv(recod_list):
    with open('data.csv', 'a', newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(recod_list)

GUI = Tk()

GUI.title('Customer Service Management System')
GUI.geometry('800x500+50+50')
####FONT#####
FONT1 = ('Angsana New',20)
FONT2 = ('Angsana New',15)

# add tab
Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)
Tab.add(T1,text='Service Order')
Tab.add(T2,text='Service History')
Tab.add(T3,text='Summary')
Tab.pack(fill=BOTH,expand=1)


#############
L = Label(T1,text='Service ID',font=FONT1)
L.place(x=80,y=10)

#-------------
L = Label(T1,text='Customer Name',font=FONT2)
L.place(x=30,y=50)
v_custname = StringVar()
E1 = ttk.Entry(T1,textvariable=v_custname,font=FONT2)
E1.place(x=150,y=50)

#-------------
L = Label(T1,text='Site Name',font=FONT2)
L.place(x=30,y=100)
v_sitename = StringVar()
E2= ttk.Entry(T1,textvariable=v_sitename,font=FONT2)
E2.place(x=150,y=100)
#-------------
L = Label(T1,text='System/Model',font=FONT2)
L.place(x=30,y=150)
v_system = StringVar()
E3 = ttk.Entry(T1,textvariable=v_system,font=FONT2)
E3.place(x=150,y=150)
#-------------
L = Label(T1,text='Description',font=FONT2)
L.place(x=30,y=200)
v_description = StringVar()
E4 = ttk.Entry(T1,textvariable=v_description,font=FONT2)
E4.place(x=150,y=200)
#-------------
L = Label(T1,text='Serial/Model',font=FONT2)
L.place(x=30,y=250)
v_serial = StringVar()
E5 = ttk.Entry(T1,textvariable=v_serial,font=FONT2)
E5.place(x=150,y=250)
#-------------
L = Label(T1,text='Contact Number',font=FONT2)
L.place(x=30,y=300)
v_phonenumber = StringVar()
E6 = ttk.Entry(T1,textvariable=v_phonenumber,font=FONT2)
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
    #generate tsid
    tsid =str(int(datetime.now().strftime('%Y%m%d%H%M%S')) + 11415214765)
    insert_caseorder(tsid,contactname,sitename,system,description,serial,phonenumber)
    #Clear ข้อมูลเก่า
    v_custname.set('')
    v_sitename.set('')
    v_system.set('')
    v_description.set('')
    v_serial.set('')
    v_phonenumber.set('')
    update_table()
    messagebox.showinfo('Save','Save Successfully')

B = Button(T1,text='Save',font=FONT2, command=Save)
B.place(x=200,y=350)

##tap2
header = ['System ID','Contactname','Sitename','System','Description','Serial','Phonenumber','Status']
headerwidth = [100,100,100,150,200,100,100,]

mtworkorderlist = ttk.Treeview(T2,columns=header,show='headings',height=10)
mtworkorderlist.pack()

mtworkorderlist.column('System ID',anchor='e')

for h,w in zip(header,headerwidth):
    mtworkorderlist.heading(h,text=h)
    mtworkorderlist.column(h,width=w,anchor='center')

def update_table():
    #clear data
    mtworkorderlist.delete(*mtworkorderlist.get_children())
    data = view_caseorder()
    for d in data:
        d= list(d)
        del d[0]
        mtworkorderlist.insert('','end',value=d)


#Start up 
update_table()

GUI.mainloop()
