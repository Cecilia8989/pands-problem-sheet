
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

mean_x = 5
std_x= 5
values_x = 1000

x = np.random.normal(mean_x, std_x, values_x)
sns.histplot(x, color='r')

x_points = np.linspace(0,10,100)
y_points = x_points**3

plt.plot(x_points,y_points, color = 'b')
plt.grid(True)

plt.xlabel('x - random normal number')
plt.ylabel('y = x^3')
plt.title('Task Week 8')


plt.show()