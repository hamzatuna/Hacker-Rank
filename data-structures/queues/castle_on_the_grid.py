import sys
from collections import deque


def minimumMoves(grid, startX, startY, goalX, goalY):

    queue = deque()
    n = len(grid)
    visited = [[True for _ in range(n)] for i in range(n)]
    start, end = (startX, startY, 0), (goalX, goalY)
    visited[start[0]][start[1]] = False
    queue.append(start)

    while len(queue) != 0:
        c = queue.popleft()
        # print(c)
        if c[0] == end[0] and c[1] == end[1]:
            print (c[2])
            break
        x, y, step = c
        t = x + 1

        # right
        while t < n and grid[t][y] == '.':
            if visited[t][y]:
                queue.append((t, y, step + 1))
                visited[t][y] = False
            t += 1
        t = y + 1
        # below
        while t < n and grid[x][t] == '.':
            if visited[x][t]:
                queue.append((x, t, step + 1))
                visited[x][t] = False
            t += 1
        t = y - 1
        # up
        while t > -1 and grid[x][t] == '.':
            if visited[x][t]:
                queue.append((x, t, step + 1))
                visited[x][t]
            t -= 1
        t = x - 1
        # left
        while t > -1 and grid[t][y] == '.':
            if visited[t][y]:
                queue.append((t, y, step + 1))
                visited[t][y] = False
            t -= 1


if __name__ == "__main__":
    n = int(input().strip())
    grid = [list(input()) for _ in range(n)]

    startX, startY, goalX, goalY = input().strip().split(' ')
    startX, startY, goalX, goalY = [
        int(startX), int(startY), int(goalX), int(goalY)]
    result = minimumMoves(grid, startX, startY, goalX, goalY)
