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
GUI.geometry('1000x500+50+50')
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
headerwidth = [100,150,150,150,200,100,100,]

mtworkorderlist = ttk.Treeview(T2,columns=header,show='headings',height=10)
mtworkorderlist.pack()

#set font and table 
style = ttk.Style()
style.configure('Treeview.Heading',padding=5,font=FONT1,)
style.configure('Treeview',rowheight=30,font=FONT1)

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

##function edit data##
edit_window_open = False

def EditPage_mtworkorder(event=None):
    global edit_window_open
    if edit_window_open:
        return
    #get data
    selected = mtworkorderlist.selection()
    if not selected:
        messagebox.showerror('Error','No record selected')
        return
    
    output = mtworkorderlist.item(selected)
    op = output['values']
    if not op:
        return

    tsid = op[0]
    t_contactname = op[1]
    t_sitename = op[2]
    t_system = op[3]
    t_description = op[4]
    t_serial = op[5]
    t_phonenumber = op[6] #'0{}'.formate(op[6])

    #open edit page. 

    GUI2 = Toplevel()
    GUI2.title('Edit Data')
    GUI2.geometry('500x500')

    def on_close():
        global edit_window_open
        edit_window_open = False
        GUI2.destroy()
    
    GUI2.protocol('WM_DELETE_WINDOW',on_close)

        #############
    L = Label(GUI2,text='Service ID',font=FONT1)
    L.place(x=80,y=10)

    #-------------
    L = Label(GUI2,text='Customer Name',font=FONT2)
    L.place(x=30,y=50)
    v_custname2 = StringVar()
    v_custname2.set(t_contactname)
    E1 = ttk.Entry(GUI2,textvariable=v_custname2,font=FONT2)
    E1.place(x=150,y=50)

    #-------------
    L = Label(GUI2,text='Site Name',font=FONT2)
    L.place(x=30,y=100)
    v_sitename2 = StringVar()
    v_sitename2.set(t_sitename)
    E2= ttk.Entry(GUI2,textvariable=v_sitename2,font=FONT2)
    E2.place(x=150,y=100)
    #-------------
    L = Label(GUI2,text='System/Model',font=FONT2)
    L.place(x=30,y=150)
    v_system2 = StringVar()
    v_system2.set(t_system)
    E3 = ttk.Entry(GUI2,textvariable=v_system2,font=FONT2)
    E3.place(x=150,y=150)
    #-------------
    L = Label(GUI2,text='Description',font=FONT2)
    L.place(x=30,y=200)
    v_description2 = StringVar()
    v_description2.set(t_description)
    E4 = ttk.Entry(GUI2,textvariable=v_description2,font=FONT2)
    E4.place(x=150,y=200)
    #-------------
    L = Label(GUI2,text='Serial/Model',font=FONT2)
    L.place(x=30,y=250)
    v_serial2 = StringVar()
    v_serial2.set(t_serial) 
    E5 = ttk.Entry(GUI2,textvariable=v_serial2,font=FONT2)
    E5.place(x=150,y=250)
    #-------------
    L = Label(GUI2,text='Contact Number',font=FONT2)
    L.place(x=30,y=300)
    v_phonenumber2 = StringVar()
    v_phonenumber2.set("0{}".format(t_phonenumber))
    E6 = ttk.Entry(GUI2,textvariable=v_phonenumber2,font=FONT2)
    E6.place(x=150,y=300)

    def Edit():
        contactname = v_custname2.get() #.get() คือ ให้แสดงผลออกมา จาก v_contactname หรือ stringvar
        sitename = v_sitename2.get()
        system = v_system2.get()
        description = v_description2.get()
        serial = v_serial2.get()
        phonenumber = v_phonenumber2.get()
        try:
            update_caseorder(tsid,'contractname',contactname)
            update_caseorder(tsid,'sitename',sitename)
            update_caseorder(tsid,'system',system)
            update_caseorder(tsid,'description',description)
            update_caseorder(tsid,'seriral',serial)
            update_caseorder(tsid,'phonenumber',phonenumber)
            update_table()
            on_close()
            messagebox.showinfo('Update','Update Successfully')
        except Exception as e:
            messagebox.showerror('Error',str(e))

    B = Button(GUI2,text='Save',font=FONT2, command=Edit)
    B.place(x=200,y=350) 
    edit_window_open = True
    GUI2.mainloop()

mtworkorderlist.bind('<Double-1>',EditPage_mtworkorder) # การ bind คือการเชื่อมโยงระหว่างเหตุการณ์กับฟังก์ชัน

#delete data

def delete_mtworkorder(event=None):
    selected = mtworkorderlist.selection()
    if not selected:
        messagebox.showerror('Error','No record selected')
        return
    
    output = mtworkorderlist.item(selected)
    tsid = output['values'][0]

    check = messagebox.askyesno('Confirm','Do you want to delete this record?')
    if check == True:
        delete_caseorder(tsid)
        update_table()

    #delete_caseorder(tsid)
# assign function to button delete for Mac OS 
mtworkorderlist.bind('<Return>',delete_mtworkorder) 

#Start up 
update_table()

GUI.mainloop()
