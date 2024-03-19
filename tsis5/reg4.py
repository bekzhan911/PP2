import re
s='akskdjf Alskdfj lKs d d  hello_world'
reg = re.compile('[A-Z]+[a-z]+')
result = reg.findall(s)
print(result)