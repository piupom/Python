import sys
def printf(format, *args):
    sys.stdout.write(format % args)
#output r = 4, c = 4, h = 3 and w = 4:
    ####    ####
    ####    ####
    ####    ####
####    ####    
####    ####    
####    ####    
    ####    ####
    ####    ####
    ####    ####
####    ####    
####    ####    
####    ####  


r=int(input('the number of rectangle rows: ') )
c=input('the number of rectangle columns: ')
h=input('the height (as character rows) of each single subrectangle: ')
w=input('the width (as characters) of each single subrectangle: ')

c=int(c)
h=int(h)
w=int(w)
kork=h*r
#lev=c*w
#täyte stringit
tyhja=" ".center(w," ")
tayte="#".center(w,"#")
r2=0; #missä rectangle rowssa ollaan menossa

for i in range (1,kork+1,1):
	for j in range (0,c,1):
		if r2%2==0 and j%2==0: # kun regtanle row on parillinen ja columni on parillinen
			printf('%s',tayte)
		elif r2%2!=0 and j%2!=0: # kun regtanle row on pariton ja columni on pariton
			printf('%s',tayte)
		else:
			printf('%s',tyhja)
	if i%h==0:
		r2+=1
	print()