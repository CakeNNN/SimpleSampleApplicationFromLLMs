# SimpleSampleApplicationFromLLMs  
## これは何か？  

## 実行するには？  
①python(3.8で確認)の使える環境にてpygameをインストールします。 
<pre>
  pip install pygame
</pre>
②あとは個々のファイルを実行するだけです。  
(例)
<pre>
python testgame00_00.py  
</pre>

## 詳細
### testgame00_00.py
以下のプロンプトで生成してもらったコードです。
<pre>
次のような簡単なゲームを作成したいと思います。pythonでコードを書いてください。
・「プレイヤー」はカーソルキーで上下左右に移動。
・画面周辺から「敵」がランダムで出現
・「敵」はプレイヤー方向に移動
・「プレイヤー」が「敵」に接触したらゲーム終了。
</pre>  

  
### testgame00_01.py
続いて、以下のプロンプトで修正してもらったコードです。  
<pre>
「敵」を複数出現するように修正してください。  
</pre>  

  
### testgame00_02.py
さらに、以下のプロンプトで修正してもらったコードです。  
<pre>
「敵」の仕様を次のように変更します。コードを修正してください。
・「敵」は出現から一定時間はプレイヤー方向に移動
・一定時間経過後はそのまま直進
・画面外に出そうになったら消滅  
</pre>
  
  
### testgame00_02_fixed_copilot.py
期待通りの動作をしなかったので以下のプロンプトで修正を試みてもらったコードです。  
<pre>
残念ながら次の不具合が見つかりましたので修正してください。
 ・敵が全く移動しません。  
</pre>

    
### testgame00_02_fixed_manual.py
結局問題は修正されなかったので期待通り動作するように手動で修正したコードです。




