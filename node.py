#!/usr/bin/env python3
#-------------node class-------------
class Node:
    def __init__(self, node_name, pos:tuple, r):
        self.id = node_name        
        self.pos = pos
        self.radius = r
        self.dijkstraDistance = 100000

        #list of neighbors
        self.adjacent = []
    
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
        

    def addNeighbor(self, neighbor):
        self.adjacent.append(neighbor)

    #returns a list of keys of adjacent nodes
    def getConnections(self):
        return self.adjacent.keys()

    def getId(self):
        return self.id