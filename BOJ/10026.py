"""
10026 - 적록색약
https://www.acmicpc.net/problem/10026
"""

from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
graph = []

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for _ in range(n):
    graph.append(list(input().rstrip()))


def bfs(y, x, color):
    q = deque()
    q.append((y, x))
    visited[y][x] = True

    while len(q):
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                if graph[ny][nx] == color:
                    q.append((ny, nx))
                    visited[ny][nx] = True

    return True


# 색약이 아닐 때
cnt = 0
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue
        bfs(i, j, graph[i][j])
        cnt += 1

print(cnt, end=" ")

# "R" -> "G" 변환
for i in range(n):
    for j in range(n):
        if graph[i][j] == "R":
            graph[i][j] = "G"

# 색약일 때
cnt = 0
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue
        bfs(i, j, graph[i][j])
        cnt += 1
print(cnt)
