class House:
	def __init__(self, name, bedroom, door, window, area):
		self.name = name
		self.bedroom = bedroom
		self.door = door
		self.window = window
		self.area = area

	def show_features(self):
		print("This is a", self.name)
		print("Bedroom: ", self.bedroom, "Doors: ", self.door, "Window: ", self.window, "Area: ", self.area)



    
h1 = House("Barrington", 3, 2, 4, 120)
h2 = House("Kensington", 4, 6, 5, 300)

h1.show_features()
h2.show_features()


