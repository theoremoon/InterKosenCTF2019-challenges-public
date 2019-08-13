from Crypto.Util.number import *
import string

with open("out.txt") as f:
    lines = f.read().splitlines()
N = int(lines[0].split(" = ")[1])
e = int(lines[1].split(" = ")[1])
c = int(lines[4].split(" = ")[1])
known_plaintext, flag_len = lines[3].split("the length of the flag = ")
flag_len = int(flag_len) - len("KosenCTF{}") - 1

for c1 in string.printable:
    high_pad = bytes_to_long(known_plaintext.encode() + b"KosenCTF{" + c1.encode() + b"\x00" * flag_len + b"}")
    low_pad = pow(256, 1)


    PR.<x> = PolynomialRing(Zmod(N))
    f = (high_pad + x*low_pad)^e - c
    f = f.monic()
    xs = f.small_roots(X=2^(flag_len*8), beta=1)
    for x in xs:
      print(b"KosenCTF{" + c1.encode() + long_to_bytes(x) + "}")

