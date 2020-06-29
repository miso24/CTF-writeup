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
