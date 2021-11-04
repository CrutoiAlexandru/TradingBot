import json
import requests
import config

#create a json file that will remember the buying price of a stock
def buy_history(symbol):
    ALPACA_URL = "https://paper-api.alpaca.markets/v2/account/activities"
    
    data = {"symbol":symbol}
    data = json.dumps(data)

    req = requests.get(ALPACA_URL, data = data, headers = {"APCA-API-KEY-ID" : config.ACC_KEY, "APCA-API-SECRET-KEY" : config.SECRET_KEY})

    #load the response as a json and isolate the last purchase
    #the last purchase in alpaca api is allways index 0
    req = json.loads(req.content)

    index = 0

    #check for our symbol
    while req:
        if req[index]["symbol"] == symbol:
            req = req[index]
            break
        else:
            index = index + 1

    if req["side"] == "buy":
        return True
    else:
        return False