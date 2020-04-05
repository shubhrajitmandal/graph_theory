import queue
from collections import defaultdict

class Graph:
    def __init__(self, n):
        self.n = n
        self.g = defaultdict(list)

    def addEdge(self, u, v):
        self.g[u].append(v)

    def shortestPath(self, s, e):
        prev = self.findPath(s)
        return self.reconstructPath(s, e, prev)

    def findPath(self, s):
        q = queue.Queue(self.n)
        visited = self.n*[False]
        prev = self.n * [-1]

        q.put(s)
        visited[s-1] = True

        while not q.empty():
            at = q.get()
            neighbors = self.g[at]

            for next in neighbors:
                if not visited[next-1]:
                    visited[next-1] = True
                    q.put(next)
                    prev[next-1] = at

        return prev

    def reconstructPath(self, s, e, prev):
        # print("prev :", prev)
        path = []
        at = e;
        while prev[at-1] != -1:
            path.append(prev[at-1])
            at = prev[at-1]

        # print(path)
        path.reverse()

        if path[0] == s:
            path.append(e)
            return path
        return -1


def main():
    # n = int(input())
    # start, end = map(int, input().split())
    g = Graph(5)

    g.addEdge(1, 2)
    g.addEdge(1, 4)
    g.addEdge(1, 5)
    g.addEdge(2, 1)
    g.addEdge(2, 5)
    g.addEdge(3, 4)
    g.addEdge(4, 3)
    g.addEdge(4, 5)
    g.addEdge(4, 1)
    g.addEdge(5, 1)
    g.addEdge(5, 2)
    g.addEdge(5, 4)

    s_path = g.shortestPath(2, 3)
    print(s_path)


if __name__ == '__main__':
    main()
