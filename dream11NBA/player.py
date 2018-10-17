import extract


class Player():
    "Implements dream11 NBA fantasy Player"

    def __init__(self, profile):
        try:
            self.name = profile["name"].upper()
            if profile["team"].upper() in extract.TEAMS:
                self.team = profile["team"].upper()
            else:
                sys.exit("Invalid Team")
            if profile["position"].upper() in extract.POSITIONS:
                self.position = profile["position"].upper()
            else:
                sys.exit("Invalid Position")
            self.credits = float(profile["credits"])
        except KeyError as error:
            print(error)

    def viewPlayer(self):
        print("Name: " + self.name)
        print("Team: " + extract.TEAMS[self.team])
        print("Position: " + self.position)
        print("Credits: " + str(self.credits))


if __name__ == "__main__":
    profile = {"name": "Joel embiid", "team": "phi0", "position": "c", "credits": 19}
    B = Player(profile)
    B.viewPlayer()
