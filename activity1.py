class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    pass
bus1 = Bus("School Volvo", 180, 12)
print("Vehicle Name:", bus1.name) 
print("Speed:", bus1.max_speed)
print("Mileage:", bus1.mileage)