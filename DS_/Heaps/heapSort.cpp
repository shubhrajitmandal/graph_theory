#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void maxHeapify(vector<int> &heap, int pos, int n) {
    int largest, l, r;
    largest = pos;
    l = 2*pos + 1;
    r = 2*pos + 2;
    if (l<n && heap[l] > heap[largest]){
        largest = l;
    }
    if (r<n && heap[r] > heap[largest]){
        largest = r;
    }
    if (largest != pos) {
        swap(heap[largest], heap[pos]);
        maxHeapify(heap, largest, n);
    }
}

void heapSort(vector<int> &heap, int n) {
    for(int i= (n/2-1); i>=0; i--) {
        maxHeapify(heap, i, n);
    }
    for(int i=0; i<n; i++) {
        swap(heap[0], heap[n-i-1]);
        maxHeapify(heap, 0, n-i-1);
    }

}

void heapSortSTL(vector<int> &heap, int n) {
    make_heap(heap.begin(), heap.end());
    sort_heap(heap.begin(), heap.end());
    //is_heap(heap.begin(), heap.end())
}

int main() {
    int n, x;
    vector<int> heap;
    cin >> n;
    for(int i=0; i<n; i++) {
        cin >> x;
        heap.push_back(x);
    }
    heapSortSTL(heap, n);
    for(auto it: heap){
        cout << it << " ";
    }
    cout << endl;
    cout << is_heap(heap.begin(), heap.end());
}
