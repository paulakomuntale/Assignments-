import matplotlib.pyplot as plt

#this is a pie chart

sizes = [30, 25, 20, 15, 10]
labels = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']
colors = ['gold', 'lightblue', 'lightgreen', 'pink', 'coral']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Programming Language Popularity')
plt.axis('equal')  # Equal aspect ratio ensures the pie is circular
plt.show()