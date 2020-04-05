#include <iostream>
#include <list>
using namespace std;

class Graph {
public:
    int V;
    list<int> *adj_list;

    Graph(int n);
    void addEdge(int u, int v);
};

Graph :: Graph(int n) {
    this->V = n;
    adj_list = new list<int>[V];
}

void Graph :: addEdge(int u, int v) {
    adj_list[u].push_back(v);
}

int dfs(int i, int at, int ordering[], bool visited[],Graph graph) {
    visited[at] = true;

    for(auto it: graph.adj_list[at]) {
        if (visited[at] == false) {
            i = dfs(i, it, ordering, visited, graph);
        }
    }

    ordering[i] = at;
    // cout << i << " " << ordering[i] << endl;
    return i-1;
}

int* topSort(Graph graph) {
    int N = graph.V, i;
    bool visited[N] = {false};
    int *ordering = new int[N];
    i = N-1;

    for(int at=0; at<N; at++){
        if (visited[at] == false) {
            i = dfs(i, at, ordering, visited, graph);
        }
    }
    return ordering;
}


int main() {
    int *order;

    Graph g(6);
    g.addEdge(5, 2);
    g.addEdge(5, 0);
    g.addEdge(4, 0);
    g.addEdge(4, 1);
    g.addEdge(3, 1);
    g.addEdge(2, 1);

    // list<int> *graph;
    // graph = g.adj_list;

    order = topSort(g);
    for(int i=0; i<6; i++) {
        cout << order[i] << " ";
    }
    return 0;
}
