import extract
import sys


class Player():
    "Implements dream11 NBA fantasy Player"

    def __init__(self, profile, injury=False):
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
        self.isInjuredRested = injury

    def __str__(self):
        if self.isInjuredRested:
            status = "Injured or Rested"
        else:
            status = "Playing"
        output = ("Name: " + self.name,
                  "Team: " + extract.TEAMS[self.team],
                  "Position: " + self.position,
                  "Credits: " + str(self.credits),
                  "Status: " + status)
        return("\n".join(output))


if __name__ == "__main__":
    profile = {"name": "Joel embiid", "team": "phi", "position": "c", "credits": 19}
    B = Player(profile)
    print(B)
