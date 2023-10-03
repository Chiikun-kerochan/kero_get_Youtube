import pytchat
import time
import os
from dotenv import load_dotenv

load_dotenv()
comepath = os.getenv("COMERAN_CSV_PATH")
come_xlsx_path = os.getenv("COMERAN_XLSL_PATH")
result_mkv_path = os.getenv("RESULT_MKV") + "/"

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
        with open(str(FILENAME)+".csv","w",encoding="utf-8",newline='\n')as f:
            text_in.append(f"{c.datetime}, {c.author.name}, {c.message} {c.amountString}")
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
    os.remove(str(FILENAME)+".csv")
else:
    print("ガッテン承知の助")

#動画をダウンロードするか否か

from yt_dlp import YoutubeDL
question2 = input("動画をdownloadしますか。最高画質と音質(mkvファイル)でdl→y/ dlしない→y以外のキー:")
if question2 == "n":
    print("ガッテン承知の助")
elif question2 == "y" :
    print("ダウンロードには時間がかかります。少々お待ちください。おすすめはベートーヴェンのワルトシュタインです。")
    ydl_opts = {'format': 'bestvideo+bestaudio/best','outtmpl':result_mkv_path+"%(title)s.%(ext)s"}
    with YoutubeDL(ydl_opts) as ydl:
        result = ydl.download(["https://m.youtube.com/watch?v=" + str(URL) ])
        print("ダウンロードが完了しました。")
else :
    print("ガッテン承知の助")

#ファイルを整理
import shutil

#csv
r1 = os.path.exists(str(FILENAME) + ".csv")
if r1 :
    Output_csv = "/" +str(FILENAME)+".csv"
    shutil.move(str(FILENAME)+".csv" , comepath + Output_csv )
else :
    print("wait a bit")

#xlsx
r = os.path.exists(str(FILENAME) + ".xlsx")
if r :
    Output_xlsx = "/" + str(FILENAME) + ".xlsx"
    shutil.move(str(FILENAME)+".xlsx" , come_xlsx_path + Output_xlsx)
else :
    print("OK")

print("全ての作業が完了しました。")