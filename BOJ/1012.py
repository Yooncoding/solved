"""
1012 - 유기농 배추
https://www.acmicpc.net/problem/1012
"""

from collections import deque


def bfs(y, x):
    queue = deque()
    queue.append([y, x])
    dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
    while len(queue) != 0:
        y, x = queue.popleft()
        if visited[y][x]:
            continue
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and land[ny][nx] == 1:
                if visited[ny][nx]:
                    continue
                queue.append([ny, nx])
        visited[y][x] = True

    return


for _ in range(int(input())):
    m, n, k = map(int, input().rsplit())
    land = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    cnt = 0

    for _ in range(k):
        x, y = map(int, input().rsplit())
        land[y][x] = 1

    for i in range(n):
        for j in range(m):
            if visited[i][j] or land[i][j] != 1:
                continue
            bfs(i, j)
            cnt += 1

    print(cnt)
