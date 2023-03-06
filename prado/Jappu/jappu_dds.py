import pandas as pd

# file = 'C:\Users\Administrator\AppData\Roaming\MetaQuotes\Terminal\/6E0D8AD1CB44552398DC2AD0D2C56F9E\MQL4\Files\/142054306_1.csv'

file = 'prado\Jappu\/142054306_1.csv'

df = pd.read_csv(file, sep=';')
print(df)