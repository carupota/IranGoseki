# MHRiseのいらない護石を教えてくれるやつ

右上の Code の Download ZIP から落とせる  

使い方  
サンプル.csv みたいな感じで護石のリスト In.csv を作る（泣きシミュとかと同じ形式）  
Pythonをダウンロードしてきて IranGoseki_v1.2.py を走らせる（ダブルクリックでたぶん動く）  
そうするとOut.csv ができる （すでにある場合は上書きされる）
それを見ると8列目に数字が追加される護石がある  
その行数にある護石の下位互換なのでいらない護石という意味  
マイナスの数字はその行の護石と同じ護石という意味   
とりあえず数字がある護石は全部輪廻に突っ込んでよし  
  
文字コードはUTF-8じゃないと動かないかも  
うまくいかない場合は In.csv の中身に変なとこがあるかも
  
履歴  
v1.2 下位互換判定にならないパターンがあったのを修正  
v1.1 BOM付きだとバグるかもしれないのを修正  
v1.0 公開  
