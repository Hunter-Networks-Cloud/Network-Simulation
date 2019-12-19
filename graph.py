#!/usr/bin/env python3
import random as rand
import math
import copy
import queue
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
    
    def addBases(self, num, radius=40):
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

    def addNodes(self, num, radius=25):
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
            #remove self from adjacency list
            self.nodes[i].adjacent.remove(self.nodes[i])

    def getBases(self):
        return self.base_stations

    def getNodes(self):
        return self.nodes

    def getEdges(self):
        return self.edges

    #Dijkstra's algorithm implementation
    def getRoute(self, s, d):
        source = copy.deepcopy(int(s))
        destination = copy.deepcopy(int(d))
        visited_set = set()
        unvisited_set = set()
        #marking nodes unvisited
        for i in range(self.num_nodes):
            unvisited_set.add(self.nodes[i])

        #initializing distance value for source node
        self.nodes[source].dijkstraDistance = 0

        #setting distances and path for neighbors of source node
        for j in self.nodes[source].adjacent:
            #print("setting neighbor to node: ", self.nodes[source].id, "neighbor: ", j.id)
            j.dijkstraDistance = self.channels[0]
            j.previousId = self.nodes[source].id

        #marking source node visited
        unvisited_set.remove(self.nodes[source])
        visited_set.add(self.nodes[source])

        #finding unvisited node with smallest tentative distance that is not "infinity"
        smallestDistance = 10000
        smallestKey = int()
        for k in unvisited_set:
            if k.dijkstraDistance < smallestDistance:
                smallestDistance = k.dijkstraDistance
                smallestKey = k.id
        #print ("smallest distance is: ", smallestDistance, "id of this node: ", smallestKey)

        #enter loop if destination not visited, or smallest distance is not infinity
        while self.nodes[destination] not in visited_set and smallestDistance < 10000:
            newDistance = self.nodes[smallestKey].dijkstraDistance + self.channels[0]

            for l in self.nodes[smallestKey].adjacent:
                if  newDistance < l.dijkstraDistance:
                    #print("setting neighbor to node: ", smallestKey, "neighbor: ", l.id)
                    l.dijkstraDistance = newDistance
                    l.previousId = smallestKey

            unvisited_set.remove(self.nodes[smallestKey])
            visited_set.add(self.nodes[smallestKey])

            #finding smallest distance again
            smallestDistance = 10000
            for m in unvisited_set:
                if m.dijkstraDistance < smallestDistance:
                    smallestDistance = m.dijkstraDistance
                    smallestKey = m.id

        if self.nodes[destination] in visited_set:
            print("Path found.")
            currentHop = self.nodes[destination].previousId
            currentNode = self.nodes[destination]
            pathQueue = queue.LifoQueue()
            while currentNode != self.nodes[source]:
                pathQueue.put(currentNode)
                currentNode = self.nodes[currentNode.previousId]
            pathQueue.put(self.nodes[source])
            while not pathQueue.empty():
                print (pathQueue.get().id, end=" ")
            print("\n")

        else:
            print("Path not found.")

    def printGraph(self):
        graphArray = [["-" for i in range(self.cols)] for j in range(self.rows)]
        for base in self.base_stations:
            baseX = self.base_stations[base].pos[0] - 1
            baseY = self.base_stations[base].pos[1] - 1
            graphArray[baseX][baseY] = "B"
        for node in self.nodes:
            nodeX = self.nodes[node].pos[0] - 1
            nodeY = self.nodes[node].pos[1] - 1
            graphArray[nodeX][nodeY] = self.nodes[node].id
        for y in range(len(graphArray)):
            for x in range(len(graphArray[0])):
                print (graphArray[x][y], end = '')
            print("\n", end='')

#helper function printing terminal ASCII representation of graph



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
    