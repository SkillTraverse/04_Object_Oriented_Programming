class Animal:

    kingdom = "Animalia"

    def __init__(self, name):
        self.name = name
        
lion = Animal("Simba")
elephant = Animal("Dumba")

print(lion.name)
print(elephant.name)

print(lion.kingdom)
print(elephant.kingdom)