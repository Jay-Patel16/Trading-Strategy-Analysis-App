import pandas_ta as ta
import yfinance as yf
import plotly.graph_objects as go
import numpy as np


def scalping(asset, startD, endD, daysT, buyP):
    data = yf.download(asset, start=startD, end=endD)
    data = data.reset_index()
    data = data[data['Volume'] != 0]
    data.isna().sum
    data.reset_index(drop=True, inplace=True)

    data['EMASlow'] = ta.ema(data.Close, length=150)
    data['EMAMedium'] = ta.ema(data.Close, length=100)
    data['EMAFast'] = ta.ema(data.Close, length=50)

    data['SlopeFast'] = data['EMAFast'].diff(periods=1)
    data['SlopeFast'] = data['SlopeFast'].rolling(window=10).mean()
    data['SlopeM'] = data['EMAMedium'].diff(periods=1)
    data['SlopeM'] = data['SlopeM'].rolling(window=10).mean()
    data['SlopeSlow'] = data['EMASlow'].diff(periods=1)
    data['SlopeSlow'] = data['SlopeSlow'].rolling(window=10).mean()
    conditions = [((data['EMASlow'] < data['EMAMedium']) & (data['EMAMedium'] < data['EMAFast']) & (data['SlopeFast'] > 0) & (data['SlopeM'] > 0) & (data['SlopeSlow'] > 0)), ((
        data['EMASlow'] > data['EMAMedium']) & (data['EMAMedium'] > data['EMAFast']) & (data['SlopeFast'] < 0) & (data['SlopeM'] < 0) & (data['SlopeSlow'] < 0))]
    choice = ['Entry', 'Exit']
    data['Signal'] = np.select(conditions, choice, default=0)
    Signals = [0] * len(data)
    day = 0
    while day < len(data):
        if data.Signal[day] == 'Entry' and data.Open[day] < data.EMAFast[day] and data.Close[day] > data.EMAFast[day]:
            Signals[day] = 'Entry'
            for days in range(1, daysT+1):
                if (data.Close[day + days]) > (data.Close[day]*(1+(buyP/100))):
                    Signals[day+days] = 'Exit'
                    break
                elif days == daysT:
                    Signals[day+days] = 'Exit'
                else:
                    Signals[day+days] = 'Wait'
            day = day+days+1

        else:
            Signals[day] = 'Wait'
            day += 1
    data['Timing'] = Signals
    return data, Signals


def displayEntryExit(data):
    Buy = []
    Sell = []
    for i in range(len(data)):
        if data.Timing[i] == 'Entry':
            Buy.append(data.iloc[i].name)
        elif data.Timing[i] == 'Exit':
            # print(data.iloc[i].name)
            Sell.append(data.iloc[i].name)
    return Buy, Sell


def graphScalping(dataF, Buy, Sell):
    fig = go.Figure(data=[go.Candlestick(x=dataF['Date'],
                                         open=dataF['Open'],
                                         high=dataF['High'],
                                         low=dataF['Low'],
                                         close=dataF['Close'],
                                         name='Candles'),
                          go.Scatter(x=dataF.Date, y=dataF.EMAFast, line=dict(
                              color='orange'), name='EMAFast'),
                          go.Scatter(x=dataF.Date, y=dataF.EMAMedium,
                                     line=dict(color='purple'), name='EMAMedium'),
                          go.Scatter(x=dataF.Date, y=dataF.EMASlow, line=dict(color='black'), name='EMASlow')],
                    layout=go.Layout(title=go.layout.Title(text="Scalping Graph")
                                     ))
    SetPlaceBuy = [0] * len(Buy)
    SetPlaceSell = [0] * len(Buy)
    fig.add_scatter(x=dataF.loc[Buy].Date, y=dataF.loc[Buy]['Open'], mode='markers', marker=dict(color='#32FF00',
                                                                                                 size=12,
                                                                                                 line=dict(
                                                                                                     color='Black',
                                                                                                     width=2
                                                                                                 ), symbol='arrow'), name='Enter')
    fig.add_scatter(x=dataF.loc[Sell].Date, y=dataF.loc[Sell]['Open'], mode='markers', marker=dict(
        color='#FF1B00',
        size=12,
        line=dict(
            color='Black',
            width=2
        ), symbol='arrow'
    ), name='Exit')
    fig.show()
