import extract
import dataLoader
import sys
from stats import Stats
from player import Player


class FantasyPlayer(Stats, Player):

    def __init__(self, profile, stats, star=False):
        Stats.__init__(self, stats)
        Player.__init__(self, profile)
        self.isStarPlayer = star

    def __str__(self):
        output = (self.name + " Fantasy Stats",
                  "Points: " + str(self.fantasyPoints()),
                  "Index: " + str(self.fantasyIndex()))
        return("\n".join(output))

    def fantasyPoints(self):
        """ Fantasy scoring rules of dream11"""
        return(self.PPG + 1.2 * self.RPG + 1.5 * self.APG
               + 3 * (self.SPG + self.BPG) - self.TO)

    def fantasyIndex(self):
        """ Defined as number of fantasy points a Player
            got per unit credit spent"""
        return(self.fantasyPoints() / self.credits)


if __name__ == "__main__":
    Z = FantasyPlayer(dataLoader.profileManual(), dataLoader.statsManual())
    print(Z)
