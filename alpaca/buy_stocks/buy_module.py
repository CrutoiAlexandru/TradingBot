import requests
import config
import json

def buy_stock(symbols):
    ALPACA_URL = "https://paper-api.alpaca.markets/v2/orders"
    
    data = {"symbol":symbols, "qty":1, "side":"buy", "type":"market", "time_in_force":"day"}
    data = json.dumps(data)

    req = requests.post(ALPACA_URL, data = data, headers = {"APCA-API-KEY-ID" : config.ACC_KEY, "APCA-API-SECRET-KEY" : config.SECRET_KEY})

    print("Purchase successfull!")