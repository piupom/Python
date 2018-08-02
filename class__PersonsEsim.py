# Some technical notes: (1) if an attribute name begins by two underscores "__", Python will mangle the attribute name so that it cannot be so easily referenced directly from outside of the class definition, (2) Python objects by default store their attributes in a dict-attribute __dict__, (2) the special member function __getattribute__ is called when an attribute is read, and (3) a member function __setattr__ is called when an attribute value is being set. Ie. a reference of form x.y (without assignment) results in the call x.__getattribute(y), and an assignment of form x.y = z will result in the call x.__setattr__(y, z). Implementing these functions allows e.g. to control how/which attributes can be accessed (e.g. it would be possible to define __setattr__ in such manner that new attributes cannot be added to the object). Below is a brief example about __setattr__, which only prints out information about newly added attributes (which is perhaps not too useful). The example has turned the attributes to have two leading underscores, so their names will be mangled by Python (see the output of dir in the end).
class Person:
  def __init__(self, name="", age=0, height=0, weight=0):
    # Using two leading underscores leads into name mangling.
    # E.g. the reference self.__name is ok here inside the class
    # definition, but a reference of form p.__name with some
    # Person-object p in outside code would fail.
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
  
  def __setattr__(self, attr, val):
    if attr not in self.__dict__:
      print("Attribute", attr, "is new!")
    object.__setattr__(self, attr, val)

tc = Person(weight=67, name="Tom Cruise", age=56, height=170)
dt = Person("Donald Trump", 72, 188, 105)
putin = Person("Vladimir Putin", 65, 168, 71)

print(dir(tc))