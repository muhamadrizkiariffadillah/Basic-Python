# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

class MotorCycle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Ride")


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("drive!")


motor = MotorCycle("Honda", "CBR")
car = Car("Suzuki", "Ertiga")

for x in (motor, car):
    x.move()


# Inheritance class polymorphism

class Vechile:
    def __init__(self, brand: str, name: str):
        self.brand = brand
        self.name = name

    def move(self):
        print("Move")

class Boat(Vechile):
    def move(self):
        print("Boat")

class Plane(Vechile):
    def move(self):
        print("Plane")


boat = Boat("Ibiza","Touring 20")
plane = Plane("Boing","854")

for x in (boat,plane):
    x.move()

