from cryptolib.encoding.basex import b64dec

with open('./cipher.txt') as f:
    c = f.read()

for i in range(25):
    c = b64dec(c)

print(c.decode())
