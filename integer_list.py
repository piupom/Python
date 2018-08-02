
def listIntegers(file):
	numbers = []
	with open(file,encoding="utf-8") as infile:
		for rivi in infile:	
			for sana in rivi.split(): #luetaan sana kerrallaan
				#if int(sana) == sana:
				if sana.isdecimal() == True:
					#numbers.append(int(sana))
					numbers.append(sana)
	return numbers
		
def main():

	file="numbers.txt"
	integers = listIntegers(file)
	print (integers)
main()