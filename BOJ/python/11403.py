"""
11403 - 경로 찾기
https://www.acmicpc.net/problem/11403
"""

from sys import stdin
from collections import defaultdict, deque

input = stdin.readline

n = int(input())
graph = []
routes = defaultdict(list)
ans = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().rsplit())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            routes[i].append(j)


def bfs(start):
    q = deque()
    q.append(start)
    visited = [False for _ in range(n)]
    while len(q):
        i = q.popleft()
        for route in routes[i]:
            if visited[route]:
                continue
            q.append(route)
            ans[start][route] = 1
            visited[route] = True


for i in range(n):
    for j in range(n):
        if ans[i][j] == 0:
            bfs(i)

for i in range(n):
    for j in range(n):
        print(ans[i][j], end=" ")
    print()
