import sys
def printf(format, *args):
    sys.stdout.write(format % args)

#floatin tarkastus
def is_float(n):
    try:
        float(n)   # Type-casting the string to `float`.
                   # If string is not a valid `float`, 
                   # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True

#integerin tarkastus
def is_int(n):
	try:
		int(n)   # Type-casting the string to `integer`.
                  # If string is not a valid `integer`, 
                   # it'll raise `ValueError` exception
	except ValueError:
		return False
	return True


#annetun arvon tyyppi
taulu=[]
tyyppi=[]
#"four 3 2.3.4", "3.14 -100.8 12b3 99.9F" and ""
#output:
#four=str 3=int 2.3.4=str
#3.14=float -100.8=float 12b3=str 99.9F=str
while True:
	#rivi = input("anna joku arvo: \n (Lopeta=<enter>)\n")
	rivi = input()
	if rivi == '':
		break
	rivi2=rivi.split(" ")

	for x in rivi2:
		taulu.append(x)
		#lisätään luetun arvon tyypit omaan tauluun
		if is_int(x):
			tyyppi.append('int')
		elif is_float(x):
			tyyppi.append('float')
		else:
			tyyppi.append('str')
	tyyppi.append('\n')
	taulu.append('\n')
#esitetään arvojen tyypit	
#esitetään arvojen tyypit	
i=0
tyhja=False
for arvo in taulu:
	if taulu[i] == '\n':
		print ()
		tyhja=False
	else:
		if tyhja :
			printf(' ')
		printf('%s=%s',taulu[i], tyyppi[i])
		tyhja=True
	i+=1

