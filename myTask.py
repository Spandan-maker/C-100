class Car:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def start(self, name):
        print("Your car,", self.name, "has started")

name = str(input("Enter your car name: "))
carA = Car(3, "black", name)

carA.start(name)