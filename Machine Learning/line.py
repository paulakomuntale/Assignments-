#basic line graph
import matplotlib.pyplot as plt

x = [0, 2, 4, 6, 10]
y = [0, 4, 8, 16, 36]

fig, ax = plt.subplots()
ax.plot(x, y,marker='o', linestyle='-', color='b', label='Line 1')

ax.set_title('Basic Line Graph')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

ax.legend()
plt.plot()

plt.show()