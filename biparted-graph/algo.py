class GraphChecker:
    def __init__(self, graph):
        self.flag = True
        self.graph = graph
        self.colored = [0] * graph.size

    def invert(self, c):
        return 2 if c == 1 else 1

    def color_dfs(self, v, color):
        self.colored[v] = color

        for vertex in self.graph.vertices[v]:
            if self.colored[vertex] == 0:
                self.color_dfs(vertex, self.invert(color))
            elif self.colored[vertex] == color:
                self.flag = False
                break

    def print_results(self):
        if self.flag:
            print('Y')
            result = {1: [], 2: []}
            for vertex_colored in range(len(self.colored)):
                result[self.colored[vertex_colored]].append(vertex_colored + 1)

            result[1].sort()
            result[2].sort()

            with open("out.txt", "a") as file:
                result_string = str(result[1]) + "\n0\n" + str(result[2]) if result[1][0] < result[2][0] else str(
                    result[2]) + "\n0\n" + str(result[1])
                file.write("Y\n" + result_string + "\n")
            return

        with open("out.txt", "a") as file:
            print('N')
            file.write("N\n")
