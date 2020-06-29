# inspector-general (1300 solves/ 112 points)

> My friend made a new webpage, can you find a flag?

## solve

与えられたURLにアクセスし、Chormeのデベロッパーツールを開き<head>の中身を見ると

``````
<meta name="redpwnctf2020" content="flag{1nspector_g3n3ral_at_w0rk}">
``````

というmetaタグがあり、フラグは`flag{1nspector_g3n3ral_at_w0rk}`であることがわかる
