"""
14503 - 로봇청소기
https://www.acmicpc.net/problem/14503
"""

from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().rsplit())
r, c, d = map(int, input().rsplit())
graph = [list(map(int, input().rsplit())) for _ in range(n)]


def bfs(r, c, d):
    cnt = 1
    graph[r][c] = 2
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    q = deque()
    q.append([r, c])
    while len(q):
        y, x = q.popleft()
        for i in range(4):
            d = (d-1) % 4
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 0:
                graph[ny][nx] = 2
                cnt += 1
                q.append([ny, nx])
                break
        else:
            ny = y + dy[(d-2) % 4]
            nx = x + dx[(d-2) % 4]
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] != 1:
                q.append([ny, nx])
                continue
            print(cnt)
            return


bfs(r, c, d)
