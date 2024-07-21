# import pandas
# from sklearn import linear_model

# df= pandas.read_csv('C:\\Users\\Olive\\Downloads\\Visual Studio Code\\W3\\python\\machine learning\\data.csv')

# x = df[['Weight', 'Volume']]
# y = df['CO2']

# regr = linear_model.LinearRegression()
# regr.fit(X, y)

# predictedCO2 = regr.predict([[2300,1300]])

# print(predictedCO2)

#################################################

import pandas
from sklearn import linear_model

df = pandas.read_csv('C:\\Users\\Olive\\Downloads\\Visual Studio Code\\W3\\python\\machine learning\\data.csv')

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_)