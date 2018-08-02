# input:  10000 1.5 4 2
s = float(input()) 	# savings year 0
i = float(input()) 	# interest rate
n = int(input()) 	# years
p = int(input())	# output precision
for y in range(0,n+1, 1):
	if y==0:
		print('Year ',y,': ',round(s,p),sep='')
	else:
		print('Year ',y,': ',round(s*i/100+s,p),sep='')
		s=s+s*i/100
	