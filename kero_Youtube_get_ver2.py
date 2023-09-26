import pytchat
import time
import os

print("どうもっこりす。少々お待ちください。")

# PytchatCoreオブジェクトの取得

URL = input("https://m.youtube.com/watch?v=より右側の11文字のurlを入れてください:")
livechat = pytchat.create(video_id = str(URL))
text_in = []
FILENAME = input("任意のファイル名を入れてください。ただし拡張子までは入れないでください。:")
while livechat.is_alive():
    # チャットデータの取得
    chatdata = livechat.get()
    for c in chatdata.items:
        with open(str(FILENAME)+".csv","w",encoding="utf-8")as f:
            text_in.append(f"{c.datetime} {c.author.name} {c.message} {c.amountString}")
            for row in text_in:
                f.write(str(row) + "\n") 

#エクセルファイルに変換するか否か
import pandas as pd
import csv
import openpyxl

question = input("xlsxファイルに変換しますか。はい→y/いいえ→それ以外のキー:")
if question == "y" :
    print("xlsxファイルに変換しました。")
    col_names = ['c{0:02d}'.format(i) for i in range(100)]
    data = pd.read_csv(str(FILENAME)+'.csv', encoding="utf-8", names = col_names)
    data.to_excel(str(FILENAME)+".xlsx")
else:
    print("ガッテン承知の助")

from yt_dlp import YoutubeDL
question2 = input("mp4としてダウンロードしますか。1時間配信はおよそ1.35GBです。はい→y/いいえ→nまたはその他のキー:")
if question2 == "n":
    print("ガッテン承知の助")
elif question2 == "y" :
    print("ダウンロードには時間がかかります。少々お待ちください。")
    ydl_opts = {'format': 'best'}
    with YoutubeDL(ydl_opts) as ydl:
        result = ydl.download(["https://m.youtube.com/watch?v=" + str(URL) ])
        print("ダウンロードが完了しました。")
else :
    print("ガッテン承知の助")

    