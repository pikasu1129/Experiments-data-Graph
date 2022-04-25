import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

pi = math.pi

x = np.linspace(0, 2 * pi, 100)
y = np.sin(x)


plt.plot(x, y, label = 'y = sinx')

plt.title('Sin Graph')
plt.xlabel('x axis')
plt.ylabel('y axis')

plt.legend()

plt.show()