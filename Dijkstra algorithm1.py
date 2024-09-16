import heapq

class Edge:
	def __init__(self, weight, start_vertex, target_vertex):
		self.weight = weight
		self.start_vertex = start_vertex
		self.target_vertex = target_vertex


class Node:
	def __init__(self, name):
		self.name = name
		self.visited = False
		self.predecessor = None
		self.neighbors = []
		self.min_distance = float('inf')

	def __lt__(self, other_node):
		return self.min_distance < other_node.min_distance

	def add_edge(self,weight, target_vertex):
		edge = Edge(weight, self, target_vertex)
		self.neighbors.append(edge)


class DijkstraAlgorithm:
	def __init__(self):
		self.heap = []

	def calculate(self, origin_vertex):
		origin_vertex.min_distance = 0
		heapq.heappush(self.heap, origin_vertex)
		while self.heap:
			inhand_vertex = heapq.heappop(self.heap)
			if inhand_vertex.visited:
				continue
			for edge in inhand_vertex.neighbors:
				start = edge.start_vertex
				target = edge.target_vertex
				new_distance = start.min_distance + edge.weight
				if new_distance < target.min_distance:
					target.min_distance = new_distance
					target.predecessor = inhand_vertex
					heapq.heappush(self.heap, target)
			inhand_vertex.visited = True

	def find_shortest_path(self, target_vertex):
		print(target_vertex.min_distance)
		origin = target_vertex
		path = ''
		while origin.predecessor is not None:
			path = origin.predecessor.name + ' ' + path
			origin = origin.predecessor
		print(path)




nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeA.add_edge(3, nodeB)
nodeA.add_edge(3, nodeC)

nodeB.add_edge(4, nodeD)
nodeC.add_edge(5, nodeD)

algorithm = DijkstraAlgorithm()
algorithm.calculate(nodeA)
algorithm.find_shortest_path(nodeD)
