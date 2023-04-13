import re

string = "RR_STAID000001.txt"
pattern = "[0-9]+"

x = re.findall(pattern, string)
print(x)
