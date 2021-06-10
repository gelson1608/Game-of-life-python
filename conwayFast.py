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
    def __init__(self, initial_state, rules, N=4):
        self.arr = np.zeros((N,N), np.uint)
        self.grid = set()
        self.initial_state = initial_state
        self.rules = rules
        self.max_size = N
        self.progression = []
        self.previous_state = None
        
    def getStates(self):
        self.arr.fill(0)
        #print("grid: {}".format(self.grid))
        for key in self.grid:
            print("hola {}".format(key))
            if (key[0]==key[1]):
                print("rompe primo")
            self.arr[key[0],key[1]] = 1
        return self.arr
    
    def getNeighbours(self, elem, max_size):
        l = []
        if elem[0]-1 >= 0:
                l.append((elem[0] - 1, elem[1]))
        if elem[0]-1 >= 0 and elem[1]-1 >= 0:
                l.append((elem[0]-1, elem[1]-1))
        if elem[0]-1 >= 0 and elem[1]+1 < max_size:
            l.append((elem[0]-1, elem[1]+1))
        if elem[1]-1 >= 0:
            l.append((elem[0], elem[1]-1))
        if elem[1]-1 >= 0 and elem[0]+1 < max_size:
            l.append((elem[0]+1, elem[1]-1))
        if elem[1]+1 < max_size:
            l.append((elem[0], elem[1]+1))
        if elem[0]+1 < max_size:
            l.append((elem[0]+1, elem[1]))
        if elem[1]+1 < max_size and elem[0]+1 < max_size:
            l.append((elem[0]+1, elem[1]+1))
        return l
    
    def evolve(self):
        state = self.grid
        #print("state: {}".format(state))
        if(state!=self.previous_state):
            #print("entro")
            self.previous_state = state.copy()
            #print(state)
            for val in self.previous_state:
                #print(val)
                self.progression.append(val)
            #print(self.progression)
            state = self.rules.apply_rules(self.grid, self.max_size, self.getNeighbours)
        self.progression.append(state)
        return self.progression
    
    def insertBlinker(self, index=(0,0)):
        '''
        Insert a blinker oscillator construct at the index position
        '''
        self.grid.add((index[0], index[1]+1))
        self.grid.add((index[0], index[1]+1))
        self.grid.add((index[0]+1, index[1]+1))
        self.grid.add((index[0]+2, index[1]+1))

    def insertGlider(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid.add((index[0], index[1]+1))
        self.grid.add((index[0]+1, index[1]+2))
        self.grid.add((index[0]+2, index[1]))
        self.grid.add((index[0]+2, index[1]+1))
        self.grid.add((index[0]+2, index[1]+2))

    def insertGliderGun(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid.add((index[0]+1, index[1]+26))

        self.grid.add((index[0]+2, index[1]+24))
        self.grid.add((index[0]+2, index[1]+26))

        self.grid.add((index[0]+3, index[1]+14))
        self.grid.add((index[0]+3, index[1]+15))
        self.grid.add((index[0]+3, index[1]+22))
        self.grid.add((index[0]+3, index[1]+23))
        self.grid.add((index[0]+3, index[1]+36))
        self.grid.add((index[0]+3, index[1]+37))

        self.grid.add((index[0]+4, index[1]+13))
        self.grid.add((index[0]+4, index[1]+17))
        self.grid.add((index[0]+4, index[1]+22))
        self.grid.add((index[0]+4, index[1]+23))
        self.grid.add((index[0]+4, index[1]+36))
        self.grid.add((index[0]+4, index[1]+37))

        #GliderGun was not working due to bad positioning of the left block 
        self.grid.add((index[0]+5, index[1]+2))
        self.grid.add((index[0]+5, index[1]+3))
        self.grid.add((index[0]+5, index[1]+12))
        self.grid.add((index[0]+5, index[1]+18))
        self.grid.add((index[0]+5, index[1]+22))
        self.grid.add((index[0]+5, index[1]+23))

        self.grid.add((index[0]+6, index[1]+2))
        self.grid.add((index[0]+6, index[1]+3))
        self.grid.add((index[0]+6, index[1]+12))
        self.grid.add((index[0]+6, index[1]+16))
        self.grid.add((index[0]+6, index[1]+18))
        self.grid.add((index[0]+6, index[1]+19))
        self.grid.add((index[0]+6, index[1]+24))
        self.grid.add((index[0]+6, index[1]+26))

        self.grid.add((index[0]+7, index[1]+12))
        self.grid.add((index[0]+7, index[1]+18))
        self.grid.add((index[0]+7, index[1]+26))

        self.grid.add((index[0]+8, index[1]+13))
        self.grid.add((index[0]+8, index[1]+17))

        self.grid.add((index[0]+9, index[1]+14))
        self.grid.add((index[0]+9, index[1]+15))
    
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
        print(conf)
        rows = conf.split('$')
        print(rows)
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
                            self.grid.add((index[0]+rowNum, index[1]+acum+j))
                    lastChar = ''
                    acum = acum + times
                    times = 1
            acum = 0
    
    def insertPeriod14GliderGun(self, index=(0,0)):
        conf = ""
        times = 1
        acum = 0
        rowNum = 0
        lastChar= ''
        file = open("./all/period14glidergun.rle", "r")
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
                            self.grid.add((index[0]+rowNum, index[1]+acum+j))
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
                            self.grid.add((index[0]+rowNum, index[1]+acum+j))
                    lastChar = ''
                    acum = acum + times
                    times = 1
            if lastChar!='':
                rowNum = rowNum + int(lastChar) - 1
            lastChar = ''
            acum = 0

    def insertKnightShipPartial(self, index=(0,0)):
        conf = ""
        times = 1
        acum = 0
        rowNum = 0
        lastChar= ''
        file = open("./all/knightshippartial.rle", "r")
        for line in file:
            if line[0]!='#' and line[0]!='x':
                conf = conf + line.strip()
        print(conf)
        rows = conf.split('$')
        print(rows)
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
                            self.grid.add((index[0]+rowNum, index[1]+acum+j))
                    lastChar = ''
                    acum = acum + times
                    times = 1
            acum = 0

class SparseSetRules():
    def apply_rules(self, grid, max_size, get_neighbours):
        counter = {}
        for elem in grid:
            if elem not in counter:
                counter[elem]=0
            nb = get_neighbours(elem, max_size)
            for n in nb:
                if n not in counter:
                    counter[n] = 1
                else:
                    counter[n] += 1
        for c in counter:
            if(counter[c] < 2 or counter[c] > 3):
                grid.discard(c)
            if counter[c] == 3:
                grid.add(c)
        return grid
    
    #
            

    
                    
                    
                    
            
        
        