#!/usr/bin/env python3

import numpy as nm
#-------------node class-------------
class Node:
    def __init__(self,x,y,node_name):
        self.x = x
        self.y = y
        self.id = node_name
        #list of neighbors
        self.adjacent = []
        #dictionary of channels; key=channel number(0-9), value=channel quality
        self.channels = {}
        for i in range(10):
            #primary arrival is distributed exponentially, so inverse of that is channel quality
            self.channels[i] = 1/nm.random.exponential(1, None)
      
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
        

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent.append(neighbor)

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id