# https://networkx.org/documentation/stable/_modules/networkx/algorithms/euler.html#is_eulerian
# https://networkx.org/documentation/stable/_modules/networkx/algorithms/components/connected.html#is_connected

from collections import deque

class Graph:

    def __init__(self, nodes):
        self.adjacencyList = {}
        self.queue = deque()
        self.unvisited = set()

    def addEdge(self, node, neighbor):
        if node not in self.adjacencyList:
            self.adjacencyList[node] = [neighbor]
            self.unvisited.add(node)
        else:
            self.adjacencyList[node].append(neighbor)
        
        if neighbor not in self.adjacencyList:
            self.adjacencyList[neighbor] = [node]
            self.unvisited.add(neighbor)
        else:
            self.adjacencyList[neighbor].append(node)

    def breadthFirstSearch(self):
            root = next(iter(self.adjacencyList.values()))[0]

            self.unvisited.remove(root)
            self.queue.append(root)

            while self.queue:
                node = self.queue.popleft()

                for edge in self.adjacencyList[node]:
                    if edge in self.unvisited:
                        self.queue.append(edge)
                        self.unvisited.remove(edge)
    
    def hasNoVerticiesOfOddDegree(self):
        return all(len(self.adjacencyList[node]) % 2 == 0 for node in self.adjacencyList)

    def isEulerianCycle(self):
        
        self.breadthFirstSearch()

        # Check if connected and if graph has no verticies of odd degree
        if not self.unvisited and self.hasNoVerticiesOfOddDegree():
            return 'Possible'
        else:
            return 'Not Possible'

# n: total cities (nodes), r: total paths (relationships between cities)    
n, r = [int(x) for x in input().split()]

# Instantiate our Graph class with n = nodes
graph = Graph(n)

for _ in range(r):
    node, neighbor = input().split(' -> ')

    graph.addEdge(node, neighbor)

print(graph.isEulerianCycle())
