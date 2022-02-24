"""
2644 - 촌수계산
https://www.acmicpc.net/problem/2644
"""

from sys import stdin
from collections import deque, defaultdict

input = stdin.readline

graph = defaultdict(list)
n = int(input())
s, e = map(int, input().rsplit())
m = int(input())

for _ in range(m):
    x, y = map(int, input().rsplit())
    graph[x].append(y)
    graph[y].append(x)


def bfs(s, e):
    visited = [False for _ in range(n+1)]
    visited[s] = True
    q = deque()
    q.append([s, 0])
    while len(q):
        u, cnt = q.popleft()
        if u == e:
            print(cnt)
            return

        for v in graph[u]:
            if visited[v]:
                continue
            q.append([v, cnt+1])
            visited[v] = True

    print(-1)
    return


bfs(s, e)
