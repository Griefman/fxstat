import pandas as pd

filename = 'prado_mar-23.xlsx'

df = pd.read_excel(filename, index_col=0)
print(df)
