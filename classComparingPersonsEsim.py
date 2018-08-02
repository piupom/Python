# The output received from dir reveals e.g. that classes also contain special functions for comparing their objects: __lt__, __gt__, __le__, __ge__, __eq__ and __ne__ correspond to the comparison-operators <, >, <=, >=, == and !=, respectively. E.g. a comparison p1 < p2 between objects p1 and p2 will result in the call p1.__le__(p2). Providing implementations for these functions allows to use the comparison operators with objects.

class Person:
  def __init__(self, name="", age=0, height=0, weight=0):
    self.name = name
    self.age = age
    self.height = height
    self.weight = weight
  
  def bmi(self):
    return self.weight/((self.height/100) ** 2)
  
  def __str__(self):
    return ("Name is {:s}\n"
            "Age is {:d}\n"
            "Height is {:.1f}\n"
            "Weight is {:.1f}\n"
            "BMI is {:.2f}").format(
            self.name, self.age, self.height, self.weight, self.bmi()) 
  
  # Define a less-than comparison that compares Person-objects based
  # on their last names (which is assumed to be the last word within
  # their names).
  def __lt__(self, other):
    lastA = self.name.split()
    lastA = lastA[-1]
    lastB = other.name.split()
    lastB = lastB[-1]
    return lastA < lastB
    
tc = Person(weight=67, name="Tom Cruise", age=56, height=170)
dt = Person("Donald Trump", 72, 188, 105)
putin = Person("Vladimir Putin", 65, 168, 71)

# Now that we have < implemented, it is possible to e.g. sort
# Person-objects (Python's sorting functions compare items with
# the less-than # operator <, so having implemented only it is enough).
# Below the persons will be sorted into the order Cruise, Putin, Trump.
persons = [tc, dt, putin]
for person in sorted(persons):
  print(person, end="\n\n")