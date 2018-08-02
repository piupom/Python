# Receives four positive integers a, b, c and d as parameters.
# Prints out a multiplication table that shows the results of multiplying a number within the interval a..b with a number from the interval c..d.
# Your program may assume that a ≤ b and c ≤ d.
# testnumbers: 1, 10, 11, 20
import sys
def printf(format, *args):
    sys.stdout.write(format % args)

#tulostetaan arvottu rivi 
def lottery(arvottu):

	print("Correct numbers:",sep='',end='')
	for a in arvottu:
		print(' ',a,sep='',end='')
	print()

#tarkistetaan ja tulostetaan oikeat numerot
def checkLottery(arvottu,tiketti):
	oikeat = []
	
	for a in arvottu:
		for t in tiketti:
			if int(a) == int(t):
				oikeat.append(a)
	
	print("Ticket:",sep='',end='')
	for t in tiketti:
		print(' ',t,sep='',end='')
	if len(oikeat) == 0:	
		print(' (',len(oikeat), ' correct',sep='',end='')
	else:
		print(' (',len(oikeat), ' correct:',sep='',end='')
	for o in oikeat:
		print(' ',o,sep='',end='')
	print(')')

		
def main():
	#lotto = input()

	lotto=[2, 30, 17, 8, 6, 19, 24]
	lottery(lotto)
	#tickets = input()
	tickets= [[7, 6, 1, 2, 3, 5, 4], [19, 3, 27, 13, 14, 17, 25], [5, 27, 6, 19, 7, 21, 14], [5, 10, 15, 20, 25, 28, 29]]
	for tick in tickets:
		checkLottery(lotto,tick)	
main()