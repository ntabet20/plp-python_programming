# Polymorphism
class Vehicles:
    
    def __init__(self, name, model):
        self.name = name
        self.model = model

class Car(Vehicles):

    def __init__(self, name, model):
        super().__init__(name, model)
    
    def move(self):
        print("Driving!")

class Plane(Vehicles):

    def __init__(self, name, model):
        super().__init__(name, model)

    def move(self):
        print("Flying!")

class Motobike(Vehicles):

    def __init__(self, name, model):
        super().__init__(name, model)
    
    def move(self):
        print("Riding!")

car1 = Car("Ford", "Mustang")       #Create a Car object
plane1 = Plane("Boeing", "747")     #Create a Plane object
motobike1 = Motobike("Honda", "PCX") #Create a Motobike  object

for vehicle in (car1, plane1, motobike1):
    vehicle.move()