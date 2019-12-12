from node import Node
from baseStation import BaseStation
from graph import Graph

G = Graph(2, 2)
G.addBases(3, 20)
print(G.num_base_stations)
for key in G.getBases():
    print (G.getBases()[key].pos)