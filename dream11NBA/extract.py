def getTeams(f):
    teamDict = dict()
    with open(f) as teamsData:
        for line in teamsData:
            line = line.strip()
            data = line.split(",")
            teamDict[data[0]] = data[1]
    return(teamDict)


TEAMS = getTeams("teams.csv")
POSITIONS = {"PG", "SG", "SF", "PF", "C"}
