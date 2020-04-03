import pygal
from randomwalk import RandomWalk

def rw_coordenadas():
    """Genera las Coordendas de los Pasos Aleatorios """
    temp = []
    for index in range(len(rw.y_values)):
        x = rw.x_values[index]
        y = rw.y_values[index]
        coordenada = x,y
        temp.append(coordenada)
    return temp


rw = RandomWalk(50)
rw.fill_walk()

rw_visual = pygal.XY()
rw_visual.title = "Randon Walk"
coordenadas = rw_coordenadas()

rw_visual.add('Inicio',[(0,0)])
rw_visual.add('Pasos',coordenadas)
rw_visual.add('Fin',[(rw.x_values[-1],rw.y_values[-1])])
rw_visual.render_to_file('rw_visual.svg')
