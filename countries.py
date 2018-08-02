def readCountries(file):
	countries = []
	c=[]
	with open(file,encoding="utf-8") as infile:
		for rivi in infile:	
			c = rivi.split("\t") #luetaan sana kerrallaan
			countries.append(c[0])
	#countries = sorted(countries, key=lambda mj: (len(mj), mj), countries) 
	countries = sorted(countries,reverse=True)
	countries = sorted(countries, key=pituus)
	#countries = sorted(countries,reverse=True)
	for c in countries:
		print(c)
#usemman alkion sorttaus
def pituus(mj):
  return(-len(mj)) 
def pituusAakkoset(mj):
  return(-len(mj), mj)   
  
def main():

	file="coutries.txt"
	countries = readCountries(file)

main()

## ja toinen
def readCountries(file):
	countries = []
	c=[]
	with open(file,encoding="utf-8") as infile:
		for rivi in infile:	
			c = rivi.split("\t") #luetaan sana kerrallaan
			countries.append(c[0])
	#countries = sorted(countries, key=lambda mj: (len(mj), mj), countries) 
	countries = sorted(countries,reverse=True)
	countries = sorted(countries, key=pituus)
	#countries = sorted(countries,reverse=True)
	
	#for c in countries:
	#	print(c)
	countries.sort(key=laji)
	print("\n".join(countries))

def laji(maa):
  return(-len(maa), maa)

def pituus(mj):
  return(-len(mj)) 
 
def main():

	file="countries.txt"
	countries = readCountries(file)

main()