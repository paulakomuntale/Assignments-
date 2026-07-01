import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Plot 1
x = np.linspace(0, 10, 50)
axes[0, 0].plot(x, np.sin(x), 'r-')
axes[0, 0].set_title('Sine')

# Plot 2
axes[0, 1].bar(['A', 'B', 'C'], [10, 20, 15])
axes[0, 1].set_title('Bar')

# Plot 3
axes[1, 0].scatter(np.random.randn(50), np.random.randn(50))
axes[1, 0].set_title('Scatter')

# Plot 4
axes[1, 1].pie([30, 20, 50], labels=['X', 'Y', 'Z'])
axes[1, 1].set_title('Pie')

plt.tight_layout()
plt.show()