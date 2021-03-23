"""
4
  A B C D
A 0 1 1 0
B 1 0 1 0
C 1 1 0 1
D 0 0 1 0

A -> B
A -> C
B -> A
B -> C
C -> A
C -> B
C -> D
D -> C
"""


class Graph:
    def __init__(self, filePath: str):
        self._vertex_amount, self._graph = self._parseFile(filePath)

    def isBipartite(self, src):
        colorArr = [-1] * self._vertex_amount
        colorArr[src] = 1
        queue = [src]

        while queue:
            u = queue.pop()

            if self._graph[u][u] == 1:
                return False

            for v in range(self._vertex_amount):
                if self._graph[u][v] == 1 and colorArr[v] == -1:
                    colorArr[v] = 1 - colorArr[u]
                    queue.append(v)
                elif self._graph[u][v] == 1 and colorArr[v] == colorArr[u]:
                    return False
        return True

    def _parseFile(self, filePath):
        adjacency_matrix = []
        with open(filePath, "r") as src:
            vertex_amount = int(src.readline())

            for line in src.readlines():
                array = []
                line = line.strip()
                for value in line.replace(' ', ''):
                    array.append(int(value))
                adjacency_matrix.append(array)

        print(adjacency_matrix)
        return vertex_amount, adjacency_matrix


with open("out.txt", "w") as src:
    g = Graph("graph.txt")
    src.write("Y" if g.isBipartite(0) else "N")

