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
