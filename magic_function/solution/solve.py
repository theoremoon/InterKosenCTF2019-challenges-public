# gdb -n -q -x solve.py ./chall
import gdb
import re
import string

gdb.execute("set pagination off", to_string=True)
gdb.execute("b *0x40080b", to_string=True)
gdb.execute("b *0x40082b", to_string=True)
gdb.execute("b *0x400845", to_string=True)

gdb.execute("r " + "A" * 0x18, to_string=True)

flag = ""
for _ in range(0x18):
    al = gdb.execute("p $al", to_string=True).strip().split("= ")[1]
    flag += chr(int(al))
    print(flag)
    gdb.execute("set $bl = {}".format(al), to_string=True)
    gdb.execute("continue", to_string=True)
print(flag)
gdb.execute("quit", to_string=True)
