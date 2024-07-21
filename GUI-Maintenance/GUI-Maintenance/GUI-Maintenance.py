from tkinter import *
from tkinter import messagebox
from datetime import datetime
from tkinter import ttk
import csv
# database #
from db_maintenance import *
from allpage import *

def writecsv(recod_list):
    with open('data.csv', 'a', newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(recod_list)

GUI = Tk()

GUI.title('Customer Service Management System')

w = 1400
h = 600
ws = GUI.winfo_screenwidth()
hs = GUI.winfo_screenheight()
x= (ws/2) - (w/2)
y= (hs/2) - (h/2)
GUI.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}')

def center_windows(w,h):
    ws = GUI.winfo_screenwidth()
    hs = GUI.winfo_screenheight()
    x= (ws/2) - (w/2)
    y= (hs/2) - (h/2)
    return f'{w}x{h}+{x:.0f}+{y:.0f}'
    


####FONT#####
FONT1 = ('Angsana New',12)
FONT2 = ('Angsana New',12)

# add tab
 #style
#s = ttk.Style()
#s.theme_create('MyStyle',parent='alt',settings={
    #'TNotebook.Tab':{'configure':{'padding':[10, 10],'font':(None,11)}}
#})
#s.theme_use('MyStyle')

Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)
T4 = Frame(Tab)
Tab.add(T1,text=f"{' '*5}Main Menu{' '*5}")
Tab.add(T2,text='Service History')
Tab.add(T3,text='Approve Service')
Tab.add(T4,text='Service Completed')
Tab.pack(fill=BOTH,expand=1)

### Menu Bar ###
menubar = Menu(GUI)
GUI.config(menu=menubar)

# File Menu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Sync Data')
filemenu.add_command(label='Update Database')

sub_menu = Menu(filemenu,tearoff=0)
sub_menu.add_cascade(label='config database')
sub_menu.add_command(label='config report')

filemenu.add_cascade(label='Config',menu=sub_menu)

filemenu.add_separator()
filemenu.add_command(label='Exit',accelerator='Ctrl+Q',command=lambda: GUI.quit())

GUI.bind('<Control-q>',lambda x: GUI.quit())

helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About')
helpmenu.add_command(label='Manual')
helpmenu.add_command(label='Software Version')
helpmenu.add_command(label='Contact')


######################### General class ############################

class MenuText(ttk.Label):
    def __init__(self,GUI,text='example',size=20):
        ttk.Label.__init__(self,GUI,text=text,font=('Angsana New',size,'bold'),foreground = 'black')

###### Class entry text ######
class ET(Frame):
    def __init__(self,GUI,label,textvariable):
        Frame.__init__(self,GUI,width=500,height=300)
        L = Label(self,text=label,font=FONT2)
        L.place(x=10,y=50)
        self.E1 = ttk.Entry(self,textvariable=textvariable,font=FONT2)
        self.E1.place(x=130,y=50)

#########################

def update_table():
    #clear data
    mtworkorderlist.delete(*mtworkorderlist.get_children())
    # data = view_caseorder() EP1 ดึงข้อมูลทั้งหมด
    data = view_caseorder_status(status='new') # ขั้นตอนนี้ สร้างจาก EP3 อัพเดทข้อมูลเฉพาะที่ เป็นืstatus new
    for d in data:
        d= list(d)
        del d[0]
        mtworkorderlist.insert('','end',value=d)
######################### Function cal new GUI2 when click Menu Workorder ############################
def WindowWorkorder():
    GUI2 = Toplevel()
    win_size = center_windows(500,500)
    GUI2.geometry(win_size)
    GUI2.title('Workorder')
    
    F1 = WorkOrder(GUI2,insert_caseorder,update_table) #insert_caseorder คือ function ทีมาจาก db_maintenance.py
    F1.pack()
    GUI2.mainloop()

FBM1 = Frame(T1)
FBM1.place(x=50,y=50)
icon_bm1 = PhotoImage(file='icon_list.png')
BM1 = Button(FBM1, text='Workorder', image=icon_bm1, compound='top', bg=T1.cget("background"),
             command=WindowWorkorder, borderwidth=0, highlightthickness=0)
