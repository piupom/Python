# USD x EUR set 1 dollar value to euro
# EUR x USD 1 euro equals x US dollars
# x USD Converts x US dollars into euros
# x EUR Converts x euros into US dollars.
# quit 

#input:
# 13.5 Usd
# Usd 0.9068 Eur
# 13.5 usd
# 125 EUR
# EUR 0.8424 USD
# 125 eur
# quit!
# quit
import sys
def printf(format, *args):
    sys.stdout.write(format % args)

usd_eur=float (0)
eur_usd=float(0)
value=float(0)
ok=True
while True:
	#rivi = input()
	rivi = input("Give a command: ")
	if rivi == 'quit':
		break
	com = rivi.split(" ")
	# print(com,' ',com[0].upper(),com[2].upper())
	
	# konvertointi
	if len(com) <=1 or len(com) >3:
		print('Illegal command!')
	elif com[1].upper() =='EUR':
		if eur_usd==float(0):
			print("No EUR-USD rate defined yet!")			
		else:
			value=eur_usd*float(com[0])
			printf("%.6f EUR = %.6f USD\n", float(com[0]), value)
	elif com[1].upper()=='USD':
		if usd_eur==float(0):			
			print("No USD-EUR rate defined yet!")			
		else:
			value=usd_eur*float(com[0])
			printf("%.6f USD = %.6f EUR\n", float(com[0]), value)
	#valuutta
	elif (com[0].upper() == 'USD') and (com[2].upper() == 'EUR'):
		usd_eur=float(com[1])
	elif (com[2].upper() == 'USD') and (com[0].upper() == 'EUR'):
		eur_usd=float(com[1])
	else:
		print('Illegal command!')