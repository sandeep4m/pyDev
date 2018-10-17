import extract
import dataLoader
import sys
from stats import Stats
from player import Player


class Fantasy(Stats, Player):

    def __init__(self, profile, stats):
        Stats.__init__(self, stats)
        Player.__init__(self, profile)

    def fantasyPoints(self):
        return(self.PPG + 1.2 * self.RPG + 1.5 * self.APG
               + 3 * (self.SPG + self.BPG) - self.TO)

    def fantasyIndex(self):
        return(self.fantasyPoints() / self.credits)

    def __str__(self):
        output = (self.name + " fantasy stats".upper(),
                  "Points: " + str(self.fantasyPoints()),
                  "Index: " + str(self.fantasyIndex()))
        return("\n".join(output))


if __name__ == "__main__":
    Z = Fantasy(dataLoader.profileManual(), dataLoader.statsManual())
    print(Z)
