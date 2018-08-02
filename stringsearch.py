# Receives three parameters:
#     string
#         The string to be searched for.
#     text
#         The text from which string is searched from. This is a single string. 
#         The text may consist of multiple lines (lines are separated in normal fashion by "\n" characters within the string).
#     caseSensitive
#        A boolean value that tells whether the string search should be case sensitive (= True) or case insensitive (= False).

def StringSearch(search,text,casesen):
	
	lines  = text.split("\n")
	loytyi = []
	l2=''
	s2=''
	lnr=0
	p2=0
	for l in lines:
		lnr +=1
		if casesen:
			l2=l
			s2=search
		else:
			l2=l.lower()
			s2=search.lower()
		paikka= l2.find(s2)
		if paikka >= 0:
			while True:
				loytyi.append([lnr, paikka+p2+1])
				l2=l2[paikka+len(s2):len(l2)]
				p2+=paikka+len(s2)
				paikka= l2.find(s2)
				if paikka < 0:
					break
				
		p2=0
	return loytyi
		
def main():
	#etsi = input()
	#teksti = input()
	#sens = input()
	etsi="smith"
	teksti="Mr Smith is a blacksmith.\nThe Smithsonian Institution is in Washington D.C."
	sens=True #False
	
	loytyi=StringSearch(etsi,teksti,sens)
	
	print (loytyi)

main()