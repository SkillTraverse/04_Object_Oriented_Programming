from animal import Animal

class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def fly(self):
        print(self.name, "is flying with a wingspan of", self.wingspan, "cm")
    
class Parrot(Bird):

    def make_sound(self):
        print(self.name, "says Hello!")

class Sparrow(Bird):

    def make_sound(self):
        print(self.name, "chirps")

class Penguin(Bird):

    def make_sound(self):
        print(self.name, "squawks")


parrot = Parrot("Polly", 2, 25)
sparrow = Sparrow("Jack", 1, 15)
penguin = Penguin("Pingu", 3, 10)

parrot.eat()
parrot.fly()
parrot.make_sound()

sparrow.eat()
sparrow.fly()
sparrow.make_sound()

penguin.eat()
penguin.fly()
penguin.make_sound()