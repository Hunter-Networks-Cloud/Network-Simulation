#!/usr/bin/env python3
#-------------node class-------------
class Node:
    def __init__(self,x,y,node_name):
        self.x = x
        self.y = y
        self.id = node_name
        self.adjacent = {}
      
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
        

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  
    def get_id(self):
        return self.id

    