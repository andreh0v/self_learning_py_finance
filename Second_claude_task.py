#Second claude task to work on pandas & csv files
import pandas as pd
from First_claude_task import convert_to_usd, EX_rate

#Task 1
df = pd.read_csv('portfolio.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
print(df)
#Task 2 Adding total return
df['total_return'] = (df['current_price'] - df['buy_price']) * df['shares']
print(df[['ticker','total_return']])
#Adding pct return
df['pct_return']= ((df['current_price']-df['buy_price'])/df['buy_price'],round(2) * 100
print(df[['ticker','pct_return']].round(2))