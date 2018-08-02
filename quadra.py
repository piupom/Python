#Reads three floating point values a, b and c from the user (from standard input; e.g. keyboard).
#The values a, b and c are assumed to be on three separate lines, so read them by three separate input() calls.

#Computes the solution(s) to the quadratic equation ax2+bx+c=0
#, where the coefficients a, b and c are specified by the values read from the user.
#The equation may have 0, 1 or 2 distinct real solutions. Depending on the case, your program should print one of the following outputs:

#   "The equation ax^2 ± bx ± c = 0 has no real solution!"
#    "The equation ax^2 ± bx ± c = 0 has one distinct real solution: x = s1"
#    "The equation ax^2 ± bx ± c = 0 has two distinct real solutions: x = s1 and x = s2"
# input
#"1", "-0.5" and "-1.5" -> "The equation x^2 - 0.5x - 1.5 = 0 has two distinct real solutions: x = -1 and x = 1.5"
# "-1.25", "2.5" and "-1.25" -> "The equation -1.25x^2 + 2.5x - 1.25 = 0 has one distinct real solution: x = 1"
#"2", "0" and "2" -> "The equation 2x^2 + 2 = 0 has no real solution!"

a=float(input('Give me an a: ') )
b=float(input('Give me an b: ') )
c=float(input('Give me an c: ') )
s1=0.0; s2=0.0
s=0.0

#a=float(input() )
#b=float(input() )
#c=float(input() )

if (b*b-(4*a*c))<0:
	print('The equation ',a, 'x^2 + ',c, ' = 0 has no real solution!', sep='')
elif (b*b-(4*a*c))==0:
	s1 = (-1*b)/(2*a)
	if int(s1):
		s1 = int(s1)
	print('The equation ',a, 'x^2 + ',b,'x - ',c, ' = 0 has one distinct real solution: x =', s1, sep='')
else:
	s=(b*b-(4*a*c))**0.5
	s1 = ((-b + s)/(2*a))
	s2 = ((-b - s)/(2*a))
	if int(s1)==s1:
		s1 = int(s1)
	else:
		s1=round(s1,1)
	if int(s2)==s2:
		s2 = int(s2)
	else:
		s2=round(s2,1)
	if s1 == 1:
		s1=''
	if s2==1:
		s2=''
	if a==1:
		a=''
	if b==1:
		b=''
	if c==1:
		c=''
	print('The equation ',a, 'x^2 - ',b,'x - ',c, ' = 0 has two distinct real solutions: x = ', s2,' and x= ',s1,sep='')
