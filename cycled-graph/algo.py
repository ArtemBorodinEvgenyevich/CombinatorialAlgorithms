import collections


class GraphChecker:
    def __init__(self, graph):
        self.graph = graph
        self.parent = [[]] * self.graph.size
        self.first_cycle = []

    def isCyclicConnected(self, s, visited: list):
        adj = self.graph.vertices
        queue = collections.deque()
        visited[s] = True
        queue.append(s)

        while queue:
            val = queue.popleft()

            for vertex in adj[val]:
                if not visited[vertex]:
                    visited[vertex] = True
                    queue.append(vertex)
                    self.parent[vertex] = [val] + self.parent[val]
                elif self.parent[val][0] is not vertex:
                    flag = False
                    for i in range(len(self.parent[vertex])):
                        for j in range(len(self.parent[val])):
                            if self.parent[vertex][i] == self.parent[val][j]:
                                if flag:
                                    continue
                                flag = True
                                curV = self.parent[vertex].index(self.parent[vertex][i]) + 1
                                curU = self.parent[val].index(self.parent[vertex][i]) + 1
                                cycle = self.parent[vertex][:curV] + self.parent[val][:curU] + [val, vertex]
                                self.first_cycle = list(map(lambda x: x + 1, cycle))
                    return True
        return False

    def isDisconnected(self):
        n = self.graph.size
        visited = [False] * n

        for i in range(n):
            if not visited[i] and self.isCyclicConnected(i, visited):
                return False
        return True

    def print_results(self):
        if self.isDisconnected():
            with open("out.txt", "a") as file:
                file.write("A\n")
            return

        with open("out.txt", "a") as file:
            file.write("N\n" + str(set(self.first_cycle)) + "\n")