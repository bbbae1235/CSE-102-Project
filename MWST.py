#!/usr/bin/env python
import sys
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices 
        self.graph = []  # List to store graph edges along with their weights
        self.graphCycle = defaultdict(list)  # To keep track of graph for cycle detection

    def addEdge(self, lineNum, u, v, w):
        """Function to add an edge to the graph."""
        self.graph.append([lineNum, u, v, w])

    def addEdgeCycle(self, u, v):
        """Function to add an edge and update both directions for cycle detection."""
        self.graphCycle[u].append(v)
        self.graphCycle[v].append(u)

    def checkCycle(self):
        """Check all vertices using DFS to detect any cycles in the graph."""
        visited = [False] * (self.V + 1)

        for i in range(self.V):
            if not visited[i]:
                stack = [(i, -1)]
                while stack:
                    (v, parent) = stack.pop()
                    if not visited[v]:
                        visited[v] = True
                        for neighbor in self.graphCycle[v]:
                            if not visited[neighbor]:
                                stack.append((neighbor, v))
                            elif parent != neighbor:
                                return True
        return False

    def kruskalsAlgorithm(self, outputFile):
        """Kruskal's algorithm to find the minimum spanning tree."""
        self.graph.sort(key=lambda x: x[3])
        with open(outputFile, 'w') as writeFile:
            total = 0
            count = 0
            for line_id, u, v, w in self.graph:
                if count < self.V - 1:
                    self.addEdgeCycle(u, v)
                    if not self.checkCycle():
                        count += 1
                        total += w
                        writeFile.write(f'{line_id:4}: ({u}, {v}) {w:.2f}\n')
                    else:
                        # Remove the edge if it creates a cycle
                        self.graphCycle[u].remove(v)
                        self.graphCycle[v].remove(u)
            writeFile.write(f'Total Weight = {total:.2f}\n')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python script.py inputFile outputFile')
    else:
        inputFile, outputFile = sys.argv[1:3]
        with open(inputFile) as f:
            vertices = int(next(f).strip())
            g = Graph(vertices)
            lineNum =0
            for line in f:
                parts = line.split()
                if len(parts) == 3:
                    u, v, w = map(int, parts)
                    g.addEdge(lineNum, u, v, w)
                    lineNum += 1
                else:
                    # print(f"Skipping invalid line {lineNum}: {line.strip()}")
                    lineNum += 1
        g.kruskalsAlgorithm(outputFile)

