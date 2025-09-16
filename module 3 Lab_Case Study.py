#Miheret Gebrehans
#Module 3 Lab - Case Study: Lists, Functions, and Classes
#This program stores the general information of vehicle and outputs that info.
#15 September 2025



class vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
class automobile(vehicle):
    def __init__(self,vehicle_type, year, make,model, doors, roof ):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
my_car = automobile('car', 2018, 'Chevrolet', 'cruze', 4, 'hardtop' )
print("vehicle type:",my_car.vehicle_type)
print("year:", my_car.year)
print("make:",my_car.make)
print("model:",my_car.model)
print("doors:",my_car.doors)
print("roof:", my_car.roof)

