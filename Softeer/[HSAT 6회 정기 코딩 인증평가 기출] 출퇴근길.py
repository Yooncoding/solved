"""
https://softeer.ai/practice/6248
24-08-12
"""

import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def bfs(start, g, visited):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        now = q.popleft()
        for next in g[now]:
            if visited[next]:
                continue
            visited[next] = True
            q.append(next)


n, m = map(int, input().rsplit())

graph = defaultdict(list)
graph_r = defaultdict(list)

for _ in range(m):
    x, y = map(int, input().rsplit())
    graph[x].append(y)
    graph_r[y].append(x)

s, t = map(int, input().rsplit())

from_s = [False for _ in range(n+1)]
from_s[t] = True
bfs(s, graph, from_s)

from_t = [False for _ in range(n+1)]
from_t[s] = True
bfs(t, graph, from_t)

from_x_to_s = [False for _ in range(n+1)]
bfs(s, graph_r, from_x_to_s)

from_x_to_t = [False for _ in range(n+1)]
bfs(t, graph_r, from_x_to_t)

ans = 0
for i in range(1, n+1):
    if i == s or i == t:
        continue

    if from_s[i] and from_t[i] and from_x_to_s[i] and from_x_to_t[i]:
        ans += 1

print(ans)
