def hello():
    print("Hello, World!")  

hello() # เรียกใช้งานฟังก์ชัน hello()

def hellofriend(name): # สร้างฟังก์ชันที่มี parameter ชื่อ name
    print(f'Hello, My name is {name}')

hellofriend('Somchai') # เรียกใช้งานฟังก์ชัน hellofriend() โดยส่งค่า 'Somchai' เข้าไปในฟังก์ชัน hellofriend() ในตัวแปร name ที่เป็น parameter


#เพิ่ม parameter สองตัว

def checkNameAge(name,age):
    print(f'Hello, My name is {name} and I am {age} years old') # f-string ใช้สำหรับการ format string โดยใส่ตัวแปรเข้าไปใน string โดยใช้ {ตัวแปร}
    print(r'Hello, My name is {} and I am {} years old'.format(name,age)) # ใช้ r-string ใช้สำหรับการ format string โดยใส่ตัวแปรเข้าไปใน string โดยใช้ .format(ตัวแปร1, ตัวแปร2)
    
checkNameAge('Somchai', 30) # เรียกใช้งานฟังก์ชัน checkNameAge() โดยส่งค่า 'Somchai' และ 30 ตามลำดับ เข้าไปในฟังก์ชัน checkNameAge() ในตัวแปร name และ age ที่เป็น parameter
checkNameAge(30, 'Somchai') # เรียกใช้งานฟังก์ชัน checkNameAge() โดยสลับการส่งค่า 30 และ 'Somchai' ตามลำดับ เข้าไปในฟังก์ชัน checkNameAge() ในตัวแปร name และ age ที่เป็น parameter
#ถ้าต้องการใส่argument ให้ตัวแปรที่ถูกต้องตามลำดับที่กำหนดไว้ในฟังก์ชัน
checkNameAge(age=30, name='Somchai') # เรียกใช้งานฟังก์ชัน checkNameAge() โดยส่งค่า 30 และ 'Somchai' ตามลำดับ เข้าไปในฟังก์ชัน checkNameAge() ในตัวแปร name และ age ที่เป็น parameter โดยใช้ชื่อตัวแปรเป็น parameter
checkNameAge('Somsri',100)

#new function bacially calculate.
def addNumber(x,y):
    return x+y # function return ต้องมีการ return ค่าออกมาจากฟังก์ชัน
sum = addNumber(10,20)
print(sum) 

# miniproject finding leap year (if/else) basic concept.
    #เงื่อนไขการเป็นปีอธิกสุรทิน คือ ปีที่หารด้วย 4 ลงตัว และ หารด้วย 100 ไม่ลงตัว หรือ หารด้วย 400 ลงตัว
    # หากเป็นปีอธิกสุรทิน ให้ return True ถ้าไม่ใช่ให้ return False
    # สร้างฟังก์ชัน isLeapYear() ที่รับค่า parameter เป็น year และ return ค่า True หรือ False ตามเงื่อนไขข้างต้น
#ประกาศตัวแปร
year = int(input('Enter year: ')) # รับค่าปีจากผู้ใช้
if year % 4 == 0 and year % 400 == 0 or year % 100 != 0:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year') 

color = ['red', 'green', 'blue', 'yellow', 'pink']
color.append('purple') # เพิ่มสมาชิกใหม่เข้าไปใน list
for c in color:
    print(c)
    