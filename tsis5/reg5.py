import re
s='akskdjfb alskdbfj lKs d d  hello_world'
reg = re.compile('a.*b')
result = reg.findall(s)
print(result)