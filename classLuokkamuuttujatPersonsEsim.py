class Person:
	#luokka muuttuja
	__id = 0 #Persons.id
	def __init__(self, name="", age=0, height=0, weight=0):
		self.__name = name
		self.__age = age
		self.__height = height
		self.__weight = weight
		self.__id = Persons.id
		Persons.id += 1
  
	def bmi(self):
		return self.__weight/((self.__height/100) ** 2)
  
	def __str__(self):
		return ("Name is {:s}\n"
            "Age is {:d}\n"
            "Height is {:.1f}\n"
            "Weight is {:.1f}\n"
            "BMI is {:.2f}").format(
            self.name, self.age, self.height, self.weight, self.bmi())
  
	@property
	def height(self):
		return self.__height


	@height.setter
	def height(self, height):
		if height < 0:
			print("Height is negative!")
		self.__height = height
		
	@classmethod
	def id():
		return Persons.__id

tc = Person("Tom Cruise", 50, 165, 75)
tc.height = -165
dt = Person("Donald Trump", 10, 11, 12)
put = Persons("Putin", 20, 21, 22)

# The following line gives an error because the "height" attribute cannot
# be used as a function.
tc.height(-25)