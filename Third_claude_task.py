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

        #Task 2 Reshape into price table
    except FileNotFoundError:
        print("Could not find historical_prices.csv - check the filename & folder path")