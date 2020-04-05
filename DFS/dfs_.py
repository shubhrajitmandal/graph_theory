from collections import defaultdict

class Graph:
    def __init__(self, n):
        self.nodes = n
        self.adj_list = defaultdict(list)
        self.visited = n * [False]

    def addEdge(self, u, v):
        self.adj_list[u].append(v)

    def DFS_(self, at):
        if self.visited[at-1]: return
        self.visited[at-1] = True
        print(at, end=' ')

        neighbors = self.adj_list[at]
        for next in neighbors:
            self.DFS_(next)


def main():
    g = Graph(6)
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 4)
    g.addEdge(2, 5)
    g.addEdge(3, 5)
    g.addEdge(3, 1)
    g.addEdge(4, 5)
    g.addEdge(4, 6)
    g.addEdge(5, 6)
    g.addEdge(5, 3)
    g.addEdge(6, 4)
    g.addEdge(6, 5)
    # print(g.adj_list)

    g.DFS_(1)

if __name__ == '__main__':
    main()
