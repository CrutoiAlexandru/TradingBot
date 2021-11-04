import websocket
import json
import time
import config

def on_message(ws, message):
    print("message:")
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

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

def get_stock(ws):
    listen = {"action" : "listen", "data" : { "streams" : ["T.TSLA"]}}

    ws.send(json.dumps(listen))

if __name__ == "__main__":
    socket = "wss://data.alpaca.markets/stream"

    if((time.gmtime().tm_hour >= 13 and time.gmtime().tm_hour < 20) and time.gmtime().tm_min >= 29):
        ws = websocket.WebSocketApp(socket,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close
                                )

        ws.run_forever()  
    else:
        print("Market is closed atm!")