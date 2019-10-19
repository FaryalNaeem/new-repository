class battery():
    def __init__(self,size,price):
        self.size = size 
        self.price = price
    def getbattery(self):
        print(f'The battery size is {self.size}')
    def setbattery(self,newsize):
        self.size = newsize
 
 ####practice


class cars():
    def __init__(self,make,model,year= ''):
        self.make = make
        self.model = model
        self.year = year
        speed = 20
        self.battery = battery(20,1000)
    def deccar(self):
        print(f"{self.make} {self.model} {self.year}")

car1 = cars("honda", "AS", 2018)
car2 = cars("civic", "BS")
class Smartcar(cars):
    def __init__(self,make,model,year=''):
        super().__init__(make,model,year)
        self.battery = 10
ecar1 = Smartcar('tesla', 'tt', 'next')