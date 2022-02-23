import pandas as pd

df = pd.read_excel("data.xlsx")

df.time = pd.to_datetime(df.time, format='%Y-%m-%d %H:%M:%S')
buckets = df.groupby([pd.Grouper(key='time', freq='15Min')])  # split data into 15 min intervals

total_sales = buckets.sum().reset_index()  # create new df with total sales
total_transactions = buckets.size().reset_index(name='transactions')  # create new df with total transactions
final_df = pd.merge(total_sales, total_transactions, left_on='time', right_on='time', how='left')  # combine both dfs to one df

final_df.to_csv('data.csv', index=False) # output df to a new csv file
