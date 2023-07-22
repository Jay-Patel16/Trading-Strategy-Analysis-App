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

def scalping(asset):
    data = yf.download(asset, start= "2011-01-01")
    data= data.reset_index()
  #  CandleChart = chart.Figure(data=[chart.Candlestick(x=data['Date'],open=data['Open'],high=data['High'],low=data['Low'],close=data['Close'])])
    data = data[data['Volume']!=0]
    data.isna().sum
    data.reset_index(drop=True,inplace=True)
    
    data['EMASlow'] = ta.ema(data.Close,length=150)
    data['EMAMedium'] = ta.ema(data.Close,length=100)
    data['EMAFast'] = ta.ema(data.Close,length=50)
    
    data['SlopeFast'] = data['EMAFast'].diff(periods=1)
    data['SlopeFast'] = data['SlopeFast'].rolling(window=10).mean()
    data['SlopeM'] = data['EMAMedium'].diff(periods=1)
    data['SlopeM'] = data['SlopeM'].rolling(window=10).mean()
    data['SlopeSlow'] = data['EMASlow'].diff(periods=1)
    data['SlopeSlow'] = data['SlopeSlow'].rolling(window=10).mean() 
    # setting up conditions for EMA

    conditions = [((data['EMASlow']<data['EMAMedium']) & (data['EMAMedium']<data['EMAFast']) & (data['SlopeFast']>0) &  (data['SlopeM']>0) &  (data['SlopeSlow']>0)),((data['EMASlow']>data['EMAMedium']) & (data['EMAMedium']>data['EMAFast']) & (data['SlopeFast']<0) &  (data['SlopeM']<0 ) &  (data['SlopeSlow']<0))]
    choice = ['Uptrend','Downtrend']
    data['Signal'] = np.select(conditions,choice,default=0)
    Signals = [0] * len(data)
    day = 0
    while day < len(data):
        if data.Signal[day] == 'Uptrend' and data.Open[day]<data.EMAFast[day] and data.Close[day]>data.EMAFast[day]:
            Signals[day] = 'Entry'
            for days in range(1,6):
                if (data.Close[day + days])>(data.Close[day]*1.02):
                    Signals[day+days] = 'Exit'
                    break
                elif days == 5:
                    Signals[day+days] = 'Exit'
                else:
                    Signals[day+days] = 'Wait'
            day = day+days+1
                    
        else:
            Signals[day]='Wait'
            day+=1
    data['Timing'] = Signals
    return data,Signals
def displayEntryExit(data):
    Buy=[]
    Sell=[]
    for i in  range(len(data)):
        if data.Timing[i]=='Entry':
            Buy.append(data.iloc[i].name)
        elif data.Timing[i] == 'Exit':
            #print(data.iloc[i].name)
            Sell.append(data.iloc[i].name)
    return Buy, Sell
