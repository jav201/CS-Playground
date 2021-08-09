# Breadth First
# Declare Nodes ####

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

def findCheapestPath(node):
    keys = list(graph[node])
    minCost = infinity
    outNode = None
    for _ in keys:
        if minCost > graph[node].get(_):
            minCost = graph[node].get(_)
            outNode = _
    return outNode

# Recursion
def findSolution(node, pathOut=[]):
    # Find cheapest path
    pathOut.append(node)
    cheapestNode = findCheapestPath(node)
    if graph.get(cheapestNode) is not None:
        return findSolution(cheapestNode, pathOut)
    return pathOut

print(findSolution('a'))