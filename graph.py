#!/usr/bin/env python3
import random as rand
import math
from node import Node
from baseStation import BaseStation

class Graph: 
    
    def __init__(self, cols = 100, rows = 100):
        self.cols = cols
        self.rows = rows

        #dicts to store base stations, nodes, edges, and channels
        #keys should be their id, usually from 0-n
        self.base_stations = {}
        self.nodes = {}
        self.edges = {}

        #single channel for now, of weight 0.5
        self.channels = {
            0 : 0.5
        }

        #housekeeping variables, might come in handy later
        self.num_nodes = 0
        self.num_base_stations = 0
        self.num_edges = 0
    
    def addBases(self, num, radius):
        for i in range(num):
            #generating coords between 1 and cols/rows inclusive
            x = rand.randint(1, self.cols)
            y = rand.randint(1, self.rows)
            new_pos = (x, y)

            #resolving collisions in base stations and nodes
            new_pos = resolveGraphCollisions(self, new_pos, self.cols, self.rows)
            
            #once satisfied, add to graph
            self.base_stations[self.num_base_stations] = BaseStation(self.num_base_stations, new_pos, radius)

            #update graph attribute for number of base stations
            self.num_base_stations += 1

    def addNodes(self, num, radius):
        for i in range(num):
            #generating coords between 1 and cols/rows inclusive
            x = rand.randint(1, self.cols)
            y = rand.randint(1, self.rows)
            new_pos = (x, y)
            
            #resolving collisions and within-range-ness
            new_pos = resolveWithinRange(self, new_pos, self.cols, self.rows)

            #once satisfied, add to graph
            self.nodes[self.num_nodes] = Node(self.num_nodes, new_pos, radius)
        
            #update graph attribute for number of nodes
            self.num_nodes += 1

    def addEdges(self, num):
        return None

    #fill out "adjacent" member in graph nodes
    def addNeighbors(self):
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                #print("doing something with ", i, "th node, comparing to ", j, "th node")
                #print(self.nodes[i].pos, self.nodes[j].pos)
                distance = calculateDistance(self.nodes[i].pos, self.nodes[j].pos)
                #print("distance found is ", distance)
                if distance < self.nodes[i].radius:
                    #print ("adding node ", j, "to node ", i)
                    self.nodes[i].addNeighbor(self.nodes[j])

    def getBases(self):
        return self.base_stations

    def getNodes(self):
        return self.nodes

    def getEdges(self):
        return self.edges

    def getRoute(self, source, destination):
        return None

#helper function that checks whether some pos is already occupied by something in the container
def positionOccupied (pos, container):
    for key in container:
        if (container[key].pos == pos):
            return True
    return False

#helper function that returns new pos that's definitely empty
def resolveGraphCollisions(graph, pos, cols, rows):
    while positionOccupied(pos, graph.base_stations) or positionOccupied(pos, graph.nodes):
        x = rand.randint(1, cols)
        y = rand.randint(1, rows)
        pos = (x, y)
    return pos

#helper function that returns new pos that's definitely empty, and within a base station's radius
def resolveWithinRange(graph, pos, cols, rows):

    #assume that it's not within range
    within = False

    while (within == False):

        #check for collision, if yes then make a new one if no then go on to check being within range
        while positionOccupied(pos, graph.base_stations) or positionOccupied(pos, graph.nodes):
            x = rand.randint(1, cols)
            y = rand.randint(1, rows)
            pos = (x, y)

        #check for being within range
        for key in graph.base_stations:
            base_station_pos = graph.base_stations[key].pos
            base_station_radius = graph.base_stations[key].radius

            #if it is within range, get out of the loop
            if (calculateDistance(pos, base_station_pos) <= graph.base_stations[key].radius):
                within = True

            #otherwise try again with new coordinate pair
            else:
                x = rand.randint(1, cols)
                y = rand.randint(1, rows)
                pos = (x, y)

    return pos

#helper function calculates the distance between two 2-tuples
def calculateDistance(pos1, pos2):  
     dist = math.sqrt((pos2[0] - pos1[0])**2 + (pos2[1] - pos1[1])**2)  
     return dist
    