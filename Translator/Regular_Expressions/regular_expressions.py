import re

pattern = re.compile(r"(^[a-zA-Z0-9$%#@]\S{8,})") # r is raw string

string = 'ni4elc'
a = pattern.search(string)





# At least 8 char long
# Contains any sort of letters, numbers, $%#@
#(^[a-zA-Z0-9$%#@]\S{8,})
# Has to end with a number

pattern2 = re.compile(r"[a-zA-Z0-9$%#@]{8,}\d")
password = 'jnfjnjfnjnnn3w'

check = pattern2.fullmatch(password)
print(check)