import requests

BASE_URL    = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)

r = requests.get(ACCOUNT_URL, headers = {'APCA-API-KEY-ID': 'PKQ107FOKBD3MUNC0XB7', 'APCA-API-SECRET-KEY': 'hgF4BsJJvutyt86rXiX9kLoRlrjDIyqUggOCn8i7'}) 

print(r.content)