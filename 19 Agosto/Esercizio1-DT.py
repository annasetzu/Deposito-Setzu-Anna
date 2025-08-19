import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# carico il dataset
df = pd.read_csv('19 Agosto\\archive\pjm_hourly_est.csv')

# converto la colonna datetime
df['Datetime'] = pd.to_datetime(df['Datetime'])

# Aggiungo colonna solo con la data
df['Date'] = df['Datetime'].dt.date

# calcolo media giornaliera
daily_mean = df.groupby('Date')['PJM_Load'].transform('mean')

# creo variabile target
df['Consumo'] = df['PJM_Load'] > daily_mean
df['Consumo'] = df['Consumo'].map({True: 1, False: 0})

# creo feature
df['hour'] = df['Datetime'].dt.hour
df['dayofweek'] = df['Datetime'].dt.dayofweek
df['month'] = df['Datetime'].dt.month

X = df[['hour', 'dayofweek', 'month']]
y = df['Consumo']

# train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# modello creazione e train
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# valutazione modello
y_pred = model.predict(X_test)

df.loc[X_test.index, 'Predicted'] = y_pred
print(df.head(24))