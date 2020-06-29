# bubbly (322 solves / 395 points)

> It never ends

## solution

main関数をghidraででコンパイルすると以下のコードになる

```c
int main(void)

{
  uint32_t i;
  int unused;
  _Bool pass;
  
  setbuf(stdout,(char *)0x0);
  setbuf(stdin,(char *)0x0);
  setbuf(stderr,(char *)0x0);
  puts("I hate my data structures class! Why can\'t I just sort by hand?");
  pass = false;
  while( true ) {
    __isoc99_scanf(&DAT_00102058);
    if (8 < i) break;
    nums[i] = nums[i] ^ nums[i + 1];
    nums[i + 1] = nums[i + 1] ^ nums[i];
    nums[i] = nums[i] ^ nums[i + 1];
    pass = check();
  }
  if (pass == false) {
    puts("Try again!");
  }
  else {
    puts("Well done!");
    print_flag();
  }
  return 0;
}
```
入力値が8より小さいならnums[i]とnums[i+1]の値を入れ替えて、checkという関数を呼び出している。
passがtrueなら`system('cat flag.txt')`を実行してflagを表示する。

check関数は以下の通り

```c
_Bool check(void)

{
  uint32_t i;
  _Bool pass;
  
  i = 0;
  while( true ) {
    if (8 < i) {
      return true;
    }
    if (nums[i + 1] < nums[i]) break;
    i = i + 1;
  }
  return false;
}

````
numsを先頭から順に見て、昇順に並んでいなければfalse、昇順に並んでいればtrueを返す関数である。

numsの中身は`[0x1, 0xa, 0x3, 0x2, 0x5, 0x9, 0x8, 0x7, 0x4, 0x6]`になっている。

以上のことからバブルソートを行なって、どこを入れ替えたかを入力してやれば良いことがわかる。

```python
# solve.py
from pwn import *

arr = [1, 10, 3, 2, 5, 9, 8, 7, 4, 6]

p = remote('2020.redpwnc.tf', 31039)

for i in range(len(arr) - 1):
  for j in range(len(arr) - i - 1):
    if arr[j] > arr[j + 1]:
      p.sendline(str(j))
      arr[j], arr[j + 1] = arr[j + 1], arr[j]
p.sendline(str(10))

print(p.readall().decode())
```
```
$ python solve.py
...
flag{4ft3r_y0u_put_u54c0_0n_y0ur_c011ege_4pp5_y0u_5t1ll_h4ve_t0_d0_th15_57uff}
```
