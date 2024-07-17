# import pandas as pd

# data =pd.DataFrame( {
#     'calories': [420,380,390],
#     'duration':[50,40,45]
# })

# print(data)


##########################################

# import pandas as pd

# data = {
#     'calories':[420,380,390],
#     'duration':[50,40,45]
# }

# df = pd.DataFrame(data, index = ['day1', 'day2', 'day3'])

# print(df)


##########################################

import pandas as pd

df = pd.read_csv("C:\\Users\\Olive\\Downloads\\Visual Studio Code\\W3\\python\\pandas\\pokemon.csv")

print(df)