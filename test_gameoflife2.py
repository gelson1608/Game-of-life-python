# -*- coding: utf-8 -*-
"""
Game of life script with animated evolution

Created on Tue Jan 15 12:37:52 2019

@author: shakes
"""
import conwayFast

N = 1024

#create the game of life object
rules = conwayFast.SparseSetRules()
state = {}
#life.insertBlinker((0,0))
life = conwayFast.GameOfLife(state, rules, N)
#life.insertGliderGun((2,2))
#life.insertKnightShipPartial((2,2))
#life.insertGliderGun((100,100))
life.insertPeriod14GliderGun((200,0))
#life.setCells()
cells = life.getStates() #initial state

#-------------------------------
#plot cells
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

plt.gray()

img = plt.imshow(cells, animated=True)

def animate(i):
    """perform animation step"""
    global life
    
    life.evolve()
    #print("bastaaaa")
    cellsUpdated = life.getStates()
    #print(cellsUpdated)
    
    img.set_array(cellsUpdated)
    
    return img,

interval = 50 #ms

#animate 24 frames with interval between them calling animate function at each frame
ani = animation.FuncAnimation(fig, animate, frames=24, interval=interval, blit=True)

plt.show()
