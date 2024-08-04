"""
11404 - 플로이드
https://www.acmicpc.net/problem/11404
"""

import math
from sys import stdin

input = stdin.readline
INF = math.inf

n = int(input())
m = int(input())
graph = [[INF for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().rsplit())
    graph[a-1][b-1] = min(c, graph[a-1][b-1])

for i in range(n):
    for j in range(n):
        for k in range(n):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF or i == j:
            graph[i][j] = 0

for cow in graph:
    print(*cow)
