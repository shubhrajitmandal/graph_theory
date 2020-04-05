import queue as Q

def main():
    q = Q.PriorityQueue()
    q.put(('A', 20))
    q.put(('B', 50))
    q.put(('0', 10))
    q.put(('D', 30))
    while not q.empty():
        print(q.get())

if __name__ == '__main__':
    main()
