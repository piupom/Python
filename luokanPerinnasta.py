# luokka joka tulostaa itsensä aina isoilla kirjaimilla
# sulkuihin, mitä peritään
class UpperStr(str):
	# pass # tyhjä luokka
	def __init__(self, string=""):
		print("init string:", string, " Upperina:",string.upper())
		#str.__init__(string.upper())
		#return string.upper()
		
	def __str__(self):
		return self.upper()
		
a = UpperStr("abcde")

print(a, type(a))