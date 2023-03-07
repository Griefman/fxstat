import pandas as pd

file = 'prado\\Jappu\\142054306_1.csv'
# file = '142054306_1.csv' # for Pycharm


df = pd.read_csv(file, sep=';')


# df_dds = pd.Series(df['Equity'] - df['Balance'], name='dds')
# print(f'Максимальная просадка: {int(df_dds.min()) - 1}$')
def dataframe_by_month(month, dataframe):
    dataframe_month = dataframe.loc[dataframe['Date'].str.contains(month)]
    return dataframe_month


def get_max_dd_by_month(month_dataframe):
    print(month_dataframe.loc[month_dataframe['dd'] == month_dataframe['dd'].min()])

df['dd'] = df['Equity'] - df['Balance']
# print(df)
dates = ['2023.02', '2023.03']
for date in dates:
    month_df = dataframe_by_month(date, df)
    get_max_dd_by_month(month_df)

