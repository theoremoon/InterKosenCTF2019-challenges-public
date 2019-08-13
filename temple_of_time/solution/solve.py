from urllib.parse import unquote
import re

qs = open("queries.txt").read().strip().split("\n")
password = ""
for q in qs:
    _, param = q.split("=")
    param = unquote(param)
    charcode = re.findall(r"=([0-9]+)", param)[0]

    password += chr(int(charcode))
print(password)
