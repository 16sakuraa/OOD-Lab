class Team:
    def __init__(self,name,wins,loss,draws,scored,conceded):
        self.name = name
        self.wins = wins
        self.loss = loss
        self.draws = draws
        self.scored = scored
        self.conceded = conceded
        self.gd = scored - conceded
        self.point = (3*wins) + draws
    def display(self):
        # ['Manchester United', {'points': 95}, {'gd': 68}]
        print("['"+str(self.name)+"', {'points': "+str(self.point)+"}, {'gd': "+str(self.gd)+"}]")

def findMaxPoint(team): #input as list , not class
    max = 0
    for i in range(len(team)):
        if team[i].point == max and team[i].gd > teamName.gd :
            teamName = team[i]
        elif team[i].point > max:
            max = team[i].point
            teamName = team[i]

    return teamName


inputstr = [e for e in input('Enter Input : ').split('/')]

count=0
team = []
for i in inputstr:
    name,wins,loss,draws,scored,conceded = i.split(',')
    item = Team(name,int(wins),int(loss),int(draws),int(scored),int(conceded))
    team.append(item)
    count+=1

print('== results ==')
for i in range(len(inputstr)):
    teamName = findMaxPoint(team)
    teamName.display()
    team.remove(teamName)

