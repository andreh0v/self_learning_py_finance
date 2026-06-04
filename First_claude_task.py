# Building a portoflio tracker for a private investor. It is tracking positions, calculating retruns and getting the full portfolio overview.
# These task was created with claude,
from datetime import date
NOK_TO_USD = 9.3166

class stock:
    def __init__(self, ticker, name, shares, currency, buy_price, current_price, buy_year, buy_month):
        self.ticker = ticker
        self.name = name
        self.shares = shares
        self.currency = currency
        self.buy_price = buy_price
        self.current_price = current_price
        self.buy_year = buy_year
        self.buy_month = buy_month

    def print_stock_info(self): pass


portfolio = {
    "AAPL": {
        "ticker": "AAPL",
        "name": "Apple Inc.",
        "shares": 10,
        "currency": "USD",
        "buy_price": 150.0,
        "current_price": 192.5,
        "buy_year": 2023,
        "buy_month": 1
    },
    "EQNR": {
        "ticker": "EQNR",
        "name": "Equinor ASA",
        "shares": 25,
        "currency": "NOK",
        "buy_price": 310.0,
        "current_price": 278.4,
        "buy_year": 2022,
        "buy_month": 6
    },
    "MSFT": {
        "ticker": "MSFT",
        "name": "Microsoft Corp.",
        "shares": 5,
        "currency": "USD",
        "buy_price": 280.0,
        "current_price": 415.0,
        "buy_year": 2021,
        "buy_month": 11
    }
}

test_stock = portfolio["AAPL"]
# Month converter to get a written output
months = {
    1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September",
    10: "October", 11: "November", 12: "December"}


# Task 1 - simply printing stock info

def print_stock_info(stock):
    print(f"Ticker: {stock['ticker']}")
    print(f"Name: {stock['name']}")
    print(f"Shares in portfolio: {stock['shares']}")
    print(f"Buy price: {stock['buy_price']} {stock['currency']} per share")
    print(f"Current stock price {stock['current_price']}  {stock['currency']} per share")
    print(f" Bought {months[stock['buy_month']]} / {stock['buy_year']}")

#Task 2-Retrurning total return in stock currency
def calculate_return(stock):
    return round((stock['current_price'] - stock['buy_price']) * stock['shares'],2)

#This is a required calculation to do since calculat_return is required furhter on
for ticker, stock in portfolio.items():
    result= calculate_return(stock)
    if result > 0:
        print(f"Stock:{stock['ticker']} Gain: {result:.2f} {stock['currency']}")
    else:
        print(f"Stock:{stock['ticker']} Loss: {result:.2f} {stock['currency']}")

#Task 3 - look at how many full years the stock have been hold
def get_holding_period(stock):
    return date.today().year - stock['buy_year']
for ticker, stock in portfolio.items():
    holding_period = get_holding_period(stock)
    print(f"{stock['ticker']} has been held for {holding_period} years")

#Task 4 A function for practise on elif
def get_percentage_return(stock):
    return calculate_return(stock) / stock['buy_price'] * 100

def get_return_level(stock):
    pct = get_percentage_return(stock)
    if pct <= -10:
        return "Large Loss"
    elif pct <= -5:
        return "Small Loss"
    elif pct < 5:
        return "Flat return"
    elif pct < 15:
        return "Good return"
    else :
        return "Great return"


#Task 5
#Adding a ffucntion that will convert a given value to usd if in nok, error if other
def convert_to_usd(value, currency, NOK_TO_USD):
#Converts a given cash value into USD based on the provided data
    if currency == "USD":
        return value
    elif currency == "NOK":
        return value/NOK_TO_USD
    else:
        # A safety fallback in case an unsupported currency slips in
        raise ValueError(f"Unsupported currency: {currency}")

#A function that run through the portfolio & returns total current value
def get_current_portfolio_value(portfolio, NOK_TO_USD):
    current_value = 0
    for ticker, stock in portfolio.items():
     current_value +=  convert_to_usd(stock['current_price'], stock['currency'], NOK_TO_USD) * stock['shares']
    return current_value
print(f"Total portfolio value: $ {get_current_portfolio_value(portfolio, NOK_TO_USD,):.2f}")

