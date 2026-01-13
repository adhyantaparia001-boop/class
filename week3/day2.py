class Car:
    # attributes (Class attributes)
    __color = None
    headlight = None
    speed = None
    wheel = 4
    spoiler = None
    Fuel = None

    # constructor
    def __init__(self,__color,headlight,speed,spoiler,fuel):
        self.__color = __color
        self.headlight = headlight
        self.speed = speed
        self.spoiler = spoiler
        self.fuel = fuel

    # methods
    def accelerate(self):
        print("Car is now accelerating")
        

    def brake(self):
        print("Car is stopped")
    def gfuel(self,d):
        arr1 = []
        for nn in self.fuel.split(' '):
            arr1.append(nn)
        fuell = arr1.pop(0)
        fuell= int(fuell)
        arr = []
        for item in d.split(' '):
            arr.append(item)
        a = arr.pop(0)
        a = int(a)

        fuelused = a / 10
        if fuelused > fuell:
            print('fuel not enough')

        else :

            remainingfuel  = fuell - fuelused
            self.fuel  = f'{remainingfuel}'
            print(f'Fuel left is {self.fuel}')
    def setfuel(self,fuel):
        self.fuel = fuel

    def toggleheadlight(self):
        if self.headlight.lower().strip() == 'off':
            self.headlight = 'on'
            print(f'Headlight is on')

        elif self.headlight.lower().strip() == 'on':
            self.headlight = 'off'
            print(f'Headlight is off')

    def setheadlight(self,headlight):
        self.headlight = headlight

    # getter
    def getColor(self):
        return self.__color

    # setter
    def setColor(self,__color):
        self.__color = __color






# making object of a class
myCar = Car("red","square","60 KM/H",True,"50 L")

# accessing attributes of a class
# print(myCar.headlight)

# changing the value of an attribute
# myCar.color = 'red'
# print(myCar.color)

# running object's methods
# myCar.accelerate()
# myCar.brake()

# use getter setter
myCar.setColor('green')
print(myCar.getColor())
myCar.setheadlight('ON')
myCar.toggleheadlight()
myCar.setfuel('50 l')
myCar.gfuel('10 km')

class Driver:
    name = ' '
    age = None
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def drive_car(self,cc) :
        print(f'Driver {self.name} is driving the car')
        print(Car.accelerate(cc))
myDriver = Driver("Devansh",18)
myDriver.drive_car(myCar)
