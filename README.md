# Tic-Tac-Toe

# Tic-Tac-Toe
# 機能紹介：
このゲームは二つのモデルがあります

1.Human vs Human

2.Human vs AI

名前だけではっきり説明しましたね

この二つのボタンをクリックして、別々のモデルに入ります

# モデル
1.Human vs Humanでは○と×が順番で替わる

2.Human vs AIでは、人が×、AIが○です

　人がチェスすると、AIが自動的にチェスする
 
　AIが負けるには難しいので、是非試してください

# ゲーム結果
ゲームの結果は三つあります

1.X is winner !

2.O is winner !

3.The game ended in a draw.



![image](https://github.com/yuzhisheng14/Tic-Tac-Toe/blob/master/screenshot/Capture.PNG)
![image](https://github.com/yuzhisheng14/Tic-Tac-Toe/blob/master/screenshot/Capture02.PNG)


# ソース構成
button.py　--ボタンを作る（ゲーム開始用）

drawPiece.py　--チェスを保存してマップに描く

game_functions.py　--このソース最も重要な部分（ゲームの機能は全部このファイルに書きます）

                   --勝負判断
                   
                   --AIロジック
                   
                   --操作イベント判定
                   
                   --スクリーン初期化と更新
                   
                   --ゲーム進め判定
                   
                   --ゲームモデル判定
                   
                   --...
                   

settings.py　--いろいろなパラメータを設定する

Tic_Tac_Toe.py　--ゲーム運行用、メイン関数

ソースコードは詳細なコメントがありますので、興味があるなら是非ご覧ください

人は勝ち機会はありますので、AIのロジックまだ不完全かもしれません

でも、もし勝ち手がないなら退屈じゃない？

そう言っても、もしこのロジックの問題が発見したら、ご指摘をお願いします！！
