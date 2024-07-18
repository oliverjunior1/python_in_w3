import pandas as pd

df = pd.read_csv('C:\\Users\\Olive\\Downloads\\Visual Studio Code\\W3\\python\\pandas\\data2.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())