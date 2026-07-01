import matplotlib.pyplot as plt

categories = ['Q1', 'Q2', 'Q3', 'Q4']
product_a = [10, 15, 12, 18]
product_b = [8, 12, 10, 14]
product_c = [5, 8, 7, 10]

plt.bar(categories, product_a, label='Product A')
plt.bar(categories, product_b, bottom=product_a, label='Product B')
plt.bar(categories, product_c, bottom=[product_a[i] + product_b[i] for i in range(len(categories))], label='Product C')

plt.title('Stacked Bar Chart')
plt.xlabel('Quarters')
plt.ylabel('Sales')
plt.legend()
plt.show()