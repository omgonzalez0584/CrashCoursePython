from dice import Dice
import pygal

#Create a D6
dice = Dice()

#Make some rolls, and store results in a list
results = []
for roll_num in range(1000):
    result = dice.roll()
    results.append(result)

#print(results)


#Analyze the results
frecuencies = []
for value in range(1,dice.num_sides+1):
    frecuency = results.count(value)
    frecuencies.append(frecuency)

#print(frecuencies)

#Visualizando resultados
hist = pygal.Bar()

hist.title = "Result of rolling one D6 1000 times."
hist.x_labels = [i for i in range(1,dice.num_sides+1)] #Usando list comprehesions 
hist.x_title = "Results"
hist.y_title = "Frecuency of Result"

hist.add('D6',frecuencies)
hist.render_to_file('dice_visual.svg')
