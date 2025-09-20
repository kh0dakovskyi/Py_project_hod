class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)

class Dog(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

Gibi = Dog('Gibi', 10, 'yellow')
Gabbi = Cat('Gabbi', 5, 'orange')

Gibi.info()
Gabbi.info()
