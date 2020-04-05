from queue import PriorityQueue
from collections import defaultdict

class Graph:
    def __init__(self, n):
        self.V = n
        self.adjList = defaultdict(list)

    def addEdge(self, u, v, w):
        self.adjList[u].append((v, w))

    # def __repr__(self):
    #     graph = [(x, self.adjList[x]) for x in self.adjList.keys()]
    #     return str(graph)


def shortestPath(g, start):
    dist, prev = findPath(g, start)
    print(prev)
    paths = reconstructPath(g, start, prev)
    return dist, paths


def findPath(g, start):
    dist = g.V * [float('inf')]
    prev = g.V * [-1]
    pq = PriorityQueue(g.V)

    dist[start] = 0
    pq.put((0, start))

    while not pq.empty():
         wts, at = pq.get()

         neighbors = g.adjList[at]
         # print(at, neighbors)
         for next in neighbors:
             to, wt = next
             if dist[to] > dist[at] + wt:
                 dist[to] = dist[at] + wt
                 pq.put((wt, to))
                 prev[to] = at
    return dist, prev


def reconstructPath(g, start, prev):
    pathList = []
    for x in g.adjList.keys():
        path = []
        at = x
        if at == start:
            path.append(x)
        while prev[at] != -1:
            path.append(at)
            at = prev[at]

        if x != start:
            path.append(at)
        path.reverse()

        if path[0] == start:
            pathList.append(path)
        else:
            pathList.append([])
    return pathList


def main():
    g = Graph(9);
    g.addEdge(0, 1, 4)
    g.addEdge(0, 7, 8)
    g.addEdge(1, 0, 4)
    g.addEdge(1, 2, 8)
    g.addEdge(1, 7, 11)
    g.addEdge(2, 1, 8)
    g.addEdge(2, 3, 7)
    g.addEdge(2, 8, 2)
    g.addEdge(2, 5, 4)
    g.addEdge(3, 2, 7)
    g.addEdge(3, 4, 9)
    g.addEdge(3, 5, 14)
    g.addEdge(4, 3, 9)
    g.addEdge(4, 5, 10)
    g.addEdge(5, 2, 4)
    g.addEdge(5, 3, 14)
    g.addEdge(5, 4, 10)
    g.addEdge(5, 6, 2)
    g.addEdge(6, 5, 2)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 6)
    g.addEdge(7, 0, 8)
    g.addEdge(7, 1, 11)
    g.addEdge(7, 6, 1)
    g.addEdge(7, 8, 7)
    g.addEdge(8, 2, 2)
    g.addEdge(8, 6, 6)
    g.addEdge(8, 7, 7)

    for k in  g.adjList.keys():
        print(k, " -->> ", g.adjList[k])

    dist, paths = shortestPath(g, 0);
    print(dist)
    print(paths)
    


if __name__ == '__main__':
    main()
