import stock_data.high_prices_average as hpa 
import stock_data.low_prices_average  as lpa
import alpaca.websocket_connection.wss as ws

if __name__ == '__main__':
    ws.ws_connection()
    hpa.high_prices_average()
    lpa.low_prices_average()