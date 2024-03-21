import re
s='akskdjfb alskdbfj lKs. d d  hello_world'
modified_text = re.sub(r'[ ,.]', ':', s)
print("Modified text:", modified_text)