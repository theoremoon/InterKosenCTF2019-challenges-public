from binascii import hexlify, unhexlify
import sys
import struct


def f(x, i, p):
    a = ((p >> 4) & 0xFF) << 8
    b = (((p >> 12) | (p << 4)) & 0xFF) << 8
    c = (((x << 4) & 0xFF) | (x >> 4)) + 1
    d = (((~i) << 4) | (i >> 4)) & 0xFF

    return (a ^ b) | (c ^ d)


bs = sys.argv[1].encode("ascii")
result = []
p = 0x1234
for i, b in enumerate(bs):
    p = f(b, i, p)
    result.append((p & 0xFF00) >> 8)
    result.append(p & 0xFF)

print(hexlify(bytes(result)).decode("ascii"))
