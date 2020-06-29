# pseudo-key (448 solves / 341 points)

> Keys are not always as they seem...
>
>  **Note:** Make sure to wrap the plaintext with `flag{}` before you submit!

pseudo-key-output.txt, pseudo-key.pyが添付されていた

## solution

pseudo-key-output.txtは以下の通り

```
Ciphertext: z_jjaoo_rljlhr_gauf_twv_shaqzb_ljtyut
Pseudo-key: iigesssaemk
```

pseudo-key.pyは以下の通り

```python
#!/usr/bin/env python3

from string import ascii_lowercase

chr_to_num = {c: i for i, c in enumerate(ascii_lowercase)}
num_to_chr = {i: c for i, c in enumerate(ascii_lowercase)}

def encrypt(ptxt, key):
    ptxt = ptxt.lower()
    key = ''.join(key[i % len(key)] for i in range(len(ptxt))).lower()
    print(key)
    ctxt = ''
    for i in range(len(ptxt)):
        if ptxt[i] == '_':
            ctxt += '_'
            continue
        x = chr_to_num[ptxt[i]]
        y = chr_to_num[key[i]]
        ctxt += num_to_chr[(x + y) % 26]
    return ctxt

with open('flag.txt') as f, open('key.txt') as k:
    flag = f.read().strip()
    key = k.read().strip()

ptxt = flag[5:-1]

ctxt = encrypt(ptxt,key)
pseudo_key = encrypt(key,key)

assert(ctxt == "z_jjaoo_rljlhr_gauf_twv_shaqzb_ljtyut")
assert(pseudo_key == "iigesssaemk")
print('Ciphertext:',ctxt)
print('Pseudo-key:',pseudo_key)
```

このソースコード から

- Ciphertextは鍵をkeyとしてflagをencryptで暗号化したもの
- Pseudo-keyは鍵をkeyとしてkeyをencryptで暗号化したもの

ということがわかる。

keyがわかれば、flagを求めることができるのでまずはkeyを求める。

以下はkeyを推測するguess_key.pyである。

```python
from string import ascii_lowercase

chr_to_num = {c: i for i, c in enumerate(ascii_lowercase)}
num_to_chr = {i: c for i, c in enumerate(ascii_lowercase)}

cipher = "z_jjaoo_rljlhr_gauf_twv_shaqzb_ljtyut"
pseudo_key = "iigesssaemk"


# guess key
key_dict = {}
for idx in range(len(pseudo_key)):
    c = 0
    key_dict[idx] = []
    while c < 26:
        tmp_c = num_to_chr[(c * 2) % 26]
        if tmp_c == pseudo_key[idx]:
            key_dict[idx].append(num_to_chr[c])
        c += 1
print(key_dict)
```

encryptを実行してkeyの文字になる文字を探しているだけである。

実行すると以下のように出力された

```
{0: ['e', 'r'], 1: ['e', 'r'], 2: ['d', 'q'], 3: ['c', 'p'], 4: ['j', 'w'], 5: ['j', 'w'], 6: ['j', 'w'], 7: ['a', 'n'], 8: ['c', 'p'], 9: ['g', 't'], 10: ['f', 's']}
```

わかりやすいように表にすると

| idx  | 候補1 | 候補2 |
| ---- | ----- | ----- |
| 0    | e     | r     |
| 1    | e     | r     |
| 2    | d     | q     |
| 3    | c     | p     |
| 4    | j     | w     |
| 5    | j     | w     |
| 6    | j     | w     |
| 7    | a     | n     |
| 8    | c     | p     |
| 9    | g     | t     |
| 10   | f     | s     |

この候補の中からそれっぽい組み合わせを見つけてkeyを`redpwwwnctf`だと推測した。

この推測した鍵を使って総当たりで復号するとフラグが手に入った。

```python
from string import ascii_lowercase

chr_to_num = {c: i for i, c in enumerate(ascii_lowercase)}
num_to_chr = {i: c for i, c in enumerate(ascii_lowercase)}

cipher = "z_jjaoo_rljlhr_gauf_twv_shaqzb_ljtyut"

key = "redpwwwnctf"

flag = ""
key = [key[idx % len(key)] for idx in range(len(cipher))]
idx = 0
for idx in range(len(cipher)):
    if cipher[idx] == "_":
        flag += "_"
        continue
    # brute force
    c = 0
    while True:
        x = c
        y = chr_to_num[key[idx]]
        tmp_c = num_to_chr[(x + y) % 26]
        if tmp_c == cipher[idx]:
            flag += num_to_chr[c]
            break
        c += 1
print("flag{" + flag + "}")
```

```
$ python solve.py
flag{i_guess_pseudo_keys_are_pseudo_secure}
```

