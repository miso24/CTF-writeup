from itertools import product

buf = open('./buf').read()

expected_pos = 0xB77C7C

pos = 0
result = None

for p in product(range(4), repeat=0xB):
  pos = 0
  for i in p:
    pos += i + 1
    pos <<= 2
  if pos == expected_pos:
    result = p
    break

pos = 0
flag = ""
for p in result:
  flag += buf[p + pos]
  pos += p + 1
  pos <<= 2
print("KosenCTF{" + flag + "}")
