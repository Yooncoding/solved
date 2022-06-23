"""
12100 - 2048 (Easy)
https://www.acmicpc.net/problem/12100
"""

import copy

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


def left_move(now_grid):
    next_grid = copy.deepcopy(now_grid)
    for i in range(n):
        p = 0
        for j in range(1, n):
            if next_grid[i][j] != 0:
                temp = next_grid[i][j]
                next_grid[i][j] = 0
                if next_grid[i][p] == 0:
                    next_grid[i][p] = temp
                elif next_grid[i][p] == temp:
                    next_grid[i][p] = temp * 2
                    p += 1
                else:
                    p += 1
                    next_grid[i][p] = temp

    return next_grid


def right_move(now_grid):
    next_grid = copy.deepcopy(now_grid)
    for i in range(n):
        p = n-1
        for j in range(n-2, -1, -1):
            if next_grid[i][j] != 0:
                temp = next_grid[i][j]
                next_grid[i][j] = 0
                if next_grid[i][p] == 0:
                    next_grid[i][p] = temp
                elif next_grid[i][p] == temp:
                    next_grid[i][p] = temp * 2
                    p -= 1
                else:
                    p -= 1
                    next_grid[i][p] = temp

    return next_grid


def up_move(now_grid):
    next_grid = copy.deepcopy(now_grid)
    for j in range(n):
        p = 0
        for i in range(1, n):
            if next_grid[i][j]:
                temp = next_grid[i][j]
                next_grid[i][j] = 0
                if next_grid[p][j] == 0:
                    next_grid[p][j] = temp
                elif next_grid[p][j] == temp:
                    next_grid[p][j] = temp * 2
                    p += 1
                else:
                    p += 1
                    next_grid[p][j] = temp

    return next_grid


def down_move(now_grid):
    next_grid = copy.deepcopy(now_grid)
    for j in range(n):
        p = n-1
        for i in range(n - 2, -1, -1):
            if next_grid[i][j]:
                temp = next_grid[i][j]
                next_grid[i][j] = 0
                if next_grid[p][j] == 0:
                    next_grid[p][j] = temp
                elif next_grid[p][j] == temp:
                    next_grid[p][j] = temp * 2
                    p -= 1
                else:
                    p -= 1
                    next_grid[p][j] = temp

    return next_grid


def go(cnt, now_grid):
    global ans

    if cnt == 5:
        max_grid = max(map(max, now_grid))
        ans = max(ans, max_grid)
        return

    go(cnt+1, up_move(now_grid))
    go(cnt+1, left_move(now_grid))
    go(cnt+1, right_move(now_grid))
    go(cnt+1, down_move(now_grid))

    return


ans = 0
go(0, grid)

print(ans)
