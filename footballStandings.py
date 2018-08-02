from sys import argv
class Team:
  def __lt__(self,other):
    return((-self.points, self.allowed - self.scored, -self.scored, self.name) <
    (-other.points, other.allowed  - other.scored, -other.scored, other.name))
  #pass #
data = []
with open(argv[1]) as infile:
  for line in infile:
    parts = line.split("\t")
    t=Team()
    t.name = parts[0]
    t.wins = int(parts[1])
    t.ties = int(parts[2])
    t.losses = int(parts[3])
    goals = parts[4].split("-")
    t.scored = int(goals[0])
    t.allowed = int(goals[1])
    t.matches = t.wins + t.ties + t.losses
    t.points = 3*t.wins + t.ties
    data.append(t)
#pisin joukkueen nimi
maxlen = str(max(data, key=lambda t: len(t.name)))
for team in sorted(data):
  print(("{:"+ maxlen + "s}{:3d}{:3d}{:3d}{:3d}{:>6s}{:3d}").format(
      t.name, t.matches, t.wins, t.ties, t.losses, 
      str(t.scored) + "-" + str(t.allowed), 
      t.points))
   