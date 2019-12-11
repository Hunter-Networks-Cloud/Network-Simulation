#!/usr/bin/env python3
from random import randint
from node import Node
from baseStation import BaseStation

class Graph: 
    
    def __init__(self, cols = 100, rows = 100):
        self.cols = cols
        self.rows = rows

        #dicts to store base stations, nodes, and edges. keys should be their id.
        self.base_stations = {}
        self.nodes = {}
        self.edges = {}

        self.num_nodes = 0
        self.num_base_stations = 0
        self.num_edges = 0
    
    def add_node(self, node):
        return None

    def add_base(self, base):
        return None

    def add_edge(self, base):
        return None
