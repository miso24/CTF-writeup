# 12-shades-of-redpwn (236 solves / 429 points)

> Everyone's favorite guess god Tux just sent me a flag that he somehow encrypted with a color wheel!
>
> I don't even know where to start, the wheel looks more like a clock than a cipher... can you help me crack the code?

ciphertext.jpg, color-wheel.jpgが添付されていた

## solution

以下の画像がciphertext.jpgである。

![](./ciphertext.jpg)

以下の画像がcolor-wheel.jpgである。

![](./color-wheel.jpg)

黄色を0として時計回りにオレンジが1、濃いオレンジが2...黄緑が11のように番号を振る。

2つ並んだ色付き正方形を12進数?だととらえて左側の色の番号に12かけたものと右側の色の番号を足す。

例えば、一番左の青・紫だと青が8、紫が6なので`12 * 8 + 6 = 102`となり、ASCIIコードから文字に直すと`f`になる。

これを全ての色付き正方形の組み合わせに対して行う。人力でやるのはさすがに面倒くさいのでPythonにやらせた。

```python
from PIL import Image
import math

# get palette
pal_img = Image.open('./color-wheel.jpg')

base_x = pal_img.width // 2
base_y = pal_img.height // 2
r = pal_img.width // 2 - 20

pal_data = pal_img.getpalette()
palette = []
for i in range(12):
    theta = math.radians(90 - i * (360/12))
    x = int(base_x + math.cos(theta) * r)
    y = int(base_y - math.sin(theta) * r)
    p = pal_img.getpixel((x, y))
    palette.append(tuple(pal_data[p*3:p*3+3]))

# パレットの中から一番近い色のindexを返す 
def search_nearest(col):
    idx = 0
    min_ = 999999
    for i, p in enumerate(palette):
        tmp = abs(p[0] - col[0]) + abs(p[1] - col[1]) + abs(p[2] - col[2])
        if min_ > tmp:
            idx = i
            min_ = tmp
    return idx

img = Image.open('./ciphertext.jpg')

block_num_x = 24 * 3 + 1
block_num_y = 3
block_width = img.width // block_num_x
block_height = img.height // block_num_y

d = []
for i in range(block_num_x - 1):
    if i % 3 == 0:
        continue
    x = block_width * i + block_width // 2
    y = block_height + block_height // 2
    pixel = img.getpixel((x, y))
    d.append(search_nearest(pixel))

flag = ""
for i in range(len(d) // 2):
    flag += chr(d[i*2] * 12 + d[i*2+1])

print(flag)
```

```
$ python solve.py
flag{9u3ss1n9_1s_4n_4rt}
```

