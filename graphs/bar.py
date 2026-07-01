#simple bar graph

import matplotlib.pyplot as plt

w=['John','Mike','Sarah','Jessica']
z=[5,7,3,8]

plt.bar(w,z)
plt.title('Simple Bar Graph')
plt.xlabel('Names of students')
plt.ylabel('Age of students')

plt.show()