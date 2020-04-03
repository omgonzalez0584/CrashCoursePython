import matplotlib.pyplot as plt

square = [1,4,9,16,25]
imput_values = [1,2,3,4,5]
plt.plot(imput_values,square,linewidth=5) #grueso de la linea generada
              #X        #Y

#Set chart title and label axes.
plt.title("Square numbers", fontsize=24) #titulo de la grafica

#Etiquetas y size de los ejes de la grafica
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#Set size of thick labels
plt.tick_params(axis='both',labelsize=14) #size de los  parametros de los ejes

plt.show() #Desplegar grafica
