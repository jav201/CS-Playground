# With the graph from the book grokking - Algorithms by Aditya Bhargava PAge 132

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

# Declare the parents ####
parents = {}
parents['b'] = 'a'
parents['c'] = 'a'
parents['f'] = None

# Keep track of processed nodes
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): # This extract the connected nodes to node and their costs
        new_cost = cost + neighbors[n] 
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)


print(parents)
print(costs)
last_one = 'f'
print(last_one, end=', ')
try:
    while parents[last_one]:
        print(parents[last_one], end=', ')
        last_one = parents[last_one]
except:
    pass