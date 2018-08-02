# python sortedrate.py sortedrate.txt

from sys import argv

rates = {"FIM":6.0}
with open (argv[1]) as infile:
	for line in infile:
		ps = line.split("\t")
		code, name, rate, inrate = ps[0], ps[1], float(ps[2]), float(ps[3])
		rates[code] = rate
print(rates.keys())
print(rates.values())

#sanakirjan (set) läpikäynti
for code in sorted(rates): 
	print(code, rates[code])

code = input("give a currency code:")
try:
	print(" Rate is ",rates[code])		# sanakirjan avaimeen viitataan olemassa olevalla arvolle. muuten se pitää tarkistaa
except KeyError:
	print("No information for",code)

#vaihtoehtoisesti voidaan suoraan katsoa,että onko arvo avainten joukossa
if code in rates:
	print(" Rate is ",rates[code])
else:
	print("No information for",code)
	
#yhtenä rivinä
rates={i: j for i in 