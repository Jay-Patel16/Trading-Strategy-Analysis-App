import yfinance as yf
import plotly.graph_objects as go


def RSI(asset, startD, endD):
    dataframe = yf.download(asset, start=startD, end=endD)
    dataframe["200 Day"] = dataframe['Adj Close'].rolling(window=200).mean()
    dataframe["RelativeReturn"] = dataframe['Adj Close'].pct_change()
    dataframe['Upmove'] = dataframe['RelativeReturn'].apply(
        lambda x: x if x > 0 else 0)
    dataframe['Downmove'] = dataframe['RelativeReturn'].apply(
        lambda x:  abs(x) if x < 0 else 0)
    dataframe['Avg Up'] = dataframe['Upmove'].ewm(span=20).mean()
    dataframe['Avg Down'] = dataframe['Downmove'].ewm(span=20).mean()
    # dataframe = dataframe.dropna()
    dataframe['RS'] = dataframe['Avg Up']/dataframe['Avg Down']
    dataframe['RSI'] = dataframe['RS'].apply(lambda x: 100-(100/(x+1)))
    dataframe.loc[(dataframe['Adj Close'] > dataframe['200 Day'])
                  & (dataframe['RSI'] < 30), 'Buy'] = 'Yes'
    dataframe.loc[(dataframe['Adj Close'] < dataframe['200 Day'])
                  | (dataframe['RSI'] > 30), 'Buy'] = 'No'
    return dataframe


def getSignals(dataframe):
    Buy = []
    Sell = []
    for i in range(len(dataframe)):
        if dataframe['Buy'].iloc[i] == 'Yes':
            Buy.append(dataframe.iloc[i+1].name)
            for j in range(1, 11):
                if dataframe['RSI'].iloc[i+j] > 40:
                    Sell.append(dataframe.iloc[i+j+1].name)
                    break
                elif j == 10:
                    Sell.append(dataframe[i+j+1].name)
    return Buy, Sell


def graphRSI(dataf, buy, sell):
    fig = go.Figure(data=[go.Candlestick(x=dataf.index,
                                         open=dataf['Open'],
                                         high=dataf['High'],
                                         low=dataf['Low'],
                                         close=dataf['Close'])], layout=go.Layout(title=go.layout.Title(text="RSI Graph")))
    fig.add_scatter(x=dataf.loc[buy].index, y=dataf.loc[buy]['Open'], mode='markers', marker=dict(color='#32FF00',
                                                                                                  size=12,
                                                                                                  line=dict(
                                                                                                      color='Black',
                                                                                                      width=2
                                                                                                  ), symbol='arrow'), name='Enter')
    fig.add_scatter(x=dataf.loc[sell].index, y=dataf.loc[sell]['Open'], mode='markers', marker=dict(
        color='#FF1B00',
        size=12,
        line=dict(
            color='Black',
            width=2
        ), symbol='arrow'
    ), name='Exit')
    fig.show()
