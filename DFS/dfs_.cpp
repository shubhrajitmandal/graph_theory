#include <iostream>
#include <map>
#include <vector>
using namespace std;

class Graph {
public:
    int V;
    map<int, vector<int>> adj_list;
    bool visited[10000];

    Graph(int n) {
        V = n;
        for(int i=0; i<n; i++) {
            visited[i] = false;
        };
    }

    void addEdge(int u, int v) {
        adj_list[u].push_back(v);
    }

    void DFS_(int at) {
        if(visited[at-1] == true) return;
        visited[at-1] = true;
        cout << at << " ";

        vector<int> neighbors;
        neighbors = adj_list[at];
        for (auto next: neighbors) {
            DFS_(next);
        }
    }

    void displayAdjList() {
        for(auto it: adj_list) {
            cout << it.first << " -> ";
            for(auto x : it.second) {
                cout << x << " ";
            }
            cout << endl;
        }
    }

};

int main() {
    int n, e, u, v;
    cin >> n >> e;

    Graph g(n);

    for (int i=0; i<e; i++) {
        cin >> u >> v;
        g.addEdge(u, v);
    }
    g.displayAdjList();
    g.DFS_(1);

    return 0;
}
