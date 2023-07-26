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
import pandas_datareader as web
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np
import xlsxwriter

def profits(Buy,Sell,data):
    Profits = (data.loc[Sell].Close.values - data.loc[Buy].Close.values)/data.loc[Buy].Close.values
    return Profits

def getWinRate(Profits):
    winnings = [i for i in Profits if i >0]
    winRate = len(winnings)/len(Profits)
    return winRate

def getStockData(asset,startDate,endDate):
    data = yf.download(asset, start= startDate, end = endDate)
    return data

def TradingViewRec(asset,exchange):
    stock = TA_Handler(symbol=asset,exchange=exchange,screener='america',interval='5m',timeout=None)
    rec = stock.get_analysis().summary
    return (rec['RECOMMENDATION'])

def exportToExcelData(data,asset):
    excelFileName = asset+".xlsx"
    excelFile = xlsxwriter.Workbook(excelFileName)
    data.to_excel(excelFileName,index=False)