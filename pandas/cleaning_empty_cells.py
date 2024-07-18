# import pandas as pd

# x = pd.read_csv('C:\\Users\\Olive\\Downloads\\Visual Studio Code\\W3\\python\\pandas\\data.csv')

# new_df = x.dropna()

# print(new_df.to_string())

#################################################

# import pandas as pd

# df = pd.read_csv('C:\\Users\\Olive\\Downloads\\Visual Studio Code\\W3\\python\\pandas\\data.csv')

# new_df = df.dropna(inplace=True)

# print(new_df.to_string())

#################################################

# import pandas as pd

# df = pd.read_csv('C:\\Users\\Olive\\Downloads\\Visual Studio Code\\W3\\python\\pandas\\data.csv')

# df.fillna(130,inplace=True)

# print(df)

#################################################

# import pandas as pd

# df = pd.read_csv('C:\\Users\\Olive\\Downloads\\Visual Studio Code\\W3\\python\\pandas\\data.csv')

# df['Calories'].fillna(130, inplace=True)

# print(df)

#################################################

# import pandas as pd

# df = pd.read_csv('C:\\Users\\Olive\\Downloads\\Visual Studio Code\\W3\\python\\pandas\\data.csv')

# df['Calories'].fillna(130, inplace= True)

# print(df)

#################################################

# import pandas as pd

# df = pd.read_csv('C:\\Users\\Olive\\Downloads\\Visual Studio Code\\W3\\python\\pandas\\data.csv')

# x = df['Calories'].mean()

# df['Calories'].fillna(x, inplace= True)

# print(df)

#################################################

# import pandas as pd

# df = pd.read_csv('C:\\Users\\Olive\\Downloads\\Visual Studio Code\\W3\\python\\pandas\\data.csv')

# x = df['Calories'].median()

# df['Calories'].fillna(x, inplace=True)

# print(df)

#################################################

import pandas as pd

df = pd.read_csv('C:\\Users\\Olive\\Downloads\\Visual Studio Code\\W3\\python\\pandas\\data.csv')

x = df['Calories'].mode()[0]

df['Calories'].fillna(x, inplace=True)

print(df)
