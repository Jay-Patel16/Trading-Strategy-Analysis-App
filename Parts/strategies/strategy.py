import alpaca_trade_api as tradeapi
from datetime import datetime
import pandas as pd
import yfinance as yf
from lumibot.backtesting import YahooDataBacktesting
from lumibot.brokers import Alpaca
from lumibot.strategies import Strategy
from lumibot.traders import Trader
import yfinance as yf
#from tradingview_ta import TA_Handler, Interval, Exchange
import pandas_datareader as web
import matplotlib.pyplot as plt


# def getData():
#     start = datatime.datatime()
#     print(apple)
    #output = TA_Handler(symbol="AAPL",screener="america",exchange="NASDAQ",interval = Interval.INTERVAL_1_MINUTE)
    #print(output.get_analysis().summary)
    #print(output.get_analysis().indicators)
    


# output = TA_Handler(symbol="AAPL",screener="america",exchange="NASDAQ",interval = Interval.INTERVAL_1_MINUTE)
# output.get_analysis().summary
class AlpacaConfig:
    API_KEY = 'PKVO139MTMLPEJQKNNI8'
    API_SECRET  = '0LHprL5OHu9J0hIVvdHxcBQo4hlhC3bF3T8GRGcD'
    ENDPOINT = 'https://paper-api.alpaca.markets'

class BuyHold(Strategy):
    data = []
    order_number = 0
    def initialize(self):
        self.sleeptime = "10m"


    def on_trading_iteration(self):
        symbol ="AAPL"
        entry_price = self.get_last_price(symbol)
        self.log_message(f"Position: {self.get_position(symbol)}")
        self.data.append(self.get_last_price(symbol))

        if len(self.data) > 3:
            temp = self.data[-3:]
            if temp[-1] > temp[1] > temp[0]:
                self.log_message(f"Last 3 prints: {temp}")
                order = self.create_order(symbol, quantity = 10, side = "buy")
                self.submit_order(order)
                self.order_number += 1
                if self.order_number == 1:
                    self.log_message(f"Entry price: {temp[-1]}")
                    entry_price = temp[-1] # filled price
            if self.get_position(symbol) and self.data[-1] < entry_price * .995:
                self.sell_all()
                self.order_number = 0
            elif self.get_position(symbol) and self.data[-1] >= entry_price * 1.015:
                self.sell_all()
                self.order_number = 0


    def before_market_closes(self):
        self.sell_all()


# if __name__== "__main__":
#     trade = False
#     if trade:
#         alpaca = Alpaca(AlpacaConfig)
#         strategy = BuyHold(broker = alpaca)
#         trader = Trader()
#         trader.add_strategy(strategy)
#         trader.run_all()
#     else:
#         start = datetime(2023,1,1)
#         end = datetime(2023,6,30)
#         BuyHold.backtest(
#             YahooDataBacktesting,
#             start,
#             end
#         )