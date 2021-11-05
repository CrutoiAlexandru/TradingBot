import websocket
import json
import time
import config
import trader.status as status
import trader.caller as caller

#show websocket message
def on_message(ws, message):\
    #we don't need to see the whole message
    #if the user wants he cand uncomment the print to analyse it
    #print("message: ", message)

    #make the call to either buy or sell
    caller.caller(message)

#show websocket error
def on_error(ws, error):
    print(error)

#show when the websocket connection closed
def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

#on connection open authenticate to personal account
def on_open(ws):
    print("### opened ###")

    data = {"action": "authenticate",
        "data": {
            "key_id": config.ACC_KEY,
            "secret_key": config.SECRET_KEY,
        }
    }
    ws.send(json.dumps(data))

    #get data for a certain stock
    caller.get_stock(ws)

#function for websocket connection
def ws_connection():
    socket = "wss://data.alpaca.markets/stream"

    #if the market is open connect to websocket
    if status.market_status():
        ws = websocket.WebSocketApp(socket,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close
                                )

        ws.run_forever()  
    else:
        print("Market is closed atm!")