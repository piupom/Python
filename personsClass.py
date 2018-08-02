class Person:
  # Define a class attribute __id with value 0. The name will be mangled due
  # to the two leading underscores.
  # We will use __id to maintain a running number which allows to
  # give unique id numbers to Person-objects.
  __id = 0
  
  def __init__(self, name="", age=0, height=0, weight=0):
    self.__name = name
    self.__age = age
    self.__height = height
    self.__weight = weight
    # Set the id for this new Person-object to be Person__id, and
    # then increment Person.__id (so the next Person-object will
    # get an id that is one larger, and so on). 
    self.__id = Person.__id
    Person.__id += 1
  
  def bmi(self):
    return self.__weight/((self.__height/100) ** 2)
  
  # Now set __str__ also to print the id of the Person-object.
  def __str__(self):
    return ("Id: {:d}\nName is {:s}\n"
            "Age is {:d}\n"
            "Height is {:.1f}\n"
            "Weight is {:.1f}\n"
            "BMI is {:.2f}\n".format(
            self.__id, self.__name, self.__age, self.__height,
            self.__weight, self.bmi()))
  
  # Define a getter for the id. This is a class method, so use the
  # @classmethod decorator directly in front of it.
  @classmethod
  def id(cls):
    return cls.__id

  # As an example, let's define a second getter for the id, but
  # this time without the @classmethod decorator. The result is
  # that this getid-function is a normal function, whose name is
  # tied under the class (needs to be called e.g. as Person.getid()).
  # As this is a normal function, it is not provided with the
  # class parameter. This may be an important difference when using
  # class inheritance.
  def getid():
    return Person.__id

tc = Person("Tom Cruise", 50, 165, 75)
dt = Person("Donald Trump", 72, 188, 105)
putin = Person("Vladimir Putin", 65, 165, 75)
print(tc, dt, putin, sep="\n")

# Both getters work in similar manner when called under the class.
print("Person.id():", Person.id())
print("Person.getid():", Person.getid())
# The class method id() works as such also when called from a Person-object.
# The normal function getid() fails because Python automatically
# tries to give the object self reference as a first parameter, which
# our getid()-function does not accept. This results in a TypeError.
print("tc.id():", tc.id())
print("tc.getid():", end=" ")
print(tc.getid())