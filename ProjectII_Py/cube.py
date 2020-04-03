import matplotlib.pyplot as plt

numbers = list(range(1,5))
cube = [ i ** 3 for i in numbers] #List Comprehension

plt.plot(numbers,cube) #Generando Grafica

#Titulos de los ejes
plt.title('Cubes Numbers',fontsize=24)
plt.xlabel('Value Numbers',fontsize=14)
plt.ylabel('Cubes Values',fontsize=14)


plt.show()