BM1.pack(ipadx=50, ipady=20)

######################### Function department ############################
def WindowDepartment():
    GUI2 = Toplevel()
    win_size = center_windows(500,500)
    GUI2.geometry(win_size)
    GUI2.title('Department')

    L = MenuText(GUI2,text='Department',size=15)
    L.pack()
    v_dep_code = StringVar()
    E1 = ET(GUI2,label='Department Code',textvariable=v_dep_code)
    E1.place(x=40,y=25)

    v_dep_title = StringVar()
    E2 = ET(GUI2,label='Department Title',textvariable=v_dep_title)
    E2.place(x=40,y=140)

    def SaveDep():
        dep_code = v_dep_code.get().strip()
        dep_title = v_dep_title.get().strip()
        if dep_code == '' or dep_title == '':
            messagebox.showwarning('Warning','Please fill all information')
        else:
            insert_department(dep_code,dep_title)
            v_dep_code.set('')
            v_dep_title.set('')
            E1.E1.focus()
            messagebox.showinfo('Save','Save Successfully')
            GUI2.destroy()
    
    B = ttk.Button(GUI2,text='Save',command=SaveDep)
    B.place(x=250,y=250)



    


    GUI2.mainloop()




FBM1 = Frame(T1)
FBM1.place(x=250,y=50)
icon_bm2 = PhotoImage(file='icon_department.png')
BM2 = Button(FBM1, text='Department', image=icon_bm2, compound='top', bg=T1.cget("background"),command = WindowDepartment, 
             borderwidth=0, highlightthickness=0)
BM2.pack(ipadx=50, ipady=20)

##########################TAP2############################################
header = ['Case ID','Contactname','Sitename','System','Description','Serial','Phonenumber','Status']
headerwidth = [100,150,150,150,200,100,100,100]

mtworkorderlist = ttk.Treeview(T2,columns=header,show='headings',height=10)
mtworkorderlist.pack()

#set font and table 
style = ttk.Style()
style.configure('Treeview.Heading',padding=5,font=FONT1,)
style.configure('Treeview',rowheight=30,font=FONT1)

mtworkorderlist.column('Case ID',anchor='e')

for h,w in zip(header,headerwidth):
    mtworkorderlist.heading(h,text=h)
    mtworkorderlist.column(h,width=w,anchor='center')

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

# Right click menu
def approved():
    selected = mtworkorderlist.selection()
    output = mtworkorderlist.item(selected)
    tisd = output['values'][0]
    # print('Approved:',tisd)
    update_caseorder(tisd,'status','Approved')
    update_table()
    update_table_approve()# update table ที่ approve แล้ว

approved_menu = Menu(GUI,tearoff=0)
approved_menu.add_command(label='Approved',command=approved)
approved_menu.add_command(label='Delete',command=delete_mtworkorder)

#futher pop up macos
def popup(event):
    approved_menu.post(event.x_root,event.y_root)

mtworkorderlist.bind('<Button-2>',popup)   #macOS การเปิด pop up menu ด้วยการคลิกขวา 

# tap3 
class WorkorderList(ttk.Treeview):
    def __init__(self,GUI,):
        header = ['Case ID','Contactname','Sitename','System','Description','Serial','Phonenumber','Status']
        headerwidth = [100,150,150,150,200,100,100,100]
        ttk.Treeview.__init__(self,GUI,columns=header,show='headings',height=10)
        for h,w in zip(header,headerwidth):
            self.heading(h,text=h)
            self.column(h,width=w,anchor='center')
    
    #insert data to table
    def insert_data(self,values):
        self.insert('','end',values=values)


#Table of Approve Service
L = Label(T3,text='Appove Service',font=FONT1)
L.pack()

approved_wlist = WorkorderList(T3)
approved_wlist.pack()

