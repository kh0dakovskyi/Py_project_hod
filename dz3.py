class Book:
    def __init__(self, name, author, rik):
        self.name = name
        self.author = author
        self.rik = rik

class Library:
    def __init__(self, name):
        self.name = name
        self.list = []

    def add_passenger(self, book):
        self.list.append(book)

    def print_passenger(self):
        for i in self.list:
            print(i.name, i.author, i.rik)

b1 = Book("вщпов", "пвпвк", "1999")
b2 = Book("врвк", "упкрпкв", "2025")
b3 = Book("крврв", "врвр", "1345")

lib = Library("Avrora")
lib.add_passenger(b1)
lib.add_passenger(b2)
lib.add_passenger(b3)

lib.print_passenger()
