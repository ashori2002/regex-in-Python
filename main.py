import re

txt = "Hello , ASHORI2002 , 123456789"

x = re.search("Hello",txt)

print(x)

#____________________________________________________________________

x = re.search("[1-5]",txt)

print(x)

#____________________________________________________________________

x = re.findall("[1-5]",txt)

print(x)

#____________________________________________________________________

x = re.findall("[1-5]+",txt)

print(x)
#____________________________________________________________________

x = re.findall("[1-5]*",txt)

print(x)

#____________________________________________________________________

x = re.findall("\d",txt)

print(x)

#____________________________________________________________________

x = re.findall("\d+",txt)

print(x)

#____________________________________________________________________

x = re.findall("\d*",txt)

print(x)
