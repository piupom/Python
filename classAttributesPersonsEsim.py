# In many cases access to attributes should be directed into function calls (so-called "getters" and "setters") e.g. in order to be able to verify that the values are legal. E.g. here we could expect that the height of a person cannot be negative. Tying an attribute into setter and getter functions can be done in Python by the property-function.
class Person:
  def __init__(self, name="", age=0, height=0, weight=0):
    self.__name = name
    self.__age = age
    self.__height = height
    self.__weight = weight
  
  def bmi(self):
    return self.__weight/((self.__height/100) ** 2)
  
  def __str__(self):
    return ("Name is {:s}\n"
            "Age is {:d}\n"
            "Height is {:.1f}\n"
            "Weight is {:.1f}\n"
            "BMI is {:.2f}").format(
            self.name, self.age, self.height, self.weight, self.bmi())
  
  # The getter for height: this simply returns the __height attribute.
  def getHeight(self):
    return self.__height

  # The setter for height: this sets the received parameter into the __height
  # attribute. The function also prints a message if the height is negative.
  def setHeight(self, height):
    if height < 0:
      print("Height is negative!")
    self.__height = height
  
  # Now define "height" as an attribute that can be accessed with
  # the getter getHeight and the setter setHeight.
  height = property(getHeight, setHeight)

tc = Person("Tom Cruise", 50, 165, 75)
# Set a new value to the attribute "height". This calls tc.setHeight(-165).
tc.height = -165
print("New height:", tc.height)
# It is also possible, but more awkward(?), to call setHeight directly.
tc.setHeight(-25)
print("New height:", tc.height)