#Eric Hayden 05/09/2021
print("Welcome to your personal digital garage. Please enter information about each of your cars.")

#Defining Vehicle and qualities of it
class Vehicle:
    def __init__(self, make, model, color, fuelType, options):
        self.make = make
        self.model = model
        self.color = color
        self.fuelType = fuelType
        self.options = options

    def get_user_input(self):
        make = input("Please enter the make of your vehicle: ")
        model = input("Please enter the model of your vehicle: ")
        color = input("Please enter the color of your vehicle: ")
        fuelType = input("Please enter the fuel type of your vehicle: ")
        options = input("Please enter the other options for your vehicle: ")
        return make, model, color, fuelType, options

#Defining Car and qualities of it
class Car(Vehicle):
    def __init__(self, engineSize, numDoors):
         self.engineSize = engineSize
         self.numDoors = numDoors

    def get_car_input(self):
        T = Vehicle.get_user_input(self)
        engineSize = input("Please enter the size of the engine in your car: ")
        numDoors = input("Please enter the number of doors on your car: ")
        return self, T, engineSize, numDoors

#Defining Pickup and qualities of it
class Pickup(Vehicle):
    def __init__(self, cabStyle, bedLength):
        self.cabStyle = cabStyle
        self.bedLength = bedLength

    def get_pickup_input(self):
        T = Vehicle.get_user_input(self)
        cabStyle = input("Pleas enter the cab style of your pickup: ")
        bedLength = input("Please enter the length of the bed of your pickup: ")
        return self, T, cabStyle, bedLength

list = []

while True:
    n = 1

    for i in range(0, n):
    
        self = input("Please enter if it is a Car or is it a Pickup:")

        if self == "Car":
            list.append(Car.get_car_input(self))
            n = n + 1
        
        elif self == "Pickup":
            list.append(Pickup.get_pickup_input(self))
            n = n + 1
        
        else:
            print("Please enter Car or Pickup all other inputs are invalid. ")

    print('Here is a list of all of your currently added vehicles: ')
    print(list)
