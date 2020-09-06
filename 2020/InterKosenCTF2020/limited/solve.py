from collections import defaultdict
from cryptolib.number import crt
import re

pattern = 'secret%2C\+([0-9]{1,2}).+\+([0-9]{1,2})$'

result = defaultdict(list)

data = open('./sqli').read().rstrip()
for d in data.split('\n'):
    n, mod = re.search(pattern, d).groups()
    with open("extract/" + d) as f:
        html = f.read()
        result[int(n)].append(
            (int(mod), len(re.findall("<th scope=\"row\">", html)))
        )

result = sorted(result.items(), key=lambda x: x[0])

flag = ""
for _, val in result:
    nl = [v[0] for v in val]
    al = [v[1] for v in val]
    flag += (chr(crt(nl, al)))
print(flag)
