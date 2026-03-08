from player import Player
from team import Team


def main():
    players = {}
    teams = {}

    print("Welcome to Team Management")
    print("Type 'help' to see available commands.\n")

    while True:
        command = input(">> ").strip().lower()

        if command == "exit":
            print("Exiting program.")
            break

        elif command == "help":
            print("""
                Available commands:

                create player
                create team
                add player to team
                show player
                show team
                retire player
                exit
                """)

        elif command == "create player":
            name = input("Name: ")
            dob = input("Date of birth (YYYY-MM-DD): ")
            position = input("Position: ")
            height = int(input("Height (cm): "))

            player = Player(name, dob, position, height, retired=False)
            players[name] = player
            print(f"Player {name} created.")

        elif command == "create team":
            name = input("Team name: ")
            team = Team(name)
            teams[name] = team
            print(f"Team {name} created.")

        elif command == "add player to team":
            player_name = input("Player name: ")
            team_name = input("Team name: ")

            if player_name in players and team_name in teams:
                teams[team_name].add_player(players[player_name])

            else:
                print("Player or Team not found.")

        elif command == "show player":
            name = input("Player name: ")
            if name in players:
                players[name].display_info()
            else:
                print("Player not found.")

        elif command == "show team":
            name = input("Team name: ")
            if name in teams:
                teams[name].display_team_info()
            else:
                print("Team not found.")

        elif command == "retire player":
            name = input("Player name: ")
            if name in players:
                players[name].change_status(True)
            else:
                print("Player not found.")

        else:
            print("Unknown command. Type 'help' to see options.")


if __name__ == "__main__":
    main()