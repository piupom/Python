# Write a Python function mode(values) that:
# 
#     Receives an iterable collection of values values as a parameter.
#         The actual type of the values does not matter in this question, but all values will be of the same type, 
#         and their type will be comparable (e.g. may use <, > and ==) and hashable (may be used as keys in dict).
#     Returns a list of modes of the values.
#         "Mode" means the most frequent value, ie. the value that occurs most often.
#         Mode is not necessarily unique; more than one value may occur the most times. E.g. the most frequent values in the list [4, 1, 2, 4, 6, 2, 1, 4, 2, 7] are 2 and 4, both occuring 3 times (and all the other values occur less than 3 times).
#         Sort the list into ascending order.
#         Note: return a list even if the mode is unique. In that case the returned list contains only one mode value.
# 
# WETO's test code prints out the input values on one line and the mode(s) on the second line, all of these separated by spaces.
# 
# WETO's first test uses the values [4, 1, 2, 4, 6, 2, 1, 4, 2, 7] and the expected output is:
# Values: 4 1 2 4 6 2 1 4 2 7
# Mode(s): 2 4

from collections import defaultdict

def mode(values):
  counts = defaultdict(int)
  for v in values:
    counts[v] += 1
  maxcount = max(counts.values())
  maxvals = filter(lambda x: x[1] == maxcount, counts.items())
  return list(sorted(map(lambda x: x[0], maxvals)))