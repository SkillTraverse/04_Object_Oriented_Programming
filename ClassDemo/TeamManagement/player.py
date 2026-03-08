from datetime import datetime

class Player:
    def __init__(self, name, date_of_birth, position, height, retired):
        self.name = name
        dob = datetime.strptime(date_of_birth, "%Y-%m-%d")
        today = datetime.today()
        self.age = today.year - dob.year
        self.position = position
        self.height = height
        self.retired = retired

    def display_info(self):
        print(f"""
        Name: {self.name}
        Age: {self.age}
        Position: {self.position}
        Height: {self.height}cm
        Status: {"Active" if not self.retired else "Inactive (Retired)"}
        """)

    def change_status(self, retired):
        self.retired = retired
        status = "Active" if not retired else "Inactive (Retired)"
        print(f"{self.name} is now {status}.")
