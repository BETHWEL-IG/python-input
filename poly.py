# Base Class
class Vehicle:
    def move(self):
        pass  # Placeholder for polymorphism

# Subclasses
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚴"

# Test the polymorphism
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for vehicle in vehicles:
    print(vehicle.move())
