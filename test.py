import requests
import config

BASE_URL    = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
HEADER      = {'APCA-API-KEY-ID' : config.ACC_KEY, 'APCA-API-SECRET-KEY' : config.SECRET_KEY}

def acc_data():
    r = requests.get(ACCOUNT_URL, headers = HEADER) 

    print(r.content)

acc_data()