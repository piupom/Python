from sys import argv
uniqueset = set()
uniquelist = []
with open(argv[1]) as infile:
  for line in infile:
    for c in filter(lambda x: not x.isspace(), line): #jää vain ne merkit riviltä, jotka eivät ole välily
      if c not in uniqueset:
        uniquelist.append(c)
      uniqueset.add(c)
with open(argv[2],"w") as outfile:
  print(" ".join(uniquelist), file=outfile)