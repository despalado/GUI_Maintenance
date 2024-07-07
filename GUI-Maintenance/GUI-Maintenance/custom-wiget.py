from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('500x500')

class WorkorderList(ttk.Treeview):
    def __init__(self,GUI,):
        header = ['System ID','Contactname','Sitename','System','Description','Serial','Phonenumber','Status']
        headerwidth = [100,150,150,150,200,100,100,100]
        ttk.Treeview.__init__(self,GUI,columns=header,show='headings',height=10)
        for h,w in zip(header,headerwidth):
            self.heading(h,text=h)
            self.column(h,width=w,anchor='center')
    
    #insert data to table
    def insert_data(self,values):
        self.insert('','end',values=values)

# t = WorkorderList(GUI)
# t.place(x=50,y=50)
# t.insert('','end',values=['1','2','3','4','5','6','7','8'])

GUI.mainloop()

