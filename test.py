from node import Node
from baseStation import BaseStation
from graph import Graph

G = Graph(100, 100)
G.addBases(1, 40)
print(G.num_base_stations)
for key in G.getBases():
    print (G.getBases()[key].pos)
G.addNodes(10, 15)
print(G.num_nodes)
for key in G.getNodes():
    print (G.getNodes()[key].pos, "key ", key)
G.addNeighbors()