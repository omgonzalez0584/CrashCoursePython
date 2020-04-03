import pygal
from dice import Dice

#Creacion de objetos
dice_1 = Dice(8)
dice_2 = Dice(8)

results = [] # Guarda resultados
for roll in range(1000000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

#print(results) #Mostrando resultados "Prueba"

#Resultado maximo al tirar dados
max_result = dice_1.num_sides + dice_2.num_sides
frecuencias = []
for value in range(2,max_result+1):
    frecuencia = results.count(value)
    frecuencias.append(frecuencia)

# print(frecuencias) #Mostrando frecuencias "Prueba"

#Graficando resultados
hist = pygal.Bar() #Creando objeto Bar

hist.title = "Resultado de lanzar dos D8"
hist.x_labels = [i for i in range(2,max_result+1)]
hist.x_title = "Resultados"
hist.y_title = "Frecuencia de resultados"

hist.add('D8 + D8', frecuencias)
hist.render_to_file('d8_visual.svg')
