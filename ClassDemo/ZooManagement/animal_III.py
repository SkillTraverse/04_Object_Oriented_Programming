from animal import Animal


class Lion(Animal):
    
    def eat(self):
        print(self.name, "is eating meat")


class Elephant(Animal):
    
    def eat(self):
       print(self.name, "is eating plants")

lion = Lion("Simba", 5)
elephant = Elephant("Dumba", 10)

lion.eat()

elephant.eat()
