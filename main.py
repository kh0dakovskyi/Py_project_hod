class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def display_info(self):
            print(f"Car {self.brand} model {self.model} year {self.year} color {self.color}")


car1 = Car('Toyota', 'M', 2019, 'Blue')
car2 = Car('Audi', 'V', 2021, 'Dark')
car3 = Car('peugeot', '508', 2018, 'Grey - green')

car1.display_info()
car2.display_info()
car3.display_info()

