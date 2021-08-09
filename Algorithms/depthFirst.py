r"""GRAPH:
YOU - Alice - Peggy
    \       /
       Bob   - Anuj
  \
   Claire - Thom
        \
         Jonny
"""
# First, declare the nodes on a hash table
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['jonny', 'thom']
graph['anuj'] = []
graph['peggy'] = [] # she will be the chosen one
graph['thom'] = []
graph['jonny'] = []

def depthFirst(nameStart, nameSearched):
    # Base case
    if nameStart == nameSearched:
        print(nameSearched+' found!')
        return True
    for name in graph[nameStart]:
        print(name)
        if depthFirst(name, nameSearched):
            return True
    return False
print(depthFirst('you', 'anuj') is True)