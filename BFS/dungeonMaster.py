'''
PATH FINDING PROBLEM

Dungeon = { S..#...
            .#..#..
            .#.....
            ..##...
            #.#E.#. }
S = Start,
E = End,
. = Empty Cell
# = Wall
'''
import numpy as np
import queue

def shortestPath(s, e, grid):
    prev = findPath(s, grid)
    return reconstructPath(s, e, prev)


# Find all possible paths from start
def findPath(s, grid):
    visited = -1 * np.ones((len(grid), len(grid[0])))
    prev = {}
    q = queue.Queue()

    q.put(s)
    (x, y) = s
    visited[x][y] = 1
    while not q.empty():
        at = q.get()

        neighbors = findNeighbors(at, grid)
        if neighbors == []:
            return prev

        for next in neighbors:
            (x, y) = next
            if visited[x][y] == -1:
                visited[x][y] = 1
                q.put((x, y))
                prev[next] = at
    return prev


#Find neighbors of a cell
def findNeighbors(pos, grid):
    (x, y) = pos
    neighbors = []
    if y - 1 >= 0 and grid[x][y-1] == 0:
        neighbors.append((x, y-1))
    if y + 1 < len(grid[0]) and grid[x][y+1] == 0:
        neighbors.append((x, y+1))
    if x - 1 >= 0 and grid[x-1][y] == 0:
        neighbors.append((x-1, y))
    if x + 1 < len(grid) and grid[x+1][y] == 0:
        neighbors.append((x+1, y))
    return neighbors


#Backtrack path from end
def reconstructPath(s, e, prev):
    path = []

    if e not in prev.keys():
        return False

    at = e
    while at in prev.keys():
        path.append(prev[at])
        at = prev[at]
    path.reverse()
    if path[0] == s:
        path.append(e)
        return path


def main():
    R, C = map(int,input().split())
    dungeon = []
    for x in range(R):
        s = input()
        row = C*[0]
        for y in range(len(s)):
            if s[y] == 'S':
                start = (x, y)
            elif s[y] == 'E':
                end = (x, y)
            elif s[y] == '#':
                row[y] = -1
        dungeon.append(row)

    path = shortestPath(start, end, dungeon)

    if path:
        print("PATH: ", end=' ')
        for x in path:
            print(x, end=' ')
        print("\nTIME: ", len(path))
    else:
        print("Trapped!!")


if __name__ == '__main__':
        main()
