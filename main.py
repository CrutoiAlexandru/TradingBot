import yfin.high_prices_average        as hpa 
import yfin.low_prices_average         as lpa
import alpaca.websocket_connection.wss as ws
import alpaca.buy_stocks.buy_history   as bh
import alpaca.buy_stocks.buy_module    as bm
import alpaca.sell_stocks.sell_module  as sm

if __name__ == '__main__':
    # bm.buy_stock("TSLA")
    # sm.sell_stock("AAPL")
    print(bh.buy_history("AAPL"))

    
    # ws.ws_connection()
    # hpa.high_prices_average()
    # lpa.low_prices_average()