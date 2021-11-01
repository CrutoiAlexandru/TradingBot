import requests

BASE_URL    = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ACC_KEY     = 'PKQ107FOKBD3MUNC0XB7'
SECRET_KEY  = 'hgF4BsJJvutyt86rXiX9kLoRlrjDIyqUggOCn8i7'
HEADER      = {'APCA-API-KEY-ID' : ACC_KEY, 'APCA-API-SECRET-KEY' : SECRET_KEY}

def acc_data():
    r = requests.get(ACCOUNT_URL, headers = HEADER) 

    print(r.content)

def market_data():
    MARKET_URL = "https://stream.data.alpaca.markets/v2/iex"

    r = requests.get(MARKET_URL, {"bars" : "AAPL"},headers = HEADER)

    print(r.content)

market_data()