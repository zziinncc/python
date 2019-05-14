import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(0, 1, 1000)

y = np.sin(2 * np.pi * 30 * x)

plt.plot(x, y)

plt.show()