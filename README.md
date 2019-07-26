# コーディングスキル演習 課題 



## 課題 1 当たり判定 -> Task01_Judgment.py

当たらない条件

 - 敵機の`x+幅`が自機の`x`より小さい
 - 敵機の`x`が自機の`x+幅`より大きい
 - 敵機の`y+高さ`が自機の`y`より小さい
 - 敵機の`y`が自機の`y+高さ`より大きい

なので、いずれにも該当しない場合標準出力を行う。



for example

```bash
$ python Task01_Judgment.py
> 100 100 70 100
> 3
> 50 60 100 50
> 10 120 100 50
> 165 115 70 70
敵機1が当たり
敵機3が当たり
```





## 課題 2 カードゲームの役を判定する  -> Task02_poker.py

標準入力を`suits`と`numbers`として受け取り、各役の条件と突き合わせ、該当した役を標準出力する。



for example

```bash
$ python Task02_poker.py
> 0 01
> 3 06
> 3 10
> 3 01
> 1 01
SA HA CA H6 H10
スリーカード
```



## 課題 3 カードゲームの役を判定する  -> Task03_eightQueen.py

動的計画法っぽい感じで再帰的に次の行のクイーンを置ける列を求める。

置けないあるいは置ききれた場合は一つ前の行からやり直す。



for example

```bash
$ python Task03_eightQueen.py
□□□□□□□Q
□□Q□□□□□
Q□□□□□□□
□□□□□Q□□
□Q□□□□□□
□□□□Q□□□
□□□□□□Q□
□□□Q□□□□
--------------------
...
□□□□□□□Q
□□□Q□□□□
Q□□□□□□□
□□Q□□□□□
□□□□□Q□□
□Q□□□□□□
□□□□□□Q□
□□□□Q□□□
 --------------------
```





## 課題 4 ライフゲーム  -> Task04_lifeGame.py

`curses`初めて触ったので勉強になりました。



![lifeGameDemo.mov](https://github.com/chanmaji10/coding-skills-exercises/lifeGameDemo.mov.gif)