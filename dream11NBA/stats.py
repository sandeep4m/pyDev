class Stats():

    """ Implements basic stats """

    def __init__(self, stats):
        try:
            self.PPG = stats["PPG"]
            self.RPG = stats["RPG"]
            self.APG = stats["APG"]
            self.SPG = stats["SPG"]
            self.BPG = stats["BPG"]
            self.TO = stats["TO"]
        except KeyError as error:
            print(error)

    def __str__(self):
        output = ("Points: " + str(self.PPG), "Rebounds: " + str(self.RPG),
                  "Assists: " + str(self.APG), "Steals: " + str(self.SPG),
                  "Blocks: " + str(self.BPG), "Turn Overs: " + str(self.TO))
        return("\n".join(output))


if __name__ == "__main__":
    score = {"PPG": 27.2, "APG": 7.2, "RPG": 7.3, "SPG": 1.6, "BPG": 0.7, "TO": 3.5}
    A = Stats(score)
    print(A)
