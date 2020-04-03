import json
from country_codes import get_country_code
from pygal.maps.world import World
from pygal.style import RotateStyle
import pygal

#Load the data into a list
filename = 'population_data.json'

with open(filename) as f:
    pop_data = json.load(f)

country_pop = {}


#Imprimir poblaciones del 2010 por pais
for pop_dictionary in pop_data:
    if pop_dictionary['Year']  == '2010':
        country = pop_dictionary['Country Name']
        population = int(float(pop_dictionary['Value']))
        code = get_country_code(country)
        if code:
            country_pop[code] = population
        else:
             missing = "Error" + ":" + country
             #print(missing)

#Grouping country by population
cc_pops1 , cc_pops2, cc_pops3 = {} , {} , {}
for cc , pop in country_pop.items():
    if pop < 10000000:
        cc_pops1[cc] = pop
    elif pop < 1000000000:
        cc_pops2[cc] = pop
    else:
        cc_pops3[cc] = pop


#See how many countries are in each level
print(len(cc_pops1),len(cc_pops2), len(cc_pops3))


##Visualizando Data
wm_style = RotateStyle('#9e6ffe') #Se crea una clase RotateStyle
wm = World(style=wm_style) # Agregar estilo a la grafica
wm.title = "World Population in 2010, by Country"
wm.add('0-10m',cc_pops1)
wm.add('10m-1bm',cc_pops2)
wm.add('>1bn',cc_pops3)
wm.render_to_file('mundial.svg')
