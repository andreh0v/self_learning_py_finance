# Portfolio analysis using pandas. Reads data from portfolio.csv.
# Reuses convert_to_usd and EX_rate from the first task file.
import pandas as pd
from First_claude_task import convert_to_usd, EX_rate

# Show all columns instead of collapsing them with "..."
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


# A function that converts one row's current value to USD.
# It reuses convert_to_usd imported from the first file (DRY principle).
def value_in_usd(row, price_column):
    return convert_to_usd(row[price_column], row['currency'], EX_rate) * row['shares']


# This block only runs when THIS file is run directly, not when imported.
if __name__ == "__main__":
    # Task 1 - Load the CSV into a DataFrame
    df = pd.read_csv('portfolio.csv')
    print(df)

    # Task 2 - Add a calculated column for total return (rounded once, so it stays rounded everywhere)
    df['total_return'] = ((df['current_price'] - df['buy_price']) * df['shares']).round(2)
    print(df)

    #Task 3- Add a percentage return colum
    df['pct_return'] = (df['total_return'] / df['shares'] / df['buy_price'] * 100).round(2)
    print(df)
   #Task 4 - filter the data
    winner = df[df['total_return'] > 0]
    looser = df[df['total_return'] < 0]
    NOK_STOCK = df[df['currency'] == 'NOK']
    Before_23 = df[df['buy_year'] < 2023]
    print("\nWinners:")
    print(winner[['ticker', 'total_return']])
    print("\nNOK holdings:")
    print(NOK_STOCK[['ticker', 'currency', 'current_price', 'pct_return']])
