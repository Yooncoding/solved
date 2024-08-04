"""
14502 - 연구소
https://www.acmicpc.net/problem/14502
"""

import copy
from collections import deque
from sys import stdin

input = stdin.readline

# input
n, m = map(int, input().rsplit())
grid = [list(map(int, input().rsplit())) for _ in range(n)]

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]


def backtracking(cnt, start_row, start_col):
    if cnt == 3:
        bfs()
        return

    for i in range(start_row, n):
        for j in range(start_col, m):
            if grid[i][j] == 0:
                grid[i][j] = 1
                backtracking(cnt+1, i, j+1)
                grid[i][j] = 0
        start_col = 0

    return


def in_range(r, c):
    return 0 <= r < n and 0 <= c < m


def bfs():
    global ans
    copied_grid = copy.deepcopy(grid)
    q = deque()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                q.append([i, j])

    while len(q):
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if in_range(nr, nc) and copied_grid[nr][nc] == 0:
                copied_grid[nr][nc] = 2
                q.append([nr, nc])

    safe_area = 0
    for i in range(n):
        for j in range(m):
            if copied_grid[i][j] == 0:
                safe_area += 1

    ans = max(ans, safe_area)
    return


ans = 0
backtracking(0, 0, 0)
print(ans)
