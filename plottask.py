#plottask.py
'''The following program built a normal distribution histogram (considering mean 5, std 2 and number of values 100)
It also plot of the function  h(x)=x3 in the range [0, 10].'''
#Author: Cecilia Pastore 

# import the needed libraries 
import numpy as np
import matplotlib.pyplot as plt

# Set the parameters for the normal distribution
mean_x = 5
std_x = 2
values_x = 1000

# Generate random values from normal distribution
x = np.random.normal(loc=mean_x, scale=std_x, size=values_x)
# plot an histongram of the random value 
plt.hist(x, alpha=0.5, color='r', label='Normal Distribution')

# Plot function h(x) = x^3
x_points = np.linspace(0, 10, 100)
y_points = x_points ** 3
plt.plot(x_points, y_points, color='b', linestyle='dotted', label='h(x) = x^3')

# Define labels, title, legend, and grid
font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}
plt.xlabel('x - random normal number', fontdict=font2)
plt.ylabel('y = x^3', fontdict=font2)
plt.title('Task Week 8', fontdict=font1)
plt.legend(loc='upper left')
plt.grid(linestyle='--', alpha=0.7)

# Show the plot
plt.show()