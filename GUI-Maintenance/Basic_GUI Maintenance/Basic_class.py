class Employee:
    #full_name = 'Annop Natesaengsri'
    #position = 'Software Engineer'
    #salary = 30000
    #สร้างคอนสตรักเตอร์ 
    def __init__(self,full_name,position,salary):
        self.full_name = full_name
        self.position = position
        self.salary = salary

    def learn(self):
        print('Learning Python')

employee01 = Employee('somchai','Manager',50000) # สร้างอ็อบเจ็กต์ employee01 จากคลาส Employee
print(employee01.full_name)
print(employee01.position)
print(employee01.salary)
employee01.learn() # เรียกใช้งานเมธอด learn() ของอ็อบเจ็กต์ employee01
print('--------------------------------')
employee02 = Employee('somsri','Manager',50000) # สร้างอ็อบเจ็กต์ employee01 จากคลาส Employee
print(employee02.full_name)
print(employee02.position)
print(employee02.salary)
employee02.learn() # เรียกใช้งานเมธอด learn() ของอ็อบเจ็กต์ employee01
print('--------------------------------')
employee03 = Employee('somboon','Manager',150000) # สร้างอ็อบเจ็กต์ employee01 จากคลาส Employee
print(employee03.full_name)
print(employee03.position)
print(employee03.salary)
employee03.learn() # เรียกใช้งานเมธอด learn() ของอ็อบเจ็กต์ employee01
print('--------------------------------') 