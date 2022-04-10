import matplotlib.pyplot as plt
from scipy.stats import laplace, norm
import numpy as np
x = np.linspace(laplace.ppf(0.01),
                laplace.ppf(0.99), 100)
plt.plot(x, laplace.pdf(x),
       'r-', lw=2, alpha=0.6, label='laplace pdf')
plt.legend()
plt.show()
