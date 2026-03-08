class House:

    def __init__(self, name, bedroom):
        self.name = name
        self.bedroom = bedroom

    def show_details(self):
        print("This is a", self.name)
        print("Bedrooms:", self.bedroom)


class Barrington(House):

    def __init__(self,bedroom, pool):
        super().__init__("Barrington", bedroom)
        self.pool = pool

    def show_details(self):
        super().show_details()
        print("Pool:", self.pool)

class Kesington(House):
    name = "Kesington"

    def __init__(self, bedroom, cinema):
        super().__init__(Kesington.name, bedroom)
        self.cinema = cinema

    def show_details(self):
        super().show_details()
        print("Cinema:", self.cinema)

housing_estate = [
    House("Carlton", 1),
    Barrington(3, True),
    Kesington(4, True)
    ]

for house in housing_estate:
    house.show_details()
