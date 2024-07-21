from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

FONT1 = ('Angsana New',12)
FONT2 = ('Angsana New',12)

class WorkOrder(Frame):
    
    def __init__(self, GUI,insert_caseorder,update_table):
        Frame.__init__(self, GUI, width=500, height=400)

        #############
        L = ttk.Label(self, text='WorkOrder', font=FONT1)
        L.place(x=80,y=10)

        #-------------
        L = Label(self,text='Customer Name',font=FONT2)
        L.place(x=30,y=50)
        v_custname = StringVar()
        E1 = ttk.Entry(self,textvariable=v_custname,font=FONT2)
        E1.place(x=150,y=50)
        E1.bind('<Return>',lambda x: E2.focus()) # การใช้ bind คือการเชื่อมโยงระหว่างเหตุการณ์กับฟังก์ชัน
        #-------------
        L = Label(self,text='Site Name',font=FONT2)
        L.place(x=30,y=100)
        v_sitename = StringVar()
        E2= ttk.Entry(self,textvariable=v_sitename,font=FONT2)
        E2.place(x=150,y=100)
        E2.bind('<Return>',lambda x: E3.focus())
        #-------------
        L = Label(self,text='System/Model',font=FONT2)
        L.place(x=30,y=150)
        v_system = StringVar()
        E3 = ttk.Entry(self,textvariable=v_system,font=FONT2)
        E3.place(x=150,y=150)
        E3.bind('<Return>',lambda x: E4.focus())
        #-------------
        L = Label(self,text='Description',font=FONT2)
        L.place(x=30,y=200)
        v_description = StringVar()
        E4 = ttk.Entry(self,textvariable=v_description,font=FONT2)
        E4.place(x=150,y=200)
        E4.bind('<Return>',lambda x: E5.focus())
        #-------------
        L = Label(self,text='Serial/Model',font=FONT2)
        L.place(x=30,y=250)
        v_serial = StringVar()
        E5 = ttk.Entry(self,textvariable=v_serial,font=FONT2)
        E5.place(x=150,y=250)
        E5.bind('<Return>',lambda x: E6.focus())
        #-------------
        L = Label(self,text='Contact Number',font=FONT2)
        L.place(x=30,y=300)
        v_phonenumber = StringVar()
        E6 = ttk.Entry(self,textvariable=v_phonenumber,font=FONT2)
        E6.place(x=150,y=300)
        E6.bind('<Return>',lambda x: Save())

        def Save(event=None):
            contactname = v_custname.get().strip() #.get() คือ ให้แสดงผลออกมา จาก v_contactname หรือ stringvar
            sitename = v_sitename.get().strip()
            system = v_system.get().strip()
            description = v_description.get().strip()
            serial = v_serial.get().strip()
            phonenumber = v_phonenumber.get().strip()
            if contactname == '' or sitename == '' or system == '' or description == '' or serial == '' or phonenumber == '':
                messagebox.showwarning('Error','Please fill all information')
                return

            text =f'Customer Name:' + contactname + '\n'
            text += f'Site Name:' + sitename + '\n'
            text += f'System/Model:' + system + '\n'
            text += f'Description:' + description + '\n'
            text += f'Serial:' + serial + '\n'
            text += f'Contact Number:' + phonenumber + '\n'
            
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
            E1.focus()

        B = Button(self,text='Save',font=FONT2, command=Save)
        B.place(x=200,y=350)