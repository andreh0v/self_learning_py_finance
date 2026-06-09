## Portfolio analysis using pandas. Reads data from portfolio.csv.
# Reuses convert_to_usd and EX_rate from the first task file.
import pandas as pd
from First_claude_task import convert_to_usd, EX_rate

# Show all columns instead of collapsing them with "..."
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


# A function that converts one row's value (for a given price column) to USD.
# It reuses convert_to_usd imported from the first file (DRY principle).
def value_in_usd(row, price_column):
    return convert_to_usd(row[price_column], row['currency'], EX_rate) * row['shares']


# This block only runs when THIS file is run directly, not when imported.
if __name__ == "__main__":
    # Task 7 - Defensive loading: everything that needs df sits inside the try,
    # so if the file is missing nothing below runs and we just show a message.
    try:
        # Task 1 - Load the CSV into a DataFrame
        df = pd.read_csv('portfolio.csv')
        print(df)

        # Task 2 - Add a calculated column for total return (rounded once, so it stays rounded everywhere)
        df['total_return'] = ((df['current_price'] - df['buy_price']) * df['shares']).round(2)
        print(df)

        # Task 3 - Add a percentage return column
        df['pct_return'] = (df['total_return'] / df['shares'] / df['buy_price'] * 100).round(2)
        print(df)

        # Task 4 - Filter the data
        winner = df[df['total_return'] > 0]
        looser = df[df['total_return'] < 0]
        NOK_STOCK = df[df['currency'] == 'NOK']
        Before_23 = df[df['buy_year'] < 2023]
        print("\nWinners:")
        print(winner[['ticker', 'total_return']])
        print("\nNOK holdings:")
        print(NOK_STOCK[['ticker', 'currency', 'current_price', 'pct_return']])

        # Task 5 - Summary statistics using pandas built-in functions
        total_value = (df['current_price'] * df['shares']).sum()
        average_return_pct = df['pct_return'].mean()
        best = df.loc[df['pct_return'].idxmax()]
        print(f"\nBest performer: {best['ticker']} with {best['pct_return']:.2f}%")

        # Task 6 - Fixing for currency (convert to USD before summing)
        df['current_price_usd'] = df.apply(value_in_usd, axis=1, price_column='current_price')
        df['buy_price_usd'] = df.apply(value_in_usd, axis=1, price_column='buy_price')
        df['total_return_usd'] = (df['current_price_usd'] - df['buy_price_usd']).round(2)
        # Whole-portfolio percentage is a single value, so it is a variable, not a column
        total_pct = df['total_return_usd'].sum() / df['buy_price_usd'].sum() * 100
        print(f"Total portfolio value : {df['current_price_usd'].sum():.2f} USD")
        print(f"Total portfolio return: {df['total_return_usd'].sum():.2f} USD")
        print(f"Total portfolio % return: {total_pct:.2f} %")

        # Stretch goal - Sort by percentage return and export the result to a new CSV
        df_sorted = df.sort_values('pct_return', ascending=False)
        df_sorted.to_csv('portfolio_analysed.csv', index=False)
        print("\nSaved analysed data to portfolio_analysed.csv")

    except FileNotFoundError:
        print("Could not find portfolio.csv - check the filename & folder path")