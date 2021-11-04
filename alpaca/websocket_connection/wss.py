import websocket
import json
import time
import config

#show websocket message
def on_message(ws, message):
    print("message:")
    print(message)

#show websocket error
def on_error(ws, error):
    print(error)

#show when the websocket connection closed
def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

#on connection open authenticate to personal account
def on_open(ws):
    print("opened")

    data = {"action": "authenticate",
        "data": {
            "key_id": config.ACC_KEY,
            "secret_key": config.SECRET_KEY,
        }
    }
    ws.send(json.dumps(data))

    get_stock(ws)

#get data for a certain stock(s)
def get_stock(ws):
    listen = {"action" : "listen", "data" : { "streams" : ["T.TSLA"]}}

    ws.send(json.dumps(listen))

#find out if the market is open
def market_status():
    if((time.gmtime().tm_hour > 13 and time.gmtime().tm_hour < 20) or (time.gmtime().tm_hour == 8 and time.gmtime().tm_min > 29)):
        return True
    else:
        return False

#function for websocket connection
def ws_connection():
    socket = "wss://data.alpaca.markets/stream"

    #if the market is open connect to websocket
    if market_status():
        ws = websocket.WebSocketApp(socket,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close
                                )

        ws.run_forever()  
    else:
        print("Market is closed atm!")