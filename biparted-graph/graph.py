class Graph:
    def __init__(self, n, adj_matrix):
        self.size = n
        self.vertices = {}
        for i in range(n):
            self.vertices[i] = []
        for j in range(n):
            for k in range(n):
                if adj_matrix[j][k] == '1' and k != j:
                    self.vertices[j].append(k)

    def __str__(self):
        return str(self.vertices)


class ReadGraphsFromFile:
    def __init__(self, file):
        self.file_name = file

    def reading(self):
        graph_list = []
        with open(self.file_name, 'r') as file:
            while True:
                n = file.readline().replace('\\n', '')
                if not n:
                    break
                if len(n.split(" ")) > 1:
                    print("first string should consist one number")
                    quit()
                n = int(n)

                i = 0
                adj_matrix = []
                while i < n:
                    line = file.readline()
                    adj_matrix.append(line.replace('\\n', '').split())
                    i += 1

                graph_list.append(Graph(n, adj_matrix))

        return graph_list
