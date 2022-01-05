"""
1260 - DFS와 BFS
https://www.acmicpc.net/problem/1260
"""

from sys import stdin
from collections import defaultdict

input = stdin.readline


def bfs(g, v, n):
    q = [v]
    visited = [0] * n
    result = []
    while len(q) != 0:
        t = q.pop(0)
        if visited[t - 1] == 1:
            continue
        for p in g[t]:
            q.append(p)

        visited[t - 1] = 1
        result.append(t)

    return result


def dfs(g, v, n, visited=None, result=None):
    if result is None:
        result = [v]
    if visited is None:
        visited = [0] * n
        visited[v - 1] = 1
    for i in g[v]:
        if visited[i - 1] == 1:
            continue
        result.append(i)
        visited[i - 1] = 1
        dfs(g, i, n, visited, result)

    return result


N, M, V = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for k in graph.keys():
    graph[k].sort()

print(*dfs(graph, V, N))
print(*bfs(graph, V, N))
