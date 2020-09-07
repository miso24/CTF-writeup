# matsushima2

## solution

ブラックジャックでディーラーに勝つとchipが2倍になる。chipが999999以上になればフラグが獲得できる。

まず、http://web.kosenctf.com:14001/initialize というURLにPOSTリクエストを送ると、cookieにchipやカードの情報などが設定される。
そして、そのcookieがある状態でhttp://web.kosenctf.com:14001/hit にPOSTリクエストを送るとhit、http://web.kosenctf.com:14001/stand にPOSTリクエストを送るとstandを実行できる。
ゲームの勝敗判定はstandで行われ、自分のポイントがディーラーのポイントより大きければ勝利し、chipが2倍になる。負けると0になる。

http://web.kosenctf.com:14001/nextgame にPOSTリクエストを送ると、カードの情報がリセットされ次のゲームに移ることができる。

standで勝敗判定が行われるが、カードのリセットは行われない。そのため、自分のカードが21になった時に、何度もstandすることで無限に勝つことができる。
chipが999999より多くなった後にhttp://web.kosenctf.com:14001/flag にPOSTリクエストを送ればフラグが手に入る。
