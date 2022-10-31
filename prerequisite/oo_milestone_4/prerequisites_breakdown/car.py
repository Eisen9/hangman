# 3. Create a Car class

class Car:
    def __init__(self, model, year = 2021):
        self.model = model
        self.year = year
        self.miles_driven = 0

    def drive(self):
        print("vroom")
        self.miles_driven += 1

    def info(self):
        print(f"{self.miles_driven} miles driven, {self.model} {self.year}")

car_1 = Car("Tesla")
print(f"{car_1.drive()}")
