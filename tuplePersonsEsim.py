# It is often convenient to bundle several pieces of data together. E.g. if the code processes information about people, then each person's information (name, age, etc.) could be bundled. This can be done in a naive manner with e.g. a tuple (also shown below), but classes provide a more convenient way. A class definition defines a new data type that can have several attributes (named pieces of data) and/or member functions. A variable whose type is a class is called an object. If x is an object, then the notation x.y refers to the attribute y (or member function) of x.

# A tuple that represents a person's name, age and height.
personTuple = ("John Doe", 45, 180)

# A class meant for representing a person. This is a minimal class:
# the body is left empty (the pass-statetement is a place-holder that
# does not do anything; Python syntax does not allow a literally empty body).
class Person:
  pass

# An object of class X can be created with the notation X(parameters),
# where parameters may or may not be required (depends on the class).
# Python classes by default allow to "define" new attributes on-the-fly,

# that is, attributes do not need to be predefined by the class definition.
# Below we set values into the attributes name, age and height of personObject.
personObject = Person()
personObject.name = "Tom Cruise"
personObject.age = 50
personObject.height = 165
personObject.weight = 75

# Printing out the type of personObject reveals that it is of type
# class Person.
print(type(personObject))

# One of the reasons why the naive tuple-representation of a person
# is awkward: we need to remember which index corresponds to which
# attribute, which is prone to accidental programming errors.
# As an example, this function prints out a person's attributes.
def printPersonTuple(person):
  print("Name is", person[0])
  print("Age is", person[1])
  print("Height is", person[2])

# A similar function as above, but using the Person-class. Named
# attribute references are much more readable.
def printPersonObject(person):
  print("Name is", person.name)
  print("Age is", person.age)
  print("Height is", person.height)

printPersonTuple(personTuple)
print()
printPersonObject(personObject)