
taulu=[]
while True:
	line=input('Give me an year ')
	if line == '':
		break
	taulu.append(line)

for arvo in taulu:
#Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400. For example, the years 1700, 1800, and 1900 were not leap years, but the years 1600 and 2000 were.
# 1900  2016  2000  1958
	if (int(arvo)%4 == 0 and (int(arvo)%100 != 0 or int(arvo)%400 == 0)):
		print ("The year",arvo,"is a leap year")
	else:
		print ("The year",arvo,"is not a leap year")
	

WETOS VERSIO
vuodet=[]
while True:
	line=input()
	if line == '':
		break
	vuodet.append(line)
for year in vuodet:
	if (int(year)%4 == 0 and (int(year)%100 != 0 or int(year)%400 == 0)):
		print ("The year",year,"is a leap year.")
	else:
		print ("The year",year,"is not a leap year.")