import re

s='akskdjf alskdfj lks d d  hello_world'
reg = re.compile('[a-z]+_[a-z]+')
result = reg.findall(s)
print(result)