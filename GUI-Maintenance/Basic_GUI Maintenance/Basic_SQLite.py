import sqlite3
### contactname = v_custname.get() sitename = v_sitename.get()system = v_system.get()description = v_description.get()serial = v_serial.get()phonenumber = v_phonenumber.get()
###

# สร้างฐานข้อมูล connection 

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
        c.execute(command,(None,tsid,contractname,sitename,system,description,seriral,phonenumber)) # ใส่ค่าที่ต้องการเพิ่มเข้าไปในตาราง caseorder None คือ ID ที่เป็น Primary Key ที่เพิ่มเข้าไปเอง
    conn.commit() # บันทึกข้อมูลลงฐานข้อมูล
    print('Saved')

insert_caseorder(2,'Somchai','Chiang Mai','Dell','Laptop','123TY99','0912345678')

def view_caseorder():
    with conn:
        command = 'SELECT * FROM caseorder'
        c.execute(command)
        result = c.fetchall()# ดึงข้อมูลทั้งหมดจากตาราง caseorder มาแสดง
        return result # ส่งค่า result ออกไป
 
# ฟังก์ชั้นอัพเดทข้อมูล
def update_caseorder(tsid,field,newvlaue):
    with conn:
        command = 'UPDATE caseorder SET {} = (?) WHERE tsid = (?)'.format(field)
        c.execute(command,(newvlaue,tsid))   
    conn.commit()
    print('Updated')

# ฟังก์ชั้นลบข้อมูล
def delete_caseorder(tsid):
    with conn:
        command = 'DELETE FROM caseorder WHERE tsid = (?)'
        c.execute(command,([tsid]))# ทำไมต้องใส่ [] ลงไป ในวงเล็บ ? ต้องใส่ค่าที่เป็น list ลงไป
    conn.commit()
    print('Deleted')

