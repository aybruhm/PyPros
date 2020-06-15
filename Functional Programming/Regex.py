import re

text = "Israelvctory87@gmail.com A random string. Testme@website.com Hello_there"
pattern = re.compile("[a-zA-Z0-9\.\_]+@[a-zA-Z0-9\.\_]+[a-zA-Z]+")

result = pattern.findall(text)
print(result)