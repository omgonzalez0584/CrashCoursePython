#Grafica en un mapa la cantidad de habitantes en America del Norte
import pygal
from pygal.maps.world import World

wm = World()
wm.title = "Population of Country in North America"
wm.add('North America',{'ca':3412600,'us':30934900,'mx':113423000})
wm.render_to_file('na_population.svg')

wm.render_to_file('na_population.svg')
