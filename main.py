import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = 'https://spreadsheets.google.com/feeds'
json = 'C:/Users/MakeBot/Desktop/test1/move_edit/autoproject-397523-25ede5dc96f7.json' # json file path
credentials = ServiceAccountCredentials.from_json_keyfile_name(json, scope)
gc = gspread.authorize(credentials)
sheet_url = 'https://docs.google.com/spreadsheets/d/1vAe719-kzvHHs8TnIMLV2s7A_TjKY_CydgbylQDPrj4/edit#gid=0' # spreadsheets url
doc = gc.open_by_url(sheet_url)

# ws = doc.worksheet('Deep') # sheet select
# ws.update_acell('B2', 'novels') # sheet update
# cell_data = ws.acell('A1').value # sheet call

ws=doc.worksheet('Deep')
ws_all = ws.get_all_values()


