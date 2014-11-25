####################
## Format is:
## First Line  ">CASH", CASH IN ACCOUNT, USER NAME
## Other LInes STOCK SYMBOL, NUMBER OF SHARES, PURCHASE PRICE
####################
import csv
import datetime

def GetCashAndUser():
    data = ReadFromCSV()
    if data[0][0] == '>CASH':
        return data[0][1], data[0][2]

def GetStockData():
    data = ReadFromCSV()
    data = data[1:]
    return data

def UpdateAccount(cash, stocks):
    dummy, user = GetCashAndUser()
    data = [['>CASH', str(cash), user]]
    data.extend(stocks)
    WriteToCSV(data)

def InitializeCSV(initialCash, userName):
    initData = [['>CASH', initialCash, userName]]
    WriteToCSV(initData)

def InitializeHistoryCSV(initialCash, userName):
    initData = [['>CASH', initialCash, userName]]
    WriteToHistoryCSV(initData)

def WriteToCSV(data):
    with open('AccountData.csv', 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data)

def ReadFromCSV():
    data = []
    with open('AccountData.csv', 'r', newline='') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            data.append(row)
    return data

def WriteToHistoryCSV(data):
    with open('HistoryData.csv', 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data)

def ReadFromHistoryCSV():
    data = []
    with open('HistoryData.csv', 'r', newline='') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            data.append(row)
    return data

def UpdateHistory(transaction, stock):
    stock.insert(0,transaction)
    dateAndTime = datetime.datetime.now()
    stock.append(dateAndTime)
    history = ReadFromHistoryCSV()
    history.append(stock)
    WriteToHistoryCSV(history)
