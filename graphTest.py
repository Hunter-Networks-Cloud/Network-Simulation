
#!/usr/bin/env python3
from random import randint
import numpy as np
from itertools import product
#-------class node-------

class Node:
    flag = "nodeType"
    def __init__(self, x, y):
        self.x = x
        self.y = y
        grid[x][y] = "N"
  
 

#-------class BaseStation------
class BaseStation:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        grid[x][y] = "B"  


    
grid = []
#Create a 100 x100 grid
for row in range(100):
    grid.append([])
    for col in range(100):
        grid[row].append(".")

number_of_nodes = input('number of nodes in network: ')
number_of_base_stations = input('number of base stations in network: ')
# creates nodes at random positions
for x in range(int(number_of_nodes)): 
    c_x = randint(0, len(grid)-1)
    c_y = randint(0, len(grid[0])-1)
    node1 = Node(c_x,c_y)
 
    

#creates base stations are random positions
for x in range(int(number_of_base_stations)): 
    c_x = randint(0, len(grid)-1)
    c_y = randint(0, len(grid[0])-1)
    node1 = BaseStation(c_x,c_y)
#prints grid
for row in grid:
    print(" ".join(row))