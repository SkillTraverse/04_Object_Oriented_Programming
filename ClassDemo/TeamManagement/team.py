from player import Player

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        if isinstance(player, Player):
            self.players.append(player)
            print(f"{player.name} has been added to {self.name}.")
        else:
            print("Only instances of Player can be added to the team.")

    def display_team_info(self):
        print(f"Team: {self.name}")
        print("Players:")
        for player in self.players:
            player.display_info()