
#warmup
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
def string_splosion(str):
  j=''
  for i in range(len(str)):
    j=j+str[:i+1]
  return j

"Given a string, return the count of the number of times that a substring length 2 appears in the\
string and also as the last 2 chars of the string,so hixxxhi yields 1 (we won't count the end substring)."

def last2(c):
    if len(c)>2:
        last=c[-2:]
        count=0
        for ind in range(len(c)):
            current=c[ind:ind+2]
            if current==last: 
                count+=1
        return (count-1)
    else:
      return 0


"Given an array of ints, return True if one of the first 4 elements in the array is a 9.\
The array length may be less than 4."

def array_front9(nums):
  count=0
  for num in nums[:4]:
    if num ==9:
      return True
  return False


"Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.\
array123([1, 1, 2, 3, 1]) → True\
array123([1, 1, 2, 4, 1]) → False\
array123([1, 1, 2, 1, 2, 3]) → True"

def array123(li):
  for i in range(len(li)-2):
    if li[i]==1 and li[i+1]==2 and li[i+2]==3:
      return True
  return False


"Given 2 strings, a and b, return the number of the positions where\
they contain the same length 2 substring. So xxcaazz and xxbaaz\
yields 3, since the xx, aa, and az substrings appear in the\
same place in both strings.\
string_match('xxcaazz', 'xxbaaz') → 3\
string_match('abc', 'abc') → 2\
string_match('abc', 'axc') → 0"

def string_match(a, b):
  # Figure which string is shorter.
  shorter = min(len(a), len(b))
  count = 0
  
  # Loop i over every substring starting spot.
  # Use length-1 here, so can use char str[i+1] in the loop
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1
  return count

#Given a string, find the length of the longest
#substring without repeating characters.

def chk(s):
    lmax = 0
    m = []
    for i,v in enumerate(s):
        if v in m:
            while m:
                if v == m.pop(0):
                    break
        m.append(v)
        lmax = max(lmax, len(m))
    return lmax

#incorrect
def chk(s):
    ansss=[]
    mid=[]
    if s=="" or s==" ":
        return 0
    elif len(s)==1:
        return 1
    else:
        for i in  s:
            if i not in mid:
                mid.append(i)
            
            elif i in mid:
                ansss.append(len(mid))
                mid=[mid[-1]]
                if mid[-1] !=i:
                    mid.append(i)
        m=len(mid)
        if len(ansss) !=0 and max(ansss)>m:
            m=max(ansss)
            
            
    ansss1=[]
    mid1=[]
    if s=="" or s==" ":
        return 0
    elif len(s)==1:
        return 1
    else:
        for i in  reversed(s):
            if i not in mid1:
                mid1.append(i)
            
            elif i in mid1:
                ansss1.append(len(mid1))
                mid1=[mid1[-1]]
                if mid1[-1] !=i:
                    mid1.append(i)
        m1=len(mid1)
        if len(ansss1) !=0 and max(ansss1)>m1:
            m1=max(ansss1)
        return max(m,m1)


#Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word
#is in the middle of the out string, e.g. "<<word>>".
def make_out_word(out, word):
  mid=len(out)/2
  return out[:mid]+word+out[mid:]


