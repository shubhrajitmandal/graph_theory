def DFS(at, visited, adj_list):
    if visited[at-1]: return
    print(at)
    visited[at-1] = True

    neighbors = adj_list[at]
    for next in neighbors:
        DFS(next, visited, adj_list)


def main():
    n, e = map(int, input().split())
    adj_list = {}
    visited = n*[False]
    for _ in range(e):
        u, v = map(int, input().split())
        if u not in adj_list:
            adj_list[u] = []
        if v not in adj_list:
            adj_list[v] = []
        adj_list[u].append(v)
        adj_list[v].append(u)
    print(adj_list, '\n')
    DFS(1, visited, adj_list)

if __name__ == '__main__':
    main()
