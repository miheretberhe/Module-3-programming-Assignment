#Miheret Gebrehans
# Module 3 Lab - Case Study: Lists, Functions, and Classes 02
#
#15 September 2025

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
class Automobile(Vehicle):
    def __init__(self,vehicle_type, year, make,model, doors, roof ):
        super().__init__(vehicle_type)

        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
print("Tell me about your car.")


year = input("what is the year?")
make = input("what make is it?")
model = input("what model is it?")
doors = input("How many doors does it have?")
roof= input("what kind of roofing does it have?")

my_car = Automobile("car", year, make, model, doors, roof)

print("\nHere are the details of your car:")
print(f"  Vehicle type: {my_car.vehicle_type}")
print(f"  Year: {my_car.year}")
print(f"  Make: {my_car.make}")
print(f"  Model: {my_car.model}")
print(f"  Number of doors: {my_car.doors}")
print(f"  Type of roof: {my_car.roof}")