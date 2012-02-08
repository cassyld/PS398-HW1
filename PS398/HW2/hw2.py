class Portfolio(object):
    def __init__(self, cash, stocks, mf):
        self.cash = 0
        self.stocks = 0
        self.mf = 0

    def addCash(self, amount):
        self.cash += (amount)

    def withdrawCash(self, amount):
        self.cash -= (amount)

    def addStock(self, shares, stock_name):
        self.shares = 0 
        if shares > 0 then (self.cash + shares * 5) #pretending .5 is price
        
        #self.price += self.cash - (quantity * price) 
        self.stock_name = stock_name

    def sellStock(self, shares, stock_name):
        self.shares = 0
        self.symbol =  stock_name

     def buyMutualFund(self, shares, fund_name):
        self.shares = 0
        self.fund_name = fund_name    

class Stock(object):
    def __init__(self, price, symbol):
        self.price = 0
        self.symbol = symbol
  
class MutualFund(object):
    def __init__(self, price, symbol):
        self.price = 0
        self.symbol = symbol

    def buyMutualFund(self, price, symbol):
        self.price = 0
        self.symbol = symbol
    
    
    
 #def print(self)
       #print ("cash:" + self.cash
        #for mf in self.mf: print mf.name







