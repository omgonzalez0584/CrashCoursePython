import matplotlib.pyplot as plt

from randomwalk import RandomWalk

#Make a random walk , and plot the points
while True:
    #Creacion de objeto y llamada al metodo
    rw = RandomWalk(50000)
    rw.fill_walk()

    #Generate scatter
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers, cmap=plt.cm.Blues,edgecolor='none',s=1)

    #Emphasize the first and last points.
    plt.scatter(0,0,c='green',edgecolor='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',s=100)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
