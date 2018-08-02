import sys
def printf(format, *args):
    sys.stdout.write(format % args)
	
h = input()
while h:
	s = input()
	h = int(h)
	#korkeus
	for x in range (0,h,1):
		#leveys
		for y in range (0,h,1):
			if h == 1:
				printf(s)
			#ylä- ja alarivi
			elif y == h/2 and (x == h or x==0):
				printf(s)
			# keskimmäinen rivi
			elif x == h/2 and (y == h or y==0):
				printf(s)
			# muut printattavat merkit
			#elif 
			else:
				printf(' ')
		print()
	print('h oli:',h,' s:',s)
	h = input()

