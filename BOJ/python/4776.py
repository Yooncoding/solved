"""
2573 - 빙산
https://www.acmicpc.net/problem/2573
"""

from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().rsplit())
graph = [list(map(int, input().rsplit())) for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs(y, x):
    q = deque()
    q.append([y, x])
    melts = []
    while len(q):
        y, x = q.popleft()
        zero_cnt = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not (0 <= ny < n and 0 <= nx < m):
                continue

            if visited[ny][nx]:
                continue

            if graph[ny][nx] == 0:
                zero_cnt += 1
                continue

            q.append([ny, nx])
            visited[ny][nx] = True
        if zero_cnt:
            melts.append([y, x, zero_cnt])
    return melts


ans = 0
while True:
    cnt = 0
    visited = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                visited[i][j] = True
                melts = bfs(i, j)
                cnt += 1
                for y, x, zero_cnt in melts:
                    graph[y][x] = max(0, graph[y][x] - zero_cnt)

    if cnt == 0:
        ans = 0
        break

    if cnt >= 2:
        break
    ans += 1

print(ans)
