from sys import argv

nums = set() # tähän tapaan tehdään tyhjä joukko
for i in map(float,argv[1:]):
	nums.add(i)
print("nums-setti:",nums)

print("nums-setti sortattuna:")
for i in sorted(nums):
	print(i)

#avain alkio parien käsittelyä
nums = {'abba':'silli'}
for idx, i in enumerate(map(float,argv[1:])):
	nums[idx]=i
print("uusi nums-setti:",nums)
