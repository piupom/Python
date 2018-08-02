import sys
import random

arvauskertoja = int(sys.argv[2]) # toisena parametrina arvauskertojan lukumäärä

# python sanalista.py sanalista.txt 5
#
#infile = open("sanalista.txt")
#	sanat = infile.read()
# infile.close() 		# tiedoston sulkeminen sen jälkeen, kun sitä ei enää tarvita. 
						#with - tavalla tiedosto suljetaan käytön jälkeen automaattisesti
						
# avataan parametrina tullut tiedosto jonkun nimisenä = infile = open("sanalista.txt")						
with open(sys.argv[1],encoding="utf-8") as infile: # jotta saadaan utf-8 tiedoston sisältö oikeaksi ääkkösten kanssa näytölle
	sanat = infile.read().split(", ")  #splitataan samantien taulukoksi
sanat=list(map(lambda mj: mj.strip().lower(), 
           sanat)) #poistetaan varmuuden vuoksi tyhjät pois ja muutetaan pieniksi kirjaimiksi
# print(sanat[:100]) 	#ekat 100 merkkiä

# sanaidx = random.randint(0,len(sanat)-1) #random-funktiolla jokin indeksi 
# sana=(sanat[sanaidx])
#vaihtoehtoisesti
sana=random.choice(sanat)
print(sana)
nykysana=["_"]*len(sana)
while arvauskertoja > 0 and ("_" in nykysana):
	print("Sana nyt:","".join(nykysana))
	print("Arvauksia jäljellä:", arvauskertoja)
	arvaus = input("Anna kirjain:")
	if len(arvaus) != 1:
		print("anna vain yksi kirjain")
	else:
		oikein = False
		# nykysana = list(map(lambda k: arvaus if # turhaa kikkailua
		for i, k in enumerate(nykysana):
			if nykysana[i] == "_" and arvaus == sana[i]:
				nykysana[i] = sana [i]
				oikein = True
		if not oikein:
			print("Väärin!")
			arvauskertoja -= 1
if ("_" in nykysana):
	print("\nHävisit! Sana oli:",sana)
else:
	print("\nVoitit!!!")