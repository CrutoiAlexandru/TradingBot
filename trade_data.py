import requests
import json

BASE_URL    = "https://data.alpaca.markets"
ACCOUNT_URL = "{}/v2/stocks/TSLA/trades".format(BASE_URL)
ACC_KEY     = 'PKQ107FOKBD3MUNC0XB7'
SECRET_KEY  = 'hgF4BsJJvutyt86rXiX9kLoRlrjDIyqUggOCn8i7'
HEADER      = {'APCA-API-KEY-ID' : ACC_KEY, 'APCA-API-SECRET-KEY' : SECRET_KEY}

def acc_data():
    r = requests.get(ACCOUNT_URL, headers = HEADER) 

    dt = r.json()

    dat = json.dumps(dt)

    with open("jsondata.json", "w") as jsonFile:
        jsonFile.write(dat)

    for p in dat:
        print(p)

acc_data()