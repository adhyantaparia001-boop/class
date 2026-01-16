class Car :
    def __init__(self,wheels,fuel):
        self.wheels = wheels
        self.fuel = fuel


    def accelerate(self):
        print('The car is accelerating')
class Suv(Car):
    def __init__(self, color,wheels,fuel):
        super().__init__(wheels, fuel)
        self.color  =color
    def brake(self):
        super().accelerate()
        print('The car has stopped')
Creta = Suv('red',4,50)
print(Creta.brake())
class Animal :
    def __init__(self,legs,name):
        self.legs = legs
        self.name = name


    def eat(self):
        print(f'{self.name} is eating food')
class Dog(Animal):
    def __init__(self,legs,name,breed):
        super().__init__(legs,name)
        self.breed  = breed
    def bark(self):

        print('The dog is barking')
class Gaurd_Dog(Dog):
    def __init__(self,legs,name,breed,duty_time):
        super().__init__(legs,name,breed)
        self.duty_time  = duty_time
    def gaurd(self):
        duty_time = self.duty_time
        super().bark()
        print(f'Guard dog is on duty for {duty_time} hours')
bruno = Gaurd_Dog(4,'Bruno','German Shephard',10)
bruno.gaurd()