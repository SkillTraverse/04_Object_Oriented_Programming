from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):

    def speak(self):
        print(self.name, "barks")


class Cat(Animal):

    def speak(self):
        print(self.name, "meows")

class Penguin(Animal):

    def speak(self):
        print(self.name, "squawks")



#dog = Dog("Buddy", 3)
#cat = Cat("Whiskers", 2)
#penguin = Penguin("Pingu", 2)

#dog.speak()
#cat.speak()
#penguin.speak()

class Sheep(Animal):

    def speak(self):
        print(self.name, "bleats")

    def move(self):
        print(self.name, "is moving")

sheep = Sheep("Dolly", 4)
sheep.move()
