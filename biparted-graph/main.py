from graph import ReadGraphsFromFile as Reader
from algo import GraphChecker

if __name__ == '__main__':
    reader = Reader("input.txt")

    graph_list = reader.reading()

    for graph in graph_list:
        checker = GraphChecker(graph)
        checker.color_dfs(1, 1)
        checker.print_results()