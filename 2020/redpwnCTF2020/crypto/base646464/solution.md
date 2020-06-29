# base646464 (1023 solves / 145 points)

> Encoding something multiple times makes it exponentially more secure!

cipher.txt, generate.jsが添付されていた

## solution

generate.jsは以下の通り

```javascript
const btoa = str => Buffer.from(str).toString('base64');

const fs = require("fs");
const flag = fs.readFileSync("flag.txt", "utf8").trim();

let ret = flag;
for(let i = 0; i < 25; i++) ret = btoa(ret);

fs.writeFileSync("cipher.txt", ret);
```

flag.txtを読み込んで25回base64エンコードして、cipher.txtとして出力しているだけである。

よって、cipher.txtに対して25回base64デコードを行えばフラグが手に入る

```python
# solve.py
from cryptolib.encoding.basex import b64dec

with open('./cipher.txt') as f:
    c = f.read()

for i in range(25):
    c = b64dec(c)

print(c.decode())
```

```
$ python solve.py
flag{l00ks_l1ke_a_l0t_of_64s}
```