# update_table + name of table = function for update that table. 
def update_table_approve():
    #clear data
    approved_wlist.delete(*approved_wlist.get_children()) #get_children() คือการclearข้อมูลทั้งหมดออกไป
    data = view_caseorder_status(status ='Approved')
    for d in data:
        d= list(d) # แปลงข้อมูล tuple ให้เป็น list
        del d[0] # ลบID จาก database ออก
        approved_wlist.insert('','end',values=d)

#### Create Note GUI when duble click tsid ####
from tkcalendar import *
def newnote(event):
    GUI3 = Toplevel()
    GUI3.title('Service Note')
    GUI3.geometry('500x500')

    selected = approved_wlist.selection()
    output = approved_wlist.item(selected)
    tsid = output['values'][0]
    
    L = ttk.Label(GUI3,text='Service Note (tsid: {})'.format(tsid),font=FONT2)
    L.pack(pady=10)

    L = ttk.Label(GUI3,text='Date Start',font=FONT2)
    L.pack(pady=10)
    #E1 = ttk.Entry(GUI3,textvariable=v_date_start,font=FONT2)
    #E1.pack()
    cal = DateEntry(GUI3,width=12, foreground='white',borderwidth=3,year=2024,date_pattern='dd/MM/yyyy')
    cal.pack(pady=10, padx=10)

    L = ttk.Label(GUI3,text='Detail',font=FONT2)
    L.pack(pady=10)
    E2 = Text(GUI3,font=FONT2,width=50,height=4)
    E2.pack()

    L = ttk.Label(GUI3,text='Other',font=FONT2)
    L.pack(pady=10)
    E3 = Text(GUI3,font=FONT2,width=50,height=5)
    E3.pack()

    # getdata from ntnote
    data = view_mt_note_tsid(tsid)
    print(data)

    
    if data != None: #รายการที่ไม่มีมาก่อน
        cal.set_date(data[2])
        E2.insert(END,data[3])
        E3.insert(END,data[4])

    # function save detail
    def Savedetail():
        date_start = cal.get()
        detail =E2.get('1.0',END).strip() #1.0 คือบรรทัดแรก ถึงสุดท้าย and strip คือการตัด /n ออก 
        other = E3.get('1.0',END).strip()
        #edit note
        if data == None:
            insert_mt_note(tsid,date_start,detail,other)
        else:
            update_mt_note(tsid,'date_start',date_start)
            update_mt_note(tsid,'detail',detail)
            update_mt_note(tsid,'other',other)
        GUI3.destroy()

    B = ttk.Button(GUI3,text='Save', command=Savedetail)
    B.pack(pady=10)

   
    GUI.mainloop()

approved_wlist.bind('<Double-1>',newnote)

# Right click menu - detail and approve ###
def done():
    selected = approved_wlist.selection()
    output = approved_wlist.item(selected)
    tisd = output['values'][0]
    # print('Approved:',tisd)
    update_caseorder(tisd,'status','Completed')
    update_table()
    update_table_approve()# update table ที่ approve แล้ว
    update_table_done()
    # update new table tap 4

done_menu = Menu(GUI,tearoff=0)
done_menu.add_command(label='Completed',command=done)

#futher pop up macos
def popup(event):
    done_menu.post(event.x_root,event.y_root)

approved_wlist.bind('<Button-2>',popup)   #macOS การเปิด pop up menu ด้วยการคลิกขวา

### Tap 4

#Table of Approve Service
L = Label(T4,text='Complete Service',font=FONT1)
L.pack()

done_wlist = WorkorderList(T4)
done_wlist.pack()

# update_table + name of table = function for update that table. 
def update_table_done():
    #clear data
    done_wlist.delete(*done_wlist.get_children()) #get_children() คือการclearข้อมูลทั้งหมดออกไป
    data = view_caseorder_status(status ='Completed')
    for d in data:
        d= list(d) # แปลงข้อมูล tuple ให้เป็น list
        del d[0] # ลบID จาก database ออก
        done_wlist.insert('','end',values=d)# สามรถเพิ่มข้อมูลเข้าไปใน table ได้

#Start up 
update_table()
update_table_approve()
update_table_done()
GUI.mainloop()
