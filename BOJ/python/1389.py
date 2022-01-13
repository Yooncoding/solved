"""
1389 - 케빈 베이컨의 6단계 법칙
https://www.acmicpc.net/problem/1389
"""

from sys import stdin, maxsize
from collections import defaultdict, deque

input = stdin.readline


def bfs(n):
    visited = [False] + [False] * N
    cnt = [0] + [0] * N

    q = deque()
    q.append(n)
    visited[n] = True

    while len(q) != 0:
        t = q.popleft()
        for p in relation[t]:
            if visited[p] == True:
                continue
            cnt[p] = cnt[t] + 1
            visited[p] = True
            q.append(p)

    return sum(cnt)


N, M = map(int, input().split())
relation = defaultdict(list)
answer = [maxsize] + [0] * N

for _ in range(M):
    u, v = map(int, input().split())
    relation[u].append(v)
    relation[v].append(u)

for i in range(1, N + 1):
    answer[i] = bfs(i)

print(answer.index(min(answer)))
