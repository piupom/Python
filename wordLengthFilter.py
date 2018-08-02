import sys
#Implement your wordLenFilter generator below
def wordLenFilter(filename,length):
  with open(filename) as infile:
    for line in infile:
      for word in line.split():
        if len(word) == length:
          yield word
#Implement your wordLenFilter generator above
for i, word in enumerate(wordLenFilter(sys.argv[1], int(sys.argv[2]))):
  if i > 0 and i % 10 == 0:
    print()
  print(" " + word, end="")
print()