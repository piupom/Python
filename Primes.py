# Reads two integers, n and k, from the user (standard input / keyboard).
# Read the values from separate lines: n from the first input line and k from the second.
# Prints out, in ascending order, every k:th prime number that is smaller or equal to n.

#    The printed prime numbers are separated from each other by a single space.
#    Every k:th: print the first prime, skip the next k-1 primes, print the next prime, skip again the next k-1 primes, and so on
import sys
def printf(format, *args):
    sys.stdout.write(format % args)
	
def is_prime(num):
    """Returns True if the number is prime
    else False."""
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True
		
n=int(input('Give me an int ') )
k=int(input('Give me an other int ') )

#alkuluvut
primes=[]
for d in range (2,int(n)+1, 1):
	if is_prime(d):
		primes.append(d)		
#tulostus
for d in range (0,  len(primes) , int(k)):
	printf('%i ',primes[d]) 
print()