# from numpy import random

# x = random.exponential(scale=2, size=(2, 3))

# print(x)

##########################################

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.exponential(size=1000), hist=False)

plt.show()





