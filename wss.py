import websocket
import _thread
import time

BASE_URL    = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ACC_KEY     = 'PKQ107FOKBD3MUNC0XB7'
SECRET_KEY  = 'hgF4BsJJvutyt86rXiX9kLoRlrjDIyqUggOCn8i7'
HEADER      = {'APCA-API-KEY-ID' : ACC_KEY, 'APCA-API-SECRET-KEY' : SECRET_KEY}

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    _thread.start_new_thread(run, ())

def auth(ws):
    data = '{"action": "auth", {HEADER}}'
    ws.send(data)
    print(ws, "da")
    _thread.start_new_thread(auth, ())

if __name__ == "__main__":
    MARKET_URL = "wss://stream.data.alpaca.markets/v2/iex"

    websocket.enableTrace(True)
    ws = websocket.create_connection(MARKET_URL,
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    auth(ws)