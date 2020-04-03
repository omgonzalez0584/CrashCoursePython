#Eleva al cubo en un rango de 1 a 5000

import matplotlib.pyplot as plt

numbers = list(range(1,5001))
cubes = [i ** 3 for i in numbers]

plt.scatter(numbers,cubes,s=20,c=cubes,cmap=plt.cm.Reds)

plt.title('Cubes 1 - 50',fontsize=24)
plt.xlabel('Value Numbers',fontsize=14)
plt.ylabel('Value Cubes',fontsize=14)



plt.show()
