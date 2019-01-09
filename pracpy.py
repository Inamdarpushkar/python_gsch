"Given a string, return a new string where not has been added to the front. However,\
if the string already begins with not,\
return the string unchanged.\
not_string('candy') → 'not candy'\
not_string('x') → 'not x'\
not_string('not bad') → 'not bad'"
def not_string(str):
  if len(str)>=3 and str[:3]=="not":
    return str
  return "not "+str

"Given a non-empty string and an int n, return a new string where the char at index n has been removed.\
The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).\
missing_char('kitten', 1) → 'ktten'\
missing_char('kitten', 0) → 'itten'\
missing_char('kitten', 4) → 'kittn'"
def missing_char(str, n):
  s = str[:n] + str[(n+1):]
  return s

"Given a string, return a new string where the first and last chars have been exchanged.\
front_back('code') → 'eodc'\
front_back('a') → 'a'\
front_back('ab') → 'ba'"
def front_back(str):
  if len(str)<=1:
    return (str)
  return str[-1]+str[1:-1]+str[0]

"Given a string, return a new string made of every other char starting with the first"
def string_bits(str):
  return str[0:len(str):2]

"Given a non-empty string like Code return a string like CCoCodCode"
