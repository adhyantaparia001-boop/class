#polymorphipsm
class Vehicle:

    def honk(self):
        print('The vehicle is honkin')

    def accelerate(self):
        print("Vehicle is now accelerating")

    def brake(self):
        print("Vehicle is stopped")
class Car(Vehicle):


    def accelerate(self):

        print("The car is speeding up!")
class Bike(Vehicle):

    def honk(self):

        print("The bike rings its bell.")
def perform_actions( vehicle):
    if vehicle == Car():
        vehicle.accelerate()
    else :
        vehicle.honk()
a = Bike()
print(perform_actions(a))