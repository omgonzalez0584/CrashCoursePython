import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values,cmap=plt.cm.Reds,edgecolor='none',s=40)

#Set chart title and label axes
plt.title("Squares Numbers", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Squares of values",fontsize=14)



#Set the range for each axis
plt.axis([0,1100,0,1100000])


plt.show()
