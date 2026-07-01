import matplotlib.pyplot as plt
import numpy as np

data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(2, 1.5, 100)
data3 = np.random.normal(-1, 0.8, 100)

plt.boxplot([data1, data2, data3], tick_labels=['Group A', 'Group B', 'Group C'])
plt.title('Box Plot Example')
plt.ylabel('Values')
plt.grid(True, alpha=0.3)
plt.show()