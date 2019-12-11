#!/usr/bin/env python3
import random as rand
from node import Node
from baseStation import BaseStation

class Graph: 
    
    def __init__(self, cols = 100, rows = 100):
        self.cols = cols
        self.rows = rows

        #dicts to store base stations, nodes, edges, and channels. keys should be their id.
        self.base_stations = {}
        self.nodes = {}
        self.edges = {}

        #single channel for now, of weight 0.5
        self.channels = {
            0 : 0.5
        }

        self.num_nodes = 0
        self.num_base_stations = 0
        self.num_edges = 0
    
    def addBases(self, num, radius):
        for i in range(num):
            #generating coords between 1 and 100 inclusive
            x = rand.randint(1,100)
            y = rand.randint(1,100)
            new_pos = (x, y)

            #resolving collisions in base stations and nodes
            resolveGraphCollisions(self, new_pos)
            
            #once satisfied, add to graph
            self.base_stations[self.num_base_stations] = BaseStation(self.num_base_stations, new_pos, radius)

        #update graph attribute for number of base stations
        self.num_base_stations += num

    def addNodes(self, num):
        return None

    def addEdges(self, num):
        return None

#helper function that checks whether some object the container already has the same pos
def positionOccupied (pos, container):
    for key in container:
        if (container[key].pos == pos):
            return True
    return False

def resolveGraphCollisions(graph, pos):
    while positionOccupied(pos, graph.base_stations) and positionOccupied(pos, graph.nodes):
        x = rand.randint(1,100)
        y = rand.randint(1,100)
        pos = (x, y)