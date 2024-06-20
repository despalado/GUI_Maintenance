import csv
from datetime import datetime

def writecsv(recod_list):
    with open('data.csv', 'a', newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(recod_list)

dt= datetime.now().strftime('%Y-%m-%d %H:%M:%S')

record = [dt,'2024-06-08 12:00:00', '30', '40', '50', '60']
writecsv(record) # เรียกใช้งานฟังก์ชัน writecsv() โดยส่งค่า record เข้าไปในฟังก์ชัน writecsv() ในตัวแปร recod_list ที่เป็น parameter   

