#!/usr/bin/env python3
#-------------node class-------------
class Node:
    def __init__(self, node_name, x, y, r):
        self.id = node_name        
        self.pos = (x, y)
        self.radius = r

        #list of neighbors
        self.adjacent = []
    
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
        

    def addNeighbor(self, neighbor):
        self.adjacent.append(neighbor)

    #returns [list?] of keys of adjacent nodes
    def getConnections(self):
        return self.adjacent.keys()  

    def getId(self):
        return self.id