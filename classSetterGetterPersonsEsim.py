# Attributes can be tied to setter and getter functions also in a slightly more direct manner, using so-called decorators. The code below defines a similar height attribute as the code above, but now with decorators. One practical difference is that this version does not allow to call the getter or setter functions directly.
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
  
  # A decorator is a "header-line" starting with @ that is placed
  # directly above the function definition. The effect of the 2 lines
  #   @some_decorator
  #   def some_function(parameters):
  # is the same as if the following line would have been added right after
  # the definition of some_function:
  #   some_function = some_decorator(some_function)
  # That is, a decorator states that the function should be replaced by a
  # function returned by the decorator function.

  # The @property decorator below has the effect of defining the following
  # function as a setter for an attribute with that function's name (here "height").
  @property
  def height(self):
    return self.__height

  # The decorator above has the same effect as if we had included the line
  #   height = property(height)
  # here (without indentation).

  # A decorator of form @name.setter defines that the following function
  # is a setter for the attribute "name" (here "height"). The function
  # has to have the same name as the corresponding attribute (again, "height").
  # A separate definition for the attribute "height" itself is not needed.
  @height.setter
  def height(self, height):
    if height < 0:
      print("Height is negative!")
    self.__height = height

tc = Person("Tom Cruise", 50, 165, 75)
tc.height = -165
print("New height:", tc.height)

# The following line gives an error because the "height" attribute cannot
# be used as a function.
tc.height(-25)