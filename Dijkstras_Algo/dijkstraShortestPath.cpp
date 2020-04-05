#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <queue>
using namespace std;

#define V 9

void findNeighbors(vector<pair<int, int>> &neighbors, int at, int graph[V][V]){
    for(int i=0; i<V; i++){
        if(graph[at][i] > 0) {
            neighbors.push_back(make_pair(graph[at][i], i));
        }
    }
}

void findPath(int graph[V][V], int start, int dist[], int prev[]) {
    priority_queue< pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>> >pq;
    int at, wt, to;
    dist[start] = 0;
    pq.push(make_pair(0, start));
    while (!pq.empty()) {
        at = pq.top().second;
        pq.pop();

        vector<pair<int, int>> neighbors;
        findNeighbors(neighbors, at, graph);
        for(auto next: neighbors){
            to = next.second;
            wt = next.first;
            if(dist[to] > dist[at] + wt) {
                dist[to] = dist[at] + wt;
                prev[to] = at;
                pq.push(make_pair(wt, to));
                cout << at << " " << to << " " << pq.empty() << " " << pq.top().second << endl;
            }
        }
    }
}

void shortestPath(int graph[V][V], int start){
    int dist[V], prev[V];
    for(int i=0; i<V; i++) {
        dist[i] = INT_MAX;
        prev[i] = -1;
    }

    findPath(graph, start, dist, prev);
    for (int i=0; i<V; i++) {
        cout << dist[i] << " ";
    }
    cout << endl;
    for (int i=0; i<V; i++) {
        cout << prev[i] << " ";
    }
    cout << endl;
}

int main() {
    int graph[V][V] = { { 0, 4, 0, 0, 0, 0, 0, 8, 0 },
                        { 4, 0, 8, 0, 0, 0, 0, 11, 0 },
                        { 0, 8, 0, 7, 0, 4, 0, 0, 2 },
                        { 0, 0, 7, 0, 9, 14, 0, 0, 0 },
                        { 0, 0, 0, 9, 0, 10, 0, 0, 0 },
                        { 0, 0, 4, 14, 10, 0, 2, 0, 0 },
                        { 0, 0, 0, 0, 0, 2, 0, 1, 6 },
                        { 8, 11, 0, 0, 0, 0, 1, 0, 7 },
                        { 0, 0, 2, 0, 0, 0, 6, 7, 0 } };

    shortestPath(graph, 0);
    return 0;
}
