class Graph:
	def __init__(self,dgraph=None):
		if not dgraph:
			dgraph = {}
		self.dgraph = dgraph

	def addVertex(self, vertex, edge):
		if not vertex in self.dgraph.keys():
			self.dgraph[vertex]=[edge]

		else:
			self.dgraph[vertex].append(edge)

	def printGraph(self):
		for vertex in self.dgraph.keys():
			print(vertex , ' : ',self.dgraph[vertex])

	def addEdge(self, vertex1, vertex2):
		if not vertex1 and vertex2 in self.dgraph.keys():
			return False
		self.dgraph[vertex1].append(vertex2)
		self.dgraph[vertex2].append(vertex1)
		return True
	def removeEdge(self, vertex1, vertex2):
		try:
			self.dgraph[vertex1].remove(vertex2)
			self.dgraph[vertex2].remove(vertex1)
		except ValueError:
			print('valueError occured')


if __name__ == '__main__':
	graphDict = {
		'A':['B'],
		'B':['A'],
		'C':['A','B']
		}
	AlphaGraph = Graph(graphDict)
	AlphaGraph.printGraph()
	AlphaGraph.removeEdge('A','C')

