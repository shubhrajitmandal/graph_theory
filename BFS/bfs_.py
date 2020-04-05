from collections import defaultdict

class Graph:
    def __init__(self, n):
        self.nodes = n
        self.adj_list = defaultdict(list)
        self.visited = n*[False]
        self.queue = []

    def addEdge(self, u, v):
        self.adj_list[u].append(v)

    def BFS_(self, s):
        self.queue.append(s)
        self.visited[s-1] = True

        while(self.queue):
            self.queue.reverse()
            at = self.queue.pop()
            self.queue.reverse()

            print(at, end=' ')

            for next in self.adj_list[at]:
                if not self.visited[next-1]:
                    self.queue.append(next)
                    self.visited[next-1] = True



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

    print(g.adj_list)
    g.BFS_(2)

if __name__ == '__main__':
    main()
