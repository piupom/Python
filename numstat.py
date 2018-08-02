# tauluun käyttäjän antamat luvut ja lasketaan niillä jotain
#output: Minimum 1.5, maximum 5.0, sum 12.5 and mean 3.125
import statistics
taulu=[]
minnum=0
maxnum=0
summa=0
ekakerta=True
print('Tulosteaan annetuista luvuista pienin ja isoin sekä annetaan keskiarvo kaikista')
while True:
	rivi=input('anna joku luku:(Lopeta=<enter>)\n')
	if rivi == '':
		break
	#ValueError tyyppinen virhe tulee, jos täyttää jotain muuta kun numeroita
	#myöhemmässä vaiheessa koodia
	#yritetään tässä kohtaa saada virheestä kiinni
	try:
		luku = float(rivi)
		taulu.append(luku)
		if ekakerta:
			minnum=luku
			maxnum=luku
			ekakerta=False
		if minnum>luku:
			minnum=luku
		if maxnum<luku:
			maxnum=luku
		summa += float(luku)
	#jos ao. kaltainen virhe tulee, regoidaan
	except ValueError:
		print(rivi, ' ei ole luku.')
#tulosteaan annetuista luvuista pienin ja isoin ja annetaan keskiarvo kaikista	
print('Minimum ', minnum, ', maximum ', maxnum, ' sum ',summa,' and mean ',statistics.mean(taulu))