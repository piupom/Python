import sys
import random

with open (tied.txt, encoding="utf-8" as infile:
	#sanat = infile.readLines()  #jokainen alkio omaan riviinsä koko tiedoston kerralla
	for rivi in infile:	#luetaan rivi kerrallaan
		print(rivi)

with open (tied.txt, encoding="utf-8" as infile:
	for rivi in infile:	
		for sana in rivi.split(): #luetaan sana kerrallaan
			print(sana)

with open (tied.txt, encoding="utf-8" as infile:
	#sanat = infile.readLines()  #jokainen alkio omaan riviinsä koko tiedoston kerralla
	for rivi in infile:	#luetaan rivi kerrallaan
		for merkki in rivi:
			print(merkki)