# from scipy import io
# import numpy as np

# arr = np.arange(10)

# io.savemat('arr.mat', {'vet':arr})

# print(arr)

#################################################

# from scipy import io
# import numpy as np

# arr = np.arry([0,1,2,3,4,5,6,7,8,9,])

# io.savemat('arr.mat', {'vec', arr})

# mydata = io.loadmat('arr.mat')

# mydata = io.loadmat('arr.mat')

# print(mydata)

#################################################

from scipy.interpolate import interp1d
import numpy as np

xs = np.arrange(10)
ys = 2*xs + 1

interp_func = interp1d(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)