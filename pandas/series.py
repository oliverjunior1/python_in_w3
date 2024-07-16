# import pandas as pd

# a = [1,7,2]

# myvar = pd.Series(a)

# print(a)


##########################################

# import pandas as pd

# a = [1,7,2]
# myvar = pd.Series(a, index = ['x', 'y', 'z'])

# print(myvar)


##########################################

# import pandas as pd

# calories = pd.Series({'day1':420, 'day2':380, 'day3': 390})

# print(calories)


##########################################

import pandas as pd

data = {
    'calories': [420,380,390],
    'duration':[50,40,45]
}

myvar = pd.DataFrame(data)

print(myvar)