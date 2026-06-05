# Building a portfolio tracker for a private investor. It tracks positions, calculates returns and gives a full portfolio overview.
# These tasks were created with Claude.
from datetime import date

EX_rate = 9.3166


class Stock:
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
    def calculate_return(self): pass
    def get_holding_period(self): pass
    def get_percentage_return(self): pass
    def get_return_level(self): pass


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
    print(f"Bought {months[stock['buy_month']]} / {stock['buy_year']}")


# Task 2 - Returning total return in stock currency
def calculate_return(stock):
    return round((stock['current_price'] - stock['buy_price']) * stock['shares'], 2)


# Task 3 - look at how many full years the stock has been held
def get_holding_period(stock):
    return date.today().year - stock['buy_year']


# Task 4 - A function for practise on elif
def get_percentage_return(stock):
    return calculate_return(stock) / stock['shares'] / stock['buy_price'] * 100


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
    else:
        return "Great return"


# Task 5 - Convert a value to USD if in NOK, error if other
def convert_to_usd(value, currency, EX_rate):
    # Converts a given cash value into USD based on the provided data
    if currency == "USD":
        return value
    elif currency == "NOK":
        return value / EX_rate
    else:
        # A safety fallback in case an unsupported currency slips in
        raise ValueError(f"Unsupported currency: {currency}")


# A function that runs through the portfolio & returns total current value
def get_current_portfolio_value(portfolio, EX_rate):
    current_value = 0
    for ticker, stock in portfolio.items():
        current_value += convert_to_usd(stock['current_price'], stock['currency'], EX_rate) * stock['shares']
    return current_value


# Task 6 - Finding the winner
def get_best_performer(portfolio):
    best_ticker = None  # Best current ticker does not exist yet
    best_return = float('-inf')  # Smallest possible value so the first stock always wins initially
    for ticker, stock in portfolio.items():
        current_return = get_percentage_return(stock)  # Only updates if a better return is found
        if current_return > best_return:
            best_ticker = ticker
            best_return = current_return
    return best_ticker, best_return


# Task 7 - (Stock class method stubs are defined at the top of the file)


# This block only runs when THIS file is run directly.
# When another file imports from this one, everything below is skipped.
if __name__ == "__main__":
    print_stock_info(test_stock)

    for ticker, stock in portfolio.items():
        result = calculate_return(stock)
        if result > 0:
            print(f"Stock:{stock['ticker']} Gain: {result:.2f} {stock['currency']}")
        else:
            print(f"Stock:{stock['ticker']} Loss: {result:.2f} {stock['currency']}")

    for ticker, stock in portfolio.items():
        holding_period = get_holding_period(stock)
        print(f"{stock['ticker']} has been held for {holding_period} years")

    print(f"{test_stock['ticker']}: {get_return_level(test_stock)}")
    print(f"Total portfolio value: $ {get_current_portfolio_value(portfolio, EX_rate):.2f}")

    best_ticker, best_return = get_best_performer(portfolio)
    print(f"Best performer : {best_ticker} {best_return:.2f}%")