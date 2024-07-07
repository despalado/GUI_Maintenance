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
          phonenumber TEXT,
          status TEXT ) """)
# tisd
# date_start
# detail 
# other

c.execute(""" CREATE TABLE IF NOT EXISTS mt_note( 
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                tsid TEXT, 
                date_start TEXT,
                detail TEXT,
                other TEXT ) """)


def insert_caseorder(tsid,contractname,sitename,system,description,seriral,phonenumber):
    
    with conn:
        command = 'INSERT INTO caseorder VALUES (?,?,?,?,?,?,?,?,?)'
        c.execute(command,(None,tsid,contractname,sitename,system,description,seriral,phonenumber,'new')) 
    conn.commit()

def view_caseorder():
    with conn:
        command = 'SELECT * FROM caseorder'
        c.execute(command)
        result = c.fetchall()
        return result 
    
def view_caseorder_status(status='approved'):
    with conn:
        command = 'SELECT * FROM caseorder WHERE status =(?)'
        c.execute(command,([status]))
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
   

#################  Note  #################

def insert_mt_note(tsid,date_start,detail,other):
    with conn:
        command = 'INSERT INTO mt_note VALUES (?,?,?,?,?)'
        c.execute(command,(None,tsid,date_start,detail,other))
    conn.commit()

def view_mt_note_tsid():
    with conn:
        command = 'SELECT * FROM mt_note'
        c.execute(command)
        result = c.fetchall()
    return result

def view_mt_note(tsid):
    with conn:
        command = 'SELECT * FROM mt_note WHERE tsid = (?)'
        c.execute(command,([tsid]))
        result = c.fetchone()
    return result


def update_mt_note(tsid,field,newvlaue):
    with conn:
        command = 'UPDATE mt_note SET {} = (?) WHERE tsid = (?)'.format(field)
        c.execute(command,(newvlaue,tsid))
    conn.commit()

def delete_mt_note(tsid):
    with conn:
        command = 'DELETE FROM mt_note WHERE tsid = (?)'
        c.execute(command,([tsid]))
    conn.commit()


