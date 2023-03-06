import pandas as pd

# file = 'C:\Users\Administrator\AppData\Roaming\MetaQuotes\Terminal\/6E0D8AD1CB44552398DC2AD0D2C56F9E\MQL4\Files\/142054306_1.csv'

file = 'prado\Jappu\/142054306_1.csv'

df = pd.read_csv(file, sep=';')


# df_dds = pd.Series(df['Equity'] - df['Balance'], name='dds')
# print(f'Максимальная просадка: {int(df_dds.min()) - 1}$')

df['dd'] = df['Equity'] - df['Balance']
# print(df)

big_dds = df['dd'].min()
print(big_dds)  
xxx = df.loc[df['dd'] == df['dd'].min()]
print(xxx)