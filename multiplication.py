# Receives four positive integers a, b, c and d as parameters.
# Prints out a multiplication table that shows the results of multiplying a number within the interval a..b with a number from the interval c..d.
# Your program may assume that a ≤ b and c ≤ d.
# testnumbers: 1, 10, 11, 20
import sys
def printf(format, *args):
    sys.stdout.write(format % args)

def multiplicationTable(a,b,c,d):
	#ylin rivi
	printf("     ")
	for i in range (a,b+1,1):
		if i==b:
			printf("%3i",i)
		else:
			printf("%3i ",i)
	print()
	
	#taulukko
	for j in range (c,d+1,1):
		printf(" %3i ",j)
		for i in range (a,b+1,1):
		  if i==b:
		    printf("%3i",i*j)
		  else:
			  printf("%3i ",i*j)
		print()
		
def main ():
	multiplicationTable(1, 10, 11, 20)
	
main()