def profileManual():
    name = input("Player name: ")
    team = input("Player Team: ")
    position = input("Player position: ")
    credits = float(input("Player credits: "))
    print("-" * 20)
    profile = {"name": name,
               "team": team,
               "position": position,
               "credits": credits}
    return(profile)


def statsManual():
    PPG = float(input("Points: "))
    RPG = float(input("Rebounds: "))
    APG = float(input("Assists: "))
    SPG = float(input("Steals: "))
    BPG = float(input("Blocks: "))
    TO = float(input("Turn Overs: "))
    print("-" * 20)
    stats = {"PPG": PPG, "RPG": RPG,
             "APG": APG, "SPG": SPG,
             "BPG": BPG, "TO": TO, }
    return(stats)
