# -*- coding: utf-8 -*-
"""
"""
import LangtonsAntColours

N = 100

state = {}
pos = (49, 49)
ant = LangtonsAntColours.langtonsAntGame(state, pos, 1000, N)
ant.setGrid()

cells = ant.getStates()
#-------------------------------
#plot cells
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.animation as animation

colors = ['white', 'red', 'yellow', 'black']
bounds = [0,1,2,3]

cmap = mpl.colors.ListedColormap(colors)
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

fig = plt.figure()

img = plt.imshow(cells, interpolation='none', cmap=cmap, norm=norm)

def animate(i):
    """perform animation step"""
    global ant
    
    ant.evolve()
    #print("bastaaaa")
    cellsUpdated = ant.getStates()
    #print(cellsUpdated)
    
    #print(cellsUpdated)
    img.set_array(cellsUpdated)
    
    return img,

interval = 1 #ms

#animate 24 frames with interval between them calling animate function at each frame
ani = animation.FuncAnimation(fig, animate, frames=24, interval=interval, blit=True)

plt.show()
