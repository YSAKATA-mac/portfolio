## Pythonanywhereのサービスを利用しdeployテストをしてみました。
http://yuuji.pythonanywhere.com/main/


あつまれどうぶつの森　カブ価予測ツール
====
## 概要
ユーザーが、ゲーム『あつまれどうぶつの森」の過去のカブ価を入力する事で、以降のカブ価を予測し表示するウェブアプリ。  
使用する言語はPython3.8.3　Django3.0.3

##  前提情報
* **カブ**とは　現実世界の株式に見立てたゲーム内での金策方法
* カブは日曜日に１００ベル(ゲーム内通貨)前後で売りに出され、以降月曜午前、月曜午後、火曜午前...土曜午後　と１２ブロックに分け、値段が変動する。
* 値段の変動パターンは４つ  
1. 緩やかに売値が上下する波型  
2. ただただ土曜日に向け下がっていくだけの下落型
3. 下落していくが、どこかで元値の6倍近く売値が跳ね上がる跳ね大型
4. 3回値上がり、3回目で2倍近く売値が上がる跳ね小型



## ひとまず実装する機能
#### カブ価予測  

日曜日に購入したカブの値段を入力と、月曜〜土曜の午前、午後の全12箇所のうち既に分かっている箇所をテキストボックスに入力。

入力された情報から、判明している４パターンと比較して  
以降どのような動き方をするか、見極め時、売り時はどこかを算出して映す。   


#### 掲示板の開設  

サイト内に掲示板を開設し
1. 投稿者の島の現在のカブ価
2. 招待コード
3. 置いていって欲しい返礼品
4. 花の水やりの有無
5. いつまで島を開けておく予定か

を入力し投稿できるようにする。


## そのうち実装したい機能

#### 株価予測の数値をグラフで可視化

売値がどういった動きをするか、グラフでわかりやすく可視化する。
javasprictの領域だと思うので、ゆっくり勉強していく。


#### ユーザーデータベース、ログイン機能を作り掲示板と紐付ける。
