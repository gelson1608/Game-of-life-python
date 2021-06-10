# -*- coding: utf-8 -*-
"""
The Game of Life (GoL) module named in honour of John Conway

This module defines the classes required for the GoL simulation.

Created on Tue Jan 15 12:21:17 2019

@author: shakes
"""
import numpy as np
from scipy import signal

class GameOfLife:
    '''
    Object for computing Conway's Game of Life (GoL) cellular machine/automata
    '''
    def __init__(self, N=256, finite=False, fastMode=False):
        self.grid = np.zeros((N,N), np.uint)
        self.neighborhood = np.ones((3,3), np.uint) # 8 connected kernel
        self.neighborhood[1,1] = 0 #do not count centre pixel
        self.finite = finite
        self.fastMode = fastMode
        self.aliveValue = 1
        self.deadValue = 0

    def getStates(self):
        '''
        Returns the current states of the cells
        '''
        return self.grid

    def getGrid(self):
        '''
        Same as getStates()
        '''
        return self.getStates()

    def evolve(self):
        '''
        Given the current states of the cells, apply the GoL rules:
        - Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        - Any live cell with two or three live neighbors lives on to the next generation.
        - Any live cell with more than three live neighbors dies, as if by overpopulation.
        - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
        '''

        #get weighted sum of neighbors
        #index = (0,0)
        nextState = []
        for i in range(0,len(self.grid)-1):
            for j in range(0,len(self.grid)-1):
                neighborsSum = 0
                if self.grid[i-1, j-1] == self.aliveValue:
                    neighborsSum=neighborsSum+1
                if self.grid[i, j-1] == self.aliveValue:
                    neighborsSum=neighborsSum+1
                if self.grid[i+1, j-1] == self.aliveValue:
                    neighborsSum=neighborsSum+1
                if self.grid[i-1, j] == self.aliveValue:
                    neighborsSum=neighborsSum+1
                if self.grid[i+1, j] == self.aliveValue:
                    neighborsSum=neighborsSum+1
                if self.grid[i-1, j+1] == self.aliveValue:
                    neighborsSum=neighborsSum+1
                if self.grid[i+1, j+1] == self.aliveValue:
                    neighborsSum=neighborsSum+1
                if self.grid[i, j+1] == self.aliveValue:
                    neighborsSum=neighborsSum+1

                #implement the GoL rules by thresholding the weights
                if self.grid[i, j] == self.aliveValue:
                    if neighborsSum < 2:
                        nextState.append(self.deadValue)
                    elif neighborsSum > 3:
                        nextState.append(self.deadValue)
                    else:
                        nextState.append(self.aliveValue)
                elif self.grid[i, j] == self.deadValue:
                    if neighborsSum == 3:
                        nextState.append(self.aliveValue)
                    else:
                        nextState.append(self.deadValue)

                neighborsSum = 0

        #update the grid
        nextState.reverse()
        for i in range(0,len(self.grid)-1):
            for j in range(0,len(self.grid)-1):
                self.grid[i,j] = nextState.pop()


    def insertBlinker(self, index=(0,0)):
        '''
        Insert a blinker oscillator construct at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue

    def insertGlider(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+2] = self.aliveValue
        self.grid[index[0]+2, index[1]] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+2] = self.aliveValue

    def insertGliderGun(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0]+1, index[1]+26] = self.aliveValue

        self.grid[index[0]+2, index[1]+24] = self.aliveValue
        self.grid[index[0]+2, index[1]+26] = self.aliveValue

        self.grid[index[0]+3, index[1]+14] = self.aliveValue
        self.grid[index[0]+3, index[1]+15] = self.aliveValue
        self.grid[index[0]+3, index[1]+22] = self.aliveValue
        self.grid[index[0]+3, index[1]+23] = self.aliveValue
        self.grid[index[0]+3, index[1]+36] = self.aliveValue
        self.grid[index[0]+3, index[1]+37] = self.aliveValue

        self.grid[index[0]+4, index[1]+13] = self.aliveValue
        self.grid[index[0]+4, index[1]+17] = self.aliveValue
        self.grid[index[0]+4, index[1]+22] = self.aliveValue
        self.grid[index[0]+4, index[1]+23] = self.aliveValue
        self.grid[index[0]+4, index[1]+36] = self.aliveValue
        self.grid[index[0]+4, index[1]+37] = self.aliveValue

        #GliderGun was not working due to bad positioning of the left block 
        self.grid[index[0]+5, index[1]+2] = self.aliveValue
        self.grid[index[0]+5, index[1]+3] = self.aliveValue
        self.grid[index[0]+5, index[1]+12] = self.aliveValue
        self.grid[index[0]+5, index[1]+18] = self.aliveValue
        self.grid[index[0]+5, index[1]+22] = self.aliveValue
        self.grid[index[0]+5, index[1]+23] = self.aliveValue

        self.grid[index[0]+6, index[1]+2] = self.aliveValue
        self.grid[index[0]+6, index[1]+3] = self.aliveValue
        self.grid[index[0]+6, index[1]+12] = self.aliveValue
        self.grid[index[0]+6, index[1]+16] = self.aliveValue
        self.grid[index[0]+6, index[1]+18] = self.aliveValue
        self.grid[index[0]+6, index[1]+19] = self.aliveValue
        self.grid[index[0]+6, index[1]+24] = self.aliveValue
        self.grid[index[0]+6, index[1]+26] = self.aliveValue

        self.grid[index[0]+7, index[1]+12] = self.aliveValue
        self.grid[index[0]+7, index[1]+18] = self.aliveValue
        self.grid[index[0]+7, index[1]+26] = self.aliveValue

        self.grid[index[0]+8, index[1]+13] = self.aliveValue
        self.grid[index[0]+8, index[1]+17] = self.aliveValue

        self.grid[index[0]+9, index[1]+14] = self.aliveValue
        self.grid[index[0]+9, index[1]+15] = self.aliveValue
    
    def insertVoldiag(self, index=(0,0)):
        conf = ""
        times = 1
        acum = 0
        rowNum = 0
        lastChar= ''
        file = open("./all/voldiag.rle", "r")
        for line in file:
            if line[0]!='#' and line[0]!='x':
                conf = conf + line.strip()
        
        rows = conf.split('$')
        for row in rows:
            rowNum = rowNum + 1
            for ch in row:
                if ch.isdigit():
                    if lastChar=='':
                        lastChar = ch
                    elif lastChar!='':
                        lastChar = lastChar + ch
                elif ch=='b' or ch=='o':
                    if lastChar!='':
                        times = int(lastChar)
                    for j in range(1, times+1):
                        if ch=='o':
                            self.grid[index[0]+rowNum, index[1]+acum+j] = self.aliveValue
                        else:
                            self.grid[index[0]+rowNum, index[1]+acum+j] = self.deadValue
                    lastChar = ''
                    acum = acum + times
                    times = 1
            acum = 0
    
    def insertPeriod256GliderGun(self, index=(0,0)):
        conf = ""
        times = 1
        acum = 0
        rowNum = 0
        lastChar= ''
        file = open("./all/period256glidergun.rle", "r")
        for line in file:
            if line[0]!='#' and line[0]!='x':
                conf = conf + line.strip()
        
        rows = conf.split('$')
        for row in rows:
            rowNum = rowNum + 1
            for ch in row:
                if ch.isdigit():
                    if lastChar=='':
                        lastChar = ch
                    elif lastChar!='':
                        lastChar = lastChar + ch
                elif ch=='b' or ch=='o':
                    if lastChar!='':
                        times = int(lastChar)
                    for j in range(1, times+1):
                        if ch=='o':
                            self.grid[index[0]+rowNum, index[1]+acum+j] = self.aliveValue
                        else:
                            self.grid[index[0]+rowNum, index[1]+acum+j] = self.deadValue
                    lastChar = ''
                    acum = acum + times
                    times = 1
            if lastChar!='':
                rowNum = rowNum + int(lastChar) - 1
            lastChar = ''
            acum = 0
            
    def insertFumaroleOnAchimsP11(self, index=(0,0)):
        conf = ""
        times = 1
        acum = 0
        rowNum = 0
        lastChar= ''
        file = open("./all/fumaroleonachimsp11.rle", "r")
        for line in file:
            if line[0]!='#' and line[0]!='x':
                conf = conf + line.strip()
        
        rows = conf.split('$')
        for row in rows:
            rowNum = rowNum + 1
            for ch in row:
                if ch.isdigit():
                    if lastChar=='':
                        lastChar = ch
                    elif lastChar!='':
                        lastChar = lastChar + ch
                elif ch=='b' or ch=='o':
                    if lastChar!='':
                        times = int(lastChar)
                    for j in range(1, times+1):
                        if ch=='o':
                            self.grid[index[0]+rowNum, index[1]+acum+j] = self.aliveValue
                        else:
                            self.grid[index[0]+rowNum, index[1]+acum+j] = self.deadValue
                    lastChar = ''
                    acum = acum + times
                    times = 1
            if lastChar!='':
                rowNum = rowNum + int(lastChar) - 1
            lastChar = ''
            acum = 0
                    
                    
                    
            
        
        