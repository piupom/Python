#lasketaan annetusta tekstistä pisin ja lyhin sana. tulostetaan myös nämä valitut sanat
minlen=1000000
maxlen=0
minw=''
maxw=''
smallest=0
largest=0
smallestw=''
largestw=''
lauseet=[]
# as a class take less sleep than labor ers sleep is sounder and longer in cold climates and among northern races women usually take more sleep than men the influence of habit is noticeable when the demand for sleep
#output: "Min length: minlen (minlenw), Max length: maxlen (maxlenw), Smallest: minw, Largest: maxw"
while True:
	rivi = input("anna joku arvoitava teksti: \n (Lopeta=<enter>)\n")

	if rivi == '':
		break

	rivi2=rivi.split(" ")

	for x in rivi2:
		if len(x) < minlen:
			minlen=len(x)
			minw=x
		elif len(x) >maxlen:
			maxlen=len(x)
			maxw=x
		lauseet.append(x)

#esitetään lopputulos	
print("Min length:", minlen,"(",minw,") Max length: ", maxlen,"(",maxw,") Smallest: ", sorted(lauseet)[0]," Largest:", sorted(lauseet)[-1])

Min length: 1 (a), Max length: 10 (noticeable), Smallest: a, Largest: women testi0
Min length: 1 (a), Max length: 10 (noticeable), Smallest: a, Largest: women
Incorrect result (more details not shown for private test)    Testi2