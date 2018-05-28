from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http
import gspread

scopes = ['https://www.googleapis.com/auth/spreadsheets']
json_file = 'hoge.json'#OAuth用クライアントIDの作成でダウンロードしたjsonファイル
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file, scopes=scopes)
http_auth = credentials.authorize(Http())

# スプレッドシート用クライアントの準備
doc_id = 'docname'#これはスプレッドシートのURLのうちhttps://docs.google.com/spreadsheets/d/以下の部分です
client = gspread.authorize(credentials)
gfile   = client.open_by_key(doc_id)#読み書きするgoogle spreadsheet
worksheet  = gfile.sheet1

cell_list = worksheet.range('A1:A60')
for cell in cell_list:
    if len(cell)>0:#セルに何か書き込まれている場合
        continue
    else:
        do_something()
        worksheet.update_acell(cell.row,cell.col,input())
