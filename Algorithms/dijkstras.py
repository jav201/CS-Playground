# With the graph from the book grokking - Algorithms by Aditya Bhargava PAge 132
# Greedy algorithm; based on local minimum

# Declare Nodes ####
graph = {}
# Node start
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

# Node a
graph['a'] = {}
graph['a']['fin'] = 1

# Node b
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

# Node fin
graph['fin'] = {}

# Declare costs, as seen from the start ####
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# Declare the parents ####
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

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

print(processed)
print(parents)
print(graph)
