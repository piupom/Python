#parametrina annettavan tiedoston sisällöstä merkkien lukumäärä
#python tiedostonMerkkienLukukmaara.py sortedrate.txt
from sys import argv
from collections import defaultdict

#käytetään merkkiä avaimena ja lukumäärä
counts = defaultdict(int) # laitetaan oletusarvo
with open (argv[1]) as infile:
	for c in infile.read():
		if c in counts:
			counts[c] += 1
		else:
			counts[c] = 1
			
print(counts)
