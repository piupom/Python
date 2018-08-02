#parametrina annettavan tiedoston sisällöstä merkkien paikka
#python tiedostonMerkit.py sortedrate.txt

from sys import argv
from collections import defaultdict

#käytetään merkkiä avaimena ja lukumäärä
pos = defaultdict(list) 
with open (argv[1]) as infile:
	for idx, c in enumerate(infile.read()):
		pos[c].append(idx)

with open (argv[2],"w") as outfile:  #"w" ylikirjoittaa -  "a" on lisää
	for row, c in enumerate(sorted(pos),start=1):
		print("{:3d} {:s}:{:s}".format(row, c," ".join(map(str,pos[c]))),file=outfile)
		#tai vaihtoehtoisesti
		# outfile.write(...
