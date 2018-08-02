# Receives a string s and an integer n as command line parameters.
# Prints out all substrings of s sorted primarily into descending order of length, and secondarily into ascending alphabetic order.
# Programming, 5
from sys import argv
s=argv[1]
n=int(argv[2])
subs = []
for i in range(len(s)):
  for j in range(i+1, len(s)+1):
    subs.append(s[i:j])
#lajittelu
subs = sorted(subs, key=lambda x: (-len(x), x)) # lajitteluavain kakispaikkaiseksi tupleksi, eka ervo pituus ja toinen arvo merkkijono itsessään
for i in range(0,len(subs),n):
  print(" ".join(subs[i:i+n]))