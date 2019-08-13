from ptrlib.pwn.sock import Socket
from Crypto.Util.number import long_to_bytes, bytes_to_long
from math import gcd
from logging import getLogger
import os

m1 = "1" * 120
m2 = "1" * 120 + "2"

sock = Socket(
    os.getenv("CHALLENGE_HOST", "localhost"), int(os.getenv("CHALLENGE_PORT", "8002"))
)
_ = sock.recvline()
enc = int(sock.recvline().decode().strip())

_ = sock.recvline()

sock.recvuntil("> ")
sock.sendline(m1)
_ = sock.recvline()
c1 = int(sock.recvline().decode().strip())

sock.recvuntil("> ")
sock.sendline(m2)
_ = sock.recvline()
c2 = int(sock.recvline().decode().strip())

n = gcd(c1 - 1, c2 - 1)

print(bytes.fromhex(hex((enc - 1) // n)[2:]).decode())
