def listLenWords(file,length):
	words = []
	w=[]
	w2=""
	i=1
	with open(file,encoding="utf-8") as infile:
		for rivi in infile:	
			w = rivi.split(" ") #luetaan sana kerrallaan
			for w2 in w:
				if len(w2) == length:
					words.append(w2.strip())
	print (words)
	for w in words:
		if i%10 == 0:
			print(w)
			i=1
		else:
			print(w," ",end='')
			i+=1
 
  
def main():

	file="words.txt"
	countries = listLenWords(file,7)
	print

main()