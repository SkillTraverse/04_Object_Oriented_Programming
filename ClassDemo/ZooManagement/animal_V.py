from animal import Animal

class Lion(Animal):

    def __init__(self, name, age, pride_size):
        super().__init__(name, age)
        self.pride_size = pride_size

    def make_sound(self):
        print(self.name, "roars")


lion = Lion("Simba", 5, 10)

print(lion.name)
print(lion.pride_size)