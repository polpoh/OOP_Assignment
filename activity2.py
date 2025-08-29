# activity2.py

class Vehicle:
    def move(self):
        print("This vehicle moves in some way.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")


# Testing Polymorphism
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        v.move()


