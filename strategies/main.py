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

def profits(Buy,Sell,data):
    Profits = (data.loc[Sell].Close.values - data.loc[Buy].Close.values)/data.loc[Buy].Close.values
    return Profits

def getWinRate(Profits):
    winnings = [i for i in Profits if i >0]
    winRate = len(winnings)/len(Profits)
    return winRate

def getStockData(asset,startDate,endDate):
    if endDate == 'PRESENT':
        data = yf.download(asset, start= startDate)
        return data
    else:
        data = yf.download(asset, start= startDate, end = endDate)
        return data

def main():
    stock = input("Which stock would you like to test:")
    dataTime = getStockData('AMD','2015-01-31','PRESENT')
    dataF,signals = scalping(stock)
    
    exportToExcelData(dataTime,stock)
    Buy,Sell = displayEntryExit(dataF)
    fig = go.Figure(data=[go.Candlestick(x=dataF['Date'],
                open=dataF['Open'],
                high=dataF['High'],
                low=dataF['Low'],
                close=dataF['Close'],
                name='Candles'),
                go.Scatter(x=dataF.Date,y=dataF.EMAFast,line=dict(color='orange'),name='EMAFast'),
                go.Scatter(x=dataF.Date,y=dataF.EMAMedium,line=dict(color='purple'),name='EMAMedium'),
                go.Scatter(x=dataF.Date,y=dataF.EMASlow,line=dict(color='black'),name='EMASlow')],
                layout=go.Layout(title=go.layout.Title(text="Scalping Graph")
    ))
    SetPlaceBuy = [0] * len(Buy)
    SetPlaceSell = [0] * len(Buy)
    fig.add_scatter(x=dataF.loc[Buy].Date, y=SetPlaceBuy, mode='markers',marker=dict(color='#32FF00',
            size=12,
            line=dict(
                color='Black',
                width=2
            ),symbol='arrow'),name='Enter')
    fig.add_scatter(x=dataF.loc[Sell].Date, y=SetPlaceSell, mode='markers',marker=dict(
            color='#FF1B00',
            size=12,
            line=dict(
                color='Black',
                width=2
            ),symbol='arrow'
        ),name='Exit')
    fig.show()
    profitsScalping = profits(Buy,Sell,dataF)
    print(profitsScalping)
    winrate = getWinRate(profitsScalping)
    print(winrate)
    print("--------------------------------------------------------------")
    dataf = RSI(stock)
    print(dataf.columns)
    print(dataf)
    buy,sell = getSignals(dataf)
    profitsRSI = (dataf.loc[sell].Open.values - dataf.loc[buy].Open.values)/dataf.loc[buy].Open.values
    print(profitsRSI)
    winrate = getWinRate(profitsRSI)
    print(winrate)
    
    fig = go.Figure(data=[go.Candlestick(x=dataf.index,
                open=dataf['Open'],
                high=dataf['High'],
                low=dataf['Low'],
                close=dataf['Close'])])
    fig.add_scatter(x=dataf.loc[buy].index, y=dataf.loc[buy]['Adj Close'], mode='markers',marker=dict(color='#32FF00',
            size=12,
            line=dict(
                color='Black',
                width=2
            ),symbol='arrow'),name='Enter')
    fig.add_scatter(x=dataf.loc[sell].index, y=dataf.loc[sell]['Adj Close'], mode='markers',marker=dict(
            color='#FF1B00',
            size=12,
            line=dict(
                color='Black',
                width=2
            ),symbol='arrow'
        ),name='Exit')
    
    fig.show()
    #exportToExcelData(dataf,stock)
    
if __name__ == "__main__":
    main()