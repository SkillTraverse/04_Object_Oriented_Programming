class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name, "is eating")

    def sleep(self):
        print(self.name, "is sleeping")