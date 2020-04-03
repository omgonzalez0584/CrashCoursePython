import matplotlib.pyplot as plt

#Valores
x = [1,2,3,4,5]
y = [1,4,9,16,25]

#Creacion de grafica
plt.scatter(x,y,s=100)

#Set chart title and label axes
plt.title("Squares Numbers",fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#Set size thick label
plt.tick_params(axis='both',which='major',labelsize=14)


#desplegar grafica
plt.show()
