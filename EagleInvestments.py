import UserInterface
import FileInterface
import WebInterface

while True:
    # READ FROM THE ACCOUNT FILE ALL DATA
    cash, user = FileInterface.GetCashAndUser()
    stocks = FileInterface.GetStockData()

    # GET THE MAIN MENU USER ACTION
    action = UserInterface.MainMenu(cash, user)

    # GET A QUOTE ON A STOCK FOR THE USER
    if action == 'g':
        symbol = UserInterface.QuoteMenu()
        if symbol == 'X':
            UserInterface.ShowError("Not Valid Symbol " + symbol)
            continue
        else:
            # SHOW THE STOCK QUOTE
            stockQuote = WebInterface.GetStockQuote(symbol)
            if stockQuote[0] == '-':
                UserInterface.ShowError("Invalid Stock Symbol " + stockQuote[0])
                continue
            else:
                UserInterface.ShowQuote(stockQuote)

    # BIG DEAL HERE - MAKE A NEW ACCOUNT
    elif action == 'n':
        # CHECK IF WE REALLY WANT TO RESET THE ACCOUNT
        yesNo = UserInterface.ConfirmNewAccount()
        if yesNo == 'y':
            userName = 'Bill Gates'
            initialCash = 1000000
            FileInterface.InitializeCSV(initialCash, userName)
            FileInterface.InitializeHistoryCSV(initialCash, userName)

    # SHOW OFF YOUR PORTFOLIO PORTFOLIO
    elif action == 'a':
        # SHOW THE ENTIRE PORTFOLIO OF STOCKS
        UserInterface.ShowPortfolio(cash, stocks)

    # BUYING OF STOCK
    elif action == 'b':
        # SHOW BUY MENU
        symbol, numberOfShares = UserInterface.BuyMenu()

        if symbol != '-':
            # GET STOCK QUOTE
            stockQuote = WebInterface.GetStockQuote(symbol)
            if stockQuote[0] == '-':
                UserInterface.ShowError('Stock symbol does not exist:' + symbol)
                continue

            # CHECK THAT WE DO NOT ALREADY OWN STOCK.
            # TO KEEP SIMPLE, PROGRAM ONLY ALLOWS ONE PURCHASE PER STOCK
            stockFound = False
            for stock in stocks:
                if symbol == stock[0]:
                    stockFound = True
                    break
            if stockFound:
                UserInterface.ShowError("You Already Own This Stock " + symbol)
                continue

            # FIGURE THE COST TO BUY
            cost = float(numberOfShares) * float(stockQuote[1])
            commission = cost * 0.05
            cost += commission
            if float(cash) < cost:
                UserInterface.ShowError("Not Enough Cash To Purchase Stock")
                continue

            # CONFIRM USER WANTS TO BUY
            yesNo = UserInterface.ConfirmBuyMenu(numberOfShares, symbol, cost, commission)
            if yesNo == 'y':
                # STOCK WAS PURCHASED, UPDATE THE ACCOUNT FILE
                newCash = float(cash) - cost
                newStock = [symbol, numberOfShares, stockQuote[1]]
                stocks.append(newStock)
                FileInterface.UpdateAccount(newCash, stocks)
                FileInterface.UpdateHistory("Bought", newStock)

    # SELLING OF STOCK
    elif action == 's':
        symbol, numberOfShares = UserInterface.SellMenu(cash, stocks)

        if symbol != '-':
            newCash = -1
            stockIndex = -1
            sharesRemaining = -1
            commission = -1
            stock = []

            # LOOP THROUGH ALL STOCKS
            for index, stock in enumerate(stocks):
                # FIND STOCK THAT MATCHES IN OUR ACCOUNT
                if symbol == stock[0]:
                    # ENSURE THERE ARE ENOUGH SHARES
                    if int(numberOfShares) <= int(stock[1]):
                        stockQuote = WebInterface.GetStockQuote(symbol)
                        proceeds = float(numberOfShares) * float(stockQuote[1])
                        commission = float(proceeds)*0.05
                        newCash = float(cash) + proceeds - commission
                        sharesRemaining = int(stock[1]) - int(numberOfShares)
                        stockIndex = index
                        break

            # CHECK IF WE ARE GOOD TO GO WITH THE SELL
            if stockIndex >= 0:
                # CONFIRM IT WITH THE USER
                yesNo = UserInterface.ConfirmSellMenu(numberOfShares, symbol, commission)
                if yesNo == 'y':
                    if sharesRemaining == 0:
                        # DELETE THE WHOLE STOCK
                        del stocks[stockIndex]
                    else:
                        # UPDATE THE STOCK WITH THE NEW NUMBER OF SHARES
                        stocks[stockIndex][1] = sharesRemaining

                    # UPDATE THE ACCOUNT FILE AND SHOW THE PORTFOLIO
                    FileInterface.UpdateAccount(newCash, stocks)
                    FileInterface.UpdateHistory("Sold", stock)
                    UserInterface.ShowPortfolio(newCash, stocks)

    # HISTORY OF BUYS AND SELLS
    elif action == 'h':
        stocks = FileInterface.ReadFromHistoryCSV()
        UserInterface.ShowHistory(stocks)

    # GET OUT OF HERE NOW
    elif action == 'x':
        break

