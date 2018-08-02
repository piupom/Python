# Classes usually contain also functions. The idea is to bundle together not only the data but also the functions that operate on the data. Having common functionality together simplifies code maintenance. One special class member function is a "constructor" (an initializing function), which is called when an object is defined. In Python the constructor is called __init__. All class member functions automatically receive a reference to the object itself as the first function parameter. This first parameter is usually named "self" in Python code; the parameter is similar to "this" e.g. in C/++ or Java (although the latter languages do not include it in the parameter list).
class Person:
  # A constructor for Person that takes the name, age, height and
  # now also weight as parameters. Default parameters are defined
  # so that is also possible to create a Person-object without
  # explicitly providing values for one or more of these attributes.
  def __init__(self, name="", age=0, height=0, weight=0):
    # Note the notation self.x when referring to the attribute x
    # of this currently initialized object.
    self.name = name
    self.age = age
    self.height = height
    self.weight = weight
  
  # Also define a member function bmi that returns the body-mass-index
  # of this person. The function does not take parameters, but as
  # mentioned above, all member functions will receive the self-reference
  # (the function caller does not give it; Python adds it automatically).
  def bmi(self):
    return self.weight/((self.height/100) ** 2)

# Define two Person-objects. The first gives one attribute to the constructor
# and sets the rest separately. The second gives all attributes directly to
# the constructor.
tc = Person(weight=67)
tc.name = "Tom Cruise"
tc.age = 56
tc.height = 170
dt = Person("Donald Trump", 72, 188, 105)

def printPersonObject(person):
  print("Name is", person.name)
  print("Age is", person.age)
  print("Height is", person.height)
  print("Weight is", person.weight)
  print("BMI is", person.bmi())

printPersonObject(tc)
print()
printPersonObject(dt)