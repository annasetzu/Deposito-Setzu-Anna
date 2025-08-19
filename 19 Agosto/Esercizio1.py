import pandas as pd

# carico il dataset
df = pd.read_csv('19 Agosto\\archive\pjm_hourly_est.csv')

# converto la colonna datetime
df['Datetime'] = pd.to_datetime(df['Datetime'])

# Aggiungo colonna solo con la data
df['Date'] = df['Datetime'].dt.date

# calcolo media giornaliera
daily_mean = df.groupby('Date')['PJM_Load'].transform('mean')

# mappo True/False in stringhe 'Alto'/'Basso'
df['Consumo'] = df['PJM_Load'] > daily_mean
df['Consumo'] = df['Consumo'].map({True: 'Alto', False: 'Basso'})

# stampo le prime 24 righe (per vedere se funziona)
print(df.head(24))