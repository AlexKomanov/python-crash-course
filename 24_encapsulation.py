# public / protected / private

class Car:

    def __init__(self, brand: str, is_electrical: bool, year: int):
        self.brand = brand  # public
        self._is_electrical = is_electrical # protected
        self.__year = year # private

    def print_my_info(self):
        print(f"Car {self.brand}, {self._is_electrical}, {self.__year}")

    def get_year(self):
        return self.__year

    def set_year(self, year: int):
        if year < 2010 or year > 2024:
            self.__year = 2024
        else:
            self.__year = year


car = Car("BMW", True, 2020)
print(car.brand)
print(car._is_electrical)
print(car.get_year())
car.set_year(2015)
print(car.get_year())
car.print_my_info()