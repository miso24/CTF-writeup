# panda-facts (280 solves/ 412 points)

> I just found a hate group targeting my favorite animal. Can you try and find their secrets? We gotta take them down!

サーバーのソースコードであるindex.jsが添付されていた。


## solution

与えられたURLにアクセスするとUSERNAMEだけ入力できるログインフォームが置かれているだけのサイトにつながった。
ログインしてみると`Click to see a member-only fact!`と書かれたボタンが存在していた。
ログイン時に与えられるtokenのmemberの値が1じゃないと`You are not member`と言われてしまう。

tokenがどのように生成されているかが重要そうだと思ったので、生成部分を覗いた。
以下がそのコード

```javascript
async function generateToken(username) {
    const algorithm = 'aes-192-cbc';
    const key = Buffer.from(process.env.KEY, 'hex');
    // Predictable IV doesn't matter here
    const iv = Buffer.alloc(16, 0);

    const cipher = crypto.createCipheriv(algorithm, key, iv);

    const token = `{"integrity":"${INTEGRITY}","member":0,"username":"${username}"}`

    let encrypted = '';
    encrypted += cipher.update(token, 'utf8', 'base64');
    encrypted += cipher.final('base64');
    return encrypted;
}
```

`username`がそのままtokenに与えられているので`","member":1,"hoge","`のような文字列をusernameとして与えてやればうまくmemberの値を書き換えることができる。

実際に入力し`Click to see a member-only fact!`をクリックするとフラグが表示された`

```
flag{1_c4nt_f1nd_4_g00d_p4nd4_pun}
```

