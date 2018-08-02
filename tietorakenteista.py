#esimerkkejä tietorakenteista

intlist=[1,2,3,4] #lista
inttuple=(1,2,3,4)#tuple

#joukko:
intset={1,2,3,4}
print(intset) #-> {1,2,3,4}

intset={1,2,3,4,3,2,1}
print(intset) #-> {1,2,3,4} # poistaa tuplat

for i in range(10):
   if i in intset:
      print(i, ' is in itset')
   else:
      print(i, ' is not in itset')

	  
# demotaan tietoranekteen tehokkuutta
intlist = [x for x in range[-5000000, 5000000)] #list compresation tyyppinen lista, hidas isojen määrien käsittelyyn
inttuple = (x for x in range[-5000000, 5000000)) 	#nopea
intset = {x for x in range[-5000000, 5000000)} 		#nopea

print("Values generated....")
matches = 0
mismatches = 0
for i in range(1000000):
   if i in intset:
      matches += 1
   else:
      mismatches += 1
print('matches:',matches, ' mismatches:',mismatches)