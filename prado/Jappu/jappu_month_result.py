import pandas as pd


file_name = 'prado_mar-23.xlsx'

df = pd.read_excel(file_name,  sheet_name='Лист1')
# print(df)
short_df = df[['Item', 'Open Time', 'Size', 'Commission', 'Taxes', 'Swap', 'Profit']]
usdjpy_df = short_df.loc[short_df['Item'] == 'usdjpy']
# print(usdjpy_df)
filtered_df = usdjpy_df.loc[usdjpy_df['Commission'] != 'cancelled']
profit = pd.to_numeric(filtered_df['Profit']).sum()
print(profit)
# pd.to_numeric(filtered_df['Size'])
lots = filtered_df['Size'].astype(float).sum()
print(lots)
# pd.to_numeric(filtered_df['Commission'])
commission = filtered_df['Commission'].astype(float).sum()
print(commission)
pd.to_numeric(filtered_df['Taxes'])
taxes = filtered_df['Taxes'].sum()
print(taxes)
pd.to_numeric(filtered_df['Swap'])
swap = filtered_df['Swap'].sum()
print(swap)
# pure_profit = profit - commission - swap - taxes
# print(pure_profit)

# day_10_march_df = filtered_df[filtered_df['Open Time'].str.contains('2023.03.10')]
# print(day_10_march_df)
# profit_100323 = day_10_march_df['Profit'].sum()
# print(profit_100323)

