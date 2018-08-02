def sortRates(currs):
  return map(lambda s: s[0] + " "+ s[2], sorted(map(lambda x: x.strip().split("\t"),currs)))