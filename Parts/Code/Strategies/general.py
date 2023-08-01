import yfinance as yf
from tradingview_ta import TA_Handler, Interval, Exchange
import xlsxwriter


def profits(Buy, Sell, data):
    Profits = (data.loc[Sell].Close.values -
               data.loc[Buy].Close.values)/data.loc[Buy].Close.values
    return Profits


def getWinRate(Profits):
    winnings = [i for i in Profits if i > 0]
    winRate = len(winnings)/len(Profits)
    winRate = round(winRate, 2)
    return winRate


def getStockData(asset, startDate, endDate):
    data = yf.download(asset, start=startDate, end=endDate)
    return data


def TradingViewRec(asset, exchange):
    stock = TA_Handler(symbol=asset, exchange=exchange,
                       screener='america', interval='5m', timeout=None)
    rec = stock.get_analysis().summary
    return (rec['RECOMMENDATION'])


def exportToExcelData(data, asset):
    excelFileName = asset+".xlsx"
    excelFile = xlsxwriter.Workbook(excelFileName)
    data.to_excel(excelFileName, index=False)


def convertDate(startD, endD):
    SDate = startD.split('/')
    EDate = endD.split('/')
    if int(SDate[0]) < 10:
        SDate[0] = '0'+SDate[0]
    if int(SDate[1]) < 10:
        SDate[1] = '0'+SDate[1]
    if int(EDate[0]) < 10:
        EDate[0] = '0'+EDate[0]
    if int(EDate[1]) < 10:
        EDate[1] = '0'+EDate[1]
    startDate = SDate[2] + "-"+SDate[0]+'-'+SDate[1]
    endDate = EDate[2] + "-"+EDate[0]+'-'+EDate[1]
    return startDate, endDate
