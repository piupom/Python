# Classes have also other "special" functions. One common is __str__, which defines how to represent the object in string format (e.g. what is printed out if the object is passed to the print-function). Here we transform the printPersonObject-function from above into a __str__-member function. Now Person-objects can be printed directly with print.
class Person:
  def __init__(self, name="", age=0, height=0, weight=0):
    self.name = name
    self.age = age
    self.height = height
    self.weight = weight
  
  def bmi(self):
    return self.weight/((self.height/100) ** 2)
  
  # If p is a Person-object, then the string-transformation call str(p)
  # will result in calling this __str__ -function. The function implementation
  # should return a string. Here we use also string formatting to set the
  # number of printed decimals.
  # Note: the way the string is split on several lines here works because the
  # strings are enclosed within parentheses.
  def __str__(self):
    return ("Name is {:s}\n"
            "Age is {:d}\n"
            "Height is {:.1f}\n"
            "Weight is {:.1f}\n"
            "BMI is {:.2f}").format(
            self.name, self.age, self.height, self.weight, self.bmi())

tc = Person(weight=67, name="Tom Cruise", age=56, height=170)
dt = Person("Donald Trump", 72, 188, 105)

# These print-calls will print the strings returned by tc.__str__() and
# dt.__str__(), respectively.
print(tc)
print()
print(dt)

# A side-note: the dir-function lists all attributes/functions of a class object.
print(dir(dt))