"""
1012 - 유기농 배추
https://www.acmicpc.net/problem/1012
"""

from sys import stdin
from collections import deque

input = stdin.readline


def bfs(x, y, l):
    q = deque()
    q.append([x, y])
    while not len(q) == 0:
        a, b = q.popleft()
        l[b][a] = 0
        if a > 0:
            if l[b][a - 1]:
                l[b][a - 1] = 0
                q.append([a - 1, b])
        if a < len(l[0]) - 1:
            if l[b][a + 1]:
                l[b][a + 1] = 0
                q.append([a + 1, b])
        if b > 0:
            if l[b - 1][a]:
                l[b - 1][a] = 0
                q.append([a, b - 1])
        if b < len(l) - 1:
            if l[b + 1][a]:
                l[b + 1][a] = 0
                q.append([a, b + 1])

    return 1


for _ in range(int(input())):
    M, N, K = map(int, input().rsplit())
    land = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().rsplit())
        land[Y][X] = 1

    cnt = 0

    for j in range(N):
        for i in range(M):
            if land[j][i] == 1:
                cnt += bfs(i, j, land)

    print(cnt)
