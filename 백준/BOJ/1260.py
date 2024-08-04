"""
1260 - DFS와 BFS
https://www.acmicpc.net/problem/1260
"""

from collections import defaultdict, deque


def bfs(v):
    visited = [False for _ in range(n + 1)]
    q = deque()
    ans = []
    q.append(v)
    while len(q):
        v = q.popleft()
        if visited[v]:
            continue

        for i in graph[v]:
            if visited[i]:
                continue
            q.append(i)
        visited[v] = True
        ans.append(v)
    return ans


def dfs(v, visited=None, ans=None):
    if visited is None:
        visited = [False for _ in range(n + 1)]
        visited[v] = True
    if ans is None:
        ans = [v]

    for i in graph[v]:
        if visited[i]:
            continue
        visited[i] = True
        ans.append(i)
        dfs(i, visited, ans)

    return ans


graph = defaultdict(list)

n, m, v = map(int, input().rsplit())

for _ in range(m):
    a, b = map(int, input().rsplit())
    graph[a].append(b)
    graph[b].append(a)

for k in graph:
    graph[k].sort()

print(*dfs(v))
print(*bfs(v))
