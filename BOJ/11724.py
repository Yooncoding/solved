"""
11724 - 연결 요소의 개수
https://www.acmicpc.net/problem/11724
"""

from sys import stdin
from collections import deque, defaultdict

input = stdin.readline

graph = defaultdict(list)
n, m = map(int, input().rsplit())
visited = [False for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().rsplit())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)


def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = True
    while len(q):
        x = q.popleft()
        for v in graph[x]:
            if visited[v]:
                continue
            q.append(v)
            visited[v] = True

    return


cnt = 0
for i in range(n):
    if visited[i]:
        continue
    bfs(i)
    cnt += 1

print(cnt)
