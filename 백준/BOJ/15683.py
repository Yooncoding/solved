"""
15683 - 감시
https://www.acmicpc.net/problem/15683
"""

import copy
from math import inf
INF = inf

# input
n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
cctv = []
for i in range(n):
    for j in range(m):
        if office[i][j] != 0 and office[i][j] != 6:
            cctv.append([office[i][j], i, j])


dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
cases = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]


def in_range(r, c):
    return 0 <= r < n and 0 <= c < m


def fill(grid, r, c, case):
    for i in case:
        nr, nc = r, c
        while True:
            nr += dr[i]
            nc += dc[i]
            if not in_range(nr, nc):
                break
            if grid[nr][nc] == 6:
                break
            elif grid[nr][nc] == 0:
                grid[nr][nc] = 7


def backtracking(cnt, grid):
    global ans
    if cnt == len(cctv):
        s = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    s += 1
        ans = min(s, ans)
        return

    temp = copy.deepcopy(grid)
    cctv_num, r, c = cctv[cnt]
    for case in cases[cctv_num]:
        fill(temp, r, c, case)
        backtracking(cnt+1, temp)
        temp = copy.deepcopy(grid)


ans = INF
backtracking(0, office)
print(ans)
