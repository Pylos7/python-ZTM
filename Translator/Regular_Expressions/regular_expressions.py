import re

pattern = re.compile(r"([a-zA-Z]).([a])") # r is raw string

string = 'search this inside of this text please! Nestor'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

print(a.group(2))