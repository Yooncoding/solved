"""
11724 - 연결 요소의 개수
https://www.acmicpc.net/problem/11724
"""

from sys import stdin
from collections import defaultdict, deque

input = stdin.readline


def bfs(k):
    q = deque()
    q.append(k)
    while len(q) != 0:
        t = q.popleft()
        if visited[t] == False:
            for p in link[t]:
                q.append(p)
            visited[t] = True


N, M = map(int, input().split())
link = defaultdict(list)
visited = [False] + [False] * 1000
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    link[u].append(v)
    link[v].append(u)

for k in range(1, N + 1):
    if visited[k] == False:
        bfs(k)
        cnt += 1

print(cnt)
