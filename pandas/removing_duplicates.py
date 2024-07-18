# import pandas as pd

# df = pd.read_csv('C:\\Users\\Olive\\Downloads\\Visual Studio Code\\W3\\python\\pandas\\data.csv')

# print(df.duplicated())

#################################################

import pandas as pd

df = pd.read_csv('C:\\Users\\Olive\\Downloads\\Visual Studio Code\\W3\\python\\pandas\\data.csv')

df.drop_duplicates(inplace=True)

print(df.to_string())