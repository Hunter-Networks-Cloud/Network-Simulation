from node import Node
from baseStation import BaseStation
from graph import Graph

G = Graph(100, 100)
G.addBases(2, 40)
"""
print(G.num_base_stations)
for key in G.getBases():
    print (G.getBases()[key].pos)
"""
G.addNodes(10, 30)
#print(G.num_nodes)
G.addNeighbors()
"""
for key in G.getNodes():
    neighborsList = []
    for neighbor in G.getNodes()[key].adjacent:
        neighborsList.append(neighbor.id)
    print (G.getNodes()[key].pos, "key ", key, "distance ", G.getNodes()[key].dijkstraDistance, neighborsList)
"""
G.getRoute(0,9)
print("\n")
"""
for key in G.getNodes():
    print (G.getNodes()[key].pos, "key ", key, "distance ", G.getNodes()[key].dijkstraDistance, G.getNodes()[key].previousId)
"""
G.printGraph()
G.scramble(0,9)
print("###########################################################################")
G.printGraph()