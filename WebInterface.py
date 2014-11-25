#########################
##
## FORMAT OF RETURNED DATA
## SYMBOL, CURRENT PRICE, CURRENT DATE
##
#########################
import urllib.request

def GetStockQuote(symbol):
    firstPart = "http://finance.yahoo.com/d/quotes.csv?s="
    lastPart = "&f=sl1d1t1c1ohgv&e=.csv"
    s = firstPart + symbol + lastPart
    response = urllib.request.urlopen(s)
    webPage = str(response.read())
    companyDataList = webPage.split(',')
    if companyDataList[4] == 'N/A':
        return '-','-','-'
    else:
        return symbol, companyDataList[1], companyDataList[2]
