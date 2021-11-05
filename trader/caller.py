import json
import websocket
import trading_stocks                 as ts
import alpaca.buy_stocks.buy_history  as bh
import alpaca.buy_stocks.buy_module   as bm
import alpaca.sell_stocks.sell_module as sm
import trader.algo                    as algo

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

        #see what symbol the message returns
        #in order to strictly get the symbol from the message we need to remove a few characters
        #we follow the message allways so we can't make mistakes about the stock we are curently interested in
        symbol = json.dumps(json_message["stream"])
        symbol = symbol.replace("T.", "")
        symbol = symbol.replace('"', "")
        
        print(symbol, " : ", price)

        #see if the received symbol is already bought
        #if the symbol is bought look to sell, otherwise look to buy
        #these functions only return booleans
        if bh.buy_history(symbol):
            #we have the stock now we sell it
            if algo.good_to_sell(price, symbol):
                sm.sell_stock(symbol)
            else:
                print("No sell!")
        else:
            #we don't have the stock now we buy it
            if algo.good_to_buy(price, symbol):
                bm.buy_stock(symbol)
            else:
                print("No buy!")