import sys
def printf(format, *args):
    sys.stdout.write(format % args)
	
# a = -1, b = 2, c = 3 and d = 7
# a = 2, b = -1, c = 7 and d = 3

a = int(input())
b = int(input())
c = int(input())
d = int(input())

iStep = 1 if a < b else -1 # javassa:  iStep = (a < b) ? 1 : -1
jStep = 1 if c < d else -1
for i in range (a,b+iStep, iStep):	
	for j in range (c, d + jStep, jStep):
		printf('(%d,%d)',i,j)
	print()