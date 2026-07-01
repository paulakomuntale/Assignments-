import matplotlib.pyplot as plt

categories = ['Product A', 'Product B', 'Product C', 'Product D']
values = [85, 70, 95, 60]

plt.barh(categories, values, color='skyblue')
plt.title('Horizontal Bar Chart')
plt.xlabel('Values')
plt.ylabel('Products')
plt.show()