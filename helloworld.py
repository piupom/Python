print('Hello')
print("   'Hello, World!' \" \nja uudelleen")
print('-------------------')
print('muuttjien käsittelystä')
x=4
x='neljä'
print('   ',x)
print('-------------------')
print('laskutoimitukset')
x=4
y=5
z=x*y
print(z)
print('-------------------')
print('viittauksista')
print('    ',id(x),id(y))
print('-------------------')
print('printtauksista')
print('    ',y,id(y), sep='')

print('-------------------')
print('loopeista')

if 5 > 2:
  print("Five is greater than two!")

for x in range(1,10,2):
  print("x:",x)

# for i in range(0,10,1): 
#	j=0
#	while(j<10):
#		print('i ja j', str(i) , str(j))
#		j += 1

print('-------------------')
print('listoista')
t10=[0]*10
t10=[0,1,2,3,4,5,6,7,8,9]
print(t10, type(t10))	
del t10[len(t10)-1]
print(t10)
t10.append([1,2,3])
print(t10)
print(t10[9][1])

print('-------------------')
print('inputtii')
rivi=input('anna rivi ')
print (rivi)
#talletetaan komennot taulukkoon
while True:
	rivi=input('anna komento: \n (Lopeta=l)\n')
	if rivi ='l'
		break
	taulu.append(rivi)
print(taulu)

	

