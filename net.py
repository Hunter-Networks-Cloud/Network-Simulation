import networkx as nx
import matplotlib.pyplot as plt
from random import randint
import numpy as np
from itertools import product
import math  

#MultiDiGraph() allows multiple edges per node
G=nx.MultiDiGraph()

number_of_nodes = input('number of nodes in network: ')
number_of_base_stations = input('number of base stations in network: ')


#function calculates the distance between two nodes
def calculateDistance(x1,y1,x2,y2):  
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist  
 
# creates base station at random positions
#attributes for each node are type of node, position and radius
#nodes can be retrieved using the first parameter of the add_node function
for i in range(int(number_of_base_stations)): 
    c_x = randint(0, 100)
    c_y = randint(0, 100)
    
    G.add_node("B"+ str(i+1),type = 'B', pos=(c_x,c_y), radius = 45, coorX = c_x, coorY = c_y)
   
# creates nodes at random positions
#node attributes are node name, type of node, position and radius 
for j in range(int(number_of_nodes)): 
    c_x = randint(0, 100)
    c_y = randint(0, 100)
    G.add_node("N"+ str(j+1),type = "N", pos=(c_x,c_y), radius = 15, coorX = c_x, coorY = c_y)
    # G.add_edge("B"+ str(i+1),"N"+ str(i+1) , weight=0, type = "B_to_N")
    #       
    
    # success = False
    # l =  1
    # #loops until it finds a coordinate within a base radius
    # while ( success == False):
    #     c_x = randint(0, 100)
    #     c_y = randint(0, 100) 
    #     for i in range(int(number_of_base_stations)):
    #     #coordinates of base station
    #         coordX = nx.get_node_attributes(G, 'coorX') 
    #         coordY = nx.get_node_attributes(G, 'coorY')
    #     #checks if distance between node and base station is within a base station
    #         if calculateDistance(coordX["B"+str(i+1)], coordY["B"+str(i+1)],c_x,c_y) <= 45:
    #             G.add_node("N"+ str(j),type = 'N', pos=(c_x,c_y), radius = 15, coorX = c_x, coorY = c_y )
    #             G.add_edge("B"+ str(i+1),"N"+ str(j) , type = 'B_to_N')
    #             success = True            
    # l =l +1   
    
################################################
#loop links bases with nodes that are in its radius
for i in range(int(number_of_base_stations)): 
    coordX = nx.get_node_attributes(G, 'coorX') #allows us to get the attribute coorX for nodes in the graph
    coordY= nx.get_node_attributes(G, 'coorY')  #allows us to get the attribute coory for nodes in the graph
    for j in range(int(number_of_nodes)):
        if calculateDistance(coordX["B"+str(i+1)], coordY["B"+str(i+1)],coordX["N"+str(j+1)], coordY["N"+str(j+1)]) <= 45:
            G.add_edge("N"+ str(j+1), "B"+ str(i+1) , type = 'B_to_N')
            break
#loop links nodes with nodes that are in its radius
for i in range(int(number_of_nodes)): 
    coordX = nx.get_node_attributes(G, 'coorX') 
    coordY= nx.get_node_attributes(G, 'coorY')
    for j in range(int(number_of_nodes)):
        if i != j: #to prevent a node from adding and edge from and to itself
            if calculateDistance(coordX["N"+str(i+1)], coordY["N"+str(i+1)],coordX["N"+str(j+1)], coordY["N"+str(j+1)]) <= 25:
                G.add_edge("N"+ str(i+1),"N"+ str(j+1) , type = 'N_to_N')            

print(G.edges())  #just for testing, it prints all the edges 



# this section is for the node colors and graph attributes
color_map = []
for node in G:
    type_of_node  = nx.get_node_attributes(G, 'type')
    if type_of_node[node] == 'B':
        color_map.append('blue')
    else:
        color_map.append('green')


####################################

pos=nx.get_node_attributes(G,'pos')
nx.draw(G,pos,node_color = color_map, with_labels = True, node_size = 40)
plt.show()