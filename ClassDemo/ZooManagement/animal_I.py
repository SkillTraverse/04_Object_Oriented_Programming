from animal import Animal

class Lion(Animal):

    def make_sound(self):
        print(self.name, "roars")


class Elephant(Animal):

    def make_sound(self):
        print(self.name, "trumpets")


lion = Lion("Simba", 5)
elephant = Elephant("Dumba", 10)

print(lion.name)
print(lion.age)

print(elephant.name)
print(elephant.age)

lion.eat()
elephant.eat()

lion.sleep()
elephant.sleep()