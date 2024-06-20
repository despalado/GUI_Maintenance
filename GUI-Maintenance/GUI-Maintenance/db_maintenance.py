import sqlite3

conn = sqlite3.connect('service.sqlite3')
c = conn.cursor() # สร้างตัวชี้ cursor ให้กับ conn
c.execute(""" CREATE TABLE IF NOT EXISTS caseorder (
          ID INTEGER PRIMARY KEY AUTOINCREMENT,
          tsid INTEGER,
          contractname TEXT,
          sitename TEXT,
          system TEXT,
          description TEXT,
          seriral TEXT,
          phonenumber TEXT) """)

def insert_caseorder(tsid,contractname,sitename,system,description,seriral,phonenumber):
    
    with conn:
        command = 'INSERT INTO caseorder VALUES (?,?,?,?,?,?,?,?)'
        c.execute(command,(None,tsid,contractname,sitename,system,description,seriral,phonenumber)) 
    conn.commit()

def view_caseorder():
    with conn:
        command = 'SELECT * FROM caseorder'
        c.execute(command)
        result = c.fetchall()
        return result 
 
def update_caseorder(tsid,field,newvlaue):
    with conn:
        command = 'UPDATE caseorder SET {} = (?) WHERE tsid = (?)'.format(field)
        c.execute(command,(newvlaue,tsid))   
    conn.commit()

def delete_caseorder(tsid):
    with conn:
        command = 'DELETE FROM caseorder WHERE tsid = (?)'
        c.execute(command,([tsid]))
    conn.commit()
   

