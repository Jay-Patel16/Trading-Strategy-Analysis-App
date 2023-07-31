import alpaca_trade_api as tradeapi
from datetime import datetime
import pandas as pd
import pandas_ta as ta
import yfinance as yf
from lumibot.backtesting import YahooDataBacktesting
from lumibot.brokers import Alpaca
from lumibot.strategies import Strategy
from lumibot.traders import Trader
import yfinance as yf
from tradingview_ta import TA_Handler, Interval, Exchange
import tradingview_ta
import pandas_datareader as web
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np
from Scalping import *
from RSI import *
from general import *
from trendFollowing import *
from gui import *


def main():
    gui()

    # stock = input("Which stock would you like to test:")
    # # data = yf.download(stock,start = '2023-07-11', end= '2023-07-12', interval="1m")
    # # print(data)
    # # buy,sell,profits = trendFollowing(data,1,1,2)
    # # print(profits)
    # # graphTrendOneDay(buy,sell,data)
    # profitsOver, winrate = rangeTrendFollowing(stock,'2023-07-10','2023-07-15',1,1,2)
    # print(profitsOver)
    # print(winrate)
    # # dataTime = getStockData('AMD','2015-01-31','PRESENT')
    # # dataF,signals = scalping(stock)

    # # exportToExcelData(dataTime,stock)
    # # Buy,Sell = displayEntryExit(dataF)

    # # profitsScalping = profits(Buy,Sell,dataF)
    # # print(profitsScalping)
    # # winrate = getWinRate(profitsScalping)
    # # print(winrate)
    # # print("--------------------------------------------------------------")
    # # dataf = RSI(stock)
    # # print(dataf.columns)
    # # print(dataf)
    # # buy,sell = getSignals(dataf)
    # # profitsRSI = (dataf.loc[sell].Open.values - dataf.loc[buy].Open.values)/dataf.loc[buy].Open.values
    # # print(profitsRSI)
    # # winrate = getWinRate(profitsRSI)
    # # print(winrate)

    # # #exportToExcelData(dataf,stock)


if __name__ == "__main__":
    main()
