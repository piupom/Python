#Sudokuruudukkoon numerot
num='823957416674821593951654287486215739539768124217349865762583941345192678198476352'
i=0 #järjestys luku stringissä
j=1 #lohkojen lukumäärä
pituus=len(num) #stringin pituus


print('\nSudoku\n')
for j in range (0,3,1):
	print("#####################################")
	print('#',num[i], '|', num[i+1], '|', num[i+2], '#',num[i+3], '|', num[i+4], '|', num[i+5],'#',num[i+6], '|', num[i+7], '|', num[i+8], '#')
	i+= 9
	print("#---+---+---#---+---+---#---+---+---#")
	print('#',num[i], '|', num[i+1], '|', num[i+2], '#',num[i+3], '|', num[i+4], '|', num[i+5],'#',num[i+6], '|', num[i+7], '|', num[i+8], '#')
	i+= 9
	print("#---+---+---#---+---+---#---+---+---#")
	print('#',num[i], '|', num[i+1], '|', num[i+2], '#',num[i+3], '|', num[i+4], '|', num[i+5],'#',num[i+6], '|', num[i+7], '|', num[i+8], '#')
	i+= 9
print("#####################################")

	
	

	

  
  

  