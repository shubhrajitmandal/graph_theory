class Heap():
    def __init__(self, type='max'):
        self.harr = []
        self.size = 0
        self.type = type

    def parent(self, pos):
        return (pos-1)//2

    def left(self, pos):
        return 2*pos + 1

    def right(self, pos):
        return 2*pos + 2

    def size(self):

        return len(self.harr)

    def getMin(self):
        return self.harr[0]

    def push(self, k):
        self.harr.append(k)
        self.size += 1
        self.siftUp(self.size-1)

    def siftUp(self, pos):
        i = pos
        while i != 0:
            if self.type == 'max':
                if self.harr[self.parent(i)] < self.harr[i]:
                    self.harr[self.parent(i)], self.harr[i] = self.harr[i], self.harr[self.parent(i)]
            else:
                if self.harr[self.parent(i)] > self.harr[i]:
                    self.harr[self.parent(i)], self.harr[i] = self.harr[i], self.harr[self.parent(i)]
            i = self.parent(i)

    def pop(self):
        if self.size == 0:
            return "Heap Empty"
        elif self.size == 1:
            self.size -= 1
            return self.harr[0]
        else:
            root = self.harr[0]
            self.harr[0], self.harr[self.size-1] = self.harr[self.size-1], self.harr[0]
            self.size -= 1
            self.siftDown(0)
            self.harr.pop()
            return root

    def siftDown(self, pos):
        i = pos
        while i < self.size:
            compIdx = i
            l = self.left(i)
            r = self.right(i)
            if self.type == 'max':
                if l < self.size and self.harr[l] > self.harr[compIdx]:
                    compIdx = l
                if r < self.size and self.harr[r] > self.harr[compIdx]:
                    compIdx = r
            else:
                if l < self.size and self.harr[l] < self.harr[compIdx]:
                    compIdx = l
                if r < self.size and self.harr[r] < self.harr[compIdx]:
                    compIdx = r
                print(self.harr[compIdx])
            if compIdx == i:
                break
            self.harr[compIdx], self.harr[i] = self.harr[i], self.harr[compIdx]
            i = compIdx


def main():
    heap = Heap()
    heap.push(4)
    heap.push(6)
    heap.push(1)
    heap.push(2)
    heap.push(5)
    heap.push(3)

    for x in heap.harr:
        print(x, end=' ')
    print()

    heap.pop()
    for x in heap.harr:
        print(x, end=' ')


if __name__ == '__main__':
    main()
