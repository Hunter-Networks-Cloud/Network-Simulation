#!/usr/bin/env python3
from random import randint
import numpy as np
from itertools import product
from node import Node
from baseStation import BaseStation

class Graph: 
   
    def __init__(self, cols = 20, rows = 20):
        self.cols = cols
        self.rows = rows
        # initialize matrix and fill with zeroes
        self.matrix = []
        self.vert_dict = {}
        self.num_nodes= 0
        self.num_base_stations =0
        
        for i in range(self.rows):
            self.matrix.append([])
            for j in range(self.cols):
                self.matrix[i].append(".")
       

    def generateRandNodePos(self, num):
        for n_id in range(num): 
            # c_x = randint(0, len(grid)-1)
            c_x = randint(0, len(self.matrix)-1)
            # c_y = randint(0, len(grid[0])-1)
            c_y = randint(0, len(self.matrix[0])-1)
            Node(c_x,c_y,n_id + 1)
            self.matrix[c_x][c_y] = "N"+ str(n_id+1)
    
    def generateRandBasePos(self, num):
        for b_id in range(num): 
            # c_x = randint(0, len(grid)-1)
            c_x = randint(0, len(self.matrix)-1)
            # c_y = randint(0, len(grid[0])-1)
            c_y = randint(0, len(self.matrix[0])-1)
            BaseStation(c_x,c_y,b_id + 1)
            self.matrix[c_x][c_y] = "B"+str(b_id+1)
 
    
    # def getNode(self, node_id):
    #     for i in range(self.rows):
    #         for j in range(self.cols):
    #             self.matrix[i].append(".")

    # def getBaseStation(self, base_id):
    #     return self.matrix[col-1][row-1]

    def display(self):
        for self.rows in self.matrix:
            print(" ".join(self.rows))


# for testing purposes

if __name__ == '__main__':

    g = Graph(20,20)
    number_of_nodes = input('number of nodes in network: ')
    number_of_base_stations = input('number of base stations in network: ')
    g.generateRandNodePos(int(number_of_nodes))
    g.generateRandBasePos(int(number_of_base_stations))
    g.display()
