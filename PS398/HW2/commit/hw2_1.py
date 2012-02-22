class Portfolio(object):


    def __init__(self, cash, stocks, mf):
        self.cash = 0
        self.stocks = ()
        self.mf = ()

    def addCash(self, amount_add):
        if addCash > 0:             #seems you don't really need "else" here bc you're not returning stuffz
        self.cash += amount_add
       
    def withdrawCash(self, amount_withdraw):
        if withdrawCash > 0 and amount_withdraw <= self.cash: #refering back up to how much cash you have
        self.cash -= amount_withdraw
        return: True
        else: 
        return False
        
    def  buyStock(self, shares, stock_name, price):
        if stock and shares > 0 and 
            if shares * stock.price <= self.cash:
                self.cash -= shares*stock.price         #shares * price has to be less than cash
            else:
                return False

    def sellStock(self, shares, stock, price):          #can't figure out 
        if shares >= 0 and
            if self.price <= self.cash:
                self.cash += shares*stock.price
            else:
                return False


     #def buyMutualFund(self, shares, fund_name, price):      #this attempt doesn't cover the fractional component
        #if shares >= 0 and
            #if shares * self.price <= self.cash:
                #self.cash -= shares * price
       

class asset:
    def __init__(self, price, name):
        if price > 0 and name:
        self.price = price
        self.name = name
        else: 
            return print ("enter price and symbol for your asset")
            
class Stock(asset):
    def sell_stock_price(self):
    return random.uniform(.5 , 1.5)*self.price              # source http://docs.python.org/library/random.html
                                                            #self.price here SHOULD refer back to moneymaker
                                                           #ugh i'm not really sure this relates correctly to port folio
  
class MutualFund(asset):
    def sell_mf_price(self)
    return random.uniform (.9,1.2) *self.price
    
    

#def print(self)
       #print ("cash:" + self.cash
       # for mf in self.mf: print mf.fund_name
       # for stocks in self.socks print sock







