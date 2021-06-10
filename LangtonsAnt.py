# -*- coding: utf-8 -*-
"""
"""
import numpy as np

class langtonsAntGame():
  
    def __init__(self, initial_state, initial_pos, it, N=256):
        self.initial_state = initial_state
        self.max_size = N
        self.arr = np.zeros((N,N), np.uint)
        self.it = it
        self.pos = initial_pos
        self.grid = set()
        self.direction = [(0,1), (1,0), (0,-1), (-1,0)]
        self.nextState = -1

    def setGrid(self):
        self.grid.add(self.pos)
        for pos in self.initial_state:
            self.grid.add(pos)
    
    def getStates(self):
        #print("\nGrid:")
        #print(self.grid)
        self.arr.fill(0)
        for pos in self.grid:
            #print("pos: {}".format(pos))
            #print(self.arr[pos])
            self.arr[pos] = 1
            #print(self.arr[pos])
        #print(self.arr)
        return self.arr
    
    def setNextState(self, num):
        if self.nextState == 3 and num == 1:
            self.nextState = 0
        elif self.nextState == 0 and num == -1:
            self.nextState = 3
        else:
            self.nextState = self.nextState + num
    
    def evolve(self):
        #print("hahahha")
        #print(self.pos)
        #print(self.grid)
        if self.pos not in self.grid: 
            #inverts the colour
            self.setNextState(1)
            self.grid.add((self.pos))
            #print("after adding")
            #print(self.grid)
            #print("Current index: {}".format(self.nextState))
            self.pos = (self.pos[0] + self.direction[self.nextState][0], self.pos[1] + self.direction[self.nextState][1])
            #print("next pos: {}".format(self.pos))
            #print("Next state: {}".format(self.nextState))
              
        elif self.pos in self.grid:
            
            self.setNextState(-1)
            self.grid.remove(self.pos)
            #print("After removing")
            #print(self.grid)
            #print("Current index: {}".format(self.nextState))
            self.pos = (self.pos[0] + self.direction[self.nextState][0], self.pos[1] + self.direction[self.nextState][1])
            #print("next pos: {}".format(self.pos))

    
                    
                    
                    
            
        
        
