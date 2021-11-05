import json
import websocket
import trading_stocks                 as ts
import alpaca.buy_stocks.buy_history  as bh
import alpaca.buy_stocks.buy_module   as bm
import alpaca.sell_stocks.sell_module as sm

#get data for a certain stock(s)
def get_stock(ws):
    index = 0

    #call for every item in list stock from ts
    while index < len(ts.stocks):
        listen = {"action" : "listen", "data" : { "streams" : ["T." + ts.stocks[index]]}}
        ws.send(json.dumps(listen))
        index += 1

def caller(message):
    #only get the current price is there is such data in the received message
    if "p" in message:
        #get the current price on message for a buying/selling oportunity at every received message
        json_message = json.loads(message)
        price = json.dumps(json_message["data"])
        price = json.loads(price)
        price = price['p']

        print(price)

        #see what symbol the message returns
        symbol = json.dumps(json_message["data"])
        symbol = json.loads(symbol)
        symbol = symbol["order"]
        symbol = json.loads(symbol)
        symbol = symbol["symbol"]

        print(symbol)

        #see if the received symbol is already bought
        #if the symbol is bought look to sell, otherwise look to buy
        #these functions only return booleans
        print(bh.buy_history(symbol))
        if bh.buy_history(symbol):
            #we have the stock now we sell it
            if algo.good_to_sell(price):
                sm.sell_stock(symbol)
            else:
                print("No sell!")
        else:
            #we don't have the stock now we buy it
            if algo.good_to_buy(price):
                bm.buy_stock(symbol)
            else:
                print("No buy!")