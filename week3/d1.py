#oop __init__(self,atrributes) for constuctor
class Phone:
    color = None
    Brand = None
    Camera = None
    Usbtype = None
    def __init__(self,color,Brand,Camera,Usbtype):
        self.color = color
        self.Brand = Brand
        self.Camera = Camera
        self.Usbtype = Usbtype
    def on (self):
        print('The phone is on')
    def off (self):
        print('The phone is off')
    def getcolour (self):
        return self.color


Myphone = Phone("Red",'Samsung','3','Type c')
print(Myphone.color)
Myphone.on()
Myphone.off()
# OOP (Object oriented Programming)

# class

class car:
    # attributes (Class attributes)
    color = None
    headlight = None
    speed = None
    wheel = 4
    spoiler = None

    # constructor
    def __init__(self,color,headlight,speed,spoiler):
        self.color = color
        self.headlight = headlight
        self.speed = speed
        self.spoiler = spoiler

    # methods
    def accelerate(self):
        print("Car is now accelerating")

    def brake(self):
        print("Car is stopped")

    # getter
    def getColor(self):
        return self.color

    # setter
    def setColor(self,color):
        self.color = color






# making object of a class
myCar = car("red","square","60 KM/H",True)

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


