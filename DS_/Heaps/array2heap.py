def makeMinHeap(heap):
    sIdx = len(heap)//2 - 1
    while sIdx >=0:
        minHeapify(heap, sIdx)
        sIdx -= 1
    return heap


def minHeapify(heap, pos):
    smallest = pos
    l = 2*pos + 1
    r = 2*pos + 2
    if l < len(heap) and heap[l] < heap[smallest]:
        smallest = l
    if r < len(heap) and heap[r] < heap[smallest]:
        smallest = r

    if smallest != pos:
        heap[pos], heap[smallest] = heap[smallest], heap[pos]
        minHeapify(heap, smallest)

def main():
    inp = list(map(int, input().split()))
    heap = makeMinHeap(inp)
    print(heap)

if __name__ == '__main__':
    main()
