from heapq import heapify, heappush, heappop, nlargest, nsmallest
## heaps in python are min heap
## to use max heap multiply all values by -1

def main():
    heap = [4, 6, 1, 2, 5, 3]
    heapify(heap)
    print(heap, heap[0])
    heappush(heap, 10)
    print(heap)
    print(heappop(heap))
    print(heap)
    # nsmallest returns k smallest numbers from the heap
    print(nsmallest(3, heap))
    # nlargest returns k largest numbers from the heap
    print(nlargest(3, heap))


if __name__ == '__main__':
    main()
