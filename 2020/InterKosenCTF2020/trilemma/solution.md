# trilemma

## solution

main.cというC言語のソースコードとlibemperor.so, libcitizen.so, libslave.soという3つの動的ライブラリが渡される。

libslave.soはlibcitizen.soが共有オブジェクトに存在すると、

```
[libslave.so] Citizen despises slave.
```

と表示してプログラムを終了し、libcitizen.soはlibemperor.soが共有オブジェクトに存在すると、

```
[libcitizen.so] Emperor manipulates cit
```

と表示してプログラムを終了し、libemperor.soはlibslave.soが共有オブジェクトに存在すると、

```
[libemperor.so] Slave makes revolution.
```

と表示してプログラムを終了する。

そのため、それらの文字列を直接弄って強制終了しないようにした。
すると、今度はResource conflictsが発生するようになり、どうしたらいいのかわからなくなったのでgdbを使って気合で調べた。

```
# slave_flag実行後
[----------------------------------registers-----------------------------------]
RAX: 0x3fcc00000000 ("ty_of_four-fifths}")
RBX: 0x0
RCX: 0xba
RDX: 0x0
RSI: 0x0
RDI: 0x16c
RBP: 0x7fffffffe240 --> 0x555555554860 (<__libc_csu_init>:      push   r15)
RSP: 0x7fffffffe230 --> 0x0
RIP: 0x555555554826 (<main+12>: mov    r12,rax)
...

# citizen_flag実行後
[----------------------------------registers-----------------------------------]
RAX: 0x3fee00000000 ("ns_with_a_probabili")
RBX: 0x0
RCX: 0xe6
RDX: 0x69 ('i')
RSI: 0x69 ('i')
RDI: 0xf9
RBP: 0x7fffffffe240 --> 0x555555554860 (<__libc_csu_init>:      push   r15)
RSP: 0x7fffffffe230 --> 0x0
RIP: 0x55555555482e (<main+20>: mov    rbx,rax)
...

# jump *main+23を実行し、無理やりemperor_flagを実行した結果
The flag is KosenCTF{emperor_wi(null)1HPTL
```

これらの結果をあわせると、KosenCTF{emperor_wins_with_a_probability_of_four-fifths}となりフラグを得られた。
