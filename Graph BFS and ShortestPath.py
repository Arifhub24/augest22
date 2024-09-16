import queue
from collections import deque
from collections import defaultdict

class Graph:
    def __init__(self,numberOfVertices):
        self.graphDict = defaultdict(list)
        self.numberOfVertices = numberOfVertices
    
    def add_vertex1(self, vertex1, vertex2):
        if not vertex1 in self.graphDict.keys():
            self.graphDict[vertex1] = [vertex2]
        else:
            if not vertex2 in self.graphDict[vertex1]:
                self.graphDict[vertex1].append(vertex2)

        if not vertex2 in self.graphDict.keys():
            self.graphDict[vertex2] = [vertex1]
        else:
            if not vertex1 in self.graphDict[vertex2]:
                self.graphDict[vertex2].append(vertex1)


    def add_vertex2(self, vertex1, vertex2):
        self.graphDict[vertex1].append(vertex2)
        self.graphDict[vertex2].append(vertex1)

    def DFS(self, startVertex):
        visited = set()
        visited.add(startVertex)
        stack = queue.LifoQueue()
        stack.put(startVertex)

        while not stack.empty():
            current_vertex = stack.get()
            print(current_vertex, ' has been visited')
            for adjacent in self.graphDict[current_vertex]:
                if adjacent not in visited:
                    visited.add(adjacent)
                    stack.put(adjacent)


    def BFS(self, startVertex):
        visited = set()
        visited.add(startVertex)
        stack = queue.Queue()
        stack.put(startVertex)

        while not stack.empty():
            current_vertex = stack.get()
            print(current_vertex, ' has been visited')
            for adjacent in self.graphDict[current_vertex]:
                if adjacent not in visited:
                    visited.add(adjacent)
                    stack.put(adjacent)

    def shortest_path(self, start, end):
        que = queue.Queue()
        que.put(start)
        while not que.empty():
            path = que.get()
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.graphDict[node]:
                newpath = list(path)
                newpath.append(adjacent)
                que.put(newpath)


                




my_gr = Graph(8)
my_gr.add_vertex1('a','d')
my_gr.add_vertex1('a','f')
my_gr.add_vertex1('b','e')
my_gr.add_vertex1('b','c')
my_gr.add_vertex1('c','d')
my_gr.add_vertex1('c','b')
my_gr.add_vertex1('d','a')
my_gr.add_vertex1('d','c')
my_gr.add_vertex1('d','f')
my_gr.add_vertex1('e','b')
my_gr.add_vertex1('f','a')
my_gr.add_vertex1('f','d')
print(my_gr.graphDict)
print("________________________________ DFS ____________________________________")
my_gr.DFS('a')
print('________________________________ BFS ______________________________________')
my_gr.BFS('a')
print('_______________________________ SSSP ________________________________')
