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

    def viewStats(self):
        print("Points: " + str(self.PPG))
        print("Rebounds: " + str(self.RPG))
        print("Assists: " + str(self.APG))
        print("Steals: " + str(self.SPG))
        print("Blocks: " + str(self.BPG))
        print("Turn Overs: " + str(self.TO))


if __name__ == "__main__":
    score = {"PPG": 27.2, "APG": 7.2, "RPG": 7.3, "SPG": 1.6, "BPG": 0.7, "TO": 3.5}
    A = Stats(score)
    A.viewStats()
