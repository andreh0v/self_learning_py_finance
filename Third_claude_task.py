#Coninuation on the skills learned in 1 & 2
#New tools:  time-series data, pct_change(), groupby(), std() for volatility, numpy, matplotlib charts
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Show all columns instead of collapsing them with "..."
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
#Importing functions
from Second_claude_task import value_in_usd

#Adding a block that makes only the coded non-functions load
if __name__ == "__main__":
    try:
        df = pd.read_csv("historical_prices.csv")
        print(df.head())
        print(df['ticker'].value_counts())

        #Task 2 Reshape into price table from long format
        prices = df.pivot (index='date', columns='ticker', values='close')
        print(prices)
        #Task 3 Monthly returns, rounded to 2 decimals
        returns = prices.pct_change()
        print((prices.pct_change() * 100).round(2))
        #Task 4 Volatility
        volatility = returns.std() #Calulates the highest std
        print((volatility * 100).round(4))
        print(f"Most volatile: {volatility.idxmax()}") #Highest std
        print(f"Least volatile: {volatility.idxmin()}") #Lowest std
        #Task 5 Average return per stock per annum
        avg_monthly = returns.mean()
        avg_annual = avg_monthly*12
        print((avg_annual * 100).round(2))
        #Task 6 Numpy
        #Numpy is the numerical engine underneath pandas.
        #Annualised volatility is the mobthly volatility scaled by the square root of the number of periods.
        annual_volatility = volatility * np.sqrt(12)
        print((annual_volatility * 100).round(2))
        #Task 7 Visualisation
        prices.plot(figsize=(10, 6), title= 'Monthly closing prices')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.tight_layout()
        plt.show()
        #Task 8 A risk comparison chart
        (volatility * 100).sort_values().plot(kind='bar', figsize=(8,5), title='Monthly volatility by stock (%)')
        plt.ylabel ('Volatility (%)')
        plt.tight_layout()
        plt.show
        #Task 8 Risk vs return
        plt.figure(figsize=(8,6))
        plt.scatter(volatility * 100, avg_monthly * 100)
        for ticker in prices.columns:
            plt.annotate(ticker, (volatility[ticker] * 100, avg_monthly[ticker] * 100))
        plt.xlabel('Risk - volatility (%)')
        plt.ylabel('Avrage monthly return (%)')
        plt.title('Risk vs return')
        plt.tight_layout()
        plt.savefig('risk_return.png')
        plt.show()
    except FileNotFoundError:
        print("Could not find historical_prices.csv - check the filename & folder path")