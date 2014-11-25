import WebInterface

webSiteName = "EagleInvestments.com 'Where Millionaires FLY'"

def Pause():
    input("Hit 'Return' Key To Continue: ")

def MainMenu(cash, user):
    while True:
        print('')
        print("Welcome to", webSiteName)
        print("Customer: ",user,", Cash Available: ", Dollars(cash),sep='')
        print("Main Menu")
        print("-----------------------------")
        print("a -> Account Summary")
        print("b -> Buy Stock")
        print("s -> Sell Stock")
        print("g -> Get Stock Quote")
        print("h -> History of Trades")
        print("n -> New Customer (Will Reset Account)")
        print("x -> Exit")
        choices = ['a', 'b', 's', 'g', 'h', 'n', 'x']
        choice = input("Enter Selection: ").lower()
        if choice in choices:
            return choice

def ConfirmNewAccount():
    while True:
        print('')
        print(webSiteName)
        print("CONFIRM NEW ACCOUNT - CAUTION, WILL RESET ACCOUNT")
        print("-----------------------------")
        print("y -> Yes")
        print("n -> No")
        choices = ['y', 'n']
        choice = input("Enter Choice: ").lower()
        if choice in choices:
            return choice

def QuoteMenu():
    print('')
    print(webSiteName)
    print("Stock Quote Menu")
    print("-----------------------------")
    print("x -> Exit")
    choice = input("Enter Stock Symbol: ").upper()
    return choice

def BuyMenu():
    print('')
    print(webSiteName)
    print("Stock Purchase Menu")
    print("-----------------------------")
    print("x -> Exit")
    symbol = input("Enter Stock Symbol: ").upper()
    if symbol == 'X':
        return '-', '-'

    shares = input("Enter Number of Shares: ")
    return symbol, shares

def ConfirmBuyMenu(shares, symbol, amount, commission):
    while True:
        print('')
        print(webSiteName)
        print("Stock Purchase Confirmation Menu")
        print("-----------------------------")
        print("y -> Yes")
        print("n -> No")
        print("Purchase", shares, "shares of", symbol, ">> total cost", Dollars(amount))
        print("Commission wil be:", Dollars(commission))
        choices = ['y', 'n']
        choice = input("Enter Choice: ").lower()
        if choice in choices:
            return choice

def SellMenu(cash, data):
    print('')
    while True:
        print(webSiteName)
        print("Stock Sell Menu")
        print("-----------------------------")
        print("x -> Exit")
        ShowPortfolio(cash, data)
        symbol = input("Enter Stock Symbol: ").upper()
        if symbol == 'X':
            return '-', '-'

        shares = input("Enter Number of Shares To Sell: ")
        return symbol, shares

def ConfirmSellMenu(shares, symbol, commission):
    print('')
    while True:
        print(webSiteName)
        print("Stock Sell Confirmation Menu")
        print("-----------------------------")
        print("y -> Yes")
        print("n -> No")
        print("Sell", shares, "of", symbol)
        print("Commission will be:", Dollars(commission))
        choices = ['y', 'n']
        choice = input("Enter Choice: ").lower()
        if choice in choices:
            return choice

def ShowQuote(quote):
    print('')
    print(webSiteName)
    print("Current Stock Price")
    print("-----------------------------")
    print("The stock price for", quote[0], "is", Dollars(quote[1]), "on", quote[2])
    Pause()

def ShowPortfolio(cash, stocks):
    print('')
    print(webSiteName)
    print("Current Holdings")
    print("Cash Available:", Dollars(cash))
    print("-----------------------------")
    totalGainLoss = 0
    netWorth = float(cash)
    for stock in stocks:
        currentPrice = WebInterface.GetStockQuote(stock[0])
        gainLoss = (float(currentPrice[1]) - float(stock[2])) * float(stock[1])
        totalGainLoss += gainLoss
        netWorth += float(currentPrice[1]) * float(stock[1])
        print(stock[0],
              "> Shares: ", stock[1],
              ", Purchase Price: ", Dollars(stock[2]),
              ", Current Price: ", Dollars(currentPrice[1]),
              ", Gain/Loss: ", Dollars(gainLoss), sep='')
    print("Total Gain/Loss >",Dollars(totalGainLoss))
    print("YOUR NET WORTH IS ------>>>", Dollars(netWorth), "<<<------")
    print('')
    Pause()

def ShowHistory(stocks):
    print('')
    print(webSiteName)
    print("Transaction History")
    print("-----------------------------")
    if len(stocks) > 0:
        for index, stock in enumerate(stocks):
            if index != 0:
                print(stock[0],
                    " >>> ",stock[1],
                    " > Shares: ", stock[2],
                    ", Price: ", Dollars(stock[3]),
                    ", Date/Time: ", stock[4],sep='')
    else:
        print ("No History Data")
    print('')
    Pause()

def ShowError(errorStr):
    print('')
    print(webSiteName)
    print("User Error!")
    print("-----------------------------")
    print(errorStr)
    Pause()

def Dollars(number):
    import math
    return '$' + str(format(math.floor(float(number) * 100) / 100, ',.2f'))
