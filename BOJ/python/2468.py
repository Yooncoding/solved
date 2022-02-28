"""
2468 - 안전 영역
https://www.acmicpc.net/problem/2468
"""

from sys import stdin
from collections import deque


input = stdin.readline

n = int(input())
graph = [list(map(int, input().rsplit())) for _ in range(n)]
max_v = max(map(max, graph))
ans = []


def bfs(y, x, h):
    q = deque()
    q.append([y, x])
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    while len(q):
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] > h:
                if visited[ny][nx]:
                    continue
                q.append([ny, nx])
                visited[ny][nx] = True
    return


for height in range(max_v):
    cnt = 0
    visited = [[False for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > height and not visited[i][j]:
                visited[i][j] = True
                bfs(i, j, height)
                cnt += 1
    ans.append(cnt)

print(max(ans))
