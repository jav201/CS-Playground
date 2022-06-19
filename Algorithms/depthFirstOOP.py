# Python3 program to print DFS traversal
# from a given given graph
from collections import defaultdict

# This class represents a directed graph using
# adjacency list representation
class Graph:

	# Constructor
	def __init__(self):
		# default dictionary to store graph
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# A function used by DFS
	def DFSUtil(self, v, visited):

		# Mark the current node as visited
		# and print it
		visited.add(v)
		print(v, end=' ')

		# Recur for all the vertices
		# adjacent to this vertex
		for neighbour in self.graph[v]:
			if neighbour not in visited:
				self.DFSUtil(neighbour, visited)

	# The function to do DFS traversal. It uses
	# recursive DFSUtil()
	def DFS(self, v):
		# Create a set to store visited vertices
		visited = set()
		# Call the recursive helper function
		# to print DFS traversal
		self.DFSUtil(v, visited)

# Driver code


# Create a graph given
# in the above diagram
g = Graph()
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)

r"""GRAPH:
YOU0 - 1Alice - 3Peggy
    \       /
       2Bob   - 4Anuj
  \
   5Claire - 6Thom
        \
         7Jonny
"""
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 5)
g.addEdge(1, 0)
g.addEdge(1, 3)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(3, 1)
g.addEdge(3, 2)
g.addEdge(4, 2)
g.addEdge(5, 6)
g.addEdge(5, 7)
g.addEdge(6, 5)
g.addEdge(7, 5)

print("Following is DFS from (starting from vertex 0)")
g.DFS(0)

# This code is contributed by Neelam Yadav