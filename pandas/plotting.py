# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('C:\\Users\\Olive\\Downloads\\Visual Studio Code\\W3\\python\\pandas\\pokemon.csv')

# df.plot()

# plt.show()

#################################################

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\Olive\\Downloads\\Visual Studio Code\\W3\\python\\pandas\\data1.csv')

# df.plot(king='scatter', x='Duration', y = 'Calories')
df['Duration'].plot(kind='hist')

plt.show()