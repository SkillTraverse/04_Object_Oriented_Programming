from animal import Animal


class Lion(Animal):

    def make_sound(self):
        print(self.name, "roars")


class Elephant(Animal):

    def make_sound(self):
        print(self.name, "trumpets")

class Monkey(Animal):

    def make_sound(self):
        print(self.name, "chatters")


class Penguin(Animal):

    def make_sound(self):
        print(self.name, "squawks")  


animals = [
    Lion("Simba", 5),
    Elephant("Dumba", 10),
    Monkey("Rafiki", 3),
    Penguin("Pingu", 2)
    ]


for animal in animals:
    animal.make_sound()
