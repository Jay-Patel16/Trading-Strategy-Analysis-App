import yfinance as yf
import plotly.graph_objects as go


def oneDayData(asset, startDate, EndDate):
    dataOneDay = yf.download(asset, start=startDate,
                             end=EndDate, interval='1m')
    return dataOneDay


def trendFollowingOneDay(data, buyPercent, sellPercent, hour):
    buy = []
    sell = []
    profits = 0

    hourCount = hour
    while hourCount < 6:
        startTime = hourCount * 60
        startingPrice = data.iloc[startTime].Open
        dayStartPrice = data.iloc[0].Open
        SellPrice = data.iloc[startTime+1].Open
        percentChange = ((startingPrice - dayStartPrice) /
                         (abs(dayStartPrice))) * 100
        percentChangeSell = ((SellPrice - startingPrice) /
                             (abs(startingPrice))) * 100
        i = startTime
        j = startTime+1
        foundSell = 0
        if percentChange >= buyPercent:
            buy.append(data.iloc[j].name)
            i = i + 1 + 1
            while i < len(data)-1:
                SellPrice = data.iloc[i].Open
                BroughtPrice = data.iloc[j].Open
                percentChangeSell = (
                    (SellPrice - BroughtPrice) / (abs(BroughtPrice))) * 100
                if percentChangeSell >= sellPercent:
                    sell.append(data.iloc[i+1].name)
                    i = i + 1
                    hourCount = hourCount + hour
                    foundSell = 1
                    break
                elif percentChangeSell <= (-abs(sellPercent)):
                    sell.append(data.iloc[i+1].name)
                    i = i + 1
                    hourCount = hourCount + hour
                    foundSell = 1
                    break
                else:
                    i = i + 1
            if foundSell == 0:
                sell.append(data.iloc[len(data)-1].name)
                i = len(data)-1
                hourCount = hourCount + hour
            profits = profits + data.iloc[i].Open - data.iloc[j].Open

        else:
            buy.append(data.iloc[j].name)
            sell.append(data.iloc[j+1].name)
            profits = profits + data.iloc[j+1].Open - data.iloc[j].Open
            hourCount = hourCount + hour
    return buy, sell, profits


def rangeTrendFollowing(asset, startDate, endDate, buyP, sellP, startHour):
    profitsOverall = []
    dataRange = yf.download(asset, start=startDate, end=endDate, interval='1d')
    for i in range(1, len(dataRange)-1):
        dataOneDay = oneDayData(
            asset, dataRange.iloc[i].name, dataRange.iloc[i+1].name)
        buy, sell, profits = trendFollowingOneDay(
            dataOneDay, buyP, sellP, startHour)
        profitsOverall.append(profits)
    return profitsOverall


def graphTrendOneDay(buy, sell, data):
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                                         open=data['Open'],
                                         high=data['High'],
                                         low=data['Low'],
                                         close=data['Close'],
                                         name='Candles'),
                          ],
                    layout=go.Layout(title=go.layout.Title(text="Trend Following Graph")
                                     ))
    fig.add_scatter(x=data.loc[buy].index, y=data.loc[buy]['Open'], mode='markers', marker=dict(color='#32FF00',
                                                                                                size=12,
                                                                                                line=dict(
                                                                                                    color='Black',
                                                                                                    width=2
                                                                                                ), symbol='arrow'), name='Enter')
    fig.add_scatter(x=data.loc[sell].index, y=data.loc[sell]['Open'], mode='markers', marker=dict(
        color='#FF1B00',
        size=12,
        line=dict(
            color='Black',
            width=2
        ), symbol='arrow'
    ), name='Exit')
    fig.show()
