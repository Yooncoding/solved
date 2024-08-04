"""
7569 - 토마토
https://www.acmicpc.net/problem/7569
"""

from sys import stdin
from collections import deque

input = stdin.readline

m, n, h = map(int, input().rsplit())

graph = []
for i in range(h):
    tgraph = []
    for j in range(n):
        tgraph.append(list(map(int, input().rsplit())))
    graph.append(tgraph)

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i, j, k))


def bfs():
    dz = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dx = [0, 0, 0, 0, 1, -1]
    while len(q):
        z, y, x = q.popleft()
        for i in range(6):
            nz = dz[i] + z
            ny = dy[i] + y
            nx = dx[i] + x
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
                if graph[nz][ny][nx] == 0:
                    q.append((nz, ny, nx))
                    graph[nz][ny][nx] = graph[z][y][x] + 1


bfs()

ans = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                exit(0)
            else:
                ans = max(ans, graph[i][j][k])

print(ans-1)
