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
