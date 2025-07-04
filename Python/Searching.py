import re

txt = "rains in banglore"
x = re.search("rains", txt)
if x:
    print("Yes, there is a match")
else:
    print("No match")

text = "The canteen of VVCE in Mysore"
y = re.findall("e", text)
print(y) 