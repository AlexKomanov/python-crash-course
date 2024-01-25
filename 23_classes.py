class Vehicle:
    def __init__(self, brand: str, year: int):
        self.brand = brand
        self.year = year

    def print_my_info(self):
        print(f"I'm a general print_my_info method")


class Car(Vehicle):
    my_class = "Car"

    def __init__(self, brand: str, year: int, wheels=4):
        super().__init__(brand, year)
        self.wheels = wheels

    def print_my_info(self):
        print(f"I'm {self.year} {self.brand} car with {self.wheels} wheels.")


class Truck(Vehicle):
    my_class = "Truck"

    def __init__(self, brand: str, year: int, wheels=8, hp=500):
        super().__init__(brand, year)
        self.wheels = wheels
        self.hp = hp

    def print_my_info(self):
        print(f"I'm {self.brand} truck with {self.wheels} wheels. I have {self.hp} HP")


bmw_car = Car("BMW", 2024)
bmw_car.print_my_info()
print(Car.my_class)

vw_truck = Truck("VW", 2023)
vw_truck.print_my_info()
