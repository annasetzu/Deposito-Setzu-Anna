import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#lavoro sul dataset
df = pd.read_csv('AirQualityUCI.csv', sep=';')

df['CO(GT)'] = pd.to_numeric(df['CO(GT)'].str.replace(',', '.'))
df = df[['Date', 'Time', 'CO(GT)']].replace(-200, np.nan).dropna()

# calcolo media e assegno etichetta
daily_mean = df.groupby('Date')['CO(GT)'].transform('mean')
df['Label'] = np.where(df['CO(GT)'] > daily_mean, "scarsa qualità dell'aria", "buona qualità dell'aria")
print(df.head(24))

# 3 valori più alti al giorno
higher = df.groupby('Date').apply(lambda g: g.nlargest(3, 'CO(GT)'))
print(higher.head(10))

# Percentuale settimanale
df['Week'] = pd.to_datetime(df['Date'], dayfirst=True).dt.isocalendar().week
weekly = df.groupby('Week')['Label'].apply(lambda x: (x == "scarsa qualità dell'aria").mean()*100)
print(weekly)

global_mean = (df['Label'] == "scarsa qualità dell'aria").mean()*100
print(global_mean)

# Random forest
df['Hour'] = pd.to_datetime(df['Time'], format='%H.%M.%S').dt.hour
X = df[['Hour', 'CO(GT)']]
y = (df['Label'] == "scarsa qualità dell'aria").astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(accuracy_score(y_test, y_pred))