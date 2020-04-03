from dice import Dice
import pygal

#Create two dice
dice_1 = Dice()
dice_2 = Dice()

#Make some rolls, and store results in a list
results = []
for roll_num in range(1000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

#print(results)


#Analyze the results
max_result = dice_1.num_sides + dice_2.num_sides
frecuencies = []
for value in range(2,max_result+1):
    frecuency = results.count(value)
    frecuencies.append(frecuency)

#print(frecuencies)

#Visualizando resultados
hist = pygal.Bar()

hist.title = "Result of rolling one D6 1000 times."
hist.x_labels = [i for i in range(2,max_result+1)]
hist.x_title = "Results"
hist.y_title = "Frecuency of Result"

hist.add('D6 + D6',frecuencies)
hist.render_to_file('dice_visual.svg')
