#include <iostream>
#include <vector>
#include <queue>
#include <map>
using namespace std;

class Graph {
public:
    int nV;
    map<int, vector<int>> adj_list;

    Graph(int n) {
        nV = n;
    }

    void addEdge(int u, int v) {
        adj_list[u].push_back(v);
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

    void BFS_(int start) {
        queue<int> q;
        bool visited[nV];
        for(int i=0; i<nV; i++) {
            visited[i] = false;
        }

        q.push(start);
        visited[start - 1] = true;

        while(!q.empty()) {
            int at = q.front();
            cout << at << " ";
            q.pop();

            vector<int> neighbors;
            neighbors = adj_list[at];
            for(auto next: neighbors) {
                if(!visited[next-1]) {
                    visited[next-1] = true;
                    q.push(next);
                }
            }
        }

    }

};

int main() {
    Graph g(6);
    g.addEdge(1, 2);
    g.addEdge(1, 3);
    g.addEdge(2, 4);
    g.addEdge(2, 5);
    g.addEdge(3, 5);
    g.addEdge(3, 1);
    g.addEdge(4, 5);
    g.addEdge(4, 6);
    g.addEdge(5, 6);
    g.addEdge(5, 3);
    g.addEdge(6, 4);
    g.addEdge(6, 5);

    g.BFS_(2);

    return 0;
}

// g.addEdge(1, 2);
// g.addEdge(1, 3);
// g.addEdge(2, 4);
// g.addEdge(2, 5);
// g.addEdge(3, 1);
// g.addEdge(3, 5);
// g.addEdge(3, 1);
// g.addEdge(4, 2);
// g.addEdge(4, 5);
// g.addEdge(4, 6);
// g.addEdge(5, 6);
// g.addEdge(5, 4);
// g.addEdge(5, 3);
// g.addEdge(5, 2);
// g.addEdge(6, 4);
// g.addEdge(6, 5);
