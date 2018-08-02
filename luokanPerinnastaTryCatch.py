class OwnException(Exception): #luokan on perittävä jotakin, ilman perittävää tulee virheilmoitus
	# pass
	def __init__(self, message=""):
		Exception.__init__(self, message)
	
try:
	raise OwnException("Oma virheilmoitus: ")
except Exception as e: # Exception on kaikkien virheluokkien ylin luokka
	print("Tuli virhe:",e, type(e))
	
	

# try:
# 	int("abcde")
# except Exception as e: # Exception on kaikkien virheluokkien ylin luokka
#	print("Tuli virhe:",e)