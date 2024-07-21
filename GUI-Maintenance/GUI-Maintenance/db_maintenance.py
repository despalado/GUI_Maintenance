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
## Note ##
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
   

################# Table Note  #################

def insert_mt_note(tsid,date_start,detail,other):
    with conn:
        command = 'INSERT INTO mt_note VALUES (?,?,?,?,?)'
        c.execute(command,(None,tsid,date_start,detail,other))
    conn.commit()

def view_mt_note():    
    with conn:
        command = 'SELECT * FROM mt_note'
        c.execute(command)
        result = c.fetchall()
    return result

def view_mt_note_tsid(tsid):
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

### Database Department ###
c.execute(""" CREATE TABLE IF NOT EXISTS department (
          ID INTEGER PRIMARY KEY AUTOINCREMENT,
          dep_code TEXT,
          dep_title TEXT ) """)

def insert_department(dep_code,dep_title):
    with conn:
        command = 'INSERT INTO department VALUES (?,?,?)'
        c.execute(command,(None,dep_code,dep_title))
    conn.commit()

def view_department():
    with conn:
        command = 'SELECT * FROM department'
        c.execute(command)
        result = c.fetchall()
    return result

def update_department(dep_code,field,newvlaue):
    with conn:
        command = 'UPDATE department SET {} = (?) WHERE dep_code = (?)'.format(field)
        c.execute(command,(newvlaue,dep_code))
    conn.commit()

def delete_department(dep_code):
    with conn:
        command = 'DELETE FROM department WHERE dep_code = (?)'
        c.execute(command,([dep_code]))
    conn.commit()

### Machine_Equipment ###
c.execute(""" CREATE TABLE IF NOT EXISTS machine_equipment (
          ID INTEGER PRIMARY KEY AUTOINCREMENT,
          machine_code TEXT,
          machine_title TEXT,
          machine_detail TEXT,
          machine_serial TEXT,
          machine_status TEXT ) """)

def insert_machine_equipment(machine_code,machine_title,machine_detail,machine_serial,machine_status):
    with conn:
        command = 'INSERT INTO machine_equipment VALUES (?,?,?,?,?,?)'
        c.execute(command,(None,machine_code,machine_title,machine_detail,machine_serial,machine_status))
    conn.commit()

def view_machine_equipment():
    with conn:
        command = 'SELECT * FROM machine_equipment'
        c.execute(command)
        result = c.fetchall()
    return result

def update_machine_equipment(machine_code,field,newvlaue):
    with conn:
        command = 'UPDATE machine_equipment SET {} = (?) WHERE machine_code = (?)'.format(field)
        c.execute(command,(newvlaue,machine_code))
    conn.commit()

def delete_machine_equipment(machine_code):
    with conn:
        command = 'DELETE FROM machine_equipment WHERE machine_code = (?)'
        c.execute(command,([machine_code]))
    conn.commit()

### Spare Part ###
c.execute(""" CREATE TABLE IF NOT EXISTS spare_part (
          ID INTEGER PRIMARY KEY AUTOINCREMENT,
          part_code TEXT,
          part_title TEXT,
          part_detail TEXT,
          part_quantity INT ) """)

def insert_spare_part(part_code,part_title,part_detail,part_quantity):
    with conn:
        command = 'INSERT INTO spare_part VALUES (?,?,?,?,?)'
        c.execute(command,(None,part_code,part_title,part_detail,part_quantity))
    conn.commit()

def view_spare_part():
    with conn:
        command = 'SELECT * FROM spare_part'
        c.execute(command)
        result = c.fetchall()
    return result

def update_spare_part(part_code,field,newvlaue):
    with conn:
        command = 'UPDATE spare_part SET {} = (?) WHERE part_code = (?)'.format(field)
        c.execute(command,(newvlaue,part_code))
    conn.commit()

def delete_spare_part(part_code):
    with conn:
        command = 'DELETE FROM spare_part WHERE part_code = (?)'
        c.execute(command,([part_code]))
    conn.commit()