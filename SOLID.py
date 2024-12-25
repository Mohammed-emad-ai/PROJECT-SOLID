# نبدا هنا بمد single principle
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_details(self):
        return f"{self.make} {self.model}"

#خلينا دا يحسب جوده الوقود لوحده عشان ميخالف مبدا الsingle
class Vehicle_data:
    def fuel_efficiency(self, vehicle):
        print(f" fuel efficiency of {vehicle.get_details()}")

#الكلاسين دول بيطبقو مبدأ open/closed
class Car(Vehicle):
    def drive(self):
        print(f"driv a car: {self.get_details()}")


class Truck(Vehicle):
    def load_cargo(self):
        print(f"Loading cargo in truck: {self.get_details()}")
        
        
        
        
#""""""""""""""""""""""""""
#عملنا الكلاس دا بيطبق مبدأ liskov 
class ElectricCar(Car):
    def battery(self):
        print(f"Charging {self.get_details()}")

#هنا بيطبق مبدأ ال interface
class Refuelable:
    def refuel(self):
        raise "overrid"


class Rechargeable:
    def recharge(self):
        raise "overrid"


class GasolineCar(Car, Refuelable):
    def refuel(self):
        print(f"Refue car {self.get_details()}")


class HybridCar(Car, Refuelable, Rechargeable):
    def refuel(self):
        print(f"Refue hybrid car {self.get_details()}")

    def recharge(self):
        print(self.get_details())
#"""
#هنا بنطبق مبدأ dependency
class Repair:
    def perform_repair(self, vehicle):
        raise "overrid"


class RepairService(Repair):
    def perform_repair(self, vehicle):
        print(f"Perform repair {vehicle.get_details()}")


car = Car("Toyota", "Corolla")
s = Vehicle_data()
s.fuel_efficiency(car)

truck = Truck("bmw", "x3")
truck.load_cargo()

tesla = ElectricCar("Tesla", "Model S")
tesla.battery()
tesla.drive()

gasoline_car = GasolineCar("Honda", "Civic")
gasoline_car.refuel()

hybrid_car = HybridCar("Toyota", "Prius")
hybrid_car.refuel()
hybrid_car.recharge()

Repair = RepairService()
Repair.perform_repair(car)
Repair.perform_repair(truck)