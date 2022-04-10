import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
loc, scale = 0., 1.
s = np.random.laplace(loc, scale, 1000)
result_list = list(map(lambda x : x+50,s))
plt.hist(result_list, 30, density=True)
plt.show()
