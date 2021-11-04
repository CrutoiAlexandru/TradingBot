import yfin.high_prices_average        as hpa 
import yfin.low_prices_average         as lpa
import alpaca.websocket_connection.wss as ws
import alpaca.buy_stocks.buy_module    as bm

if __name__ == '__main__':
    bm.buy_stock()
    # ws.ws_connection()
    # hpa.high_prices_average()
    # lpa.low_prices_average()