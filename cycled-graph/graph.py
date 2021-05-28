class ReadGraphsFromFile:
    def __init__(self, file_name):
        self.file_name = file_name

    def reading(self):
        graph_list = []
        with open(self.file_name, 'r') as f:
            while True:
                n = f.readline().replace('\\n', '')
                if not n:
                    break
                if len(n.split(" ")) > 1:
                    print("first string should consist one number")
                    quit()
                n = int(n)

                i = 0
                adj_list = []
                while i < n:
                    line = f.readline().replace('\\n', '').split()
                    adj_list.append(line)
                    i += 1

                graph_list.append(Graph(n, adj_list))

        return graph_list


class Graph:
    def __init__(self, n, adj_list):
        self.size = n
        self.vertices = {}
        for i in range(n):
            self.vertices[i] = []
        for j in range(n):
            for v in adj_list[j]:
                if v != '0':
                    self.vertices[j].append(int(v) - 1)