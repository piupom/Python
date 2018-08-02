# Reads an integer n from the user (use the input-function).
# 
#     Do not give any parameter to input, as that would appear in your program's output.
#     Convert the read input into an integer.

# Prints out the value √i for i = 1, ..., n.
# Each value is printed out on a separate line in the form "sqrt(i): x", where x is the square root of i with i decimals of precision. Set the precision by using the round-function.

i=int(input('Give me an int ') )
for i in range (1,i+1,1):
	print("sqrt(",i,"): ", round (i ** 0.5, i), sep='')