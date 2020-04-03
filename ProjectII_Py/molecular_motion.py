import matplotlib.pyplot as plt

from randomwalk import RandomWalk

#Make a random walk , and plot the points
while True:
    #Creacion de objeto y llamada al metodo
    rw = RandomWalk(5000)
    rw.fill_walk()

    #Generate scatter
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values,rw.y_values,linewidth=1)

    #Emphasize the first and last points.

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
