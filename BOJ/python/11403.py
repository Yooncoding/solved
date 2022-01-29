"""
11403 - 경로 찾기
https://www.acmicpc.net/problem/11403
"""

from sys import stdin
from collections import defaultdict, deque

input = stdin.readline

N = int(input())

matrix = []
graph = defaultdict(list)

for _ in range(N):
    matrix.append(list(map(int, input().rsplit())))

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            graph[i].append(j)


def bfs(start, end):
    q = deque()
    q.append(start)
    visited = [False] * 100
    while len(q) != 0:
        t = q.popleft()

        if visited[t] is True:
            continue

        for g in graph[t]:
            if g == end:
                return 1
            if visited[g] is True:
                continue
            q.append(g)

        visited[t] = True

    return 0


for i in range(N):
    for j in range(N):
        print(bfs(i, j), end=" ")
    print()
