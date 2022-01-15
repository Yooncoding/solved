"""
10026 - 적록색약
https://www.acmicpc.net/problem/10026
"""

from sys import stdin
from collections import deque
from copy import deepcopy

input = stdin.readline

N = int(input())
original_cnt = 0
changed_cnt = 0
original_grid = []
changed_grid = []
visited = [[False for _ in range(N)] for _ in range(N)]


def bfs(x, y, grid):
    q = deque()
    q.append([x, y])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    while len(q) != 0:
        x, y = q.popleft()
        if visited[y][x] == True:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == grid[x][y]:
                q.append([nx, ny])
        visited[y][x] = True

    return True


for _ in range(N):
    original_grid.append(list(input().rstrip()))

changed_grid = deepcopy(original_grid)

for j in range(N):
    for i in range(N):
        if original_grid[i][j] == "G":
            changed_grid[i][j] = "R"
        if visited[j][i] == True:
            continue
        bfs(i, j, original_grid)
        original_cnt += 1

print(original_cnt, end=" ")

visited = [[False for _ in range(N)] for _ in range(N)]

for j in range(N):
    for i in range(N):
        if visited[j][i] == True:
            continue
        bfs(i, j, changed_grid)
        changed_cnt += 1

print(changed_cnt)
