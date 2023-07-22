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

def TradingViewRec(asset,screener,interval,exchange):
    stock = TA_Handler(symbol=asset,exchange=exchange,screener=screener,interval=interval,timeout=None)
    rec = stock.get_analysis().summary
    return (rec['RECOMMENDATION'])

def exportToExcelData(data,asset):
    excelFileName = asset+".xlsx"
    excelFile = xlsxwriter.Workbook(excelFileName)
    # sheet = excelFile.add_worksheet()
    data.to_excel(excelFileName,index=False)