# Declare Nodes ####
from collections import deque

graph = {}
# Node a
graph['a'] = {}
graph['a']['b'] = 2
graph['a']['c'] = 4

# Node b
graph['b'] = {}
graph['b']['c'] = 1
graph['b']['d'] = 4
graph['b']['e'] = 2

# Node c
graph['c'] = {}
graph['c']['e'] = 3

# Node d
graph['d'] = {}
graph['d']['f'] = 2

# Node e
graph['e'] = {}
graph['e']['d'] = 3
graph['e']['f'] = 2

# Node f
graph['f'] = {}

# Declare costs, as seen from the start ####
infinity = float('inf')

costs = {}
costs['b'] = 2
costs['c'] = 4
costs['d'] = infinity
costs['e'] = infinity
costs['f'] = infinity

parents = {}
parents['b'] = 'a'
parents['c'] = 'a'

processed = []

def findCheapestNode(costs):
    minCost = infinity
    minNode = None
    for n in costs:
        nodeCost = costs[n]
        if nodeCost < minCost and n not in processed:
            minCost = nodeCost
            minNode = n
    return minNode


node = findCheapestNode(costs)
while node is not None:
    # Get actual cost and vertices
    cost = costs[node]
    vertices = graph[node]
    for n in vertices:
        # The new cost is the default cost + the vertex we are iterating
        newCost = cost + vertices[n]
        # if default cost is greater than new cost
        # we have encountered a cheaper path
        if costs[n] > newCost:
            costs[n] = newCost
            parents[n] = node
    processed.append(node)
    node = findCheapestNode(costs)

print(parents)
    
        
    


            
        
