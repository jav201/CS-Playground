from collections import defaultdict
from logging import getLevelName

from sympy import nextprime

INF = float('inf')

class Graph:

    def __init__(self):
        self.nodes = defaultdict(dict)
        self.costs = None
        self.visited = set()

    def insert(self, origin, distance, destination):
        self.nodes[origin][destination] = distance 

    def __repr__(self):
        return str(self.nodes.items())
    
    def get(self, node):
        return self.nodes.get(node)
    
    def getLowerCostNode(self, node):
        minCostNode = None
        minCost = INF
        for node in self.nodes:
            cost = self.nodes.get(node)
            if cost < minCost:
                minCostNode = node
                minCostNode = cost
        return minCostNode, minCost

    def solve(self, source, destination):
        # Calculate the cost from source
        for node in self.nodes:
            if node == source:
                self.costs = self.get(node)
            elif node not in self.costs.keys():
                self.costs[node] = INF
        # Update visited
        self.visited.add(source)
        # Find the lowest cost from current position
        nextNode, minCost = self.getLowerCostNode(source)
        print(nextNode, minCost)
            
# this still needs more thought... and the parents dictionary


                

# Declare graph
g = Graph()
g.insert('a',2,'b')
g.insert('a',4,'c')
g.insert('b',1,'c')
g.insert('b',4,'d')
g.insert('b',2,'e')
g.insert('c',3,'e')
g.insert('d',2,'f')
g.insert('e',3,'d')
g.insert('e',2,'f')

g.solve('a','f')