import pandas as pd 

df = pd.read_csv('candidatura.csv', low_memory=False)

for year, value in df.groupby('ano_eleicao'):
    value.to_csv(f'eleicao_{year}.csv', index=False)