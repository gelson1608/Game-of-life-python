# -*- coding: utf-8 -*-
"""
"""
import LangtonsAnt

N = 100

state = {}
pos = (49, 49)
ant = LangtonsAnt.langtonsAntGame(state, pos, 1000, N)
ant.setGrid()

cells = ant.getStates()
#-------------------------------
#plot cells
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
for i in range(10000):
    ant.evolve()
    
plt.gray()

img = plt.imshow(cells, animated=True)

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
