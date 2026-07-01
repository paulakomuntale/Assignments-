import matplotlib.pyplot as plt
import numpy as np
#this is a scatter plot

x = np.random.randn(100)
y = np.random.randn(100)
colors = np.random.rand(100)
sizes = np.random.randint(20, 100, 100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')
plt.title('Scatter Plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.colorbar()
plt.show()