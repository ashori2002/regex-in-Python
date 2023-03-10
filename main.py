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

#____________________________________________________________________

x = re.search("He..o",txt)

print(x)

#____________________________________________________________________

x = re.search("^Hello",txt)

print(x)

#____________________________________________________________________

x = re.search("ri$",txt)

print(x)

#____________________________________________________________________

x = re.search("l{2}",txt)

print(x)

#____________________________________________________________________

x = re.search("^Hello|^Hi",txt)

print(x)

#____________________________________________________________________
number = "0933678987987987"
x = re.search("^093([3]|[5-9])",number)

print(x)

#____________________________________________________________________

x = re.sub("\d"," ",txt)

print(x)

#____________________________________________________________________
test_text = "ASHORI \n \t \r 2002"
x = re.findall(r"\n \t",test_text)

print(x)

#____________________________________________________________________

x = re.search("ASHORI2002",txt)

print(x.span())

#____________________________________________________________________

x = re.search("ASHORI2002",txt)

print(x.string)

#____________________________________________________________________

x = re.search("ASHORI2002",txt)

print(x.group())

#____________________________________________________________________

x = re.search("ASHORI2002",txt)

print(x.span())

#____________________________________________________________________