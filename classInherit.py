class UpperStr(str):
  def __str__(self):
    return self.upper()

a = UpperStr("abcde")
print(a, type(a), sep="\n")

class OwnException(Exception):
  def __init__(self, message=""):
    Exception.__init__(self, message)

# We may catch an OwnException directly.
try:
  raise OwnException("Our own special exception")
except OwnException as e:
  print("Caught an error:", e)
  print(type(e))
  
# An OwnException will be caught also as an Exception
# due to the fact that it inherits Exception.
try:
  raise OwnException("Our own special exception")
except Exception as e:
  print("Caught an error:", e)
  print(type(e))