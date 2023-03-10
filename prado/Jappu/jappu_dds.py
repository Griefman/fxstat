import pandas as pd

file = 'prado\\Jappu\\142054306_1.csv'
# file = '142054306_1.csv'  # for Pycharm


df = pd.read_csv(file, sep=';')


def dataframe_by_month(month, dataframe):
    dataframe_month = dataframe.loc[dataframe['Date'].str.contains(month)]
    return dataframe_month


def get_max_dd_by_month(month_dataframe):
   max_dd = round(month_dataframe['dd'].min(), 2)
   max_dd_percent = int(month_dataframe['dd'].max()) + 1
#    print(month_dataframe.loc[month_dataframe['dd'] == max_dd])
   return max_dd, max_dd_percent


df['dd'] = df['Equity'] - df['Balance']
df['percent'] = (df['Balance'] - df['Equity']) / df['Balance'] * 100

dates = ['2023.02', '2023.03']
for date in dates:
    month_df = dataframe_by_month(date, df)
    print(f'---------- {date} ----------')
    print(f'Max DD: {get_max_dd_by_month(month_df)[0]}$')
    print(f'Max DD in percents: {get_max_dd_by_month(month_df)[1]}%')
    # get_max_dd_by_month(month_df)

