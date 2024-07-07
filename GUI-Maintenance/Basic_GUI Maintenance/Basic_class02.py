class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def drive(self):
        print('The car is moving.')
    
class ElectricCar(Car):
    def __init__(self,brand,model,year):
        super().__init__(brand,model,year)

    def charge(self):
        print('The car is fully charged.')

elecCar01 = ElectricCar('Tesla','Model S',2021)
print(elecCar01.brand)
print(elecCar01.model)
print(elecCar01.year)
elecCar01.drive()
print('--------------------------------')
elecCar02 = ElectricCar('Tesla','Model 3',2021)
print(elecCar02.brand)
print(elecCar02.model)
print(elecCar02.year)
elecCar02.drive()
print('--------------------------------')
elecCar03 = ElectricCar('Tesla','Model X',2021)
print(elecCar03.brand)
print(elecCar03.model)
print(elecCar03.year)
elecCar03.charge()
print('--------------------------------')